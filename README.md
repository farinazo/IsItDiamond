# 💎 IsItDiamond - theHunter: Call of the Wild Diamond Trophy Mod

> **Mod in-game nativo para theHunter: Call of the Wild que mostra a pontuação mínima de Diamante e nível máximo diretamente na luneta/binóculos ao avistar qualquer animal!**  
> 100% auditado e validado para **todas as 19 reservas** e **130 animais** do jogo (incluindo as DLCs Salzwiesen Park, Sundarpatan e Intisuyu).

[![Nexus Mods](https://img.shields.io/badge/Nexus_Mods-Em_Breve-orange?logo=nexusmods)](https://www.nexusmods.com/thehuntercallofthewild)  
> 📢 **Aviso:** Em breve este mod estará disponível para download direto também no **Nexus Mods**!

---

## 🌟 O que o Mod faz?

Ao avistar ou rastrear qualquer animal com binóculos ou mira no jogo, o mod exibe automaticamente ao lado do nome do animal a **pontuação mínima para Diamante** e seu **nível máximo de dificuldade**:

* **Exemplo 1 (Geral):** `CABRA-DA-MONTANHA [83.2+ | Nvl 5]` / `RED DEER [251.07+ | Lvl 9 (GO)]`
* **Exemplo 2 (GO / Great One):** Animais com variante *Great One* recebem a indicação especial `(GO)`!
* **Exemplo 3 (Fichas Oficiais):** Todos os dados foram extraídos e corrigidos diretamente das tabelas de colheita oficiais e binários internos do jogo.

---

## 🎨 3 Opções de Visualização Disponíveis

O mod já vem pronto para você escolher o estilo que preferir dentro da pasta `OPCOES_MOD/`:

1. **Opção 1: Compacto sem a palavra Diamante (Padrão Instalado)**  
   * Exibe: `CABRA-DA-MONTANHA [83.2+ | Nvl 5]` ou `RED DEER [251.07+ | Lvl 9 (GO)]`
   * Remove a palavra "DIAMANTE: " para deixar a interface limpa e elegante.

2. **Opção 2: Linha Abaixo do Nome (com quebra de linha `\n`)**  
   * Exibe o nome do animal na primeira linha e as informações logo abaixo:  
     `CABRA-DA-MONTANHA`  
     `[83.2+ | Nvl 5]`

3. **Opção 3: Ultra Compacto (Apenas Pontuação)**  
   * Exibe apenas a pontuação mínima para Diamante:  
     `CABRA-DA-MONTANHA [83.2+]`

---

## 🛠️ Como Instalar no Jogo

### Passo 1: Copiar os arquivos
1. Baixe ou use a pasta `COTW_Diamond_Trophy_Mod/dropzone/` (ou extraia `COTW_Diamond_Trophy_Mod.zip`).
2. Copie a pasta `dropzone` para a pasta raiz onde seu theHunter está instalado:
   * **Steam:** `C:\Program Files (x86)\Steam\steamapps\common\theHunterCotW\`
   * **Epic Games:** `C:\Program Files\Epic Games\theHunterCotW\`

*(Para trocar de opção, basta copiar a pasta `dropzone` de dentro de `OPCOES_MOD/<sua_opcao_preferida>/` e colar na pasta do jogo sobrescrevendo).*

### Passo 2: Ativar no Inicializador do Jogo
Para que o theHunter carregue arquivos modificados, é obrigatório adicionar o parâmetro de inicialização:

* **Na Steam:**
  1. Clique com o botão direito no **theHunter: Call of the Wild** na sua biblioteca da Steam e selecione **Propriedades...**
  2. Na aba **Geral**, encontre o campo **Opções de Inicialização** no final da página.
  3. Cole exatamente o seguinte comando:
     ```text
     --vfs-fs dropzone --vfs-archive patch_win64 --vfs-archive archives_win64 --vfs-fs.
     ```

* **Na Epic Games:**
  1. Abra o inicializador da Epic Games e clique no seu perfil / **Configurações**.
  2. Role até a seção de jogos instalados e clique em **theHunter: Call of the Wild**.
  3. Marque a caixa **Linha de comando adicional** e cole:
     ```text
     --vfs-fs dropzone --vfs-archive patch_win64 --vfs-archive archives_win64 --vfs-fs.
     ```

---

## 🧭 Guia Visual Interativo & Calculadora

O projeto acompanha o arquivo **[`Guia_Visual_Diamantes_COTW.html`](COTW_Diamond_Trophy_Mod/Guia_Visual_Diamantes_COTW.html)**:
* Abra no seu navegador do PC ou no celular.
* Pesquise rapidamente por qualquer animal.
* Filtre por Reserva ou Classe de Calibre (1 a 9).
* Use a calculadora embutida para digitar a estimativa de peso/troféu que você avistou e saber na hora se tem chance real de ser Diamante, Ouro ou Prata!

---

## 🗺️ Reservas Auditadas e Suportadas (130 Espécies)

Todas as 19 reservas do jogo têm cobertura completa:
* **Layton Lake District** (9 espécies)
* **Hirschfelden Hunting Reserve** (9 espécies)
* **Medved-Taiga National Park** (8 espécies)
* **Vurhonga Savanna** (10 espécies)
* **Parque Fernando** (8 espécies)
* **Yukon Valley** (8 espécies)
* **Cuatro Colinas Game Reserve** (11 espécies)
* **Silver Ridge Peaks** (9 espécies)
* **Te Awaroa National Park** (9 espécies)
* **Rancho del Arroyo** (10 espécies)
* **Mississippi Acres Preserve** (10 espécies)
* **Revontuli Coast** (19 espécies)
* **New England Mountains** (15 espécies)
* **Emerald Coast** (14 espécies)
* **Sundarpatan** (13 espécies)
* **Salzwiesen Park** (15 espécies)
* **Askiy Ridge Hunting Preserve** (19 espécies)
* **Intisuyu** (14 espécies)
* **Tòrr nan Sithean** (17 espécies)

---

## 🔬 Auditoria de Dados & Correções Notáveis

Diferente de tabelas genéricas da internet que possuem erros de digitação e dados defasados, todas as 130 espécies foram auditadas contra os binários do jogo (`codex_data.bin`, `animal_settings.bin`) e as fichas oficiais de colheita:
* **Urso-de-Óculos (*Spectacled Bear*)**: Corrigido de 26.45 para **`20.45`** (o site de origem havia errado a digitação).
* **Cabra-da-Montanha (*Mountain Goat*)**: Corrigido de 107.67 para **`83.20`** (ajuste pós-TruRACs).
* **Codorna-dos-Restolhos (*Stubble Quail*)**: Corrigido de 238.0 para **`126.0`** (o site havia duplicado da Bobwhite Quail).
* **Ganso-Pega (*Magpie Goose*)**: Corrigido de 3.85 para **`3.02`** (o site havia duplicado do Greylag Goose).
* **Jaguatirica (*Ocelot*)**: Nível máximo corrigido para **`Nível 9 (Lendário)`**.
* Ajustes de precisão para *Galinhola-Euroasiática* (`41.03`), *Carneiro-Bighorn* (`196.93`), *Sambar* (`166.24`) e *Corço* (`81.86`).

---

## 📜 Licença e Isenção de Responsabilidade

* Mod desenvolvido para a comunidade de fãs de *theHunter: Call of the Wild*.
* theHunter: Call of the Wild® é marca registrada da Expansive Worlds AB e Avalanche Studios.
