@echo off
:: Variables
set filename="genius"

:: Does the Compiler thing
pyinstaller index.py --onefile --name %filename%.exe

:: Copy compiled file to root
del %filename%.exe
copy dist\%filename%.exe .
