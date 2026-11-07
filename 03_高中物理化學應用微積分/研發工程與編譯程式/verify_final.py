import fitz
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

pdf_path = r'C:\Users\user\Documents\中學超前自學_微積分先修體系企劃白皮書.pdf'
html_path = r'C:\Users\user\Documents\中學超前自學_微積分先修體系企劃白皮書.html'

print("=== CHECKING HTML STRUCTURE ===")
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

banners = re.findall(r'<div class="ladder-banner[^"]*">([^<]+)</div>', html)
print(f"Total ladder banners: {len(banners)}")
for b in banners:
    print("  Ladder Banner:", b)

sections = re.findall(r'<h3 class="section-title[^"]*">([^<]+)</h3>', html)
print(f"\nTotal section titles: {len(sections)}")
for s in sections:
    print("  Section Title:", s)

print("\n=== CHECKING PDF PAGE STRUCTURE & ANNOTATIONS ===")
doc = fitz.open(pdf_path)
print(f"Total pages: {len(doc)}")

for i in range(len(doc)):
    page = doc[i]
    annots = list(page.annots())
    text = page.get_text()
    first_lines = [l.strip() for l in text.split('\n') if l.strip()][:2]
    # Check if header is present
    has_header = "woieyufan EDUCATION" in text if i >= 1 else False
    has_footer = "© woieyufan" in text if i >= 1 else False
    ann_str = f", Annots: {len(annots)}" if annots else ""
    print(f"P.{i+1:02d}: Head={has_header}, Foot={has_footer}{ann_str} | First: {first_lines[0] if first_lines else ''}")
