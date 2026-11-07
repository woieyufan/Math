import fitz

svg_path = r'C:\Users\user\Documents\woieyufan-logo_downward.svg'
try:
    svg_doc = fitz.open(svg_path)
    print("SVG opened successfully, page count:", len(svg_doc))
    page = svg_doc[0]
    rect = page.rect
    print("SVG rect:", rect)
    pix = page.get_pixmap(dpi=300)
    print("Pixmap dimensions:", pix.width, "x", pix.height)
except Exception as e:
    print("Error:", e)
