import fitz

doc = fitz.open(r'C:\Users\user\Documents\中學超前自學_微積分先修體系企劃白皮書.pdf')

print("=== PAGE 1 ===")
print(doc[0].get_text())

print("=== PAGE 2 ===")
print(doc[1].get_text())
