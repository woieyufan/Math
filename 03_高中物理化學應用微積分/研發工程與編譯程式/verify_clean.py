import fitz

doc = fitz.open(r'C:\Users\user\Documents\中學超前自學_微積分先修體系企劃白皮書.pdf')
print("Total pages:", len(doc))

for i in range(len(doc)):
    p = doc[i]
    blocks = p.get_text("blocks")
    txt = blocks[0][4].strip().replace('\n', ' ') if blocks else "EMPTY"
    print(f"Page {i+1}: ({len(blocks)} blocks) First: '{txt[:60]}'")
