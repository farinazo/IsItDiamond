"""
================================================================================
   theHunter: Call of the Wild - In-Game Overlay HUD (Abordagem 1) v1.0
================================================================================
Este aplicativo cria um HUD transparente e 'click-through' sobre o jogo em tempo real.
Ele monitora a área de avistamento (spotting HUD) com OCR ultrarrápido da Windows Media,
detecta o animal e os pontos sorteados ('123 - 145') e mostra na hora se é DIAMANTE!
"""

import os
import sys
import json
import time
import re
import ctypes
import threading
import unicodedata
import asyncio
import tkinter as tk
from tkinter import font as tkfont
from PIL import Image, ImageGrab, ImageEnhance, ImageOps
import winocr

# Load Config and Database
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIG_PATH = os.path.join(SCRIPT_DIR, "config.json")
DATABASE_PATH = os.path.join(SCRIPT_DIR, "database.json")

with open(CONFIG_PATH, "r", encoding="utf-8") as f:
    CONFIG = json.load(f)

with open(DATABASE_PATH, "r", encoding="utf-8") as f:
    ANIMALS_DB = json.load(f)

def normalize(text):
    text = unicodedata.normalize('NFKD', text)
    text = ''.join(c for c in text if not unicodedata.combining(c))
    return re.sub(r'[^a-zA-Z0-9]', '', text).lower()

# Build search index for fast lookup
ANIMAL_INDEX = []
for a in ANIMALS_DB:
    ANIMAL_INDEX.append({
        'data': a,
        'norm_pt': normalize(a['orig_pt']),
        'norm_en': normalize(a['orig_en']),
        'norm_name': normalize(a['name_en']),
    })

# Win32 click-through constants
GWL_EXSTYLE = -20
WS_EX_TRANSPARENT = 0x00000020
WS_EX_LAYERED = 0x00080000
WS_EX_NOACTIVATE = 0x08000000

class COTWOverlayApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("COTW Trophy Diamond Overlay")
        
        # Screen dimensions
        user32 = ctypes.windll.user32
        user32.SetProcessDPIAware()
        self.screen_w = user32.GetSystemMetrics(0)
        self.screen_h = user32.GetSystemMetrics(1)
        
        # Position overlay
        pos_cfg = CONFIG["overlay_position"]
        self.overlay_w = pos_cfg["width"]
        self.overlay_h = pos_cfg["height"]
        self.overlay_x = int(self.screen_w * pos_cfg["pos_x_percent"])
        self.overlay_y = int(self.screen_h * pos_cfg["pos_y_percent"])
        
        self.root.geometry(f"{self.overlay_w}x{self.overlay_h}+{self.overlay_x}+{self.overlay_y}")
        self.root.overrideredirect(True)
        self.root.attributes("-topmost", True)
        
        # Transparent background color key
        self.trans_color = "#010101"
        self.root.configure(bg=self.trans_color)
        self.root.attributes("-transparentcolor", self.trans_color)
        
        # Make click-through so game receives all mouse and keyboard inputs
        hwnd = self.root.winfo_id()
        style = user32.GetWindowLongW(hwnd, GWL_EXSTYLE)
        user32.SetWindowLongW(hwnd, GWL_EXSTYLE, style | WS_EX_TRANSPARENT | WS_EX_LAYERED | WS_EX_NOACTIVATE)
        
        # Calculate screen scan bounding box
        s_cfg = CONFIG["scan_region_percent"]
        self.scan_bbox = (
            int(self.screen_w * s_cfg["left"]),
            int(self.screen_h * s_cfg["top"]),
            int(self.screen_w * s_cfg["right"]),
            int(self.screen_h * s_cfg["bottom"])
        )
        
        self.last_detection_time = 0
        self.is_visible = False
        self.calibration_mode = CONFIG.get("calibration_mode", False)
        
        self.build_ui()
        
        # Background worker thread
        self.running = True
        self.worker_thread = threading.Thread(target=self.scanner_loop, daemon=True)
        self.worker_thread.start()
        
        # UI check loop
        self.root.after(100, self.ui_refresh_loop)

    def build_ui(self):
        # Container Card Frame
        self.card = tk.Frame(
            self.root,
            bg="#101726",
            highlightthickness=2,
            highlightbackground="#00d2d3",
            padx=14,
            pady=12
        )
        self.card.place(x=0, y=0, width=self.overlay_w, height=self.overlay_h)
        
        # Header Badge (DIAMANTE / OURO / PRATA)
        self.badge_lbl = tk.Label(
            self.card,
            text="💎 POTENCIAL DIAMANTE!",
            font=("Segoe UI", 13, "bold"),
            fg="#00f0ff",
            bg="#182236",
            padx=8,
            pady=3
        )
        self.badge_lbl.pack(fill="x", pady=(0, 6))
        
        # Animal Name
        self.animal_lbl = tk.Label(
            self.card,
            text="VEADO-VERMELHO",
            font=("Segoe UI", 12, "bold"),
            fg="#ffffff",
            bg="#101726",
            anchor="w"
        )
        self.animal_lbl.pack(fill="x")
        
        # Score comparison
        self.score_lbl = tk.Label(
            self.card,
            text="Estimativa: 235 - 268   |   Diamante: 251.07+",
            font=("Segoe UI", 10),
            fg="#00d2d3",
            bg="#101726",
            anchor="w"
        )
        self.score_lbl.pack(fill="x", pady=2)
        
        # Level & Info
        self.info_lbl = tk.Label(
            self.card,
            text="Nível Máximo: 9 (Fabled)   |   Classe: 6",
            font=("Segoe UI", 9),
            fg="#94a3b8",
            bg="#101726",
            anchor="w"
        )
        self.info_lbl.pack(fill="x")
        
        # Status Tip
        self.tip_lbl = tk.Label(
            self.card,
            text="🎯 Pontuação suficiente para Diamante!",
            font=("Segoe UI", 9, "italic"),
            fg="#38ef7d",
            bg="#101726",
            anchor="w"
        )
        self.tip_lbl.pack(fill="x", pady=(4, 0))

        # Initially hidden
        self.card.place_forget()

    def scanner_loop(self):
        """Asynchronous OCR scanning loop running on background thread"""
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        
        lang = CONFIG.get("language", "pt")
        ocr_lang = "pt" if lang == "pt" else "en"
        interval = CONFIG.get("refresh_interval_ms", 350) / 1000.0

        print(f"[COTW Overlay] Monitorando tela ({self.screen_w}x{self.screen_h})...")
        print(f"[COTW Overlay] Região de leitura: {self.scan_bbox}")
        print(f"[COTW Overlay] Jogo deve estar em modo 'Janela Sem Bordas' (Borderless).")

        while self.running:
            try:
                # Capture screen crop
                screen_crop = ImageGrab.grab(bbox=self.scan_bbox)
                
                # Image preprocessing for OCR: grayscale & contrast
                gray = screen_crop.convert('L')
                enhancer = ImageEnhance.Contrast(gray)
                preprocessed = enhancer.enhance(2.0)
                
                # Run Windows OCR
                result = loop.run_until_complete(winocr.recognize_pil(preprocessed, lang=ocr_lang))
                raw_text = result.text.strip()
                
                if raw_text:
                    animal, scores = self.parse_text(raw_text)
                    if animal:
                        self.on_detected(animal, scores, raw_text)
                
            except Exception as e:
                # Silently catch transient capture errors
                pass
                
            time.sleep(interval)

    def parse_text(self, ocr_text):
        norm_ocr = normalize(ocr_text)
        
        matched_animal = None
        best_len = 0
        for item in ANIMAL_INDEX:
            for key in ['norm_pt', 'norm_en', 'norm_name']:
                target = item[key]
                if len(target) >= 3 and target in norm_ocr:
                    if len(target) > best_len:
                        best_len = len(target)
                        matched_animal = item['data']
                        
        score_match = re.search(r'(\d+(?:\.\d+)?)\s*[-–~]\s*(\d+(?:\.\d+)?)', ocr_text)
        scores = None
        if score_match:
            try:
                s_min = float(score_match.group(1))
                s_max = float(score_match.group(2))
                scores = (s_min, s_max)
            except ValueError:
                pass

        return matched_animal, scores

    def on_detected(self, animal, scores, raw_text):
        self.last_detection_time = time.time()
        
        name_display = animal['orig_pt'] if CONFIG.get("language") == "pt" else animal['orig_en']
        dia_min = animal['diamond_min']
        lvl = animal['max_level']
        cls = animal['class']
        
        tier = "INFO"
        if scores:
            s_min, s_max = scores
            if s_min >= dia_min:
                tier = "DIAMANTE_CERTO"
            elif s_max >= dia_min:
                tier = "DIAMANTE_POTENCIAL"
            elif s_max >= dia_min * 0.8:
                tier = "OURO"
            elif s_max >= dia_min * 0.6:
                tier = "PRATA"
            else:
                tier = "BRONZE"
                
        # Send update to main UI thread
        self.root.after(0, self.update_display, animal, name_display, scores, dia_min, lvl, cls, tier)

    def update_display(self, animal, name, scores, dia_min, lvl, cls, tier):
        self.animal_lbl.config(text=name.upper())
        
        fabled = "(Fabled / Great One)" if "Fabled" in lvl else ""
        lvl_clean = lvl.replace(" (10 Fabled)", "")
        self.info_lbl.config(text=f"Nível Máx: {lvl_clean} {fabled}   |   Classe: {cls}")
        
        if scores:
            s_min, s_max = scores
            self.score_lbl.config(text=f"Estimativa: {s_min:.1f} - {s_max:.1f}   |   Diamante: {dia_min:.2f}+")
        else:
            self.score_lbl.config(text=f"Requisito Diamante: {dia_min:.2f}+")
            
        # Update badge styling according to trophy tier
        if tier == "DIAMANTE_CERTO":
            self.card.config(highlightbackground="#00f0ff")
            self.badge_lbl.config(text="💎 DIAMANTE GARANTIDO! 💎", fg="#00f0ff", bg="#0a2a3a")
            self.tip_lbl.config(text="🎯 A pontuação mínima já ultrapassou o corte!", fg="#00f0ff")
        elif tier == "DIAMANTE_POTENCIAL":
            self.card.config(highlightbackground="#00d2d3")
            self.badge_lbl.config(text="💎 POTENCIAL DIAMANTE!", fg="#00d2d3", bg="#082b30")
            self.tip_lbl.config(text="🎯 A estimativa máxima alcança o requisito de Diamante!", fg="#38ef7d")
        elif tier == "OURO":
            self.card.config(highlightbackground="#f1c40f")
            self.badge_lbl.config(text="🥇 PROVÁVEL OURO", fg="#f1c40f", bg="#332805")
            self.tip_lbl.config(text=f"Trophy alto, porém abaixo de {dia_min:.2f} (Diamante)", fg="#f1c40f")
        elif tier == "PRATA":
            self.card.config(highlightbackground="#cbd5e1")
            self.badge_lbl.config(text="🥈 PROVÁVEL PRATA", fg="#e2e8f0", bg="#202938")
            self.tip_lbl.config(text=f"Troféu médio, distante de {dia_min:.2f}", fg="#94a3b8")
        elif tier == "BRONZE":
            self.card.config(highlightbackground="#cd7f32")
            self.badge_lbl.config(text="🥉 PROVÁVEL BRONZE", fg="#d38b5d", bg="#2b1a0d")
            self.tip_lbl.config(text="Animal de porte pequeno / pontuação básica.", fg="#a0aec0")
        else:
            self.card.config(highlightbackground="#00d2d3")
            self.badge_lbl.config(text="🔍 ANIMAL AVISTADO", fg="#00d2d3", bg="#0f1f2e")
            self.tip_lbl.config(text=f"Mínimo para Diamante: {dia_min:.2f}+", fg="#e2e8f0")
            
        if not self.is_visible:
            self.card.place(x=0, y=0, width=self.overlay_w, height=self.overlay_h)
            self.is_visible = True

    def ui_refresh_loop(self):
        """Auto-hide when animal spotting box is closed"""
        now = time.time()
        auto_hide_delay = CONFIG.get("auto_hide_delay_seconds", 2.5)
        
        if self.is_visible and (now - self.last_detection_time > auto_hide_delay):
            if not self.calibration_mode:
                self.card.place_forget()
                self.is_visible = False
                
        self.root.after(100, self.ui_refresh_loop)

    def run(self):
        print("\n=======================================================")
        print("  theHunter: COTW - Overlay HUD Ativo!")
        print("  - Abra o jogo e coloque em: Janela Sem Bordas (Borderless).")
        print("  - Aponte a luneta/binóculo para qualquer animal.")
        print("  - O HUD avaliará instantaneamente se ele é DIAMANTE!")
        print("  - Feche esta janela para encerrar o overlay.")
        print("=======================================================\n")
        self.root.mainloop()

if __name__ == "__main__":
    app = COTWOverlayApp()
    app.run()
