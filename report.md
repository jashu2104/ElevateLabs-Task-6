# Report — Task 6: Create a Strong Password and Evaluate Its Strength

## Objective
To practice generating and evaluating passwords using multiple tools on Kali Linux, and to learn password best practices. (Based on the given task brief.)

## Tools Used
- `pwscore` (libpwquality) — evaluates password strength from 0–100.
- `cracklib-check` — detects dictionary words / patterns in passwords.
- `zxcvbn` (Python library) — realistic strength estimator with feedback.
- HaveIBeenPwned (k-anonymity API) — checks if a password appears in breach databases.

## Method
1. Created `passwords.txt` with multiple example passwords.
2. Tested them with `pwscore`, `cracklib-check`, and `zxcvbn`.
3. Optionally queried HaveIBeenPwned API for breach counts.
4. Collected results into structured outputs (TSV/JSON).
5. Summarized findings and recommendations.

## Results (example, not actual run)
| Password                  | pwscore | cracklib        | zxcvbn_score | Pwned Count |
|----------------------------|---------|-----------------|--------------|-------------|
| password123               | 0       | dictionary word | 0            | 100000+     |
| Summer2025                | 15      | dictionary word | 1            | 5000        |
| P@ssw0rd!                 | 20      | dictionary word | 1            | 200000+     |
| CorrectHorseBatteryStaple  | 80      | OK              | 4            | 0           |

(Your actual results will vary when you run the tools.)

## Analysis
- Short or dictionary-based passwords fail both pwscore and cracklib.
- Simple substitutions (`P@ssw0rd!`) are weak and often breached.
- Long passphrases (e.g., `CorrectHorseBatteryStaple`) score high and resist attacks.
- Checking against known breaches is essential.

## Recommendations
- Use passphrases ≥ 12–16 characters.
- Avoid dictionary words and personal info.
- Do not reuse passwords across sites.
- Use a password manager to generate and store strong, unique passwords.
- Enable multi-factor authentication (MFA).

## Short Interview Answers
- **Strong password** = long, random, unique, not breached.
- **Common attacks** = brute force, dictionary, credential stuffing, rainbow tables.
- **Length matters** = each extra char exponentially increases difficulty.
- **Dictionary attack** = guesses common words instead of all possibilities.
- **MFA** = combines password with token/biometric, making compromise harder.
- **Password managers** = store/generate strong passwords, reduce reuse.
- **Passphrases** = easy-to-remember multi-word strings with high entropy.
- **Common mistakes** = reusing, short/simple passwords, personal details.

## Screenshots
Screenshots of commands and results should be placed in `screenshots/` folder.
