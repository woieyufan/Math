# -*- coding: utf-8 -*-
"""
Master Builder for
《看見幾何：從寫字、拍照、剪衣服到文藝復興名畫的視覺解密》
Advanced Extracurricular STEM/STEAM Book Edition.
Grounded in Elementary School (K-9) Mathematical Tools.

Assembles 14 modular pages, renders to HTML & PDF via headless Chrome,
and embeds 8 native PyMuPDF interactive educational annotations.
"""

import os
import sys
import subprocess
import base64
import shutil
import fitz

# Import modular page definitions
from styles import HTML_HEAD
from pages_front import get_page_1, get_page_2, get_page_3
from pages_sample_1_2 import get_page_4, get_page_5, get_page_6, get_page_7
from pages_sample_3_4_5 import get_page_8, get_page_9, get_page_10, get_page_11, get_page_12, get_page_13
from pages_back import get_page_14

# Paths setup
workspace_dir = r'C:\Users\user\Documents'
logo_png_path = os.path.join(workspace_dir, r'woieyufan-brand-assets\woieyufan-logo-transparent-300dpi.png')
svg_watermark_path = os.path.join(workspace_dir, r'woieyufan-brand-assets\woieyufan-logo_downward.svg')
output_html = os.path.join(workspace_dir, '看見幾何_進階視覺數學課外讀物.html')
output_pdf = os.path.join(workspace_dir, '看見幾何_進階視覺數學課外讀物.pdf')
temp_pdf = os.path.join(workspace_dir, '看見幾何_進階視覺數學課外讀物_temp.pdf')

def run_build():
    print("=== Step 1: Base64 Encoding Brand Assets ===")
    if not os.path.exists(logo_png_path):
        raise FileNotFoundError(f"Missing logo file: {logo_png_path}")
    with open(logo_png_path, "rb") as f:
        logo_base64 = base64.b64encode(f.read()).decode("utf-8")
    logo_data_uri = f"data:image/png;base64,{logo_base64}"

    if not os.path.exists(svg_watermark_path):
        raise FileNotFoundError(f"Missing watermark svg: {svg_watermark_path}")
    with open(svg_watermark_path, "rb") as f:
        svg_base64 = base64.b64encode(f.read()).decode("utf-8")
    svg_data_uri = f"data:image/svg+xml;base64,{svg_base64}"
    print("Brand assets encoded successfully.")

    print("=== Step 2: Assembling 14 Pages into Book HTML ===")
    pages = [
        get_page_1(),   # P. 1 Cover
        get_page_2(),   # P. 2 Manifesto
        get_page_3(),   # P. 3 TOC (24 Chapters)
        get_page_4(),   # P. 4 Sample 1 (Ch 01 Calligraphy Left)
        get_page_5(),   # P. 5 Sample 1 (Ch 01 Calligraphy Right)
        get_page_6(),   # P. 6 Sample 2 (Ch 03 Stars & Remainders Left)
        get_page_7(),   # P. 7 Sample 2 (Ch 03 Stars & Remainders Right)
        get_page_8(),   # P. 8 Sample 3 (Ch 17 Pisa Tower Left)
        get_page_9(),   # P. 9 Sample 3 (Ch 17 Pisa Tower Right)
        get_page_10(),  # P. 10 Sample 4 (Ch 13 Darts & Cone Left)
        get_page_11(),  # P. 11 Sample 4 (Ch 13 Darts & Cone Right)
        get_page_12(),  # P. 12 Sample 5 (Ch 22 Lamentation Left)
        get_page_13(),  # P. 13 Sample 5 (Ch 22 Lamentation Right)
        get_page_14(),  # P. 14 Appendix & Imprint
    ]

    html_footer = r'''
</div><!-- .page-container -->
<script>
  document.addEventListener("DOMContentLoaded", function() {
    if (window.renderMathInElement) {
      renderMathInElement(document.body, {
        delimiters: [
          {left: '$$', right: '$$', display: true},
          {left: '$', right: '$', display: false}
        ],
        throwOnError: false
      });
    }
  });
</script>
</body>
</html>
'''

    full_html = HTML_HEAD + "".join(pages) + html_footer
    full_html = full_html.replace("__LOGO_DATA_URI__", logo_data_uri)
    full_html = full_html.replace("__SVG_DATA_URI__", svg_data_uri)

    with open(output_html, "w", encoding="utf-8") as f:
        f.write(full_html)

    print(f"HTML generated at: {output_html} ({len(full_html)} bytes)")

    print("=== Step 3: Headless Chrome Compilation to PDF (iPad 4:3) ===")
    chrome_paths = [
        r'C:\Program Files\Google\Chrome\Application\chrome.exe',
        r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe',
        os.path.expanduser(r'~\AppData\Local\Google\Chrome\Application\chrome.exe')
    ]

    chrome_bin = None
    for p in chrome_paths:
        if os.path.exists(p):
            chrome_bin = p
            break

    if not chrome_bin:
        print("Error: Google Chrome not found!")
        sys.exit(1)

    chrome_cmd = [
        chrome_bin,
        "--headless=new",
        "--disable-gpu",
        "--no-sandbox",
        "--disable-dev-shm-usage",
        "--run-all-compositor-stages-before-draw",
        f"--print-to-pdf={output_pdf}",
        output_html
    ]

    print("Executing Chrome headless print...")
    res = subprocess.run(chrome_cmd, capture_output=True, encoding="utf-8", errors="replace")
    if res.returncode != 0:
        print(f"Chrome error: {res.stderr}")
        sys.exit(1)

    if not os.path.exists(output_pdf):
        print("Error: Chrome failed to produce output PDF!")
        sys.exit(1)

    raw_pages = len(fitz.open(output_pdf))
    print(f"Raw PDF compiled successfully: {output_pdf} ({os.path.getsize(output_pdf)} bytes, {raw_pages} pages)")

    print("=== Step 4: Embedding 8 Native Interactive Educational Annotations ===")
    doc = fitz.open(output_pdf)

    annotations_data = [
        {
            "target_page": 2,
            "search": "世界背後，藏著一張看不見的幾何網",
            "title": "編輯手記 1：從小學數學工具出發的視覺革命",
            "content": "【出版核心理念】：本書徹底打破「數學是枯燥計算」的枷鎖。我們不講高深術語，而是直接從孩子每天在學的「餘數、坐標、比、內角和、展開圖」出發，讓孩子親眼看見手中的小學工具如何主宰全世界的國旗、名畫、攝影與立體裁縫！",
            "color": (0.12, 0.45, 0.85)
        },
        {
            "target_page": 4,
            "search": "寫字也是算幾何？書法家是隱藏的幾何學家",
            "title": "漢字幾何 2：書法九宮格坐標系與不倒翁重心",
            "content": "【小學工具對接】：生字簿上的田字格、米字格與九宮格，正是世界上最早的二維直角坐標系。歐陽詢楷書之所以斜而不倒，是因為所有筆畫質點的質量力矩總和嚴格平衡（∑ r_i m_i = 0），寫字其實是在算動態平衡！",
            "color": (0.85, 0.45, 0.15)
        },
        {
            "target_page": 6,
            "search": "時鐘上的流星雨：除法餘數、互質與一筆畫五角星",
            "title": "星形幾何 3：除法餘數、互質與一筆畫星星",
            "content": "【神來之筆・除法餘數】：為什麼五角星能一筆畫完，大衛六角星卻會卡死？當頂點數 n 與步長 k 互質（gcd=1）時，餘數循環會一筆畫連滿圓周；當有公因數時，星星必定分裂為多個多邊形！",
            "color": (0.85, 0.20, 0.20)
        },
        {
            "target_page": 7,
            "search": "模運算與最大公因數：主宰全宇宙星形的生死算式",
            "title": "核心算式 4：模運算公式與咖啡杯心臟線",
            "content": "【同餘算術的視覺奇蹟】：星形公式 x_new = (x + k) mod n。如果不做跳步加法改做乘法表 x ➜ 2x mod n，圓周裡竟然會浮現出極度震撼的光滑「心臟線（Cardioid）」，揭開陽光照進馬克杯的幾何奧秘！",
            "color": (0.15, 0.65, 0.35)
        },
        {
            "target_page": 8,
            "search": "推倒比薩斜塔！攝影師的「相似三角形」借位懸案",
            "title": "生活幾何 5：比薩斜塔借位拍照的相似三角形",
            "content": "【小學比例式對接】：相機底片將三維深度抹平成二維。利用相似三角形 AAA 原理，近處 18cm 的手掌與遠處 56m 的大塔在視網膜上產生相同視角 tanθ = h/d = H/D，解構借位攝影的幾何秘密。",
            "color": (0.15, 0.50, 0.90)
        },
        {
            "target_page": 10,
            "search": "打版師的幾何剪刀：衣服如何把平面的布，穿成三維的身體？",
            "title": "實作工坊 6：內角和、角虧定理與衣服省道",
            "content": "【小學內角和的立體延伸】：布料是曲率 K=0 的歐式平面。裁縫師剪去一個角度 θ 的扇形（省道 Dart），該點周圍內角和小於 360°，消失的角度轉化為第三維度的立體高度 H = √(R² - r²)，讓平面的布穿成立體人體！",
            "color": (0.55, 0.25, 0.75)
        },
        {
            "target_page": 12,
            "search": "躺著的巨人：曼特尼亞《哀悼基督》的透視懸案",
            "title": "大師暗門 7：曼特尼亞《哀悼基督》的透視縮短",
            "content": "【終極壓軸・深度縮短】：如果純粹遵照相機直線光學，躺著的人體腳部會比頭部大上整整 2.2 倍，遮蔽全臉。曼特尼亞的天才之處在於『主動壓抑剛性透視』，利用非線性衰減保全了頭部的尊嚴，展現對大腦形狀恆常性的深層洞察。",
            "color": (0.85, 0.35, 0.15)
        },
        {
            "target_page": 13,
            "search": "調和平均數：眼睛視野裡的「非線性減速檔」",
            "title": "核心數學 8：調和平均數 H = 2ab / (a+b)",
            "content": "【平均數的幾何物理本質】：國中生最常卡關的往返平均速度 2v1v2/(v1+v2) 與電阻並聯，正是調和平均數！在透視學中，深度空間的非線性壓縮由反比關係主導，調和平均是空間深度的真正幾何中心！",
            "color": (0.20, 0.60, 0.60)
        }
    ]

    annot_count = 0
    for note in annotations_data:
        t_page = note.get("target_page", None)
        keyword = note["search"]
        found = False
        target_pages = [t_page - 1] if t_page and t_page <= len(doc) else range(1, len(doc))
        for p_idx in target_pages:
            p = doc[p_idx]
            rects = p.search_for(keyword)
            if rects:
                r = rects[0]
                hl = p.add_highlight_annot(r)
                hl.set_colors(stroke=note["color"])
                hl.set_info(title=note["title"], content=note["content"])
                hl.update()

                icon_point = fitz.Point(min(r.x1 + 14, p.rect.width - 25), max(r.y0 - 2, 15))
                sticky = p.add_text_annot(icon_point, note["content"], icon="Comment")
                sticky.set_info(title=note["title"])
                sticky.set_colors(stroke=note["color"])
                sticky.update()
                annot_count += 1
                print(f"Annotated [{keyword[:12]}...] on Page {p_idx + 1}")
                found = True
                break
        if not found:
            print(f"Warning: Keyword '{keyword}' not found for annotation!")

    doc.save(temp_pdf)
    doc.close()
    shutil.move(temp_pdf, output_pdf)

    final_size = os.path.getsize(output_pdf)
    final_doc = fitz.open(output_pdf)
    final_pages = len(final_doc)
    final_doc.close()

    print(f"=== ALL COMPLETE! Book Edition created ===")
    print(f"File: {output_pdf}")
    print(f"Final Size: {final_size} bytes, Pages: {final_pages}, Annotated: {annot_count}/8 entries.")

    if final_pages != 14:
        print(f"WARNING: Page count is {final_pages}, expected exactly 14!")
    else:
        print("PERFECT: Page count is exactly 14 pages!")

if __name__ == '__main__':
    run_build()
