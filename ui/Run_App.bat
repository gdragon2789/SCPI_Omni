@echo off
call ..\.venv\Scripts\activate.bat
start "" ..\.venv\Scripts\pythonw.exe BK9129B.py
deactivate
exit
