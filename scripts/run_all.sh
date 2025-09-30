#!/bin/bash
# Run all password strength checks

echo "[*] Running pwscore..."
while IFS= read -r pw; do
  score=$(printf "%s" "$pw" | pwscore 2>/dev/null || echo "FAILED")
  printf "%s\t%s\n" "$pw" "$score"
done < passwords.txt > results_pwscore.tsv

echo "[*] Running cracklib-check..."
while IFS= read -r pw; do
  printf "%s\n" "$pw" | cracklib-check
done < passwords.txt > results_cracklib.txt

echo "[*] Running zxcvbn..."
python3 scripts/zxcvbn_check.py > results_zxcvbn.jsonl

echo "[*] (Optional) Running HaveIBeenPwned check..."
python3 scripts/pwned_check.py > results_pwned.txt

echo "[*] Done. See results_* files."
