import json, os

with open(r'C:\Users\Bolt\.gemini\antigravity\brain\a364eab8-5d66-45d0-aa69-f8fb75050f46\scratch\matched_animals.json', 'r', encoding='utf-8') as f:
    animals = json.load(f)

# Sort animals by Portuguese name
animals_sorted = sorted(animals, key=lambda x: x['orig_pt'])

html_template = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>theHunter: COTW - Guia de Diamantes & Troféus (Mod Oficial)</title>
<style>
  :root {
    --bg-main: #0e1217;
    --bg-card: #181f2a;
    --bg-header: #121822;
    --accent-orange: #e67e22;
    --accent-diamond: #00d2d3;
    --accent-gold: #f1c40f;
    --accent-silver: #bdc3c7;
    --accent-bronze: #e17055;
    --accent-fabled: #9b59b6;
    --text-main: #ecf0f1;
    --text-muted: #8b9bb4;
    --border: #263244;
  }
  * { box-sizing: border-box; margin: 0; padding: 0; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; }
  body { background: var(--bg-main); color: var(--text-main); line-height: 1.5; padding: 20px; }
  .container { max-width: 1400px; margin: 0 auto; }
  
  header {
    background: linear-gradient(135deg, #182232, #0d131d);
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 25px;
    margin-bottom: 25px;
    box-shadow: 0 8px 24px rgba(0,0,0,0.5);
    position: relative;
    overflow: hidden;
  }
  header::after {
    content: '';
    position: absolute;
    top: 0; right: 0; width: 300px; height: 100%;
    background: radial-gradient(circle, rgba(0,210,211,0.15) 0%, transparent 70%);
    pointer-events: none;
  }
  h1 { font-size: 28px; color: #fff; margin-bottom: 8px; display: flex; align-items: center; gap: 12px; }
  h1 span.badge { background: var(--accent-orange); color: #fff; font-size: 13px; font-weight: 700; padding: 3px 10px; border-radius: 20px; text-transform: uppercase; }
  p.subtitle { color: var(--text-muted); font-size: 15px; margin-bottom: 15px; }
  
  .mod-banner {
    background: rgba(0, 210, 211, 0.1);
    border: 1px solid rgba(0, 210, 211, 0.3);
    border-radius: 8px;
    padding: 12px 16px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    flex-wrap: wrap;
    gap: 10px;
  }
  .mod-banner .txt { font-size: 14px; color: #d0f7f7; }
  .mod-banner .btn {
    background: var(--accent-orange);
    color: #fff;
    padding: 8px 16px;
    border-radius: 6px;
    text-decoration: none;
    font-weight: 600;
    font-size: 13px;
    cursor: pointer;
    border: none;
    transition: 0.2s;
  }
  .mod-banner .btn:hover { background: #d35400; }
  
  /* Calculator Section */
  .calc-card {
    background: var(--bg-card);
    border: 1px solid var(--border);
    border-radius: 10px;
    padding: 20px;
    margin-bottom: 25px;
    box-shadow: 0 4px 15px rgba(0,0,0,0.3);
  }
  .calc-card h2 { font-size: 18px; margin-bottom: 12px; color: var(--accent-diamond); display: flex; align-items: center; gap: 8px; }
  .calc-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 15px; align-items: end; }
  .calc-input-group label { display: block; font-size: 13px; color: var(--text-muted); margin-bottom: 6px; font-weight: 600; }
  .calc-input-group input, .calc-input-group select {
    width: 100%;
    padding: 10px 14px;
    background: #0f141c;
    border: 1px solid var(--border);
    border-radius: 6px;
    color: #fff;
    font-size: 15px;
    outline: none;
  }
  .calc-input-group input:focus, .calc-input-group select:focus { border-color: var(--accent-diamond); }
  .calc-result {
    background: #0f141c;
    border: 1px solid var(--border);
    border-radius: 6px;
    padding: 10px 15px;
    min-height: 44px;
    display: flex;
    align-items: center;
    font-size: 15px;
    font-weight: 700;
  }
  .calc-result.diamond { color: var(--accent-diamond); border-color: var(--accent-diamond); }
  .calc-result.gold { color: var(--accent-gold); border-color: var(--accent-gold); }
  .calc-result.silver { color: var(--accent-silver); }
  
  /* Filters */
  .controls-bar {
    display: flex;
    gap: 15px;
    flex-wrap: wrap;
    margin-bottom: 20px;
  }
  .search-box {
    flex: 1;
    min-width: 280px;
    position: relative;
  }
  .search-box input {
    width: 100%;
    padding: 12px 16px 12px 42px;
    background: var(--bg-card);
    border: 1px solid var(--border);
    border-radius: 8px;
    color: #fff;
    font-size: 15px;
    outline: none;
  }
  .search-box input:focus { border-color: var(--accent-orange); }
  .search-box::before {
    content: '🔍';
    position: absolute;
    left: 14px;
    top: 50%;
    transform: translateY(-50%);
    font-size: 16px;
    opacity: 0.6;
  }
  select.filter-select {
    padding: 12px 16px;
    background: var(--bg-card);
    border: 1px solid var(--border);
    border-radius: 8px;
    color: #fff;
    font-size: 14px;
    outline: none;
    cursor: pointer;
  }
  select.filter-select:focus { border-color: var(--accent-orange); }
  
  /* Table & Grid */
  .stats-counter { font-size: 13px; color: var(--text-muted); margin-bottom: 12px; }
  .table-container {
    background: var(--bg-card);
    border: 1px solid var(--border);
    border-radius: 10px;
    overflow-x: auto;
    box-shadow: 0 4px 15px rgba(0,0,0,0.3);
  }
  table { width: 100%; border-collapse: collapse; text-align: left; font-size: 14px; }
  th {
    background: var(--bg-header);
    color: var(--text-muted);
    font-weight: 600;
    text-transform: uppercase;
    font-size: 12px;
    letter-spacing: 0.5px;
    padding: 14px 18px;
    border-bottom: 2px solid var(--border);
    white-space: nowrap;
  }
  td { padding: 14px 18px; border-bottom: 1px solid var(--border); vertical-align: middle; }
  tr:hover td { background: rgba(255,255,255,0.03); }
  
  .animal-name { font-weight: 700; color: #fff; font-size: 15px; }
  .animal-en { font-size: 12px; color: var(--text-muted); }
  .class-pill {
    background: #232c3a;
    color: #e4e7eb;
    padding: 3px 10px;
    border-radius: 12px;
    font-size: 12px;
    font-weight: 600;
    display: inline-block;
  }
  .diamond-val {
    color: var(--accent-diamond);
    font-weight: 800;
    font-size: 15px;
    display: inline-flex;
    align-items: center;
    gap: 4px;
  }
  .level-badge {
    background: #1c2635;
    border: 1px solid #32445a;
    padding: 4px 10px;
    border-radius: 6px;
    font-size: 13px;
    font-weight: 600;
  }
  .fabled-badge {
    background: rgba(155, 89, 182, 0.2);
    border: 1px solid rgba(155, 89, 182, 0.5);
    color: #d7bde2;
    padding: 2px 7px;
    border-radius: 4px;
    font-size: 11px;
    font-weight: 700;
    margin-left: 5px;
  }
  .reserves-list { font-size: 12px; color: #a0aec0; max-width: 400px; line-height: 1.4; }
  
  /* Modal Installation */
  .modal-overlay {
    display: none;
    position: fixed;
    top: 0; left: 0; width: 100%; height: 100%;
    background: rgba(0,0,0,0.8);
    backdrop-filter: blur(4px);
    z-index: 999;
    align-items: center;
    justify-content: center;
    padding: 20px;
  }
  .modal-overlay.active { display: flex; }
  .modal-box {
    background: var(--bg-card);
    border: 1px solid var(--border);
    border-radius: 12px;
    max-width: 700px;
    width: 100%;
    padding: 25px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.7);
    max-height: 90vh;
    overflow-y: auto;
  }
  .modal-box h3 { font-size: 20px; color: #fff; margin-bottom: 15px; display: flex; justify-content: space-between; align-items: center; }
  .modal-close { background: none; border: none; color: var(--text-muted); font-size: 22px; cursor: pointer; }
  .step { background: #0f141c; border-left: 4px solid var(--accent-orange); padding: 12px 15px; margin-bottom: 12px; border-radius: 0 6px 6px 0; }
  .step strong { color: var(--accent-orange); display: block; margin-bottom: 4px; }
  .code-snip { background: #000; padding: 8px 12px; border-radius: 4px; font-family: monospace; font-size: 13px; color: #00d2d3; margin: 6px 0; word-break: break-all; display: block; }
</style>
</head>
<body>

<div class="container">

  <header>
    <h1>
      theHunter: Call of the Wild
      <span class="badge">Mod de Diamantes v1.0</span>
    </h1>
    <p class="subtitle">Guia Oficial & Mod Nativo de Troféus Diamante para todos os animais e reservas.</p>
    
    <div class="mod-banner">
      <div class="txt">
        🎮 <strong>Mod In-Game Ativo:</strong> Exibe a pontuação de Diamante e Nível Máximo na luneta/binóculo ao avistar qualquer animal!
      </div>
      <button class="btn" onclick="openModal()">📖 Como Instalar no Jogo</button>
    </div>
  </header>

  <!-- Simulação / Calculadora Rápida -->
  <div class="calc-card">
    <h2>🎯 Verificador Rápido de Diamante no Avistamento</h2>
    <div class="calc-grid">
      <div class="calc-input-group">
        <label for="calc-animal">Selecione o Animal:</label>
        <select id="calc-animal" onchange="calcEvaluate()">
          <!-- Populated by JS -->
        </select>
      </div>
      <div class="calc-input-group">
        <label for="calc-score">Pontuação Estimada (ex: 250 ou 250 - 270):</label>
        <input type="text" id="calc-score" placeholder="Ex: 260" oninput="calcEvaluate()">
      </div>
      <div class="calc-input-group">
        <label>Resultado da Avaliação:</label>
        <div id="calc-result" class="calc-result">Selecione um animal e digite a pontuação</div>
      </div>
    </div>
  </div>

  <!-- Controles de Busca e Filtro -->
  <div class="controls-bar">
    <div class="search-box">
      <input type="text" id="search-input" placeholder="Buscar por nome em português, inglês ou classe..." oninput="filterAnimals()">
    </div>
    
    <select id="reserve-filter" class="filter-select" onchange="filterAnimals()">
      <option value="">Todas as Reservas (19 Reservas)</option>
    </select>

    <select id="class-filter" class="filter-select" onchange="filterAnimals()">
      <option value="">Todas as Classes (1 a 9)</option>
      <option value="1">Classe 1 (Pequeno porte / Aves)</option>
      <option value="2">Classe 2 (Raposas, etc.)</option>
      <option value="3">Classe 3 (Veados pequenos, etc.)</option>
      <option value="4">Classe 4 (Javalis, etc.)</option>
      <option value="5">Classe 5 (Gamos, etc.)</option>
      <option value="6">Classe 6 (Veado-vermelho, etc.)</option>
      <option value="7">Classe 7 (Ursos, etc.)</option>
      <option value="8">Classe 8 (Alces, etc.)</option>
      <option value="9">Classe 9 (Grandes predadores / Bisões)</option>
    </select>
  </div>

  <div class="stats-counter" id="stats-counter">Exibindo 130 animais</div>

  <!-- Tabela de Animais -->
  <div class="table-container">
    <table>
      <thead>
        <tr>
          <th>Animal (Português / Inglês)</th>
          <th>Classe</th>
          <th>Nível Máx.</th>
          <th>Pontuação Mín. Diamante</th>
          <th>No Mod In-Game</th>
          <th>Reservas Onde Encontrar</th>
        </tr>
      </thead>
      <tbody id="animals-tbody">
        <!-- Rows inserted by JS -->
      </tbody>
    </table>
  </div>

</div>

<!-- Modal Instruções de Instalação -->
<div class="modal-overlay" id="installModal">
  <div class="modal-box">
    <h3>
      <span>🛠️ Instruções de Instalação do Mod</span>
      <button class="modal-close" onclick="closeModal()">&times;</button>
    </h3>
    
    <div class="step">
      <strong>Passo 1: Copiar a pasta 'dropzone'</strong>
      Copie a pasta <code>dropzone</code> que acompanha este mod para a pasta raiz onde o jogo está instalado na Steam:
      <code class="code-snip">C:\\SteamLibrary\\steamapps\\common\\theHunterCotW\\</code>
      <small style="color:var(--text-muted)">O arquivo ficará em: ...\\theHunterCotW\\dropzone\\settings\\hp_settings\\string_ids.stringlookup</small>
    </div>

    <div class="step">
      <strong>Passo 2: Ativar Parâmetro de Inicialização na Steam</strong>
      1. Abra a sua <strong>Steam</strong> e vá na <strong>Biblioteca</strong>.<br>
      2. Clique com o <strong>botão direito</strong> em <strong>theHunter: Call of the Wild</strong> e selecione <strong>Propriedades</strong>.<br>
      3. Na aba <strong>Geral</strong>, localize o campo <strong>Opções de Inicialização</strong> (Launch Options).<br>
      4. Cole o seguinte comando exatamente como abaixo:
      <code class="code-snip">--vfs-fs dropzone --vfs-archive patch_win64 --vfs-archive archives_win64 --vfs-fs .</code>
    </div>

    <div class="step">
      <strong>Passo 3: Jogar e Aproveitar!</strong>
      Abra o jogo. Ao mirar em qualquer animal com binóculo ou luneta, o nome exibirá automaticamente:
      <code class="code-snip">VEADO-VERMELHO [DIAMANTE: 251.07+ | Nvl 9 (GO)]</code>
    </div>

    <div class="step">
      <strong>Como Desinstalar:</strong>
      Basta apagar a pasta <code>dropzone</code> de dentro da pasta do jogo ou remover o comando das opções de inicialização na Steam.
    </div>

    <button class="btn" style="width:100%; padding:12px; margin-top:10px;" onclick="closeModal()">Entendido!</button>
  </div>
</div>

<script>
const animalsData = """ + json.dumps(animals_sorted, ensure_ascii=False) + """;

function init() {
  populateFilters();
  renderAnimals(animalsData);
  populateCalcSelect();
}

function populateFilters() {
  const reservesSet = new Set();
  animalsData.forEach(a => {
    a.reserves.forEach(r => reservesSet.add(r));
  });
  
  const reserveSelect = document.getElementById('reserve-filter');
  Array.from(reservesSet).sort().forEach(r => {
    const opt = document.createElement('option');
    opt.value = r;
    opt.textContent = r;
    reserveSelect.appendChild(opt);
  });
}

function populateCalcSelect() {
  const sel = document.getElementById('calc-animal');
  sel.innerHTML = '<option value="">-- Selecione o animal --</option>';
  animalsData.forEach(a => {
    const opt = document.createElement('option');
    opt.value = a.name_en;
    opt.textContent = `${a.orig_pt} (${a.orig_en})`;
    sel.appendChild(opt);
  });
}

function renderAnimals(list) {
  const tbody = document.getElementById('animals-tbody');
  tbody.innerHTML = '';
  
  document.getElementById('stats-counter').textContent = `Exibindo ${list.length} de ${animalsData.length} animais`;

  list.forEach(a => {
    const tr = document.createElement('tr');
    
    const isFabled = a.max_level.includes('Fabled');
    const fabledTag = isFabled ? '<span class="fabled-badge">⭐ Great One</span>' : '';
    const lvlClean = a.max_level.replace(' (10 Fabled)', ' (GO)');
    
    tr.innerHTML = `
      <td>
        <div class="animal-name">${a.orig_pt}</div>
        <div class="animal-en">${a.name_en}</div>
      </td>
      <td><span class="class-pill">Classe ${a.class}</span></td>
      <td><span class="level-badge">Nvl ${lvlClean}</span> ${fabledTag}</td>
      <td><span class="diamond-val">💎 ${a.diamond_min}+</span></td>
      <td><code style="color:#00d2d3; font-size:12px;">[DIAMANTE: ${a.diamond_min}+ | Nvl ${lvlClean}]</code></td>
      <td class="reserves-list">${a.reserves.join(', ')}</td>
    `;
    tbody.appendChild(tr);
  });
}

function filterAnimals() {
  const query = document.getElementById('search-input').value.toLowerCase().trim();
  const reserve = document.getElementById('reserve-filter').value;
  const cls = document.getElementById('class-filter').value;

  const filtered = animalsData.filter(a => {
    const matchQuery = !query || 
      a.orig_pt.toLowerCase().includes(query) ||
      a.orig_en.toLowerCase().includes(query) ||
      a.name_en.toLowerCase().includes(query) ||
      String(a.class).includes(query);
      
    const matchReserve = !reserve || a.reserves.includes(reserve);
    const matchClass = !cls || String(a.class) === cls;

    return matchQuery && matchReserve && matchClass;
  });

  renderAnimals(filtered);
}

function calcEvaluate() {
  const selAnimalName = document.getElementById('calc-animal').value;
  const scoreRaw = document.getElementById('calc-score').value.trim();
  const resDiv = document.getElementById('calc-result');

  if (!selAnimalName) {
    resDiv.className = 'calc-result';
    resDiv.textContent = 'Selecione um animal primeiro';
    return;
  }

  const animal = animalsData.find(a => a.name_en === selAnimalName);
  if (!animal) return;

  if (!scoreRaw) {
    resDiv.className = 'calc-result';
    resDiv.textContent = `Diamante mín: ${animal.diamond_min} (Nível Máx: ${animal.max_level})`;
    return;
  }

  // Parse score (could be '250', '240 - 260', etc)
  let val = 0;
  if (scoreRaw.includes('-')) {
    const parts = scoreRaw.split('-');
    val = parseFloat(parts[parts.length - 1].trim()) || 0;
  } else {
    val = parseFloat(scoreRaw) || 0;
  }

  if (val >= animal.diamond_min) {
    resDiv.className = 'calc-result diamond';
    resDiv.innerHTML = `💎 POTENCIAL DIAMANTE! (Estimativa máxima ${val} &ge; ${animal.diamond_min})`;
  } else if (val >= animal.diamond_min * 0.8) {
    resDiv.className = 'calc-result gold';
    resDiv.innerHTML = `🥇 Provável OURO (Estimativa ${val} &lt; ${animal.diamond_min})`;
  } else {
    resDiv.className = 'calc-result silver';
    resDiv.innerHTML = `🥈 Provável PRATA / BRONZE (Estimativa ${val} &lt; ${animal.diamond_min})`;
  }
}

function openModal() {
  document.getElementById('installModal').classList.add('active');
}

function closeModal() {
  document.getElementById('installModal').classList.remove('active');
}

window.onclick = function(event) {
  const modal = document.getElementById('installModal');
  if (event.target === modal) {
    closeModal();
  }
}

window.onload = init;
</script>

</body>
</html>
"""

guide_path = r'D:\coding\TheHunterCOTWTrophyChart\COTW_Diamond_Trophy_Mod\Guia_Visual_Diamantes_COTW.html'
with open(guide_path, 'w', encoding='utf-8') as f:
    f.write(html_template)

print(f"Generated visual guide: {guide_path}")
