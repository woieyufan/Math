import fitz

pdf_path = r'C:\Users\user\Documents\中學超前自學_微積分先修體系企劃白皮書.pdf'
doc = fitz.open(pdf_path)

for i in range(min(3, len(doc))):
    p = doc[i]
    print(f"Page {i+1} rect: {p.rect}")
