import fitz

pdf_path = r'C:\Users\user\Documents\中學超前自學_微積分先修體系企劃白皮書.pdf'
doc = fitz.open(pdf_path)

print(f"Total pages: {len(doc)}")
for i in range(len(doc)):
    p = doc[i]
    # Check text near the top (y < 65)
    top_text = p.get_text("text", clip=fitz.Rect(0, 0, p.rect.width, 65)).strip().replace('\n', ' ')
    first_block = p.get_text("blocks")[0][4].strip().replace('\n', ' ') if p.get_text("blocks") else "EMPTY"
    print(f"Page {i+1}: First line: '{first_block[:60]}' | Top area: '{top_text[:40]}'")
