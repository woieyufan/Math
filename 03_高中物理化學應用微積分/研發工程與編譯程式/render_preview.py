import fitz
import os

pdf_path = r'C:\Users\user\Documents\中學超前自學_微積分先修體系企劃白皮書.pdf'
doc = fitz.open(pdf_path)

out_dir = r'C:\Users\user\.gemini\antigravity\brain\17c5c8ea-1f34-4270-a5e4-410bdd5037d4\scratch'
for i in range(min(6, len(doc))):
    p = doc[i]
    pix = p.get_pixmap(dpi=150)
    out_img = os.path.join(out_dir, f"page_{i+1}.png")
    pix.save(out_img)
    print(f"Rendered Page {i+1} to {out_img}")
