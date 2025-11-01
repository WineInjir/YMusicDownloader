@echo off

if not exist ".venv" (
    echo venv не найдено. Создаю новое...
    python -m venv .venv
    echo venv успешно создано
) else (
    echo venv найден, продолжаю...
)

if not exist "api.key" (
    type nul > api.key
)

call .venv\Scripts\activate.bat
pip install -r requirements.txt
python main.py
