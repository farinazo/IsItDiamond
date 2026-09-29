================================================================================
     theHunter: Call of the Wild - Native Diamond Trophy Mod v2.0
================================================================================

This mod natively updates the in-game HUD for all 130 species to show their
minimum DIAMOND trophy score requirement and species MAX LEVEL when spotting.

--------------------------------------------------------------------------------
CHOOSE YOUR PREFERRED VERSION ("OPCOES_MOD" FOLDER):
--------------------------------------------------------------------------------

Inside "OPCOES_MOD", you have 3 ready-to-use choices:

1. OPTION 1 - COMPACT (DEFAULT INSTALLED IN "dropzone"):
   Removes the word "DIAMOND:" to keep the species name concise.
   Example:
     RED DEER [251.07+ | Lvl 9 (GO)]
     VEADO-VERMELHO [251.07+ | Nvl 9 (GO)]

2. OPTION 2 - NEWLINE BELOW NAME:
   Uses a newline (\n) so trophy requirements appear on a dedicated second line
   directly below the species name!
   Example:
     RED DEER
     [251.07+ | Lvl 9 (GO)]

3. OPTION 3 - ULTRA COMPACT (SCORE ONLY):
   Displays only the minimum diamond score in brackets.
   Example:
     RED DEER [251.07+]
     VEADO-VERMELHO [251.07+]

* Note: The (GO) tag indicates the species has a Great One (Fabled) variant.

--------------------------------------------------------------------------------
HOW TO INSTALL
--------------------------------------------------------------------------------

STEP 1: Copy the "dropzone" folder
  - By default, the root "dropzone" folder is loaded with OPTION 1 (Compact).
  - If you prefer Option 2 or 3, open the corresponding folder inside "OPCOES_MOD"
    and copy that "dropzone" folder instead.
  - Paste the "dropzone" folder into your main game directory:
    Steam: ...\steamapps\common\theHunterCotW\

  The target file path is:
  ...\theHunterCotW\dropzone\settings\hp_settings\string_ids.stringlookup


STEP 2: Set Steam Launch Options
  1. Open Steam -> Library.
  2. Right-click "theHunter: Call of the Wild" -> Properties.
  3. Under General -> LAUNCH OPTIONS, paste:

  --vfs-fs dropzone --vfs-archive patch_win64 --vfs-archive archives_win64 --vfs-fs .

  4. Close Properties.


STEP 3: Launch the Game!
  Spot any animal with binoculars or scopes to see its diamond score requirement!


--------------------------------------------------------------------------------
HOW TO UNINSTALL
--------------------------------------------------------------------------------
Delete the "dropzone" folder from your game directory.
Original game files are never altered.

Happy hunting! 💎🎯
================================================================================
