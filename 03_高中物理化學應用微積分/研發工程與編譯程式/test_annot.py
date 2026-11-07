import fitz

doc = fitz.open(r'C:\Users\user\Documents\中學超前自學_微積分先修體系企劃白皮書.pdf')
print('Total pages:', len(doc))

# Search for 第 17 堂
found = False
for i, page in enumerate(doc):
    rects = page.search_for('第 17 堂')
    if rects:
        print(f'Found 第 17 堂 on page {i+1} at {rects[0]}')
        annot = page.add_text_annot(fitz.Point(rects[0].x1 + 10, rects[0].y0), '【工程實體註解】：家用 110V 峰值實為 156V，220V 冷氣插座峰值實為 311V。', icon='Comment')
        annot.update()
        found = True
        break

if found:
    doc.save(r'C:\Users\user\Documents\test_annot.pdf')
    print('Annotation successfully added to test_annot.pdf')
