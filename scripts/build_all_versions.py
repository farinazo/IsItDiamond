import sys, os, io, struct, json
sys.path.insert(0, r'C:\Users\Bolt\.gemini\antigravity\brain\a364eab8-5d66-45d0-aa69-f8fb75050f46\scratch')
sys.path.append(r'C:\Users\Bolt\.gemini\antigravity\brain\a364eab8-5d66-45d0-aa69-f8fb75050f46\scratch\deca\python\deca')
from deca.ff_adf import Adf
from deca.file import ArchiveFile
from test_deca_hash import hash32

ORIGINAL_LOOKUP = r'D:\coding\TheHunterCOTWTrophyChart\_BACKUP_ORIGINAIS\string_ids.stringlookup'
MATCHED_ANIMALS = r'C:\Users\Bolt\.gemini\antigravity\brain\a364eab8-5d66-45d0-aa69-f8fb75050f46\scratch\matched_animals.json'

with open(MATCHED_ANIMALS, 'r', encoding='utf-8') as f:
    animals = json.load(f)
animal_map = {int(a['hash']): a for a in animals}

lang_pair_offsets = [
    448, 1413504, 2826560, 4239616, 5652672,
    7065728, 8478784, 9891840, 11304896, 12717952
]

def generate_mod_version(mode_name, formatter_func, output_file_path):
    print(f"\n==========================================")
    print(f"Generating version: {mode_name}")
    print(f"Destination: {output_file_path}")
    
    with open(ORIGINAL_LOOKUP, 'rb') as f:
        raw = bytearray(f.read())
        
    buf = ArchiveFile(io.BytesIO(bytes(raw)))
    adf = Adf()
    adf.deserialize(buf)
    
    val = adf.table_instance_values[0]
    languages = val['Languages']
    text_buf = val['Text']
    
    text_base = 14131008
    orig_text_len = struct.unpack('<I', raw[120:124])[0]
    text_end = text_base + orig_text_len
    
    new_strings_bytes = bytearray()
    updates = []
    
    for lang_idx, lang in enumerate(languages):
        pairs = lang['SortedPairs']
        for p_idx, p in enumerate(pairs):
            h = int(p['Hash'])
            if h in animal_map:
                anim = animal_map[h]
                off = int(p['TextOffset'])
                end = text_buf.find(b'\x00', off)
                orig_text = text_buf[off:end].decode('utf-8', errors='ignore').strip()
                
                dia = anim['diamond_min']
                lvl = anim['max_level']
                lvl_clean = lvl.replace(' (10 Fabled)', ' (GO)') if '(10 Fabled)' in lvl else lvl
                
                mod_text = formatter_func(orig_text, dia, lvl_clean, lang_idx)
                
                encoded = mod_text.encode('utf-8') + b'\x00'
                rel_offset = orig_text_len + len(new_strings_bytes)
                new_strings_bytes.extend(encoded)
                
                updates.append((lang_idx, p_idx, rel_offset, mod_text))
                
    added_bytes = len(new_strings_bytes)
    
    # Insert text
    raw[text_end:text_end] = new_strings_bytes
    
    # Update length
    struct.pack_into('<I', raw, 120, orig_text_len + added_bytes)
    
    # Update headers
    for hdr_off in [12, 20, 28, 36, 40]:
        v = struct.unpack('<I', raw[hdr_off:hdr_off+4])[0]
        struct.pack_into('<I', raw, hdr_off, v + added_bytes)
        
    new_inst_off = struct.unpack('<I', raw[12:16])[0]
    inst_sz = struct.unpack('<I', raw[new_inst_off + 12:new_inst_off + 16])[0]
    struct.pack_into('<I', raw, new_inst_off + 12, inst_sz + added_bytes)
    
    # Update SortedPairs
    for lang_idx, p_idx, rel_offset, mod_text in updates:
        pair_off = lang_pair_offsets[lang_idx] + p_idx * 8
        struct.pack_into('<I', raw, pair_off + 4, rel_offset)
        
    os.makedirs(os.path.dirname(output_file_path), exist_ok=True)
    with open(output_file_path, 'wb') as f:
        f.write(raw)
        
    print(f"File saved: {len(raw)} bytes.")
    
    # Verify with ADF deserializer
    buf_v = ArchiveFile(io.BytesIO(bytes(raw)))
    adf_v = Adf()
    adf_v.deserialize(buf_v)
    v_langs = adf_v.table_instance_values[0]['Languages']
    v_text = adf_v.table_instance_values[0]['Text']
    
    h_reddeer = hash32('animal_reddeer_name')
    for lang_i, l_name in [(0, 'EN'), (7, 'PT')]:
        for p in v_langs[lang_i]['SortedPairs']:
            if int(p['Hash']) == h_reddeer:
                o = int(p['TextOffset'])
                e = v_text.find(b'\x00', o)
                sample = repr(v_text[o:e].decode('utf-8'))
                print(f"Sample {l_name}: {sample}")
                break
    print(f"Version {mode_name} verified successfully!")

# Formatters:

# 1. Version 1: Compact (No "DIAMANTE: " or "DIAMOND: ")
def fmt_compact(orig, dia, lvl, lang_idx):
    if lang_idx == 7: # PT
        return f"{orig} [{dia}+ | Nvl {lvl}]"
    else: # EN & others
        return f"{orig} [{dia}+ | Lvl {lvl}]"

# 2. Version 2: Newline Below Name
def fmt_newline(orig, dia, lvl, lang_idx):
    if lang_idx == 7: # PT
        return f"{orig}\n[{dia}+ | Nvl {lvl}]"
    else: # EN & others
        return f"{orig}\n[{dia}+ | Lvl {lvl}]"

# 3. Version 3: Ultra Compact (Score Only)
def fmt_score_only(orig, dia, lvl, lang_idx):
    return f"{orig} [{dia}+]"

base_mod_dir = r'D:\coding\TheHunterCOTWTrophyChart\COTW_Diamond_Trophy_Mod'

# Generate Versão 1: Compacta (Also sets as the default dropzone)
generate_mod_version(
    "1. Compacta (Sem 'DIAMANTE:')",
    fmt_compact,
    os.path.join(base_mod_dir, "dropzone", "settings", "hp_settings", "string_ids.stringlookup")
)
generate_mod_version(
    "1. Compacta (Sem 'DIAMANTE:') [Pasta Opção]",
    fmt_compact,
    os.path.join(base_mod_dir, "OPCOES_MOD", "1_COMPACTO_SEM_DIAMANTE", "dropzone", "settings", "hp_settings", "string_ids.stringlookup")
)

# Generate Versão 2: Nova Linha Abaixo do Nome
generate_mod_version(
    "2. Linha Abaixo do Nome (com quebra de linha)",
    fmt_newline,
    os.path.join(base_mod_dir, "OPCOES_MOD", "2_LINHA_ABAIXO_DO_NOME", "dropzone", "settings", "hp_settings", "string_ids.stringlookup")
)

# Generate Versão 3: Ultra Compacto (Apenas Pontuação)
generate_mod_version(
    "3. Ultra Compacto (Apenas Pontuação)",
    fmt_score_only,
    os.path.join(base_mod_dir, "OPCOES_MOD", "3_APENAS_PONTUACAO", "dropzone", "settings", "hp_settings", "string_ids.stringlookup")
)

print("\nALL VERSIONS GENERATED SUCCESSFULLY!")
