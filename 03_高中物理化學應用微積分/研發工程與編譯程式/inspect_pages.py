import fitz

doc = fitz.open(r'C:\Users\user\Documents\中學超前自學_微積分先修體系企劃白皮書.pdf')

for i in [0, 1, 2, 3, 4, 5, 6, 7]:
    p = doc[i]
    print(f"=== PAGE {i+1} (height={p.rect.height}) ===")
    blocks = p.get_text("blocks")
    for b in blocks[:4]:
        # b: (x0, y0, x1, y1, text, block_no, block_type)
        txt = b[4].strip().replace('\n', ' ')
        print(f"  y0={b[1]:.1f}, y1={b[3]:.1f}: {txt[:70]}")
