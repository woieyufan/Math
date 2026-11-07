import fitz

doc = fitz.open(r'C:\Users\user\Documents\中學超前自學_微積分先修體系企劃白皮書.pdf')

# Test highlight annotation
page = doc[16] # page 17 (0-indexed 16)
rects = page.search_for('第 17 堂')
if rects:
    highlight = page.add_highlight_annot(rects[0])
    highlight.set_colors(stroke=(0.2, 0.6, 1.0)) # soft blue
    highlight.set_info(title="教研註解：交流電峰值與有效值", content="【工程實體註解】：家用 110V 交流電是發熱有效值，其瞬時峰值高達 156V（110*sqrt(2)）；220V 冷氣插座瞬時峰值更達到 311V。工程設計絕緣時必須以峰值為準。")
    highlight.update()
    print('Highlight annotation added successfully!')

doc.save(r'C:\Users\user\Documents\test_highlight.pdf')
