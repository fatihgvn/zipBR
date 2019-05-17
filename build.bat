@echo off

rmdir /s /q __pycache__
rmdir /s /q dist
rmdir /s /q build
del zipBR.exe
del zipBR.spec

timeout 1

pyinstaller --onefile zipBR.py
