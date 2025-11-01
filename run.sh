#!/bin/bash

if [ ! -d ".env" ]; then
    echo "env не найден. Создаю новый..."
    python3 -m venv .env
    echo "env успешно создан"
else
    echo "env найден, продолжаю..."
fi

.env/bin/pip3 install -r requirements.txt
.env/bin/python3 main.py