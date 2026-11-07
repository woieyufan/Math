import fitz

doc = fitz.open(r'C:\Users\user\Documents\中學超前自學_微積分先修體系企劃白皮書.pdf')

for idx in [0, 1, 2, 3]:
    p = doc[idx]
    txt = p.get_text()
    first_lines = [l.strip() for l in txt.split('\n') if l.strip()][:5]
    last_lines = [l.strip() for l in txt.split('\n') if l.strip()][-3:]
    print(f"Page {idx+1}: line count={len(txt.splitlines())}")
    print(f"  First: {first_lines}")
    print(f"  Last:  {last_lines}")
