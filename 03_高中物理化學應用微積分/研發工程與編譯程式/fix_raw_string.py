# -*- coding: utf-8 -*-
import re

with open(r"C:\Users\user\.gemini\antigravity\brain\17c5c8ea-1f34-4270-a5e4-410bdd5037d4\scratch\build_chapter_01.py", "r", encoding="utf-8") as f:
    code = f.read()

# Replace ch01_content = """ with ch01_content = r"""
code = code.replace('ch01_content = """', 'ch01_content = r"""')

with open(r"C:\Users\user\.gemini\antigravity\brain\17c5c8ea-1f34-4270-a5e4-410bdd5037d4\scratch\build_chapter_01.py", "w", encoding="utf-8") as f:
    f.write(code)

print("Fixed build_chapter_01.py with raw string!")
