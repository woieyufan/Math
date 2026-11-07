import fitz

doc = fitz.open(r'C:\Users\user\Documents\中學超前自學_微積分先修體系企劃白皮書.pdf')

def show(idx):
    p = doc[idx]
    txt = p.get_text()
    print(f"=== PAGE {idx+1} ({len(p.get_text().splitlines())} lines) ===")
    for line in txt.splitlines():
        safe_line = line.encode('utf-8', errors='replace').decode('utf-8', errors='replace')
        print(safe_line)

with open(r'C:\Users\user\.gemini\antigravity\brain\17c5c8ea-1f34-4270-a5e4-410bdd5037d4\scratch\p2_p3_p4.txt', 'w', encoding='utf-8') as f:
    for idx in [1, 2, 3]:
        p = doc[idx]
        f.write(f"=== PAGE {idx+1} ===\n")
        f.write(p.get_text() + "\n\n")

print("Saved to p2_p3_p4.txt successfully")
