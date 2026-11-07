import fitz

doc = fitz.open(r'C:\Users\user\Documents\中學超前自學_微積分先修體系企劃白皮書.pdf')
annots_found = 0
for idx, page in enumerate(doc):
    for annot in page.annots():
        info = annot.info
        print(f"Page {idx+1}: [{annot.type[1]}] {info.get('title')}")
        annots_found += 1

print(f"Total annotations in PDF: {annots_found}")
