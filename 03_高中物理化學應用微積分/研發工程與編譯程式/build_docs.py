import os
import sys
import re
import subprocess

input_md = r'C:\Users\user\.gemini\antigravity\brain\17c5c8ea-1f34-4270-a5e4-410bdd5037d4\calculus_precollege_curriculum_whitepaper.md'
output_html = r'C:\Users\user\Documents\中學超前自學_微積分先修體系企劃白皮書.html'
output_pdf = r'C:\Users\user\Documents\中學超前自學_微積分先修體系企劃白皮書.pdf'

with open(input_md, 'r', encoding='utf-8') as f:
    text = f.read()

lines = text.split('\n')
html_parts = []
in_mermaid = False
table_rows = []

def format_inline(s):
    # Bold
    s = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', s)
    # Inline code
    s = re.sub(r'`([^`]+)`', r'<code>\1</code>', s)
    # Markdown links [text](#anchor)
    s = re.sub(r'\[(.*?)\]\((.*?)\)', r'<a href="\2">\1</a>', s)
    return s

def render_table(rows):
    if not rows:
        return ''
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

    # Handle Mermaid blocks
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

    # Handle Tables
    if stripped.startswith('|') and stripped.endswith('|'):
        table_rows.append(stripped)
        i += 1
        continue
    else:
        if table_rows:
            html_parts.append(render_table(table_rows))
            table_rows = []

    # Headings
    if stripped.startswith('# '):
        title = stripped[2:].strip()
        html_parts.append(f'''
        <div class="cover-page">
          <div class="cover-tag">ACADEMIC SPECIFICATION WHITE PAPER</div>
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
    --accent-gold: #b45309;
    --accent-chem: #0d9488;
    --text-dark: #1e293b;
    --text-muted: #64748b;
    --bg-card: #f8fafc;
    --border-light: #e2e8f0;
    --font-main: -apple-system, BlinkMacSystemFont, "SF Pro Text", "SF Pro Display", "PingFang TC", "Noto Sans TC", "Microsoft JhengHei", sans-serif;
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

  /* Cover Page Styling */
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

  /* Table of Contents */
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
    transition: background 0.2s;
  }}
  .toc-item a:hover {{
    background: var(--primary-light);
    color: var(--accent);
  }}

  /* Chapters & Sections */
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

  /* Stage & Lesson Cards */
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

  /* Content elements */
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
  .bullet-content {{
    flex: 1;
    color: #334155;
  }}
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

  /* Tables */
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
  .doc-table tr:last-child td {{
    border-bottom: none;
  }}

  /* Flowchart Visual Box */
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
    box-shadow: 0 1px 3px rgba(0,0,0,0.02);
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

  .flow-bridge {{
    margin-top: 15px;
    text-align: center;
  }}
  .flow-bridge-arrow {{
    font-size: 12px;
    font-weight: 800;
    color: var(--accent);
    margin-bottom: 6px;
  }}
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

  .divider {{
    border: none;
    border-top: 1px solid var(--border-light);
    margin: 35px 0;
  }}

  /* Print and PDF Specific Rules */
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

print(f'HTML generated: {output_html} ({os.path.getsize(output_html)} bytes)')

# Convert HTML to PDF using Chrome
chrome_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
file_uri = 'file:///' + output_html.replace('\\', '/')
cmd = [
    chrome_path,
    '--headless',
    '--disable-gpu',
    '--virtual-time-budget=8000',
    '--no-pdf-header-footer',
    f'--print-to-pdf={output_pdf}',
    file_uri
]

print('Running Chrome to generate polished PDF...')
p = subprocess.run(cmd, capture_output=False)
if os.path.exists(output_pdf):
    print(f'SUCCESS! PDF generated: {output_pdf} ({os.path.getsize(output_pdf)} bytes)')
else:
    print('Failed to generate PDF')
