# -*- coding: utf-8 -*-
"""
Master Builder for Middle-School Gifted Math White Paper Version 4.0
Assembles 16 modular pages, compiles to HTML and A4 PDF via Headless Chrome,
and embeds 8 native PyMuPDF interactive educational annotations + PDF bookmarks outline.
"""

import os
import sys
import subprocess
import base64
import shutil
import pymupdf as fitz

# Import page modules
from styles import HTML_HEAD
from pages_front import get_page_1, get_page_2, get_page_3, get_page_4
from pages_pillars import (
    get_page_5, get_page_6, get_page_7, get_page_8,
    get_page_9, get_page_10, get_page_11, get_page_12
)
from pages_pedagogy import get_page_13, get_page_14, get_page_15
from pages_back import get_page_16

def run_build():
    # Paths
    src_dir = os.path.dirname(os.path.abspath(__file__))
    gifted_math_dir = os.path.abspath(os.path.join(src_dir, '..'))
    repo_root = os.path.abspath(os.path.join(gifted_math_dir, '..'))
    brand_assets_dir = os.path.join(repo_root, '02_藝術中的數學_美術與音樂', 'woieyufan-brand-assets')

    logo_png_path = os.path.join(brand_assets_dir, 'woieyufan-logo-transparent-300dpi.png')
    svg_watermark_path = os.path.join(brand_assets_dir, 'woieyufan-logo_downward.svg')
    output_html = os.path.join(gifted_math_dir, '中學數理資優思維與奧賽教研白皮書.html')
    output_pdf = os.path.join(gifted_math_dir, '中學數理資優思維與奧賽教研白皮書.pdf')

    print("=== Step 1: Base64 Encoding Brand Assets ===")
    if not os.path.exists(logo_png_path):
        print(f"Warning: Logo not found at {logo_png_path}")
        logo_data_uri = ""
    else:
        with open(logo_png_path, "rb") as f:
            logo_base64 = base64.b64encode(f.read()).decode("utf-8")
        logo_data_uri = f"data:image/png;base64,{logo_base64}"

    if not os.path.exists(svg_watermark_path):
        print(f"Warning: SVG not found at {svg_watermark_path}")
        svg_data_uri = ""
    else:
        with open(svg_watermark_path, "rb") as f:
            svg_base64 = base64.b64encode(f.read()).decode("utf-8")
        svg_data_uri = f"data:image/svg+xml;base64,{svg_base64}"
    print("Brand assets encoded successfully.")

    print("=== Step 2: Assembling 16 Modular Pages into HTML ===")
    html_footer = r'''
</div>
<script>
  document.addEventListener("DOMContentLoaded", function() {
    renderMathInElement(document.body, {
      delimiters: [
        {left: "$$", right: "$$", display: true},
        {left: "$", right: "$", display: false}
      ],
      throwOnError: false
    });
  });
</script>
</body>
</html>
'''

    full_html = (
        HTML_HEAD +
        get_page_1() +
        get_page_2() +
        get_page_3() +
        get_page_4() +
        get_page_5() +
        get_page_6() +
        get_page_7() +
        get_page_8() +
        get_page_9() +
        get_page_10() +
        get_page_11() +
        get_page_12() +
        get_page_13() +
        get_page_14() +
        get_page_15() +
        get_page_16() +
        html_footer
    )

    full_html = full_html.replace("__LOGO_DATA_URI__", logo_data_uri)
    full_html = full_html.replace("__SVG_DATA_URI__", svg_data_uri)

    with open(output_html, "w", encoding="utf-8") as f:
        f.write(full_html)

    print(f"HTML generated at: {output_html} ({len(full_html)} bytes)")

    print("=== Step 3: Headless Chrome Compilation to PDF ===")
    chrome_paths = [
        shutil.which('google-chrome'),
        shutil.which('chromium'),
        shutil.which('chromium-browser'),
        '/usr/bin/google-chrome',
        '/usr/bin/chromium'
    ]

    chrome_bin = next((p for p in chrome_paths if p and os.path.exists(p)), None)
    if not chrome_bin:
        print("Error: Chrome / Chromium binary not found.")
        return False

    chrome_cmd = [
        chrome_bin,
        "--headless=new",
        "--disable-gpu",
        "--no-sandbox",
        "--disable-dev-shm-usage",
        "--no-pdf-header-footer",
        "--run-all-compositor-stages-before-draw",
        f"--print-to-pdf={output_pdf}",
        output_html
    ]

    print("Running Chrome PDF generation...")
    res = subprocess.run(chrome_cmd, capture_output=True, text=True)
    if res.returncode != 0:
        print(f"Chrome error: {res.stderr}")
        return False

    if not os.path.exists(output_pdf):
        print("Error: Output PDF file was not created.")
        return False

    print(f"PDF compiled successfully: {output_pdf} ({os.path.getsize(output_pdf)} bytes)")

    print("=== Step 4: Injecting PyMuPDF Interactive Annotations & Table of Contents ===")
    doc = fitz.open(output_pdf)
    print(f"Total pages in PDF: {len(doc)}")

    # 1. Bookmarks / Table of Contents (Outline)
    toc = [
        [1, "封面：中學數理資優思維與奧賽教研白皮書", 1],
        [1, "第一章：資優數學第一性原理與典範轉移", 2],
        [1, "第二章：數理資優四大支柱全域圖譜", 3],
        [1, "第三章：國中三年數理資優進階課程路線圖", 4],
        [1, "第四章：數論支柱（上）除法、同餘與不定方程", 5],
        [1, "第五章：數論支柱（下）指數同餘、原根與勒讓德公式", 6],
        [1, "第六章：代數支柱（上）韋達定理與牛頓和", 7],
        [1, "第七章：代數支柱（下）柯西-施瓦茨與 Nesbitt 不等式", 8],
        [1, "第八章：幾何支柱（上）塞瓦與梅涅勞斯定理", 9],
        [1, "第九章：幾何支柱（下）圓方冪、根軸與反演幾何", 10],
        [1, "第十章：組合支柱（上）狄利克雷鴿籠與算兩次", 11],
        [1, "第十一章：組合支柱（下）不變量原理與離散博弈", 12],
        [1, "第十二章：資優教法與搭橋提問模型（節稅任務）", 13],
        [1, "第十三章：國中數學獨立研究五步法", 14],
        [1, "第十四章：忠孝國中 43 套歷年數理資優題庫矩陣", 15],
        [1, "封底：學術使命與出版規範", 16]
    ]
    doc.set_toc(toc)
    print("Table of Contents bookmarks injected.")

    # 2. Interactive Educational Annotations
    annotations_data = [
        {
            "page_idx": 4,  # Page 5
            "search": "經典真題 1.1",
            "title": "名師解題批註：同餘逆元與輾轉倒推",
            "content": "【核心考點剖析】：同餘方程 17x ≡ 1 (mod 43) 的本質是求解不定方程 17x - 43y = 1。利用歐幾里得輾轉相除倒推 Bézout 等式，是求模逆元最穩健之公理路徑，完全避免盲目試根。",
            "color": (0.12, 0.45, 0.85)
        },
        {
            "page_idx": 5,  # Page 6
            "search": "奧林匹克真題 1.2",
            "title": "名師解題批註：指數不定方程之模週期排除法",
            "content": "【競賽破局殺手鐧】：面對 3^x + 55 = y^2，未知數在指數上無法直接因式分解。此時利用模 4 考察平方數餘數只有 0 或 1，立即鎖定 x 必為偶數！進而化為平方差公式分解求解，堪稱模運算之神來之筆。",
            "color": (0.05, 0.60, 0.40)
        },
        {
            "page_idx": 6,  # Page 7
            "search": "經典真題 2.1",
            "title": "名師解題批註：牛頓和對稱多項式降次威力",
            "content": "【高等代數維度】：本題若直接解聯立方程求解 x, y, z 將極為繁瑣。牛頓和公式將冪和 p_k 與初等對稱多項式 e_k 建立遞迴關係，三步算出特徵多項式為 t^2(t-3)=0，實現全局對稱降維打擊。",
            "color": (0.12, 0.45, 0.85)
        },
        {
            "page_idx": 7,  # Page 8
            "search": "奧林匹克經典名題 2.2",
            "title": "名師解題批註：Nesbitt 不等式分子補全術",
            "content": "【構造法典範】：每項加 1 將分子統一構造為 (a+b+c)，隨後運用安杜因分式柯西不等式 ∑ 1/(b+c) ≥ 9/(2∑a)，整體代回立得 3/2！此題是訓練資優生齊次化與局部化意識的基石名題。",
            "color": (0.85, 0.45, 0.15)
        },
        {
            "page_idx": 8,  # Page 9
            "search": "真題示範 3.1",
            "title": "名師解題批註：塞瓦逆定理之射影連乘",
            "content": "【幾何作圖跳脫】：傳統國中生遇到三線共點會做多條平行輔助線。掌握塞瓦定理後，將三邊分比相乘直接等於 1，兩行算式秒殺，這就是現代射影幾何相對於傳統歐氏幾何的維度優勢！",
            "color": (0.85, 0.20, 0.20)
        },
        {
            "page_idx": 9,  # Page 10
            "search": "第九屆國中奧林匹克真題 3.2",
            "title": "名師解題批註：根軸連心垂直性判定",
            "content": "【共圓證明最高境界】：四點共圓最怕角度倒角陷入死循環。透過兩圓交點公共弦即為根軸、根軸必垂直兩圓連心線的幾何本質，將四點共圓問題轉化為方冪相等性，瞬間明晰。",
            "color": (0.55, 0.25, 0.75)
        },
        {
            "page_idx": 10, # Page 11
            "search": "幾何幾值範例 4.1",
            "title": "名師解題批註：幾何網格分割之極值邊界",
            "content": "【鴿籠原理幾何化】：正方形內任放 5 點，將正方形四等分構造 4 個籠子。由小正方形對角線長 √(1/4+1/4)=√2/2，無可辯駁地鎖定衝突必發生在該直徑內，是存在性證明的經典。",
            "color": (0.15, 0.50, 0.90)
        },
        {
            "page_idx": 11, # Page 12
            "search": "不變量經典名題 4.2",
            "title": "名師解題批註：黑白染色不變量否定覆蓋",
            "content": "【不可行性證題核心】：骨牌覆蓋問題從不依靠枚舉。黑白棋盤剪去兩同色對角格後，黑格 30 個、白格 32 個，而每塊骨牌必然覆蓋一黑一白。顏色不變量直接否定了覆蓋的可能性，乾淨俐落。",
            "color": (0.85, 0.35, 0.15)
        }
    ]

    annot_count = 0
    for item in annotations_data:
        p_idx = item["page_idx"]
        if p_idx < len(doc):
            page = doc[p_idx]
            text_instances = page.search_for(item["search"])
            rect = None
            if text_instances:
                rect = text_instances[0]
            else:
                rect = fitz.Rect(50, 150, 200, 180)

            annot_rect = fitz.Rect(rect.x1 + 4, rect.y0 - 2, rect.x1 + 24, rect.y0 + 16)
            annot = page.add_text_annot(annot_rect.tl, item["content"], icon="Note")
            annot.set_info(title=item["title"])
            annot.set_colors(stroke=item["color"])
            annot.update()
            annot_count += 1

    print(f"Injected {annot_count} interactive educational annotations.")

    temp_save_path = output_pdf.replace(".pdf", "_final.pdf")
    doc.save(temp_save_path)
    doc.close()

    shutil.move(temp_save_path, output_pdf)
    print(f"Final PDF saved to: {output_pdf} ({os.path.getsize(output_pdf)} bytes)")
    return True

if __name__ == '__main__':
    run_build()
