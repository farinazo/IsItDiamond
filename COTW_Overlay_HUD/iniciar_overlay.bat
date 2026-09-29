@echo off
chcp 65001 > nul
title theHunter: COTW - In-Game Overlay HUD
color 0b

echo ======================================================================
echo       theHunter: Call of the Wild - In-Game Overlay HUD v1.0
echo ======================================================================
echo.
echo Verificando dependências...
python -m pip install --quiet winocr pillow

echo.
echo Iniciando Overlay...
echo LEMBRETE: Coloque o seu jogo em modo 'Janela Sem Bordas' (Borderless).
echo.
python cotw_overlay.py

pause
