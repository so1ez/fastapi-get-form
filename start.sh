#!/bin/bash

sleep 10

echo "sleep is over"

python3 src/database.py

python3 -m pytest src

uvicorn src.main:app --host 0.0.0.0 --port 8000

echo "script end"