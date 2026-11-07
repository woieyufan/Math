import fitz

doc = fitz.open(r'C:\Users\user\Documents\中學超前自學_微積分先修體系企劃白皮書.pdf')

print(f"Total pages: {len(doc)}")
annots_found = 0
for idx, p in enumerate(doc):
    annots = list(p.annots())
    if annots:
        for a in annots:
            annots_found += 1
            print(f"Page {idx+1}: {a.type[1]} '{a.info.get('title', '')}'")

print(f"Total annotations found: {annots_found}")
