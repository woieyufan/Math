# -*- coding: utf-8 -*-
import sys
import re
sys.path.insert(0, r'C:\Users\user\Documents')
from art_math_v3_src import pages_lessons

text = pages_lessons.get_page_6() + pages_lessons.get_page_7() + pages_lessons.get_page_8() + pages_lessons.get_page_9() + pages_lessons.get_page_10() + pages_lessons.get_page_11()

badges = re.findall(r'<span class="lesson-num">(.*?)</span>', text)
titles = re.findall(r'<span class="lesson-title-text">(.*?)</span>', text)

with open(r'C:\Users\user\Documents\v3_lessons.txt', 'w', encoding='utf-8') as f:
    for b, t in zip(badges, titles):
        f.write(f"{b} | {t}\n")

print("Written v3_lessons.txt")
