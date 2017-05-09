#!/bin/bash
python3 ChardonayOrCabernet.py input1 > myOut

if diff myOut expectedOut; then
  echo "SUCCESS"
else
  echo "FAILED"
fi
