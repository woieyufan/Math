# -*- coding: utf-8 -*-
import os
import subprocess

candidates = [
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    os.path.expanduser(r"~\AppData\Local\Google\Chrome\Application\chrome.exe"),
    os.path.expanduser(r"~\AppData\Local\Microsoft\Edge\Application\msedge.exe"),
]

found = []
for c in candidates:
    if os.path.exists(c):
        found.append(c)
        print("Found:", c)

if not found:
    print("No browser binary found.")
