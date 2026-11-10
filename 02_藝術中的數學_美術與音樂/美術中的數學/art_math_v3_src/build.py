# -*- coding: utf-8 -*-
"""
Master Builder for Art Math White Paper Version 4.0 (Path B - Spacious Luxury Edition)
Assembles all 24 modular pages with comfortable, airy typography (13.5px-14px body),
compiles to HTML and iPad 4:3 PDF,
and embeds 8 native PyMuPDF interactive educational annotations.
"""

import os
import sys
import subprocess
import base64
import shutil
import fitz

# Import modules
from styles import HTML_HEAD
from pages_front import (
    get_page_1, get_page_2, get_page_3, get_page_4,
    get_page_5, get_page_6, get_page_7, get_page_8
)
from pages_lessons import (
    get_lesson_page_1, get_lesson_page_2, get_lesson_page_3, get_lesson_page_4,
    get_lesson_page_5, get_lesson_page_6, get_lesson_page_7, get_lesson_page_8,
    get_lesson_page_9, get_lesson_page_10, get_lesson_page_11, get_lesson_page_12
)
from pages_back import (
    get_page_back_1, get_page_back_2, get_page_back_3, get_page_back_4
)

# Paths
current_dir = os.path.dirname(os.path.abspath(__file__))
math_art_dir = os.path.abspath(os.path.join(current_dir, '..'))
repo_root = os.path.abspath(os.path.join(math_art_dir, '..'))
brand_assets_dir = os.path.join(repo_root, 'woieyufan-brand-assets')

logo_png_path = os.path.join(brand_assets_dir, 'woieyufan-logo-transparent-300dpi.png')
svg_watermark_path = os.path.join(brand_assets_dir, 'woieyufan-logo_downward.svg')
output_html = os.path.join(math_art_dir, '小學全域_美術中的數學企劃白皮書.html')
output_pdf = os.path.join(math_art_dir, '小學全域_美術中的數學企劃白皮書.pdf')
temp_pdf = os.path.join(math_art_dir, '小學全域_美術中的數學企劃白皮書_temp.pdf')

print("=== Step 1: Base64 Encoding Brand Assets ===")
with open(logo_png_path, "rb") as f:
    logo_base64 = base64.b64encode(f.read()).decode("utf-8")
logo_data_uri = f"data:image/png;base64,{logo_base64}"

with open(svg_watermark_path, "rb") as f:
    svg_base64 = base64.b64encode(f.read()).decode("utf-8")
svg_data_uri = f"data:image/svg+xml;base64,{svg_base64}"
print("Brand assets encoded successfully.")

print("=== Step 2: Assembling 24 Pages into Full HTML (Path B Spacious Typography) ===")
html_content = (
    HTML_HEAD +
    get_page_1() +
    get_page_2() +
    get_page_3() +
    get_page_4() +
    get_page_5() +
    get_page_6() +
    get_page_7() +
    get_page_8() +
    get_lesson_page_1() +
    get_lesson_page_2() +
    get_lesson_page_3() +
    get_lesson_page_4() +
    get_lesson_page_5() +
    get_lesson_page_6() +
    get_lesson_page_7() +
    get_lesson_page_8() +
    get_lesson_page_9() +
    get_lesson_page_10() +
    get_lesson_page_11() +
    get_lesson_page_12() +
    get_page_back_1() +
    get_page_back_2() +
    get_page_back_3() +
    get_page_back_4()
)

html_content = html_content.replace("__LOGO_DATA_URI__", logo_data_uri)
html_content = html_content.replace("__SVG_DATA_URI__", svg_data_uri)

with open(output_html, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"HTML generated at: {output_html} ({len(html_content)} bytes)")

print("=== Step 3: Headless Chrome Compilation to PDF (iPad 4:3) ===")
chrome_paths = [
    shutil.which('google-chrome'),
    shutil.which('chromium'),
    shutil.which('chromium-browser'),
    shutil.which('chrome'),
    r'C:\Program Files\Google\Chrome\Application\chrome.exe',
    r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe',
    os.path.expanduser(r'~\AppData\Local\Google\Chrome\Application\chrome.exe'),
    '/usr/bin/google-chrome',
    '/usr/bin/chromium',
    '/usr/bin/chromium-browser',
    '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
]

chrome_bin = None
for p in chrome_paths:
    if p and os.path.exists(p):
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
    "--no-pdf-header-footer",
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

print(f"Raw PDF compiled successfully: {output_pdf} ({os.path.getsize(output_pdf)} bytes)")

print("=== Step 4: Embedding 8 Native Interactive Educational Annotations ===")
doc = fitz.open(output_pdf)
print(f"Total pages in PDF: {len(doc)}")

annotations_data = [
    {
        "search": "第 1 堂",
        "title": "批註 1：模矩比與古典人體比例分割",
        "content": "【K-9 數學錨點對接】：小六與國一課堂反覆計算「內外項相乘」，學生深感枯燥。本堂將波利克萊托斯《持矛者》作為實驗室，以「頭長」為基準模數，學生手繪 1:2:3:7.5 人體連比，讓死板比例式化為空間人體美學。",
        "color": (0.12, 0.45, 0.85)
    },
    {
        "search": "第 2 堂",
        "title": "批註 2：三大古典平均數之幾何作圖",
        "content": "【課堂淺嚐未深究】：國中生只會算加總除以人數的算術平均，對幾何平均數 √(ab) 缺乏空間直覺。本堂透過直尺圓規作半圓，直觀證明 A ≥ G ≥ H，並在達文西《維特魯威人》中精確定位肚臍的黃金分割比。",
        "color": (0.15, 0.65, 0.45)
    },
    {
        "search": "第 3 堂",
        "title": "批註 3：調和平均數與人體透視縮短（Foreshortening）",
        "content": "【痛點破局震撼】：國中生最頭痛的「往返平均速度 2v1v2/(v1+v2)」與合作工程問題，其數學實體正是「調和平均數」！曼特尼亞在《哀悼基督》中，人體等距骨節向前伸展時在畫布上的投影間距正是嚴格的調和數列！",
        "color": (0.85, 0.45, 0.15)
    },
    {
        "search": "第 4 堂",
        "title": "批註 4：畢氏定理無理數作圖與提奧多魯斯螺線",
        "content": "【無理數幾何具象化】：學生只會背勾股數 3:4:5 與開根號，本堂以連鎖直角三角形親手畫出 √2、√3、√4、√5 螺線，證明無理數長度是可以拿圓規精確畫出來的，並推導 A4 紙與古典動態黃金矩形。",
        "color": (0.85, 0.20, 0.20)
    },
    {
        "search": "第 7 堂",
        "title": "批註 5：艾雪密鋪面積守恆與滑移反射群",
        "content": "【密鋪深度拓展】：課本只提正多邊形鋪滿（內角整除 360°），淺嚐輒止。本堂以艾雪《蜥蜴》為範本，傳授「面積守恆剪貼術」：在一邊剪除一塊、滑移反射貼至對邊，在平面剛體群變換下無縫鋪滿平面。",
        "color": (0.55, 0.25, 0.75)
    },
    {
        "search": "第 10 堂",
        "title": "批註 6：一次函數直線方程與透視消失點",
        "content": "【代數與透視對接】：學生解聯立方程 y=mx+b 痛苦不堪，本堂將達文西《最後的晚餐》天花板與長桌邊緣全部建立坐標方程，手算聯立方程證明所有不同斜率的射線精確交會於耶穌額頭的消失點！",
        "color": (0.15, 0.50, 0.90)
    },
    {
        "search": "第 14 堂",
        "title": "批註 7：三視圖與 30° 等角軸測投影《紀念碑谷》",
        "content": "【工程製圖美學】：國中三視圖考試死記硬背，本堂引入全球爆紅手遊《紀念碑谷》，捨棄透視消失點，改用三維座標以 120° 均分投影的「等角軸測圖」，讓孩子親手畫出無透視衰減的經典立體城堡。",
        "color": (0.85, 0.35, 0.15)
    },
    {
        "search": "第 22 堂",
        "title": "批註 8：平面向量加法與點彩派視網膜混色",
        "content": "【跨學科幾何光學】：國中理化講力的合成平行四邊形法、數學講重心坐標。秀拉在《大碗島》畫布點上純黃色與純藍色小圓點，在視網膜上透過向量加法與重心坐標公式 (C1+C2)/2 融合成最明亮的鮮綠！",
        "color": (0.20, 0.60, 0.60)
    }
]

annot_count = 0
for note in annotations_data:
    keyword = note["search"]
    found = False
    for page_idx, p in enumerate(doc):
        if page_idx < 8:  # skip front pages 1-8; annotate actual lesson cards (P.9+)
            continue
        rects = p.search_for(keyword)
        if rects:
            r = rects[0]
            hl = p.add_highlight_annot(r)
            hl.set_colors(stroke=note["color"])
            hl.set_info(title=note["title"], content=note["content"])
            hl.update()

            icon_point = fitz.Point(r.x1 + 14, r.y0 - 2)
            sticky = p.add_text_annot(icon_point, note["content"], icon="Comment")
            sticky.set_info(title=note["title"])
            sticky.set_colors(stroke=note["color"])
            sticky.update()
            annot_count += 1
            print(f"Annotated [{keyword}] on Page {page_idx + 1}")
            found = True
            break
    if not found:
        print(f"Warning: Keyword '{keyword}' not found for annotation!")

doc.save(temp_pdf)
doc.close()
shutil.move(temp_pdf, output_pdf)

final_size = os.path.getsize(output_pdf)
final_pages = len(fitz.open(output_pdf))
print(f"=== ALL COMPLETE! Version 4.0 Art Math Whitepaper created (Path B) ===")
print(f"File: {output_pdf}")
print(f"Final Size: {final_size} bytes, Pages: {final_pages}, Annotated: {annot_count}/8 entries.")
