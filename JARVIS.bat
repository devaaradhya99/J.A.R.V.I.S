@echo off
title J.A.R.V.I.S - Voice Assistant
cd /d D:\JARVIS

echo Starting Ollama AI engine...
start /min "" "C:\Users\Nice\AppData\Local\Programs\Ollama\ollama.exe" serve
timeout /t 5 /nobreak >nul

echo Starting JARVIS...
"C:\Users\Nice\AppData\Local\Programs\Python\Python313\python.exe" jarvis.py
pause
