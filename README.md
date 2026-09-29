# 🦌 theHunter: Call of the Wild - Diamond Trophy Indicator & Companion HUD

> **Mod Oficial de Indicador de Pontuação Diamante, Níveis e HUD Overlay para o jogo theHunter: Call of the Wild.**  
> Compatível com todas as 19 reservas e 130 animais do jogo (incluindo as DLCs mais recentes como Salzwiesen Park, Sundarpatan e Intisuyu).

---

## 🌟 Recursos Principais

1. **Abordagem 1: Overlay HUD em Tempo Real (`COTW_Overlay_HUD/`)**
   - Janela flutuante e translúcida (always-on-top) com atalho de teclado `F8`.
   - Busca instantânea por nome do animal (Português ou Inglês).
   - Calculadora integrada de probabilidade de Diamante com base na estimativa de avistamento (*Spotting*).
   - Mostra a pontuação mínima para Diamante, nível máximo e a **Classe de Munição (1 a 9)** para não falhar o *Harvest Check*.

2. **Abordagem 2: Mod Nativo no Jogo via Dropzone (`COTW_Diamond_Trophy_Mod/`)**
   - Altera diretamente as strings do jogo ao avistar ou rastrear qualquer animal com binóculos ou lunetas.
   - Disponível em **3 opções de exibição**:
     * **Opção 1 (Padrão): Compacto sem a palavra Diamante**  
       Ex: `CABRA-DA-MONTANHA [83.2+ | Nvl 5]` / `RED DEER [251.07+ | Lvl 9 (GO)]`
     * **Opção 2: Linha Abaixo do Nome (com quebra de linha `\n`)**  
       Ex: `CABRA-DA-MONTANHA`  
       `[83.2+ | Nvl 5]`
     * **Opção 3: Ultra Compacto (Apenas Pontuação)**  
       Ex: `CABRA-DA-MONTANHA [83.2+]`
   - Suporte multilíngue nativo (Português e Inglês atualizados).

3. **Guia Visual Interativo & Calculadora (`Guia_Visual_Diamantes_COTW.html`)**
   - Página interativa completa que pode ser aberta no navegador ou celular.
   - Filtros por Reserva (todas as 19 reservas), Classe (1 a 9) e busca rápida.
   - Calculadora interativa de medalhas (Bronze, Prata, Ouro, Diamante).

---

## 🛠️ Instalação do Mod Nativo (Dropzone)

1. Extraia o conteúdo de `COTW_Diamond_Trophy_Mod.zip` (ou use a pasta `COTW_Diamond_Trophy_Mod/dropzone/`).
2. Copie a pasta `dropzone` para a pasta raiz do seu jogo:
   - **Steam:** `C:\Program Files (x86)\Steam\steamapps\common\theHunterCotW\`
   - **Epic Games:** `C:\Program Files\Epic Games\theHunterCotW\`
3. Ative o parâmetro de inicialização:
   - **Steam:** Clique com botão direito em theHunter: COTW > *Propriedades* > *Opções de Inicialização* e cole:
     ```text
     --vfs-fs dropzone --vfs-archive patch_win64 --vfs-archive archives_win64 --vfs-fs.
     ```
   - **Epic Games:** Abra a Epic Games > *Configurações* > role até o final em theHunter: COTW > marque *Linha de comando adicional* e cole o texto acima.
4. Para trocar entre as 3 opções de visualização, basta copiar a pasta `dropzone` de dentro de `OPCOES_MOD/<opcao_desejada>/` e sobrescrever na pasta do jogo.

---

## 💻 Instalação do Overlay HUD

1. Entre na pasta `COTW_Overlay_HUD/`.
2. Dê um duplo clique em `iniciar_overlay.bat`.
3. Pressione **F8** para mostrar ou ocultar o painel durante o jogo.

---

## 📊 Reservas Suportadas (130 Espécies Validadas)

- **Layton Lake District**
- **Hirschfelden Hunting Reserve**
- **Medved-Taiga National Park**
- **Vurhonga Savanna**
- **Parque Fernando**
- **Yukon Valley**
- **Cuatro Colinas Game Reserve**
- **Silver Ridge Peaks**
- **Te Awaroa National Park**
- **Rancho del Arroyo**
- **Mississippi Acres Preserve**
- **Revontuli Coast**
- **New England Mountains**
- **Emerald Coast**
- **Sundarpatan**
- **Salzwiesen Park**
- **Askiy Ridge Hunting Preserve**
- **Intisuyu**
- **Tòrr nan Sithean**

---

## 📝 Auditoria e Validação dos Dados

Todas as pontuações foram auditadas e validadas diretamente contra a **Wiki Oficial do theHunter: Call of the Wild** e conferidas nos arquivos de dados binários internos do jogo (`codex_data.bin` e `animal_settings.bin`). Correções notáveis incluem:
- *Urso-de-Óculos (Spectacled Bear)*: Corrigido de 26.45 para **20.45**
- *Cabra-da-Montanha (Mountain Goat)*: Corrigido de 107.67 para **83.20**
- *Codorna-dos-Restolhos (Stubble Quail)*: Corrigido de 238.0 para **126.0**
- *Ganso-Pega (Magpie Goose)*: Corrigido de 3.85 para **3.02**
- *Jaguatirica (Ocelot)*: Dificuldade máxima corrigida para **Nível 9 (Lendário)**
- Atualizadas as classes de integridade e munição de 16 animais pós-rebalanceamento de armas.

---

## 📄 Licença & Isenção de Responsabilidade

* Este projeto é um mod e ferramenta de fã criado pela comunidade para aprimorar a experiência de jogo.
* theHunter: Call of the Wild é marca registrada da Expansive Worlds AB e Avalanche Studios.
