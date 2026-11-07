import fitz
import os
import shutil

pdf_path = r'C:\Users\user\Documents\中學超前自學_微積分先修體系企劃白皮書.pdf'
temp_path = r'C:\Users\user\Documents\中學超前自學_微積分先修體系企劃白皮書_temp.pdf'

doc = fitz.open(pdf_path)

annotations_data = [
    {
        "search": "第 2 堂",
        "title": "教研註解 1：角度單位與弧度制本質",
        "content": "【國中認知摩擦化解】：度數制（360°）是巴比倫人的人為規定。如果微積分用度數，每次對 sin(x) 微分都會甩出醜陋的常數係數 (π/180)；只有使用弧度制（弧長/半徑的無量綱純數），極限 lim(sin θ / θ) 才會剛好等於 1，微積分公式才能保持極致簡潔與自然。",
        "color": (0.15, 0.45, 0.85) # Royal Blue
    },
    {
        "search": "第 3 堂",
        "title": "教研註解 2：重根定理與切線代數接觸階數",
        "content": "【代數視野拓寬】：國中二次拋物線的判別式 Δ=0 只能處理二次多項式。遇到三次曲線的反曲點切線時，切線會「直接穿過曲線」，國中代數會崩潰。微積分切線的代數本質是「方程聯立差式必含 (x-x0)^2 之二重根（或以上）」，這才是高等代數與微積分看待幾何切觸的真正第一原理。",
        "color": (0.85, 0.45, 0.15) # Warm Amber
    },
    {
        "search": "第 5 堂",
        "title": "教研註解 3：連鎖律的物理本質（嚴禁分數約分教學）",
        "content": "【編寫防呆與學術嚴謹】：傳統教學常偷懶說「dy/dt = (dy/du)*(du/dt) 就像 du 上下約分一樣」，這在嚴格數學上是錯的。微分算子不是孤立整數。講義必須貫徹「尺度齒輪轉換（Gear Ratio）」的物理量綱本質（例如 Hz 換 rpm 產生的 60 倍斜率齒輪轉換），防止學生建立含混的約分概念。",
        "color": (0.85, 0.20, 0.20) # Crimson Warning
    },
    {
        "search": "第 6 堂",
        "title": "教研註解 4：自然常數 e 與半衰期 0.693 的純數來源",
        "content": "【自然常數哲學】：宇宙中所有「變化率與現存量成正比」的自指現象（細菌增殖、電容放電、放射性衰變），內在底數都是 e。若用底數 10，每次微分都會甩出 ln(10)≈2.302；只有底數為 e，自身求導才等於自身。半衰期中的 0.693 也不是實驗測得的經驗數，而是純數學常數 ln(2) 的數值近似。",
        "color": (0.15, 0.65, 0.45) # Emerald Green
    },
    {
        "search": "第 13 堂",
        "title": "教研註解 5：消去時間的狀態空間微商 a = v(dv/dx)",
        "content": "【高階競賽物理技巧】：國中運動學總是追著時間 t 計算。但當面對空氣阻力與速度平方成正比（F=-kv^2）或萬有引力隨位置變化時，時間 t 會成為極大累贅。利用連鎖律消去時間得到的 a = v(dv/dx)，是大學理論力學與物理奧林匹亞在「位置-速度」狀態相空間中直接求解微積分的關鍵武器。",
        "color": (0.55, 0.25, 0.75) # Purple
    },
    {
        "search": "第 17 堂",
        "title": "教研註解 6：110V 交流電壓的微積分發熱有效值本質",
        "content": "【工程實體對照】：正弦交流電簡單平均為 0，物理上以「一個週期內的焦耳熱做功定積分」定義有效值。台灣/美規家用 110V 插座的瞬間最大峰值電壓實為 110*√2 ≈ 156V（每秒在 ±156V 震盪 60 次）；台灣 220V 冷氣插座瞬間峰值更達到 311V。工程設計絕緣耐壓時必須以微積分峰值為準。",
        "color": (0.15, 0.50, 0.90) # Blue
    },
    {
        "search": "第 18 堂",
        "title": "教研註解 7：化學反應級數嚴禁等同於計量係數",
        "content": "【跨科認知防呆】：國中生習慣看化學方程式係數（如 2A + B -> C），極易誤以為反應級數就等於係數 2 和 1。講義必須強烈標註：巨觀反應級數純由實驗測定，絕不能想當然爾套用化學方程式計量數！只有在微觀單步的「基元反應」中兩者才恰好吻合。",
        "color": (0.85, 0.20, 0.20) # Crimson Warning
    },
    {
        "search": "第 23 堂",
        "title": "教研註解 8：最壞情況全微分與隨機誤差均方根合成",
        "content": "【測量科學哲學】：全微分算式 dz/z = a(dx/x) + b(dy/y) 給出的是「各誤差同時往最不利方向偏離時的數學絕對上限」；但真實世界各儀器誤差彼此獨立且隨機，現代國際度量衡委員會（BIPM）規範採用統計正交合成（均方根合成）。此處是微積分全微分過渡到機率統計的完美橋樑。",
        "color": (0.20, 0.60, 0.60) # Teal
    }
]

total_added = 0
for note in annotations_data:
    keyword = note["search"]
    found = False
    for page_idx, page in enumerate(doc):
        if page_idx < 3:
            continue
        rects = page.search_for(keyword)
        if rects:
            r = rects[0]
            # Add highlight annotation on the keyword
            highlight = page.add_highlight_annot(r)
            highlight.set_colors(stroke=note["color"])
            highlight.set_info(title=note["title"], content=note["content"])
            highlight.update()

            # Also add an interactive Sticky Note icon right next to it
            icon_point = fitz.Point(r.x1 + 14, r.y0 - 2)
            sticky = page.add_text_annot(icon_point, note["content"], icon="Comment")
            sticky.set_info(title=note["title"])
            sticky.set_colors(stroke=note["color"])
            sticky.update()

            print(f'Added [{note["title"]}] on page {page_idx+1}')
            total_added += 1
            found = True
            break
    if not found:
        print(f'Warning: keyword "{keyword}" not found after page 3')

doc.save(temp_path)
doc.close()
shutil.move(temp_path, pdf_path)
print(f'SUCCESS! Total {total_added} native PDF annotations embedded directly into: {pdf_path}')
