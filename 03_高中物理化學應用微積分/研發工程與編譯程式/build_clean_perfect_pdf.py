import fitz
import numpy as np
from PIL import Image
import os
import re
import subprocess
import shutil
import base64

# Step 1: Prepare Clean Transparent Badge PNG from SVG
svg_path = r'C:\Users\user\Documents\woieyufan-brand-assets\woieyufan-logo_downward.svg'
if not os.path.exists(svg_path):
    svg_path = r'C:\Users\user\Documents\woieyufan-logo_downward.svg'

doc_svg = fitz.open(svg_path)
page_svg = doc_svg[0]
pix = page_svg.get_pixmap(dpi=300, alpha=False)
temp_png = r'C:\Users\user\.gemini\antigravity\brain\17c5c8ea-1f34-4270-a5e4-410bdd5037d4\scratch\temp_render.png'
pix.save(temp_png)

pil_img = Image.open(temp_png).convert("RGBA")
img_data = np.array(pil_img)
non_white = (img_data[:, :, 0] < 240) | (img_data[:, :, 1] < 240) | (img_data[:, :, 2] < 240)
coords = np.argwhere(non_white)
y0, x0 = coords.min(axis=0)
y1, x1 = coords.max(axis=0) + 1
pil_img = pil_img.crop((x0, y0, x1, y1))

# Process transparency
cropped_data = np.array(pil_img)
white_mask = (cropped_data[:, :, 0] > 230) & (cropped_data[:, :, 1] > 230) & (cropped_data[:, :, 2] > 230)
cropped_data[white_mask, 3] = 0
pil_img = Image.fromarray(cropped_data)

badge_png_path = r'C:\Users\user\.gemini\antigravity\brain\17c5c8ea-1f34-4270-a5e4-410bdd5037d4\scratch\clean_logo.png'
pil_img.save(badge_png_path, "PNG")

with open(badge_png_path, "rb") as f:
    logo_base64 = base64.b64encode(f.read()).decode("utf-8")
logo_data_uri = f"data:image/png;base64,{logo_base64}"
print("Step 1: Logo prepared cleanly.")

# Step 2: Build HTML with Disciplined, Spacious Book-Grade Typography
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
    return r'''
    <div class="flowchart-container">
      <div class="flow-header">
        <h4 class="flow-main-title">純數學工具生長之樹與自然科學跨科降維對照</h4>
        <p class="flow-subtitle">以純數學工具向上生長為唯一骨架主軸，自然科學為驗證載體與降維打擊舞台</p>
      </div>
      <div class="flow-grid">
        <div class="flow-col flow-col-a">
          <div class="flow-col-title">純數學工具生長之樹（核心主幹）</div>
          <div class="flow-node">1. 階梯一：差商消元與多項式求導算子</div>
          <div class="flow-arrow">↓</div>
          <div class="flow-node">2. 階梯二：量綱連鎖律與狀態空間微商 $a = v(dv/dx)$</div>
          <div class="flow-arrow">↓</div>
          <div class="flow-node">3. 階梯三：無量綱弧度制與極坐標微分幾何</div>
          <div class="flow-arrow">↓</div>
          <div class="flow-node">4. 階梯四：黎曼和、基本定理 (FTC) 與第一面積矩</div>
          <div class="flow-arrow">↓</div>
          <div class="flow-node highlight-a">5. 階梯五：狀態空間定積分幾何形態學 $dE = v\,dp$</div>
          <div class="flow-arrow">↓</div>
          <div class="flow-node">6. 階梯六：超越函數發明、常微分方程 (ODE) 與正弦降冪</div>
          <div class="flow-arrow">↓</div>
          <div class="flow-node highlight-b">7. 階梯七：連續機率密度微積分 (PDF/CDF) 與矩理論</div>
        </div>

        <div class="flow-col flow-col-b">
          <div class="flow-col-title">自然科學跨科驗證與降維打擊（應用載體）</div>
          <div class="flow-node">1. 瞬時速度、加速度與代數切線重根定理</div>
          <div class="flow-arrow">↓</div>
          <div class="flow-node">2. 消去時間之相空間運動學與費馬時間極值折射</div>
          <div class="flow-arrow">↓</div>
          <div class="flow-node">3. 向心加速度純代數兩步得證 $a = -\omega^2 r$</div>
          <div class="flow-arrow">↓</div>
          <div class="flow-node">4. 彈簧變力做功與形心 $\frac{1}{3}h$ 之冪反演</div>
          <div class="flow-arrow">↓</div>
          <div class="flow-node highlight-physics">5. 物質動能 $\frac{1}{2}mv^2$ (三角形) vs 光子 $E=pc$ (矩形)</div>
          <div class="flow-arrow">↓</div>
          <div class="flow-node highlight-chem">6. 簡諧 SHM 解析解、110V 交流電峰值 156V 與化學反應級數</div>
          <div class="flow-arrow">↓</div>
          <div class="flow-node highlight-quantum">7. 馬克士威速率尾部面積、波函數歸一化與測不準原理</div>
        </div>
      </div>

      <div class="flow-bridge">
        <div class="flow-bridge-arrow">↓↓ 兩階段數理閉環：書籍啟蒙地圖 ──> 課堂道場親炙 ↓↓</div>
        <div class="flow-center-box">
          <strong>核心心法</strong>：工具未備絕不強解；書籍給予全景降維震撼，課堂帶領黑板實彈推演與深水區破局！
        </div>
      </div>
    </div>
    '''

i = 0
open_lesson = False
in_toc = False
just_saw_ladder = False

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
        <div class="cover-wrapper page-break-after">
          <div class="cover-top-bar">
            <div class="cover-tag">ACADEMIC SPECIFICATION WHITE PAPER</div>
            <img src="{logo_data_uri}" class="cover-brand-logo" alt="Logo" />
          </div>
          <div class="cover-title-area">
            <h1 class="doc-title">{title}</h1>
            <h2 class="doc-subtitle">從出版級進階自學專著（書籍）到黑板研討道場（課堂）之兩階段工程母本</h2>
          </div>
          <div class="meta-badge-row">
            <span class="badge badge-primary">兩階段工程定稿 v3.0</span>
            <span class="badge">階段一：案頭進階專著</span>
            <span class="badge">階段二：黑板研討道場</span>
            <span class="badge">24 專題 / 48 小時</span>
            <span class="badge">iPad 舒展閱讀典藏版</span>
          </div>
          <div class="cover-meta-grid">
            <div class="meta-item"><span class="meta-label">體系架構</span><span class="meta-val">階段一（出版自學專著）＋ 階段二（黑板研討道場）</span></div>
            <div class="meta-item"><span class="meta-label">課時規格</span><span class="meta-val">7 大數學階梯 · 24 專題研討（每堂 120 分鐘）</span></div>
            <div class="meta-item"><span class="meta-label">核心宗旨</span><span class="meta-val">純數學工具向上生長為唯一骨架，自然科學為驗證載體</span></div>
            <div class="meta-item"><span class="meta-label">閱讀格式</span><span class="meta-val">跨平台出版級 PDF · iPad 舒展流式排版</span></div>
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
            html_parts.append(f'''
            <div class="toc-wrapper page-break-after">
              <h2 class="toc-main-title">課程企劃白皮書 · 總體目錄</h2>
              <div class="toc-grid">
            ''')
        else:
            if in_toc:
                html_parts.append('</div></div>')
                in_toc = False
            html_parts.append(f'''
            <div class="chapter-header-box page-break-before">
              <h2 class="chapter-title">{subtitle}</h2>
            </div>
            ''')
    elif stripped.startswith('### '):
        if open_lesson:
            html_parts.append('</div>')
            open_lesson = False
        h3 = stripped[4:].strip()
        # Strictly match Chapter 4 Ladder Banners: "第一階", "第二階", ..., "第七階"
        if re.match(r'^第[一二三四五六七]階', h3):
            # 第一階 follows right under Chapter 4 title on Page 11, so no page-break-before
            # 第二階 to 第七階 start on a fresh page
            banner_cls = "stage-banner" if "第一階" in h3 else "stage-banner page-break-before"
            html_parts.append(f'''
            <div class="{banner_cls}">
              <h3>{h3}</h3>
            </div>
            ''')
            just_saw_ladder = True
        else:
            # Regular Section Title (e.g. 1.1, 1.2, 1.3, 1.4, 2.1, 2.2, 2.3, 3.1-3.6, 5.1-5.3, 6.1-6.3)
            # Enforce thematic page breaks to eliminate awkward mid-derivation splits and orphan lines:
            # - Chapter 1: 1.3 starts on Page 4 (keeping 1.3 + 1.4 together cleanly)
            # - Chapter 2: 2.2 starts on Page 6 (keeping 2.2 Table + 2.3 together cleanly)
            # - Chapter 3: 3.3 starts on Page 8 (keeping 3.3 complete on Page 8)
            # - Chapter 3: 3.4 starts on Page 9 (keeping 3.4 complete on Page 9)
            # - Chapter 3: 3.5 starts on Page 10 (keeping 3.5 + 3.6 complete on Page 10)
            break_cls = ""
            if any(h3.startswith(p) for p in ['1.3 ', '2.2 ', '3.3 ', '3.4 ', '3.5 ']):
                break_cls = " page-break-before"
            
            html_parts.append(f'<h3 class="section-title{break_cls}">{format_inline(h3)}</h3>')
            just_saw_ladder = False
    elif stripped.startswith('#### '):
        if open_lesson:
            html_parts.append('</div>')
        open_lesson = True
        h4 = stripped[5:].strip()
        # Disciplined page breaks for Chapter 4:
        # Every single lesson gets exactly ONE full page!
        # If it immediately follows a Stage Banner (Lessons 1, 4, 7, 10, 14, 16, 20), stay on that page!
        # Otherwise, start on a fresh page!
        if just_saw_ladder:
            lesson_cls = "lesson-section"
            just_saw_ladder = False
        else:
            lesson_cls = "lesson-section page-break-before"

        html_parts.append(f'''
        <div class="{lesson_cls}">
          <div class="lesson-header-row">
            <span class="lesson-pill">雙軌工程規格</span>
            <h4 class="lesson-title">{format_inline(h4)}</h4>
          </div>
        ''')
    elif stripped.startswith('---'):
        if in_toc:
            html_parts.append('</div></div>')
            in_toc = False
    elif stripped.startswith('* ') or stripped.startswith('- '):
        raw_c = stripped[2:].strip()
        content = format_inline(raw_c)
        if in_toc:
            html_parts.append(f'<div class="toc-item">{content}</div>')
        else:
            if '【書籍章節藍圖' in raw_c:
                html_parts.append('<div class="subtrack-title subtrack-book"><span class="track-icon">📖</span> 階段一：書籍章節藍圖（The Book）</div>')
            elif '【課堂道場實戰' in raw_c:
                html_parts.append('<div class="subtrack-title subtrack-sanctuary"><span class="track-icon">⚔️</span> 階段二：課堂道場實戰（The Sanctuary）</div>')
            elif '導師邊欄手札' in raw_c:
                text_clean = content.replace('<strong>導師邊欄手札</strong>：', '')
                html_parts.append(f'''
                <div class="callout-box callout-mentor">
                  <span class="callout-tag">💡 導師邊欄手札</span>
                  <div class="callout-text">{text_clean}</div>
                </div>
                ''')
            elif '章末思想擂台' in raw_c or '章末終極道場召喚' in raw_c:
                text_clean = content.replace('<strong>章末思想擂台</strong>：', '').replace('<strong>章末終極道場召喚</strong>：', '')
                html_parts.append(f'''
                <div class="callout-box callout-arena">
                  <span class="callout-tag">🔥 章末開放擂台（課堂召喚）</span>
                  <div class="callout-text">{text_clean}</div>
                </div>
                ''')
            else:
                html_parts.append(f'<div class="bullet-item"><span class="bullet-dot">•</span><div class="bullet-content">{content}</div></div>')
    elif re.match(r'^\d+\.\s', stripped):
        m = re.match(r'^(\d+)\.\s*(.*)', stripped)
        num = m.group(1)
        content = format_inline(m.group(2))
        html_parts.append(f'<div class="numbered-item"><span class="num-badge">{num}</span><div class="num-content">{content}</div></div>')
    elif stripped.startswith('$$'):
        eq = stripped.strip('$')
        if not eq:
            math_lines = []
            i += 1
            while i < len(lines) and not lines[i].strip().startswith('$$'):
                math_lines.append(lines[i].strip())
                i += 1
            eq = ' '.join(math_lines)
        html_parts.append(f'<div class="math-block">$${eq}$$</div>')
    elif stripped.startswith('> '):
        quote_text = format_inline(stripped[2:])
        html_parts.append(f'<div class="quote-box">{quote_text}</div>')
    elif stripped:
        html_parts.append(f'<p class="para">{format_inline(stripped)}</p>')

    i += 1

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
<title>中學超前自學：以近代高等數學工具為骨架之數理跨科先修體系白皮書</title>

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
    --text-body: #24292f;
    --text-muted: #64748b;
    --border-light: #e2e8f0;
    --font-main: -apple-system, BlinkMacSystemFont, "Segoe UI", "PingFang TC", "Microsoft JhengHei", "Noto Sans TC", sans-serif;
  }}

  * {{ box-sizing: border-box; }}
  body {{
    font-family: var(--font-main);
    color: var(--text-body);
    line-height: 1.78;
    background-color: #f8fafc;
    margin: 0;
    padding: 0;
    -webkit-font-smoothing: antialiased;
    text-rendering: optimizeLegibility;
  }}

  .page-container {{
    max-width: 900px;
    margin: 24px auto;
    background: #ffffff;
    padding: 30px 60px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.06);
    border-radius: 16px;
  }}

  @media (max-width: 768px) {{
    .page-container {{
      margin: 0;
      padding: 20px 16px;
      border-radius: 0;
    }}
  }}

  /* Page Break Controls */
  .page-break-before {{
    page-break-before: always;
    break-before: page;
  }}
  .page-break-after {{
    page-break-after: always;
    break-after: page;
  }}

  /* Cover Page Wrapper */
  .cover-wrapper {{
    background: linear-gradient(135deg, #f8fafc 0%, #edf2f7 100%);
    border: 1.5px solid #cbd5e1;
    border-radius: 14px;
    padding: 45px 45px;
    min-height: 900px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
  }}
  .cover-top-bar {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 24px;
  }}
  .cover-brand-logo {{
    height: 52px;
    width: auto;
    object-fit: contain;
  }}
  .cover-tag {{
    font-size: 11px;
    font-weight: 800;
    letter-spacing: 2px;
    color: var(--accent);
    background: #ffffff;
    border: 1.5px solid var(--primary-border);
    padding: 4px 10px;
    border-radius: 6px;
    white-space: nowrap;
  }}
  .doc-title {{
    font-size: 28px;
    font-weight: 800;
    color: var(--primary);
    margin: 0 0 14px 0;
    letter-spacing: -0.5px;
    line-height: 1.38;
  }}
  .doc-subtitle {{
    font-size: 16px;
    font-weight: 500;
    color: var(--text-muted);
    margin: 0 0 24px 0;
    line-height: 1.55;
  }}
  .meta-badge-row {{
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
    margin-bottom: 28px;
  }}
  .badge {{
    background: #ffffff;
    color: var(--text-dark);
    border: 1px solid #cbd5e1;
    padding: 4px 12px;
    border-radius: 20px;
    font-size: 12.5px;
    font-weight: 600;
    white-space: nowrap;
  }}
  .badge-primary {{
    background: var(--primary);
    color: #ffffff;
    border-color: var(--primary);
  }}

  .cover-meta-grid {{
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 16px;
    border-top: 2px solid var(--primary-border);
    padding-top: 22px;
  }}
  @media (max-width: 600px) {{
    .cover-meta-grid {{ grid-template-columns: 1fr; }}
  }}
  .meta-item {{
    font-size: 13.5px;
    display: flex;
    flex-direction: column;
  }}
  .meta-label {{
    color: var(--text-muted);
    font-weight: 600;
    margin-bottom: 3px;
  }}
  .meta-val {{
    color: var(--primary-dark);
    font-weight: 700;
  }}

  /* Table of Contents Wrapper (Strictly Single Page) */
  .toc-wrapper {{
    background: #ffffff;
    border: 1px solid var(--border-light);
    border-radius: 12px;
    padding: 16px 24px;
    margin-bottom: 16px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.03);
  }}
  .toc-main-title {{
    font-size: 18px;
    font-weight: 800;
    color: var(--primary);
    margin: 0 0 10px 0;
    padding-bottom: 6px;
    border-bottom: 2px solid var(--primary);
  }}
  .toc-grid {{
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 4px 12px;
  }}
  @media (max-width: 640px) {{
    .toc-grid {{ grid-template-columns: 1fr; }}
  }}
  .toc-item {{
    font-size: 11px;
    color: #334155;
    padding: 3.5px 7px;
    border-radius: 4px;
    line-height: 1.4;
    background: #f8fafc;
    border-left: 2.5px solid var(--accent);
  }}
  .toc-item a {{
    color: var(--text-dark);
    text-decoration: none;
    font-weight: 500;
  }}
  .toc-item a:hover {{
    color: var(--accent);
  }}

  /* Chapter Headers */
  .chapter-header-box {{
    margin-top: 18px;
    margin-bottom: 14px;
  }}
  .chapter-title {{
    font-size: 22px;
    font-weight: 800;
    color: var(--primary);
    margin: 4px 0 10px 0;
    letter-spacing: -0.3px;
    border-bottom: 2.5px solid var(--primary);
    padding-bottom: 6px;
    line-height: 1.35;
  }}
  
  /* Standard Section Titles (Completely Uniform for 1.x, 2.x, 3.x, 5.x, 6.x) */
  .section-title {{
    font-size: 16px;
    font-weight: 700;
    color: #1e3a8a;
    margin: 18px 0 8px 0;
    padding-bottom: 4px;
    border-bottom: 1.5px solid #e2e8f0;
    line-height: 1.4;
  }}

  /* Chapter 4 Stage Banner (Strictly Ladder Banners) */
  .stage-banner {{
    background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
    color: #ffffff;
    padding: 10px 18px;
    border-radius: 8px;
    margin: 16px 0 14px 0;
    page-break-after: avoid;
    break-after: avoid;
    box-shadow: 0 4px 12px rgba(15, 23, 42, 0.08);
  }}
  .stage-banner h3 {{
    margin: 0;
    font-size: 15px;
    letter-spacing: 0.5px;
    font-weight: 800;
  }}

  /* Lesson Section (Fluid Book-Style, NO CRAMPED BOXES) */
  .lesson-section {{
    margin-top: 12px;
    margin-bottom: 20px;
    padding-top: 0;
    page-break-inside: avoid;
    break-inside: avoid;
  }}
  .lesson-header-row {{
    display: flex;
    align-items: center;
    gap: 8px;
    margin-bottom: 8px;
  }}
  .lesson-pill {{
    font-size: 11px;
    font-weight: 700;
    background: var(--primary-light);
    color: var(--accent);
    padding: 2px 7px;
    border-radius: 5px;
    border: 1px solid var(--primary-border);
    white-space: nowrap;
    flex-shrink: 0;
  }}
  .lesson-title {{
    font-size: 16px;
    font-weight: 800;
    color: var(--primary);
    margin: 0;
    line-height: 1.4;
  }}

  /* Subtracks */
  .subtrack-title {{
    font-size: 13.5px;
    font-weight: 700;
    padding: 5px 12px;
    border-radius: 0 6px 6px 0;
    margin: 10px 0 5px 0;
    display: flex;
    align-items: center;
    gap: 6px;
  }}
  .subtrack-book {{
    background: #f0f9ff;
    color: #0369a1;
    border-left: 4px solid #0284c7;
  }}
  .subtrack-sanctuary {{
    background: #fffbeb;
    color: #b45309;
    border-left: 4px solid #f59e0b;
  }}
  .track-icon {{
    font-size: 13px;
  }}

  /* Callout Boxes (Book Style) */
  .callout-box {{
    margin: 8px 0 10px 0;
    padding: 10px 14px;
    border-radius: 0 8px 8px 0;
    font-size: 13px;
    line-height: 1.68;
  }}
  .callout-mentor {{
    background: #faf5ff;
    border-left: 4px solid #a855f7;
    color: #581c87;
  }}
  .callout-mentor .callout-tag {{
    font-weight: 800;
    font-size: 11.5px;
    color: #7e22ce;
    margin-bottom: 4px;
    display: block;
  }}
  .callout-arena {{
    background: #fff1f2;
    border-left: 4px solid #f43f5e;
    color: #881337;
  }}
  .callout-arena .callout-tag {{
    font-weight: 800;
    font-size: 11.5px;
    color: #be123c;
    margin-bottom: 4px;
    display: block;
  }}
  .callout-text {{
    display: block;
  }}

  /* Paragraphs & Lists */
  .para {{
    font-size: 14.5px;
    color: var(--text-body);
    margin: 8px 0;
    text-align: justify;
    line-height: 1.78;
    letter-spacing: 0.02em;
  }}
  .bullet-item {{
    display: flex;
    align-items: flex-start;
    gap: 8px;
    margin: 4px 0;
    font-size: 14px;
    line-height: 1.72;
  }}
  .bullet-dot {{
    color: var(--accent);
    font-weight: bold;
    font-size: 13px;
    line-height: 1.6;
  }}
  .bullet-content {{ flex: 1; color: var(--text-body); }}
  .numbered-item {{
    display: flex;
    align-items: flex-start;
    gap: 8px;
    margin: 5px 0;
    font-size: 14px;
    line-height: 1.72;
  }}
  .num-badge {{
    background: #e2e8f0;
    color: #1e293b;
    font-size: 11px;
    font-weight: 700;
    padding: 2px 6px;
    border-radius: 4px;
    margin-top: 2px;
    flex-shrink: 0;
  }}
  .num-content {{ flex: 1; color: var(--text-body); }}

  .quote-box {{
    background: #f8fafc;
    border-left: 4px solid var(--accent);
    padding: 8px 14px;
    margin: 10px 0;
    font-size: 12.5px;
    line-height: 1.6;
    color: #334155;
    border-radius: 0 6px 6px 0;
  }}

  .math-block {{
    background: #f8fafc;
    border: 1px solid #edf2f7;
    padding: 10px 16px;
    border-radius: 8px;
    margin: 10px 0;
    text-align: center;
    overflow-x: auto;
    font-size: 14.5px;
  }}

  /* Table styling */
  .table-container {{
    margin: 14px 0;
    overflow-x: auto;
  }}
  .doc-table {{
    width: 100%;
    border-collapse: collapse;
    font-size: 13px;
    line-height: 1.6;
  }}
  .doc-table th {{
    background: #f1f5f9;
    color: var(--primary);
    font-weight: 700;
    border: 1px solid #cbd5e1;
    padding: 8px 12px;
    text-align: left;
  }}
  .doc-table td {{
    border: 1px solid #e2e8f0;
    padding: 8px 12px;
    color: #334155;
  }}
  .doc-table tr:nth-child(even) {{
    background: #f8fafc;
  }}

  /* Flowchart / Topology styling */
  .flowchart-container {{
    background: #ffffff;
    border: 1.5px solid var(--primary-border);
    border-radius: 12px;
    padding: 16px 20px;
    margin: 18px 0;
    box-shadow: 0 4px 12px rgba(0,0,0,0.04);
  }}
  .flow-header {{
    text-align: center;
    margin-bottom: 14px;
    padding-bottom: 10px;
    border-bottom: 1.5px solid #f1f5f9;
  }}
  .flow-main-title {{
    font-size: 16px;
    font-weight: 800;
    color: var(--primary);
    margin: 0 0 4px 0;
  }}
  .flow-subtitle {{
    font-size: 12.5px;
    color: var(--text-muted);
    margin: 0;
  }}
  .flow-grid {{
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 16px;
  }}
  .flow-col {{
    display: flex;
    flex-direction: column;
    gap: 5px;
  }}
  .flow-col-title {{
    font-size: 13px;
    font-weight: 800;
    padding: 5px 10px;
    border-radius: 6px;
    text-align: center;
    margin-bottom: 5px;
  }}
  .flow-col-a .flow-col-title {{
    background: #eff6ff;
    color: #1d4ed8;
    border: 1px solid #bfdbfe;
  }}
  .flow-col-b .flow-col-title {{
    background: #f0fdf4;
    color: #15803d;
    border: 1px solid #bbf7d0;
  }}
  .flow-node {{
    font-size: 12px;
    padding: 5px 8px;
    border-radius: 5px;
    background: #f8fafc;
    border: 1px solid #e2e8f0;
    color: #334155;
    line-height: 1.45;
  }}
  .highlight-a {{
    background: #e0f2fe;
    border-color: #7dd3fc;
    color: #0369a1;
    font-weight: 700;
  }}
  .highlight-b {{
    background: #fae8ff;
    border-color: #f0abfc;
    color: #86198f;
    font-weight: 700;
  }}
  .highlight-physics {{
    background: #fee2e2;
    border-color: #fca5a5;
    color: #b91c1c;
    font-weight: 700;
  }}
  .highlight-chem {{
    background: #fef3c7;
    border-color: #fcd34d;
    color: #b45309;
    font-weight: 700;
  }}
  .highlight-quantum {{
    background: #ccfbf1;
    border-color: #5eead4;
    color: #0f766e;
    font-weight: 700;
  }}
  .flow-arrow {{
    text-align: center;
    font-size: 11px;
    color: #94a3b8;
    line-height: 1;
    font-weight: bold;
  }}
  .flow-bridge {{
    margin-top: 12px;
    padding-top: 10px;
    border-top: 1.5px dashed var(--primary-border);
    text-align: center;
  }}
  .flow-bridge-arrow {{
    font-size: 12px;
    font-weight: 800;
    color: var(--accent);
    margin-bottom: 4px;
  }}
  .flow-center-box {{
    font-size: 12.5px;
    color: var(--primary-dark);
    background: #eff6ff;
    padding: 6px 12px;
    border-radius: 6px;
    display: inline-block;
  }}

  /* Print specific layout */
  @page {{
    size: A4 portrait;
    margin: 18mm 16mm 20mm 16mm;
  }}
  @media print {{
    body {{
      background-color: #ffffff;
    }}
    .page-container {{
      max-width: 100%;
      margin: 0;
      padding: 0;
      box-shadow: none;
      border-radius: 0;
    }}
  }}
</style>
</head>
<body>

<div class="page-container">
{body_content}
</div>

<script>
  document.addEventListener("DOMContentLoaded", function() {{
    renderMathInElement(document.body, {{
      delimiters: [
        {{left: '$$', right: '$$', display: true}},
        {{left: '$', right: '$', display: false}},
        {{left: '\\\\(', right: '\\\\)', display: false}},
        {{left: '\\\\[', right: '\\\\]', display: true}}
      ],
      throwOnError: false
    }});
  }});
</script>

</body>
</html>
'''

with open(output_html, 'w', encoding='utf-8') as f:
    f.write(html_template)
print("Step 2: Disciplined Book-Grade HTML compiled successfully.")

# Step 3: Run Chrome headless to generate clean PDF
chrome_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
if not os.path.exists(chrome_path):
    chrome_path = r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'

cmd = [
    chrome_path,
    '--headless=new',
    '--disable-gpu',
    '--no-pdf-header-footer',
    f'--print-to-pdf={output_pdf}',
    output_html
]

print("Step 3: Generating disciplined book-grade PDF with Chrome...")
subprocess.run(cmd, capture_output=False)

# Step 4: Stamping Exclusive woieyufan Running Header & Running Footer onto PDF
print("Step 4: Stamping exclusive woieyufan Running Headers and Footers onto all pages (2+)...")
doc = fitz.open(output_pdf)
total_pages = len(doc)
print(f"Total pages in clean PDF: {total_pages}")

font_path = r'C:\Windows\Fonts\msjh.ttc'

for page_idx in range(len(doc)):
    if page_idx == 0:
        continue  # Skip cover page

    p = doc[page_idx]
    w = p.rect.width
    h = p.rect.height
    x0 = 45.35
    x1 = w - 45.35

    # 1. Running Header
    # Badge rect (24x24 pt) in top-right
    badge_rect = fitz.Rect(x1 - 24, 15, x1, 39)
    p.insert_image(badge_rect, filename=badge_png_path, overlay=True)

    # Header text (left)
    header_text = 'woieyufan EDUCATION ｜ 中學超前自學 · 兩階段數理先修白皮書'
    p.insert_textbox(
        fitz.Rect(x0, 20, x1 - 32, 38),
        header_text,
        fontname='msjh',
        fontfile=font_path,
        fontsize=8.5,
        color=(0.12, 0.23, 0.54)
    )

    # Hairline divider under header
    p.draw_line(
        fitz.Point(x0, 43),
        fitz.Point(x1, 43),
        color=(0.80, 0.84, 0.88),
        width=0.5
    )

    # 2. Running Footer
    footer_y = h - 38
    # Hairline divider above footer
    p.draw_line(
        fitz.Point(x0, footer_y),
        fitz.Point(x1, footer_y),
        color=(0.80, 0.84, 0.88),
        width=0.5
    )

    # Footer left text: Brand & Curriculum Phase
    footer_copy = '© woieyufan · 機密智庫工程母本 · 階段一書籍 ── 階段二道場'
    p.insert_textbox(
        fitz.Rect(x0, footer_y + 6, x1 - 100, footer_y + 22),
        footer_copy,
        fontname='msjh',
        fontfile=font_path,
        fontsize=8,
        color=(0.39, 0.45, 0.55)
    )

    # Footer right text: Dynamic Page numbering
    page_str = f'Page {page_idx + 1} / {total_pages}'
    p.insert_textbox(
        fitz.Rect(x1 - 100, footer_y + 6, x1, footer_y + 22),
        page_str,
        fontname='msjh',
        fontfile=font_path,
        fontsize=8.5,
        color=(0.39, 0.45, 0.55),
        align=fitz.TEXT_ALIGN_RIGHT
    )

print("Step 4 complete: Headers, footers, badges and page numbers stamped.")

# Step 5: Embed native PDF interactive annotations
print("Step 5: Embedding native PDF interactive annotations...")
annotations_data = [
    {
        "search": "第 3 堂",
        "title": "教研註解 1：切線代數本質與二重根定理",
        "content": "【超越國中代數】：國中判別式 Δ=0 只能解二次拋物線。遇到三次曲線反曲點切線時，切線會「直接穿過曲線」，國中代數徹底崩潰。微積分切線的第一性原理是「聯立差式必含 (x-x0)^2 之二重根（或三重根）」，這才是高等代數看待切觸的真正本質。",
        "color": (0.85, 0.45, 0.15)
    },
    {
        "search": "第 4 堂",
        "title": "教研註解 2：連鎖律的物理本質（嚴禁分數約分教學）",
        "content": "【編寫防呆】：傳統教學常偷懶說「dy/dt = (dy/du)*(du/dt) 就像 du 上下約分」，這在數學上是錯的。微分算子不是孤立整數。講義必須貫徹「尺度齒輪轉換（Gear Ratio）」的物理量綱本質（如 Hz 換 rpm 產生的 60 倍斜率齒輪轉換），防止學生建立含混的約分概念。",
        "color": (0.85, 0.20, 0.20)
    },
    {
        "search": "第 6 堂",
        "title": "教研註解 3：消去時間的狀態空間微商 a = v(dv/dx)",
        "content": "【競賽物理神器】：國中運動學總是追著時間 t 計算。但當面對空氣阻力 F=-kv^2 或萬有引力隨位置變化時，時間 t 會成為累贅。利用連鎖律消去時間得到的 a = v(dv/dx)，是大學理論力學與物理奧賽在「位置-速度」狀態相空間中直接求解的關鍵武器。",
        "color": (0.55, 0.25, 0.75)
    },
    {
        "search": "第 9 堂",
        "title": "教研註解 4：費馬極值原理導出斯乃爾折射定律",
        "content": "【幾何光學第一性原理】：斯乃爾定律 n1*sinθ1 = n2*sinθ2 在高中被當成孤立經驗公式。微積分從「光走時間最短路徑」出發，對傳播時間函數求導 dt/dx = 0，兩步純代數推導出折射定律，論證幾何光學是大自然微分求極值的必然結果。",
        "color": (0.15, 0.65, 0.45)
    },
    {
        "search": "第 12 堂",
        "title": "教研註解 5：三角形形心 1/3h 的冪反演本質",
        "content": "【形心幾何解密】：三角形形心高距底邊 1/3h 與圓錐體積 1/3 係數，在國中只能死背。微積分揭示其本質：第一面積矩微元積分中，一次冪反導出二次項，二次項反導出三次項分母 1/3，兩者在微積分冪函數代數反演上完全同構。",
        "color": (0.15, 0.45, 0.85)
    },
    {
        "search": "第 14 堂",
        "title": "教研註解 6：動能量綱通用微分式 dE = v dp（三角形 vs 矩形）",
        "content": "【微積分終極幾何解密】：為什麼物質動能有 1/2mv^2，而光子能量是 E=pc（沒有 1/2）？做功微元 dW = v dp。物質速度隨動量線性上升 v=p/m，積分圖形是「三角形」，面積必帶 1/2；而光速 c 恆定，積分圖形是「長方形」，係數必為 1！",
        "color": (0.90, 0.15, 0.15)
    },
    {
        "search": "第 16 堂",
        "title": "教研註解 7：自然常數 e 與半衰期 0.693 的純數來源",
        "content": "【自然常數哲學】：宇宙中所有「變化率與現存量成正比」的自指現象（細菌增殖、電容放電、放射性衰變），內在底數都是 e。半衰期公式中的 0.693 不是實驗測量出來的經驗數，而是純數學常數 ln(2) 的數值近似。",
        "color": (0.15, 0.65, 0.45)
    },
    {
        "search": "第 18 堂",
        "title": "教研註解 8：二階 ODE 特徵根法（徹底淘汰參考圓投影）",
        "content": "【物理現代化】：高中教材強行用「參考圓水平投影」包裝簡諧運動，是極其繁複且與現代科學脫節的假教學。微積分以二階常微分方程 x'' + ω^2 x = 0 的特徵根法 r = ±iω，純代數演繹出正弦餘弦振盪解，從第一性原理秒殺 SHM。",
        "color": (0.85, 0.45, 0.15)
    },
    {
        "search": "第 19 堂",
        "title": "教研註解 9：110V 交流電壓的方均根 RMS 定積分本質",
        "content": "【工程實體對照】：正弦交流電簡單平均為 0，物理上以焦耳熱做功定積分定義有效值。台灣家用 110V 插座的瞬間最大峰值電壓實為 110*√2 ≈ 156V（每秒在 ±156V 震盪 60 次）；220V 冷氣插座瞬間峰值更達到 311V。工程絕緣耐壓必須以峰值為準。",
        "color": (0.15, 0.50, 0.90)
    },
    {
        "search": "第 22 堂",
        "title": "教研註解 10：馬克士威-波茲曼速率分佈與活化能尾部面積",
        "content": "【化學世紀之謎】：升溫 10K 分子平均動能只增加約 3%，為什麼反應速率會暴增 2~3 倍？因為活化能分子比例是微積分的「尾部積分（Tail Integral）」。在指數衰減曲線下，溫度微升會導致高能尾部覆蓋的幾何面積指數級暴增！",
        "color": (0.75, 0.20, 0.75)
    },
    {
        "search": "第 24 堂",
        "title": "教研註解 11：近代物理測不準原理的統計標準差本質",
        "content": "【量子力學正名】：測不準原理 Δx · Δp ≥ ħ/2 不是因為「儀器碰撞粒子導致測不準」（物理學史上的假說），而是波包在坐標與動量傅立葉對偶空間中，兩個連續機率分佈「標準差之積」的純數學下限！",
        "color": (0.20, 0.60, 0.60)
    }
]

temp_pdf = r'C:\Users\user\Documents\中學超前自學_微積分先修體系企劃白皮書_temp.pdf'

for note in annotations_data:
    target = note["search"]
    found = False
    for pno in range(len(doc)):
        p = doc[pno]
        rects = p.search_for(target)
        if rects:
            r = rects[0]
            hl = p.add_highlight_annot(r)
            hl.set_colors(stroke=note["color"])
            hl.set_info(title=note["title"], content=note["content"])
            hl.update()
            
            icon_point = fitz.Point(r.x1 + 16, r.y0 - 2)
            sticky = p.add_text_annot(icon_point, note["content"], icon="Comment")
            sticky.set_info(title=note["title"], content=note["content"])
            sticky.set_colors(stroke=note["color"])
            sticky.update()
            found = True
            break
    if not found:
        print(f"Warning: Annotation target not found: {target}")

doc.save(temp_pdf)
doc.close()

shutil.move(temp_pdf, output_pdf)
print(f"SUCCESS! Pristine disciplined book-grade PDF generated at: {output_pdf} ({os.path.getsize(output_pdf)} bytes)")
