================================================================================
   theHunter: Call of the Wild - In-Game Overlay HUD (Approach 1) v1.0
================================================================================

Real-time In-Game Transparent Overlay HUD for theHunter: Call of the Wild.

HOW IT WORKS:
- Runs in the background and creates a transparent, click-through HUD over the game.
- Monitors the spotting HUD area when you aim with binoculars or scopes.
- When an animal and its score estimate (e.g. "235 - 268") are detected,
  it instantly computes whether it qualifies for Diamond and renders a floating badge:
    💎 POTENTIAL DIAMOND! (or 💎 GUARANTEED DIAMOND!)
    🥇 LIKELY GOLD
    🥈 LIKELY SILVER
    🥉 LIKELY BRONZE
- Displays exact minimum score for Diamond, max level, and required ammo class.
- Automatically disappears when you stop spotting the animal.
- 100% click-through: mouse clicks and keystrokes pass directly to the game.

--------------------------------------------------------------------------------
GAME DISPLAY REQUIREMENT:
--------------------------------------------------------------------------------
In theHunter: Call of the Wild:
1. Open in-game Settings -> Video.
2. Change Display Mode from "Fullscreen" to:
   "BORDERLESS" (or Borderless Windowed).

Why?
In Borderless mode, the game covers your entire monitor (looks identical to fullscreen),
while allowing Windows to draw the transparent overlay smoothly on top without
risky DLL memory injection.

--------------------------------------------------------------------------------
HOW TO RUN:
--------------------------------------------------------------------------------
1. Double-click "iniciar_overlay.bat".
2. The console window will confirm the overlay is active and monitoring.
3. In-game, aim your binoculars or scope at any animal.
4. The HUD card will automatically appear next to the in-game spotting box!

--------------------------------------------------------------------------------
CONFIGURATION (config.json):
--------------------------------------------------------------------------------
You can adjust screen positioning in "config.json":
- "pos_x_percent": Horizontal screen position (default: 0.68)
- "pos_y_percent": Vertical screen position (default: 0.46)
- "language": "pt" or "en"

Happy hunting! 💎🎯
================================================================================
