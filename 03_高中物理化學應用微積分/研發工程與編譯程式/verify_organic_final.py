# -*- coding: utf-8 -*-
import sys
import re

book_path = r"C:\Users\user\.gemini\antigravity\brain\17c5c8ea-1f34-4270-a5e4-410bdd5037d4\calculus_precollege_bluepaper_book.md"
dojo_path = r"C:\Users\user\.gemini\antigravity\brain\17c5c8ea-1f34-4270-a5e4-410bdd5037d4\calculus_precollege_bluepaper_dojo.md"

with open(book_path, "r", encoding="utf-8") as f:
    book_text = f.read()

with open(dojo_path, "r", encoding="utf-8") as f:
    dojo_text = f.read()

book_chs = re.findall(r"### Chapter (\d+)：", book_text)
dojo_tps = re.findall(r"### Topic (\d+)：", dojo_text)

print(f"Book chapters found: {len(set(book_chs))}, from {book_chs[0]} to {book_chs[-1]}")
print(f"Dojo topics found: {len(set(dojo_tps))}, from {dojo_tps[0]} to {dojo_tps[-1]}")

# Check search terms for purged items
for term in ["希爾伯特", "鄧煜", "Hilbert"]:
    b_count = book_text.count(term)
    d_count = dojo_text.count(term)
    print(f"Term '{term}': Book={b_count}, Dojo={d_count}")

# Check key new topics
for term in ["高爾頓板", "二項分佈", "畢奧-薩伐爾", "長直導線", "圓線圈", "絕熱過程", "高斯積分", "68-95-99.7", "馬克士威", "簡諧運動"]:
    b_count = book_text.count(term)
    d_count = dojo_text.count(term)
    print(f"Core Concept '{term}': Book={b_count}, Dojo={d_count}")
