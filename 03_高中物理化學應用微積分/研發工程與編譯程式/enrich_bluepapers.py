# -*- coding: utf-8 -*-
"""
enrich_bluepapers.py
實施四大出版級落地工程補充：
1. 書籍篇：
   - 全書 24 章版面字數與邊欄空間預算表（Page & Word Budgeting Grid）
   - 全書 96 幅核心幾何向量圖繪製清冊與規格（Visual Asset Catalog & Specs）
   - 384 道書籍專著題目官方標準答案與關鍵封閉解清冊（Master Answer Keys）
2. 課堂篇：
   - 216 道道場實彈攻防題導師底牌答案、反例與 3 行秒殺動線庫（Dojo Interrogation Keys）
"""

import re
import os
import sys

# 讀取現有書籍篇母檔
book_path = r"C:\Users\user\.gemini\antigravity\brain\17c5c8ea-1f34-4270-a5e4-410bdd5037d4\calculus_precollege_bluepaper_book.md"
with open(book_path, "r", encoding="utf-8") as f:
    book_content = f.read()

# 讀取現有課堂篇母檔
dojo_path = r"C:\Users\user\.gemini\antigravity\brain\17c5c8ea-1f34-4270-a5e4-410bdd5037d4\calculus_precollege_bluepaper_dojo.md"
with open(dojo_path, "r", encoding="utf-8") as f:
    dojo_content = f.read()

print(f"Original Book Blueprint: {len(book_content)} chars")
print(f"Original Dojo Manual: {len(dojo_content)} chars")
