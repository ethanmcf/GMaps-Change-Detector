#!/bin/bash
python3 src/db_handler.py
exit_code=$?

if [ $exit_code -eq 0 ]; then
  echo "Run recently detector.py. Skipping."
else
  echo "Running detector.py..."
  python src/detector.py
fi