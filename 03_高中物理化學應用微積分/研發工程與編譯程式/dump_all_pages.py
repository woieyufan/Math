import fitz

doc = fitz.open(r'C:\Users\user\Documents\中學超前自學_微積分先修體系企劃白皮書.pdf')

with open(r'C:\Users\user\.gemini\antigravity\brain\17c5c8ea-1f34-4270-a5e4-410bdd5037d4\scratch\all_pages_summary.txt', 'w', encoding='utf-8') as f:
    for idx in range(len(doc)):
        p = doc[idx]
        lines = [l.strip() for l in p.get_text().splitlines() if l.strip()]
        f.write(f"=== PAGE {idx+1} (Total {len(lines)} lines) ===\n")
        f.write(f"First 3: {lines[:3]}\n")
        f.write(f"Last 2:  {lines[-2:]}\n\n")

print("Dumped all pages summary.")
