# Password Strength Evaluation — Task 6

This repo contains my work for Task 6: Create a Strong Password and Evaluate Its Strength.

## What I did
- Created multiple password samples (see `passwords.txt`)
- Evaluated with `pwscore` (libpwquality), `cracklib-check`, and `zxcvbn` (Python)
- Checked breach status via HaveIBeenPwned k-anonymity API (optional)
- Collected results into CSV / JSONL for reporting and screenshots

## How to reproduce (Kali)
1. `sudo apt update && sudo apt install -y libpwquality-tools cracklib-runtime git python3-pip`
2. `pip3 install --user zxcvbn-python requests`
3. `./scripts/run_all.sh`

## Deliverables
- `report.md` — results, observations, recommendations
- `screenshots/` — UI screenshots
