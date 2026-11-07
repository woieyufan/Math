import fitz
import numpy as np
from PIL import Image
import os
import re
import subprocess
import shutil

# Step 1: Prepare high-res cropped transparent logo
svg_path = r'C:\Users\user\Documents\woieyufan-logo_downward.svg'
svg_doc = fitz.open(svg_path)
page = svg_doc[0]
pix = page.get_pixmap(dpi=300)
img = np.frombuffer(pix.samples, dtype=np.uint8).reshape((pix.height, pix.width, pix.n))

scale = 300 / 150
x_min, x_max = int(260 * scale), int(1014 * scale)
y_min, y_max = int(472 * scale), int(1209 * scale)
cropped = img[y_min:y_max, x_min:x_max]

pil_img = Image.fromarray(cropped).convert("RGBA")
# Convert near-white pixels to transparent
datas = list(pil_img.getdata())
new_data = []
for item in datas:
    if item[0] > 245 and item[1] > 245 and item[2] > 245:
        new_data.append((255, 255, 255, 0))
    else:
        new_data.append(item)

pil_img.putdata(new_data)
badge_png_path = r'C:\Users\user\.gemini\antigravity\brain\17c5c8ea-1f34-4270-a5e4-410bdd5037d4\scratch\logo_badge.png'
pil_img.save(badge_png_path, "PNG")
print("Step 1: Logo badge created at", badge_png_path)

# Step 2: Build HTML with generous top margin for header branding
input_md = r'C:\Users\user\.gemini\antigravity\brain\17c5c8ea-1f34-4270-a5e4-410bdd5037d4\calculus_precollege_curriculum_whitepaper.md'
output_html = r'C:\Users\user\Documents\中學超前自學_微積分先修體系企劃白皮書.html'
raw_pdf = r'C:\Users\user\.gemini\antigravity\brain\17c5c8ea-1f34-4270-a5e4-410bdd5037d4\scratch\raw_doc.pdf'
final_pdf = r'C:\Users\user\Documents\中學超前自學_微積分先修體系企劃白皮書.pdf'

with open(input_md, 'r', encoding='utf-8') as f:
    text = f.read()

lines = text.split('\n')
html_parts = []
in_mermaid = False
table_rows = []

def format_inline(s):
    s = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', s)
    s = re.sub(r'`([^`]+)`', r'<code>\1</code>', s)
    s = re.sub(r'\[(.*?)\]\((.*?)\)', r'<a href="\2">\1</a>', s)
    return s

def render_table(rows):
    if not rows: return ''
    h = ['<div class="table-container"><table class="doc-table">']
    for idx, row in enumerate(rows):
        cols = [c.strip() for c in row.strip('|').split('|')]
        if idx == 1 and all(set(c) <= set('-: ') for c in cols):
            continue
        tag = 'th' if idx == 0 else 'td'
        cell_str = ''.join(f'<{tag}>{format_inline(c)}</{tag}>' for c in cols)
        h.append(f'  <tr>{cell_str}</tr>')
    h.append('</table></div>')
    return '\n'.join(h)

def render_flowchart_card():
    return '''
    <div class="flowchart-container">
      <div class="flow-grid">
        <div class="flow-col flow-col-a">
          <div class="flow-col-title">出發點 A：坐標運動與瞬時斜率（微分學）</div>
          <div class="flow-node">1. Cartesian 坐標系與函數映射</div>
          <div class="flow-arrow">↓</div>
          <div class="flow-node">2. 割線斜率與差商算子 $\\Delta y / \\Delta x$</div>
          <div class="flow-arrow">↓</div>
          <div class="flow-node">3. 極限推進：從割線到切線（重根定理）</div>
          <div class="flow-arrow">↓</div>
          <div class="flow-node">4. 微分算子 $d/dt$：瞬時速度與加速度</div>
          <div class="flow-arrow">↓</div>
          <div class="flow-node highlight-a">5. 量綱連鎖律：尺度齒輪比與頻率項 $\\omega$</div>
        </div>

        <div class="flow-col flow-col-b">
          <div class="flow-col-title">出發點 B：幾何平衡與力矩積聚（積分學）</div>
          <div class="flow-node">1. 槓桿原理與力矩平衡 $\\sum \\tau = 0$</div>
          <div class="flow-arrow">↓</div>
          <div class="flow-node">2. 離散質心加權平均 $\\sum (m_i x_i)/M$</div>
          <div class="flow-arrow">↓</div>
          <div class="flow-node">3. 微元分割：連續第一面積矩 $\\int x\\,dA$</div>
          <div class="flow-arrow">↓</div>
          <div class="flow-node">4. 幾何形心：三角形 $\\frac{1}{3}h$ 雙重證明</div>
          <div class="flow-arrow">↓</div>
          <div class="flow-node highlight-b">5. 微元積聚：旋轉體體積與做功 $\\frac{1}{2}kx^2$</div>
        </div>
      </div>

      <div class="flow-bridge">
        <div class="flow-bridge-arrow">↓↓ 必然合流與對偶統一 ↓↓</div>
        <div class="flow-center-box">
          <strong>微積分基本定理（FTC）</strong>：$\\frac{d}{dx}\\int_a^x f(t)\\,dt = f(x)$（變化率與微元積聚對偶統一）
        </div>
      </div>

      <div class="flow-grid" style="margin-top: 15px;">
        <div class="flow-col flow-col-physics">
          <div class="flow-col-title">物理學分支閉環</div>
          <div class="flow-node">二階常微分方程（ODE）：$\\ddot{x} + \\omega^2 x = 0$</div>
          <div class="flow-arrow">↓</div>
          <div class="flow-node highlight-physics">機械能守恆閉環：$\\frac{1}{2}mv^2 + \\frac{1}{2}kx^2 = \\frac{1}{2}kA^2$</div>
          <div class="flow-arrow">↓</div>
          <div class="flow-node highlight-physics">電磁發熱有效值：$V_{rms} = \\frac{V_0}{\\sqrt{2}}$（110V 插座峰值 156V）</div>
        </div>
        <div class="flow-col flow-col-chem">
          <div class="flow-col-title">化學分支閉環</div>
          <div class="flow-node">微分速率方程式：$-\\frac{d[A]}{dt} = k[A]^n$</div>
          <div class="flow-arrow">↓</div>
          <div class="flow-node highlight-chem">動態平衡常數閉環：$K = \\frac{k_f}{k_r}$ 與阿瑞尼斯斜率</div>
        </div>
      </div>
    </div>
    '''

i = 0
open_lesson = False
in_toc = False

while i < len(lines):
    line = lines[i]
    stripped = line.strip()

    if stripped.startswith('```mermaid'):
        in_mermaid = True
        i += 1
        continue
    if in_mermaid:
        if stripped.startswith('```'):
            in_mermaid = False
            html_parts.append(render_flowchart_card())
        i += 1
        continue

    if stripped.startswith('|') and stripped.endswith('|'):
        table_rows.append(stripped)
        i += 1
        continue
    else:
        if table_rows:
            html_parts.append(render_table(table_rows))
            table_rows = []

    if stripped.startswith('# '):
        title = stripped[2:].strip()
        html_parts.append(f'''
        <div class="cover-page">
          <div class="cover-top-row">
            <div class="cover-tag">ACADEMIC SPECIFICATION WHITE PAPER</div>
          </div>
          <h1 class="doc-title">{title}</h1>
          <h2 class="doc-subtitle">48 小時 / 24 堂課全域工程架構、頁面規格與題型設計母本矩陣</h2>
          <div class="meta-badge-row">
            <span class="badge badge-primary">企劃書正式定稿</span>
            <span class="badge">學術先修規格</span>
            <span class="badge">24 堂課 / 48 小時</span>
            <span class="badge">微積分核心·跨科應用</span>
            <span class="badge">iPad 優化排版</span>
          </div>
          <div class="cover-meta-grid">
            <div class="meta-item"><span class="meta-label">核心目標</span><span class="meta-val">中學資優自學生微積分先修與高中物化降維打擊</span></div>
            <div class="meta-item"><span class="meta-label">課時規格</span><span class="meta-val">5 大階段 · 24 堂課（每堂 120 分鐘）</span></div>
            <div class="meta-item"><span class="meta-label">研發宗旨</span><span class="meta-val">微積分為骨架主體，物理化學為現實載體舞台</span></div>
            <div class="meta-item"><span class="meta-label">閱讀格式</span><span class="meta-val">跨平台通用 PDF · iPad 滿版流式排版</span></div>
          </div>
        </div>
        ''')
    elif stripped.startswith('## '):
        if open_lesson:
            html_parts.append('</div>')
            open_lesson = False
        subtitle = stripped[3:].strip()
        if '目錄' in subtitle:
            in_toc = True
            html_parts.append('<div class="toc-container"><h2 class="toc-title">課程企劃白皮書 · 總體目錄</h2><div class="toc-grid">')
        elif '全域工程架構' in subtitle:
            pass
        else:
            if in_toc:
                html_parts.append('</div></div>')
                in_toc = False
            html_parts.append(f'<div class="chapter-divider"></div><h2 class="chapter-title">{subtitle}</h2>')
    elif stripped.startswith('### '):
        if open_lesson:
            html_parts.append('</div>')
            open_lesson = False
        h3 = stripped[4:].strip()
        if h3.startswith('第一階段') or h3.startswith('第二階段') or h3.startswith('第三階段') or h3.startswith('第四階段') or h3.startswith('第五階段'):
            html_parts.append(f'<div class="stage-banner"><h3>{h3}</h3></div>')
        else:
            html_parts.append(f'<h3 class="section-title">{format_inline(h3)}</h3>')
    elif stripped.startswith('#### '):
        if open_lesson:
            html_parts.append('</div>')
        open_lesson = True
        h4 = stripped[5:].strip()
        html_parts.append(f'<div class="lesson-card"><div class="lesson-header"><span class="lesson-pill">單堂 4 頁規範</span><h4 class="lesson-title">{format_inline(h4)}</h4></div>')
    elif stripped.startswith('---'):
        if in_toc:
            html_parts.append('</div></div>')
            in_toc = False
        html_parts.append('<hr class="divider"/>')
    elif stripped.startswith('* ') or stripped.startswith('- '):
        content = format_inline(stripped[2:])
        if in_toc:
            html_parts.append(f'<div class="toc-item">{content}</div>')
        else:
            html_parts.append(f'<div class="bullet-item"><span class="bullet-dot">•</span><div class="bullet-content">{content}</div></div>')
    elif re.match(r'^\d+\.\s', stripped):
        m = re.match(r'^(\d+)\.\s*(.*)', stripped)
        num = m.group(1)
        content = format_inline(m.group(2))
        html_parts.append(f'<div class="numbered-item"><span class="num-badge">{num}</span><div class="num-content">{content}</div></div>')
    elif stripped.startswith('$$'):
        html_parts.append(f'<div class="math-block">{stripped}</div>')
    elif stripped == '':
        pass
    else:
        html_parts.append(f'<p class="para">{format_inline(line)}</p>')
    i += 1

if table_rows:
    html_parts.append(render_table(table_rows))
if open_lesson:
    html_parts.append('</div>')
if in_toc:
    html_parts.append('</div></div>')

body_content = '\n'.join(html_parts)

html_template = f'''<!DOCTYPE html>
<html lang="zh-Hant">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
<title>中學超前自學：以微積分為核心之數理跨科先修體系白皮書</title>

<!-- KaTeX for high-precision Math typesetting -->
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.css">
<script src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/contrib/auto-render.min.js"></script>

<style>
  :root {{
    --primary: #1e3a8a;
    --primary-dark: #0f172a;
    --primary-light: #eff6ff;
    --primary-border: #bfdbfe;
    --accent: #2563eb;
    --text-dark: #1e293b;
    --text-muted: #64748b;
    --border-light: #e2e8f0;
    --font-main: -apple-system, BlinkMacSystemFont, "SF Pro Text", "PingFang TC", "Noto Sans TC", "Microsoft JhengHei", sans-serif;
  }}

  * {{ box-sizing: border-box; }}
  body {{
    font-family: var(--font-main);
    color: var(--text-dark);
    line-height: 1.75;
    background-color: #f1f5f9;
    margin: 0;
    padding: 0;
    -webkit-font-smoothing: antialiased;
  }}

  .page-container {{
    max-width: 960px;
    margin: 30px auto;
    background: #ffffff;
    padding: 65px 85px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.06);
    border-radius: 18px;
  }}

  @media (max-width: 768px) {{
    .page-container {{
      margin: 0;
      padding: 30px 18px;
      border-radius: 0;
    }}
  }}

  .cover-page {{
    background: linear-gradient(135deg, #f8fafc 0%, #eff6ff 100%);
    border: 1px solid var(--primary-border);
    border-radius: 16px;
    padding: 40px;
    margin-bottom: 40px;
  }}
  .cover-tag {{
    display: inline-block;
    font-size: 11px;
    font-weight: 800;
    letter-spacing: 1.5px;
    color: var(--accent);
    background: #ffffff;
    border: 1px solid var(--primary-border);
    padding: 4px 10px;
    border-radius: 6px;
    margin-bottom: 15px;
  }}
  .doc-title {{
    font-size: 28px;
    font-weight: 800;
    color: var(--primary);
    margin: 0 0 12px 0;
    letter-spacing: -0.5px;
    line-height: 1.35;
  }}
  .doc-subtitle {{
    font-size: 16px;
    font-weight: 500;
    color: var(--text-muted);
    margin: 0 0 20px 0;
    line-height: 1.5;
  }}
  .meta-badge-row {{
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
    margin-bottom: 25px;
  }}
  .badge {{
    background: #ffffff;
    color: var(--text-dark);
    border: 1px solid #cbd5e1;
    padding: 4px 12px;
    border-radius: 20px;
    font-size: 13px;
    font-weight: 600;
  }}
  .badge-primary {{
    background: var(--primary);
    color: #ffffff;
    border-color: var(--primary);
  }}

  .cover-meta-grid {{
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 12px;
    border-top: 1px solid #cbd5e1;
    padding-top: 20px;
  }}
  @media (max-width: 600px) {{
    .cover-meta-grid {{ grid-template-columns: 1fr; }}
  }}
  .meta-item {{
    font-size: 13px;
    display: flex;
    flex-direction: column;
  }}
  .meta-label {{
    color: var(--text-muted);
    font-weight: 600;
    margin-bottom: 2px;
  }}
  .meta-val {{
    color: var(--text-dark);
    font-weight: 600;
  }}

  .toc-container {{
    background: #f8fafc;
    border: 1px solid var(--border-light);
    border-radius: 14px;
    padding: 28px 32px;
    margin-bottom: 40px;
  }}
  .toc-title {{
    font-size: 18px;
    font-weight: 700;
    color: var(--primary);
    margin: 0 0 18px 0;
    border-bottom: 2px solid var(--primary-border);
    padding-bottom: 10px;
  }}
  .toc-grid {{
    display: grid;
    grid-template-columns: 1fr;
    gap: 8px;
  }}
  .toc-item a {{
    color: #334155;
    text-decoration: none;
    font-size: 14.5px;
    display: block;
    padding: 4px 8px;
    border-radius: 6px;
  }}

  .chapter-divider {{
    height: 3px;
    background: linear-gradient(to right, var(--primary), #93c5fd, transparent);
    margin: 50px 0 25px 0;
  }}
  .chapter-title {{
    font-size: 22px;
    font-weight: 800;
    color: var(--primary);
    margin: 0 0 22px 0;
    padding-left: 14px;
    border-left: 6px solid var(--accent);
  }}
  .section-title {{
    font-size: 17px;
    font-weight: 700;
    color: #1e293b;
    margin: 28px 0 12px 0;
    padding-bottom: 6px;
    border-bottom: 1px dashed var(--border-light);
  }}

  .stage-banner {{
    background: linear-gradient(90deg, #0f172a 0%, #1e293b 100%);
    color: #ffffff;
    padding: 14px 22px;
    border-radius: 10px;
    margin: 40px 0 24px 0;
    box-shadow: 0 4px 12px rgba(15,23,42,0.15);
  }}
  .stage-banner h3 {{
    margin: 0;
    font-size: 16px;
    letter-spacing: 0.5px;
    font-weight: 700;
  }}
  .lesson-card {{
    background: #ffffff;
    border: 1px solid var(--border-light);
    border-radius: 12px;
    padding: 22px 26px;
    margin-bottom: 24px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.03);
    page-break-inside: avoid;
    break-inside: avoid;
  }}
  .lesson-header {{
    display: flex;
    align-items: center;
    gap: 10px;
    margin-bottom: 14px;
    padding-bottom: 10px;
    border-bottom: 1px solid #f1f5f9;
  }}
  .lesson-pill {{
    font-size: 11px;
    font-weight: 700;
    background: var(--primary-light);
    color: var(--accent);
    padding: 2px 8px;
    border-radius: 4px;
    border: 1px solid var(--primary-border);
  }}
  .lesson-title {{
    font-size: 16.5px;
    font-weight: 700;
    color: var(--primary);
    margin: 0;
  }}

  .para {{
    font-size: 15px;
    color: #334155;
    margin: 10px 0;
    text-align: justify;
  }}
  .bullet-item {{
    display: flex;
    align-items: flex-start;
    gap: 10px;
    margin: 7px 0;
    font-size: 14.5px;
  }}
  .bullet-dot {{
    color: var(--accent);
    font-weight: bold;
    line-height: 1.6;
    font-size: 16px;
  }}
  .bullet-content {{ flex: 1; color: #334155; }}
  .numbered-item {{
    display: flex;
    align-items: flex-start;
    gap: 10px;
    margin: 9px 0;
    font-size: 14.5px;
  }}
  .num-badge {{
    background: #e2e8f0;
    color: #334155;
    font-size: 11.5px;
    font-weight: 700;
    padding: 2px 7px;
    border-radius: 4px;
    margin-top: 3px;
  }}
  .num-content {{ flex: 1; }}

  .table-container {{
    overflow-x: auto;
    margin: 22px 0;
    border-radius: 10px;
    border: 1px solid var(--border-light);
  }}
  .doc-table {{
    width: 100%;
    border-collapse: collapse;
    font-size: 14px;
    text-align: left;
  }}
  .doc-table th {{
    background: #f8fafc;
    color: #1e293b;
    font-weight: 700;
    padding: 13px 16px;
    border-bottom: 2px solid var(--border-light);
  }}
  .doc-table td {{
    padding: 13px 16px;
    border-bottom: 1px solid #f1f5f9;
    color: #334155;
  }}

  .flowchart-container {{
    background: #ffffff;
    border: 1px solid var(--primary-border);
    border-radius: 14px;
    padding: 24px;
    margin: 25px 0 35px 0;
    box-shadow: 0 4px 12px rgba(30,58,138,0.04);
  }}
  .flow-grid {{
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 20px;
  }}
  @media (max-width: 650px) {{
    .flow-grid {{ grid-template-columns: 1fr; }}
  }}
  .flow-col {{
    background: #f8fafc;
    border: 1px solid var(--border-light);
    border-radius: 10px;
    padding: 16px;
  }}
  .flow-col-title {{
    font-size: 13.5px;
    font-weight: 800;
    color: var(--primary);
    text-align: center;
    padding-bottom: 8px;
    margin-bottom: 10px;
    border-bottom: 2px solid var(--border-light);
  }}
  .flow-node {{
    background: #ffffff;
    border: 1px solid #cbd5e1;
    border-radius: 6px;
    padding: 8px 10px;
    font-size: 12.5px;
    font-weight: 600;
    color: #334155;
    text-align: center;
  }}
  .flow-arrow {{
    text-align: center;
    color: #94a3b8;
    font-weight: bold;
    font-size: 13px;
    margin: 3px 0;
  }}
  .highlight-a {{ background: #eff6ff; border-color: #93c5fd; color: #1e40af; }}
  .highlight-b {{ background: #fefce8; border-color: #fde047; color: #854d0e; }}
  .highlight-physics {{ background: #f0fdf4; border-color: #86efac; color: #166534; }}
  .highlight-chem {{ background: #f0fdfa; border-color: #99f6e4; color: #115e59; }}
  .flow-bridge {{ margin-top: 15px; text-align: center; }}
  .flow-bridge-arrow {{ font-size: 12px; font-weight: 800; color: var(--accent); margin-bottom: 6px; }}
  .flow-center-box {{
    background: #eff6ff;
    border: 2px solid var(--accent);
    border-radius: 8px;
    padding: 12px 16px;
    font-size: 13.5px;
    color: var(--primary);
    font-weight: 600;
    display: inline-block;
  }}
  .divider {{ border: none; border-top: 1px solid var(--border-light); margin: 35px 0; }}

  /* Print and PDF Specific Rules: Give 22mm top margin so running header & logo badge have dedicated space */
  @page {{
    size: letter;
    margin: 22mm 15mm 18mm 15mm;
  }}

  @media print {{
    body {{
      background: #ffffff;
      font-size: 13pt;
    }}
    .page-container {{
      max-width: 100%;
      margin: 0;
      padding: 0;
      box-shadow: none;
      border-radius: 0;
    }}
    .chapter-divider {{
      page-break-before: always;
      break-before: page;
      margin-top: 0;
    }}
    .lesson-card {{
      page-break-inside: avoid;
      break-inside: avoid;
      box-shadow: none;
      border: 1px solid #cbd5e1;
      margin-bottom: 18px;
    }}
    .flowchart-container {{
      page-break-inside: avoid;
      break-inside: avoid;
    }}
    .doc-title {{ font-size: 23pt; }}
    .chapter-title {{ font-size: 17pt; }}
  }}
</style>
</head>
<body>
<div class="page-container">
{body_content}
</div>

<script>
document.addEventListener("DOMContentLoaded", function() {{
  if (typeof renderMathInElement !== 'undefined') {{
    renderMathInElement(document.body, {{
      delimiters: [
        {{left: "$$", right: "$$", display: true}},
        {{left: "$", right: "$", display: false}}
      ],
      throwOnError: false
    }});
  }}
}});
</script>
</body>
</html>
'''

with open(output_html, 'w', encoding='utf-8') as f:
    f.write(html_template)

print("Step 2: HTML compiled successfully.")

# Step 3: Run Chrome headless to generate raw PDF
chrome_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
file_uri = 'file:///' + output_html.replace('\\', '/')
cmd = [
    chrome_path,
    '--headless',
    '--disable-gpu',
    '--virtual-time-budget=8000',
    '--no-pdf-header-footer',
    f'--print-to-pdf={raw_pdf}',
    file_uri
]

print("Step 3: Running Chrome to generate raw PDF...")
subprocess.run(cmd, capture_output=False)

if not os.path.exists(raw_pdf):
    print("Error: raw_pdf failed to generate")
    sys.exit(1)

# Step 4: Open raw PDF in PyMuPDF, add running header + Logo badge on EVERY page!
print("Step 4: Stamping logo badge and running headers onto PDF...")
doc = fitz.open(raw_pdf)

# Badge dimension: 32x32 pt
badge_w = 32
badge_h = 32
header_y = 20 # pt from top

for page_idx, p in enumerate(doc):
    w = p.rect.width
    h = p.rect.height

    # Badge rect in top-right header
    badge_rect = fitz.Rect(w - 42 - badge_w, header_y, w - 42, header_y + badge_h)
    p.insert_image(badge_rect, filename=badge_png_path, overlay=True)

    # For pages 2+, add subtle running header text and a delicate divider line
    if page_idx > 0:
        header_text = "中學超前自學 · 微積分跨科先修體系白皮書"
        p.insert_text(fitz.Point(42, header_y + 20), header_text, fontname="helv", fontsize=8.5, color=(0.4, 0.45, 0.52))
        # Hairline divider under header
        p.draw_line(fitz.Point(42, header_y + badge_h + 4), fitz.Point(w - 42, header_y + badge_h + 4), color=(0.85, 0.88, 0.92), width=0.5)

print(f"Stamped logo and header on all {len(doc)} pages.")

# Step 5: Add the 8 native PDF interactive annotations
print("Step 5: Adding native interactive annotations...")
annotations_data = [
    {
        "search": "第 2 堂",
        "title": "教研註解 1：角度單位與弧度制本質",
        "content": "【國中認知摩擦化解】：度數制（360°）是巴比倫人的人為規定。如果微積分用度數，每次對 sin(x) 微分都會甩出醜陋的常數係數 (π/180)；只有使用弧度制（弧長/半徑的無量綱純數），極限 lim(sin θ / θ) 才會剛好等於 1，微積分公式才能保持極致簡潔與自然。",
        "color": (0.15, 0.45, 0.85)
    },
    {
        "search": "第 3 堂",
        "title": "教研註解 2：重根定理與切線代數接觸階數",
        "content": "【代數視野拓寬】：國中二次拋物線的判別式 Δ=0 只能處理二次多項式。遇到三次曲線的反曲點切線時，切線會「直接穿過曲線」，國中代數會崩潰。微積分切線的代數本質是「方程聯立差式必含 (x-x0)^2 之二重根（或以上）」，這才是高等代數與微積分看待幾何切觸的真正第一原理。",
        "color": (0.85, 0.45, 0.15)
    },
    {
        "search": "第 5 堂",
        "title": "教研註解 3：連鎖律的物理本質（嚴禁分數約分教學）",
        "content": "【編寫防呆與學術嚴謹】：傳統教學常偷懶說「dy/dt = (dy/du)*(du/dt) 就像 du 上下約分一樣」，這在嚴格數學上是錯的。微分算子不是孤立整數。講義必須貫徹「尺度齒輪轉換（Gear Ratio）」的物理量綱本質（例如 Hz 換 rpm 產生的 60 倍斜率齒輪轉換），防止學生建立含混的約分概念。",
        "color": (0.85, 0.20, 0.20)
    },
    {
        "search": "第 6 堂",
        "title": "教研註解 4：自然常數 e 與半衰期 0.693 的純數來源",
        "content": "【自然常數哲學】：宇宙中所有「變化率與現存量成正比」的自指現象（細菌增殖、電容放電、放射性衰變），內在底數都是 e。若用底數 10，每次微分都會甩出 ln(10)≈2.302；只有底數為 e，自身求導才等於自身。半衰期中的 0.693 也不是實驗測得的經驗數，而是純數學常數 ln(2) 的數值近似。",
        "color": (0.15, 0.65, 0.45)
    },
    {
        "search": "第 13 堂",
        "title": "教研註解 5：消去時間的狀態空間微商 a = v(dv/dx)",
        "content": "【高階競賽物理技巧】：國中運動學總是追著時間 t 計算。但當面對空氣阻力與速度平方成正比（F=-kv^2）或萬有引力隨位置變化時，時間 t 會成為極大累贅。利用連鎖律消去時間得到的 a = v(dv/dx)，是大學理論力學與物理奧林匹亞在「位置-速度」狀態相空間中直接求解微積分的關鍵武器。",
        "color": (0.55, 0.25, 0.75)
    },
    {
        "search": "第 17 堂",
        "title": "教研註解 6：110V 交流電壓的微積分發熱有效值本質",
        "content": "【工程實體對照】：正弦交流電簡單平均為 0，物理上以「一個週期內的焦耳熱做功定積分」定義有效值。台灣/美規家用 110V 插座的瞬間最大峰值電壓實為 110*√2 ≈ 156V（每秒在 ±156V 震盪 60 次）；台灣 220V 冷氣插座瞬間峰值更達到 311V。工程設計絕緣耐壓時必須以微積分峰值為準。",
        "color": (0.15, 0.50, 0.90)
    },
    {
        "search": "第 18 堂",
        "title": "教研註解 7：化學反應級數嚴禁等同於計量係數",
        "content": "【跨科認知防呆】：國中生習慣看化學方程式係數（如 2A + B -> C），極易誤以為反應級數就等於係數 2 和 1。講義必須強烈標註：巨觀反應級數純由實驗測定，絕不能想當然爾套用化學方程式計量數！只有在微觀單步的「基元反應」中兩者才恰好吻合。",
        "color": (0.85, 0.20, 0.20)
    },
    {
        "search": "第 23 堂",
        "title": "教研註解 8：最壞情況全微分與隨機誤差均方根合成",
        "content": "【測量科學哲學】：全微分算式 dz/z = a(dx/x) + b(dy/y) 給出的是「各誤差同時往最不利方向偏離時的數學絕對上限」；但真實世界各儀器誤差彼此獨立且隨機，現代國際度量衡委員會（BIPM）規範採用統計正交合成（均方根合成）。此處是微積分全微分過渡到機率統計的完美橋樑。",
        "color": (0.20, 0.60, 0.60)
    }
]

for note in annotations_data:
    keyword = note["search"]
    for page_idx, p in enumerate(doc):
        if page_idx < 3: continue
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
            break

# Step 6: Save final PDF
doc.save(final_pdf)
doc.close()
print(f"SUCCESS! Masterpiece PDF generated with Logo & Annotations at: {final_pdf} ({os.path.getsize(final_pdf)} bytes)")
