import fitz

pdf_path = r'C:\Users\user\Documents\中學超前自學_微積分先修體系企劃白皮書.pdf'
doc = fitz.open(pdf_path)

for i in range(min(5, len(doc))):
    p = doc[i]
    blocks = p.get_text("blocks")
    min_y = min(b[1] for b in blocks) if blocks else 0
    max_x = max(b[2] for b in blocks) if blocks else 0
    print(f"Page {i+1}: min_y = {min_y:.1f}, max_x = {max_x:.1f}, page width = {p.rect.width}")
