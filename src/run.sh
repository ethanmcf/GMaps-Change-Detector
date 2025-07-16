#!/bin/bash

if [ "$1" == "loop" ]; then
  while true; do
    python3 src/detector.py
    sleep 86400  # 24 * 60 * 60 seconds = 24 hours
  done
else
  python3 src/db_handler.py
  exit_code=$?

  if [ $exit_code -eq 0 ]; then
    echo "Run recently detector.py. Skipping."
  else
    echo "Running detector.py..."
    python src/detector.py
  fi
fi

