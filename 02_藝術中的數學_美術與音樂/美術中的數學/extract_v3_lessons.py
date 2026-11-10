# -*- coding: utf-8 -*-
import os
import sys
import re

base_dir = os.path.dirname(os.path.abspath(__file__))
if base_dir not in sys.path:
    sys.path.insert(0, base_dir)

from art_math_v3_src import pages_lessons

text = ''.join([getattr(pages_lessons, f'get_lesson_page_{i}')() for i in range(1, 13)])

badges = re.findall(r'<span class="lesson-num">(.*?)</span>', text)
titles = re.findall(r'<span class="lesson-title-text">(.*?)</span>', text)

output_txt = os.path.join(base_dir, 'v3_lessons.txt')
with open(output_txt, 'w', encoding='utf-8') as f:
    for b, t in zip(badges, titles):
        f.write(f"{b} | {t}\n")

print(f"Extracted {len(badges)} lessons to {output_txt}")
