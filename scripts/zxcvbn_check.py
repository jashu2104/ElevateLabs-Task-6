#!/usr/bin/env python3
from zxcvbn import zxcvbn
import json

with open('passwords.txt') as f:
    for pw in f:
        pw = pw.strip()
        if not pw:
            continue
        r = zxcvbn(pw)
        print(json.dumps({
            "password": pw,
            "score": r['score'],
            "guesses": r.get('guesses'),
            "feedback": r.get('feedback',{})
        }))
