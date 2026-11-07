import fitz

pdf_path = r'C:\Users\user\Documents\中學超前自學_微積分先修體系企劃白皮書.pdf'
doc = fitz.open(pdf_path)

badge_rect = fitz.Rect(530, 22, 572, 64) # 42x42 pt

conflicts = 0
for idx, page in enumerate(doc):
    text = page.get_text("text", clip=badge_rect).strip()
    if text:
        print(f"Page {idx+1} has text in badge area: '{text}'")
        conflicts += 1

print(f"Total conflicts: {conflicts}")
