#!/usr/bin/env python3
import hashlib, requests

def pwned_count(pw):
    h = hashlib.sha1(pw.encode('utf-8')).hexdigest().upper()
    prefix, suffix = h[:5], h[5:]
    r = requests.get('https://api.pwnedpasswords.com/range/' + prefix)
    for line in r.text.splitlines():
        s, count = line.split(':')
        if s == suffix:
            return int(count)
    return 0

with open('passwords.txt') as f:
    for pw in f:
        pw = pw.strip()
        if not pw:
            continue
        print(pw, pwned_count(pw))
