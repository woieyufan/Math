import fitz

doc = fitz.open(r'C:\Users\user\Documents\中學超前自學_微積分先修體系企劃白皮書.pdf')

with open(r'C:\Users\user\.gemini\antigravity\brain\17c5c8ea-1f34-4270-a5e4-410bdd5037d4\scratch\p4_p5_detail.txt', 'w', encoding='utf-8') as f:
    f.write("=== PAGE 4 ===\n")
    f.write(doc[3].get_text() + "\n")
    f.write("=== PAGE 5 ===\n")
    f.write(doc[4].get_text() + "\n")

print("Dumped p4 and p5")
