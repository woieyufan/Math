# -*- coding: utf-8 -*-
import os
import sys
import subprocess
import base64
import fitz

# Paths
logo_png_path = r'C:\Users\user\Documents\woieyufan-brand-assets\woieyufan-logo-transparent-300dpi.png'
svg_watermark_path = r'C:\Users\user\Documents\woieyufan-brand-assets\woieyufan-logo_downward.svg'
output_html = r'C:\Users\user\Documents\小學全域_美術中的數學企劃白皮書.html'
output_pdf = r'C:\Users\user\Documents\小學全域_美術中的數學企劃白皮書.pdf'

with open(logo_png_path, "rb") as f:
    logo_base64 = base64.b64encode(f.read()).decode("utf-8")
logo_data_uri = f"data:image/png;base64,{logo_base64}"

with open(svg_watermark_path, "rb") as f:
    svg_base64 = base64.b64encode(f.read()).decode("utf-8")
svg_data_uri = f"data:image/svg+xml;base64,{svg_base64}"

print("Assets encoded to Base64.")

html_content = f'''<!DOCTYPE html>
<html lang="zh-Hant">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
<title>小學全域：美術中的數學工程企劃白皮書</title>

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
    --accent: #0284c7;
    --neon-cyan: #00e5ff;
    --text-dark: #1e293b;
    --text-muted: #64748b;
    --border-light: #e2e8f0;
    --font-main: -apple-system, BlinkMacSystemFont, "SF Pro Text", "PingFang TC", "Noto Sans TC", "Microsoft JhengHei", sans-serif;
  }}

  * {{ box-sizing: border-box; }}
  body {{
    font-family: var(--font-main);
    color: var(--text-dark);
    line-height: 1.65;
    background-color: #f8fafc;
    margin: 0;
    padding: 0;
    -webkit-font-smoothing: antialiased;
    background-image: url("{svg_data_uri}");
    background-repeat: no-repeat;
    background-position: center 380px;
    background-size: 580px;
    background-attachment: fixed;
  }}

  .page-container {{
    max-width: 920px;
    margin: 20px auto;
    background: rgba(255, 255, 255, 0.98);
    padding: 35px 55px;
    box-shadow: 0 8px 30px rgba(0,0,0,0.06);
    border-radius: 16px;
    position: relative;
  }}

  @media (max-width: 768px) {{
    .page-container {{
      margin: 0;
      padding: 15px 14px;
      border-radius: 0;
    }}
  }}

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
    background: linear-gradient(135deg, #f8fafc 0%, #eff6ff 50%, #f0fdfa 100%);
    border: 1.5px solid var(--primary-border);
    border-radius: 16px;
    padding: 38px 45px;
    min-height: 780px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    page-break-after: always;
    break-after: page;
    position: relative;
    box-shadow: inset 0 0 20px rgba(0, 229, 255, 0.05);
  }}
  .cover-top-bar {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 25px;
  }}
  .cover-brand-logo {{
    height: 48px;
    width: auto;
    object-fit: contain;
  }}
  .cover-tag {{
    font-size: 11px;
    font-weight: 800;
    letter-spacing: 1.5px;
    color: var(--primary);
    background: #ffffff;
    border: 1px solid var(--primary-border);
    padding: 4px 12px;
    border-radius: 6px;
    white-space: nowrap;
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
    font-size: 15px;
    font-weight: 600;
    color: #475569;
    margin: 0 0 20px 0;
    line-height: 1.55;
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
    font-size: 12px;
    font-weight: 600;
    white-space: nowrap;
  }}
  .badge-primary {{
    background: var(--primary);
    color: #ffffff;
    border-color: var(--primary);
  }}
  .badge-accent {{
    background: #0284c7;
    color: #ffffff;
    border-color: #0284c7;
  }}

  .cover-meta-grid {{
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 14px;
    border-top: 2px solid var(--primary-border);
    padding-top: 20px;
  }}
  .meta-item {{
    font-size: 12.5px;
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
    font-weight: 700;
  }}

  /* Table of Contents Wrapper */
  .toc-wrapper {{
    background: #f8fafc;
    border: 1px solid var(--border-light);
    border-radius: 12px;
    padding: 22px 30px;
    margin-bottom: 0;
    page-break-after: always;
    break-after: page;
  }}
  .section-top-brand {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-bottom: 1.5px solid var(--primary-border);
    padding-bottom: 6px;
    margin-bottom: 12px;
  }}
  .brand-subtext {{
    font-size: 10px;
    font-weight: 800;
    letter-spacing: 1.5px;
    color: var(--accent);
    white-space: nowrap;
  }}
  .header-mini-logo {{
    height: 22px;
    width: auto;
    object-fit: contain;
  }}
  .toc-main-title {{
    font-size: 17px;
    font-weight: 800;
    color: var(--primary);
    margin: 0 0 10px 0;
  }}
  .toc-grid {{
    display: grid;
    grid-template-columns: 1fr;
    gap: 4px;
  }}
  .toc-item {{
    font-size: 12px;
    line-height: 1.4;
    color: #334155;
    padding: 3px 5px;
    border-bottom: 1px dashed #e2e8f0;
  }}
  .toc-item a {{
    color: #1e293b;
    text-decoration: none;
    font-weight: 600;
    display: flex;
    justify-content: space-between;
  }}
  .toc-item a:hover {{
    color: var(--accent);
  }}

  /* Chapter Header Box */
  .chapter-header-box {{
    margin: 18px 0 12px 0;
    padding-bottom: 6px;
    border-bottom: 2.5px solid var(--primary);
  }}
  .chapter-title {{
    font-size: 19px;
    font-weight: 800;
    color: var(--primary);
    margin: 0;
  }}
  .section-title {{
    font-size: 15px;
    font-weight: 700;
    color: #1e293b;
    margin: 14px 0 8px 0;
    padding-bottom: 3px;
    border-bottom: 1px dashed var(--border-light);
  }}

  /* Stage Banner */
  .stage-banner {{
    background: linear-gradient(90deg, #0f172a 0%, #1e3a8a 100%);
    color: #ffffff;
    padding: 8px 16px;
    border-radius: 8px;
    margin: 16px 0 10px 0;
    page-break-after: avoid;
    break-after: avoid;
  }}
  .stage-banner h3 {{
    margin: 0;
    font-size: 14px;
    letter-spacing: 0.5px;
    font-weight: 700;
  }}

  /* Lesson Cards */
  .lesson-card {{
    background: #ffffff;
    border: 1px solid var(--border-light);
    border-radius: 10px;
    padding: 12px 16px;
    margin-bottom: 12px;
    page-break-inside: avoid;
    break-inside: avoid;
    box-shadow: 0 2px 6px rgba(0,0,0,0.03);
  }}
  .lesson-header {{
    display: flex;
    align-items: center;
    gap: 8px;
    margin-bottom: 6px;
    padding-bottom: 4px;
    border-bottom: 1px solid #f1f5f9;
  }}
  .lesson-pill {{
    font-size: 10px;
    font-weight: 800;
    background: var(--primary-light);
    color: var(--accent);
    padding: 2px 7px;
    border-radius: 4px;
    border: 1px solid var(--primary-border);
    white-space: nowrap;
    flex-shrink: 0;
  }}
  .lesson-title {{
    font-size: 14px;
    font-weight: 700;
    color: var(--primary);
    margin: 0;
  }}

  .para {{
    font-size: 12.5px;
    color: #334155;
    margin: 6px 0;
    text-align: justify;
    line-height: 1.6;
  }}
  .bullet-item {{
    display: flex;
    align-items: flex-start;
    gap: 6px;
    margin: 3px 0;
    font-size: 12px;
    line-height: 1.5;
  }}
  .bullet-dot {{
    color: var(--accent);
    font-weight: bold;
    font-size: 12px;
    line-height: 1.5;
  }}
  .bullet-content {{ flex: 1; color: #334155; }}
  .homework-box {{
    background: #f8fafc;
    border-left: 3.5px solid var(--accent);
    padding: 6px 12px;
    margin-top: 6px;
    border-radius: 0 6px 6px 0;
    font-size: 11.8px;
    line-height: 1.55;
    color: #1e293b;
  }}

  /* Tables */
  .table-container {{
    overflow-x: auto;
    margin: 12px 0;
    border-radius: 8px;
    border: 1px solid var(--border-light);
  }}
  .doc-table {{
    width: 100%;
    border-collapse: collapse;
    font-size: 11.5px;
    text-align: left;
  }}
  .doc-table th {{
    background: #f1f5f9;
    color: #0f172a;
    font-weight: 700;
    padding: 8px 10px;
    border-bottom: 2px solid var(--border-light);
  }}
  .doc-table td {{
    padding: 7px 10px;
    border-bottom: 1px solid #f1f5f9;
    color: #334155;
  }}

  /* Flowchart Box */
  .flowchart-container {{
    background: #ffffff;
    border: 1.5px solid var(--primary-border);
    border-radius: 10px;
    padding: 10px 14px;
    margin: 10px 0;
    page-break-inside: avoid;
    break-inside: avoid;
  }}
  .flow-grid {{
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 10px;
  }}
  .flow-col {{
    background: #f8fafc;
    border: 1px solid var(--border-light);
    border-radius: 6px;
    padding: 8px 10px;
  }}
  .flow-col-title {{
    font-size: 12px;
    font-weight: 700;
    color: var(--primary);
    margin-bottom: 6px;
    border-bottom: 1px solid var(--primary-border);
    padding-bottom: 3px;
    text-align: center;
  }}
  .flow-node {{
    background: #ffffff;
    border: 1px solid #cbd5e1;
    border-radius: 4px;
    padding: 4px 6px;
    font-size: 10.5px;
    margin-bottom: 4px;
    text-align: center;
    color: #334155;
    font-weight: 600;
  }}
  .flow-arrow {{
    text-align: center;
    color: var(--accent);
    font-size: 11px;
    margin: 1px 0;
  }}
  .highlight-node {{
    background: #eff6ff;
    border-color: var(--accent);
    color: var(--primary);
  }}

  .rubric-card {{
    background: #ffffff;
    border: 1px solid #e2e8f0;
    border-radius: 8px;
    padding: 8px 12px;
    margin-bottom: 8px;
  }}
  .rubric-title {{
    font-weight: 700;
    color: var(--primary);
    font-size: 12.5px;
    margin-bottom: 4px;
  }}
</style>
</head>
<body>

<div class="page-container">

  <!-- ==================== COVER PAGE (PAGE 1) ==================== -->
  <div class="cover-wrapper">
    <div class="cover-top-bar">
      <img src="{logo_data_uri}" class="cover-brand-logo" alt="woieyufan EDUCATION" />
      <div class="cover-tag">ENGINEERING SPECIFICATION WHITE PAPER</div>
    </div>

    <div>
      <h1 class="doc-title">小學全域：美術中的數學<br>工程企劃白皮書</h1>
      <div class="doc-subtitle">從平面坐標、漢字間架、三大棋盤、魔術方塊、鏡頭光學到空間透視</div>
      
      <div class="meta-badge-row">
        <span class="badge badge-primary">國小全年段（中年級懂除法起步）</span>
        <span class="badge badge-accent">48 小時 / 24 堂課全域工程架構</span>
        <span class="badge">學校作業直交方案</span>
        <span class="badge">iPad 出版級規格</span>
        <span class="badge">woieyufan EDUCATION</span>
      </div>
    </div>

    <div class="cover-meta-grid">
      <div class="meta-item">
        <span class="meta-label">專案代號</span>
        <span class="meta-val">ELEM-ART-MATH-MASTER (小學全域旗艦版)</span>
      </div>
      <div class="meta-item">
        <span class="meta-label">研發母法</span>
        <span class="meta-val">工程級白皮書標準模組規範（單堂 4 頁標準化模組）</span>
      </div>
      <div class="meta-item">
        <span class="meta-label">視覺資產</span>
        <span class="meta-val">綁定 woieyufan 品牌視覺資產庫（母標 300 DPI 向量規範）</span>
      </div>
      <div class="meta-item">
        <span class="meta-label">交付規格</span>
        <span class="meta-val">跨平台通用 PDF · iPad 4:3 滿版自適應 HTML</span>
      </div>
    </div>
  </div>

  <!-- ==================== TABLE OF CONTENTS (PAGE 2) ==================== -->
  <div class="toc-wrapper">
    <div class="section-top-brand">
      <span class="brand-subtext">WOIEYUFAN EDUCATION · CURRICULUM BLUEPRINT</span>
      <img src="{logo_data_uri}" class="header-mini-logo" alt="Logo" />
    </div>
    <div class="toc-main-title">課程企劃白皮書 · 總體目錄</div>

    <div class="toc-grid">
      <div class="toc-item"><a href="#ch1"><span>第一章：體系定位與教育哲學宣言（視覺進化四階梯與痛點診斷）</span><span>P. 3</span></a></div>
      <div class="toc-item"><a href="#ch2"><span>第二章：雙軌驅動全域知識地圖（坐標、曲面解構與透視空間合流）</span><span>P. 4</span></a></div>
      <div class="toc-item"><a href="#ch3"><span>第三章：核心跨界幾何與數學對接公理（奇偶著色、排疊等距、角虧損曲率、角大小公式）</span><span>P. 5</span></a></div>
      <div class="toc-item"><a href="#ch4-1"><span>第四章 · 階段一：平面坐標、多邊形與棋盤密鋪（第 1–4 堂）</span><span>P. 6</span></a></div>
      <div class="toc-item"><a href="#ch4-2"><span>第四章 · 階段二：漢字間架結構與寫字坐標學（第 5–8 堂）</span><span>P. 7</span></a></div>
      <div class="toc-item"><a href="#ch4-3"><span>第四章 · 階段三：空間升維——正多面體與曲面解構（動物與衣物合流）（第 9–12 堂）</span><span>P. 8</span></a></div>
      <div class="toc-item"><a href="#ch4-4"><span>第四章 · 階段四：相機光學、錯位裁切與單點透視（第 13–16 堂）</span><span>P. 9</span></a></div>
      <div class="toc-item"><a href="#ch4-5"><span>第四章 · 階段五：旋轉的立體方塊——兩點透視與萬物方塊法（第 17–20 堂）</span><span>P. 10</span></a></div>
      <div class="toc-item"><a href="#ch4-6"><span>第四章 · 階段六：光影空間、綜合大創作與全域策展（第 21–24 堂）</span><span>P. 11</span></a></div>
      <div class="toc-item"><a href="#ch5"><span>第五章：學校作業直交方案與階段成品清冊（7 大學校 A+ 王牌作業）</span><span>P. 12</span></a></div>
      <div class="toc-item"><a href="#ch6"><span>第六章：iPad 出版級交付規範與 woieyufan 視覺資產綁定</span><span>P. 13</span></a></div>
      <div class="toc-item"><a href="#ch7"><span>第七章：評量規準與成果檢定試卷架構（三層次能力指標與 6 大題型）</span><span>P. 14</span></a></div>
    </div>
  </div>

  <!-- ==================== CHAPTER 1 (PAGE 3) ==================== -->
  <div class="page-break-before" id="ch1">
    <div class="section-top-brand">
      <span class="brand-subtext">ACADEMIC PHILOSOPHY · SPECIFICATION</span>
      <img src="{logo_data_uri}" class="header-mini-logo" alt="Logo" />
    </div>

    <div class="chapter-header-box">
      <div class="chapter-title">第一章：體系定位與教育哲學宣言</div>
    </div>

    <div class="section-title">1.1 當前兒童美術與數學教育的雙向斷層診斷</div>
    <div class="para">
      當前小學美育普遍陷於「感性空洞與隨意塗鴉」的陷阱，而數學教育則被困在「乾癟脫離感官的計算題海」中。小學中年級（9~10 歲）的孩子正面臨空間認知躍升的關鍵窗口，卻因缺乏幾何坐標與透視工具，在繪畫時陷入巨大的無力感：想畫立體房間卻畫得扁平塌陷，想畫人物五官卻東倒西歪、左右失調，想畫建築街景線條卻到處亂撞。
    </div>

    <div class="section-title">1.2 視覺進化的四大階梯（兒童繪畫認知的數學躍升）</div>
    <div class="para">
      本課程建立了一條清晰嚴密的認知演進鏈條，帶領孩子從手感直覺走向科學視覺化：
    </div>
    <div class="bullet-item"><span class="bullet-dot">•</span><div class="bullet-content"><strong>第一階：概念符號期（幼兒直覺）</strong>：大腦畫的是「概念」而非「光學現實」（用圓圈當頭、線條當四肢的火柴人，正面眼睛配側面鼻子，毫無坐標約束）。</div></div>
    <div class="bullet-item"><span class="bullet-dot">•</span><div class="bullet-content"><strong>第二階：特徵寫意期（少兒盲點）</strong>：注意到了局部的幾何形狀（知道畫長條、畫橢圓、抓特徵），但缺乏全局尺度與空間坐標約束，形體永遠鬆散歪斜。</div></div>
    <div class="bullet-item"><span class="bullet-dot">•</span><div class="bullet-content"><strong>第三階：平面坐標分析期（★ 課程前半核心）</strong>：<strong>坐標解決平面！</strong> 白紙不是虛無的，它有原點 $(0, 0)$ 與直角坐標系。漢字書法與三大棋類（西洋棋、圍棋、象棋），就是人類歷史上最高智慧的二維坐標資產！</div></div>
    <div class="bullet-item"><span class="bullet-dot">•</span><div class="bullet-content"><strong>第四階：透視空間投影期（★ 課程後半核心）</strong>：<strong>真正的科學視覺化是透視的！</strong> 把二維棋盤推倒在地上，自然誕生視平線與消失點；把 2D 九宮格折疊起來，就是手裡的魔術方塊！</div></div>

    <div class="section-title">1.3 雙重客群價值定位</div>
    <div class="bullet-item"><span class="bullet-dot">•</span><div class="bullet-content"><strong>對普通班愛畫畫的學生</strong>：本課程是「畫畫的超能力外掛」，破除手繪歪斜與平面扁塌，提供即時的視覺成就感，讓孩子成為班上最懂立體透視的繪畫高手。</div></div>
    <div class="bullet-item"><span class="bullet-dot">•</span><div class="bullet-content"><strong>對專業美術班/畫室資優生</strong>：本課程是「結構素描與透視的底層作業系統」，消除手感玄學，直接降維打擊升學考科，培養無中生有的默寫場景構圖能力。</div></div>
  </div>

  <!-- ==================== CHAPTER 2 & 3 (PAGE 4 & 5) ==================== -->
  <div class="page-break-before" id="ch2">
    <div class="section-top-brand">
      <span class="brand-subtext">KNOWLEDGE TOPOGRAPHY · DUAL ORIGINS</span>
      <img src="{logo_data_uri}" class="header-mini-logo" alt="Logo" />
    </div>

    <div class="chapter-header-box">
      <div class="chapter-title">第二章：雙軌驅動全域知識地圖</div>
    </div>

    <div class="flowchart-container">
      <div class="flow-grid">
        <div class="flow-col">
          <div class="flow-col-title">軌道 I：平面坐標、書寫與棋盤幾何</div>
          <div class="flow-node">1. 西洋棋盤 a1-h8 與直角坐標系</div>
          <div class="flow-arrow">↓</div>
          <div class="flow-node">2. 圍棋交點哲學 vs 象棋向量步法</div>
          <div class="flow-arrow">↓</div>
          <div class="flow-node">3. 六角網格 (Hex Grid) 與大自然蜂巢</div>
          <div class="flow-arrow">↓</div>
          <div class="flow-node">4. 正多邊形平面密鋪公理 ($\sum\theta=360^\circ$)</div>
          <div class="flow-arrow">↓</div>
          <div class="flow-node highlight-node">5. 漢字田字/米字格對稱與九宮格中宮收緊</div>
        </div>

        <div class="flow-col">
          <div class="flow-col-title">軌道 II：曲面解構、透視光學與空間大場景</div>
          <div class="flow-node">1. 正多面體宇宙：柏拉圖五大立體展開</div>
          <div class="flow-arrow">↓</div>
          <div class="flow-node">2. 角虧損與曲率：多面動物與衣服打版</div>
          <div class="flow-arrow">↓</div>
          <div class="flow-node">3. 相機三分構圖、裁切魔術與比薩斜塔錯位</div>
          <div class="flow-arrow">↓</div>
          <div class="flow-node">4. 棋盤推倒變地面：單點透視與對角線測深</div>
          <div class="flow-arrow">↓</div>
          <div class="flow-node highlight-node">5. 兩點透視畫魔方、萬物方塊法與光影大交響</div>
        </div>
      </div>
    </div>

    <div class="section-title">2.1 雙軌合流樞紐：魔術方塊與表面展開</div>
    <div class="para">
      魔術方塊正是 2D 九宮格走向 3D 空間坐標的物理關節。6 個九宮格平鋪在紙上是展開圖，折疊起來是實體立方體，而在兩點透視中利用「梯形對角線三等分神技」畫出立體魔方，則是訓練孩子空間三維思維的終極里程碑。
    </div>
  </div>

  <div class="page-break-before" id="ch3">
    <div class="section-top-brand">
      <span class="brand-subtext">CORE AXIOMS · CROSS-DISCIPLINARY</span>
      <img src="{logo_data_uri}" class="header-mini-logo" alt="Logo" />
    </div>

    <div class="chapter-header-box">
      <div class="chapter-title">第三章：核心跨界幾何與數學對接公理</div>
    </div>

    <div class="section-title">3.1 畫布直角坐標系與奇偶性著色定理</div>
    <div class="para">
      西洋棋盤的黑白交替本質：格子坐標 $(x, y)$，當 $(x+y) \pmod 2 = 0$ 塗白，$(x+y) \pmod 2 = 1$ 塗黑。這是現代像素藝術（Pixel Art）與歐普藝術的底層代數基石。
    </div>

    <div class="section-title">3.2 漢字間架結構的三大幾何公理</div>
    <div class="bullet-item"><span class="bullet-dot">•</span><div class="bullet-content"><strong>中宮收緊公理</strong>：核心部件必須錨定在九宮格第 5 宮（中心宮），幾何重心鉛垂線貫穿上下。</div></div>
    <div class="bullet-item"><span class="bullet-dot">•</span><div class="bullet-content"><strong>歐陽詢排疊公理（等距除法）</strong>：多橫多豎筆畫之間的平行留白間隙，滿足線段除法相等性：$\text{間距} = \frac{\text{總高度}}{\text{筆畫數} + 1}$。</div></div>
    <div class="bullet-item"><span class="bullet-dot">•</span><div class="bullet-content"><strong>凸包避讓公理</strong>：左右結構依據 $1:2$ 或 $1:1$ 劃分水平坐標，左側收斂讓位，右側穿插伸展。</div></div>

    <div class="section-title">3.3 角虧損與曲率生成公理（動物與衣物的統一幾何理論）</div>
    <div class="para">
      平坦表面（曲率為 0）如何包裹 3D 非零曲面？在頂點處剪掉一個三角形（角虧損 $\Delta\theta = 360^\circ - \sum\alpha$），縫合後平面必隆起形成 3D 曲面！在服裝上稱為「省道（Darts）」，在多面體上稱為「頂點角虧」。動物的肌肉切面素描與衣服受力衣褶素描，本質上都是表面法向量 $\vec{N}$ 與光線向量 $\vec{L}$ 的點積光影運算。
    </div>

    <div class="section-title">3.4 攝影光學與比薩斜塔錯位除法公式</div>
    <div class="para">
      角大小公式 $\theta = \frac{H}{D}$。當相機單鏡頭將三維深度 $Z$ 抹殺為零時，只要滿足相似三角形除法等式：
      $$\frac{H_{\text{塔}}}{D_{\text{塔}}} = \frac{h_{\text{手}}}{d_{\text{手}}} \implies \theta_{\text{塔}} = \theta_{\text{手}}$$
      手掌像素大小與遠處斜塔完全相等，再透過<strong>裁切相片消除中間路人參照物</strong>，大腦便會產生「手推斜塔」的超現實錯位！
    </div>
  </div>

  <!-- ==================== CHAPTER 4: 24 LESSON MATRIX (PAGES 6-11) ==================== -->
  
  <!-- STAGE 1 (PAGE 6) -->
  <div class="page-break-before" id="ch4-1">
    <div class="section-top-brand">
      <span class="brand-subtext">24-LESSON MATRIX · STAGE 1</span>
      <img src="{logo_data_uri}" class="header-mini-logo" alt="Logo" />
    </div>

    <div class="stage-banner">
      <h3>【第一階段：平面坐標、多邊形與棋盤密鋪（第 1–4 堂）】</h3>
    </div>

    <div class="lesson-card">
      <div class="lesson-header">
        <span class="lesson-pill">第 1 堂</span>
        <div class="lesson-title">白紙上的坐標門牌：西洋棋記譜法 (a1–h8) 與直角坐標系</div>
      </div>
      <div class="para"><strong>P.1 視覺動機</strong>：白紙沒有方向與尺度，隨手畫畫沒有錨點；棋盤是人類最古老的二維網格地圖。</div>
      <div class="para"><strong>P.2 幾何推導</strong>：直角坐標系；橫軸 $a\sim h$（$X$ 軸 1~8）、縱軸 $1\sim 8$（$Y$ 軸）；原點 $(1, 1)$；格子地址 $(x, y)$；黑白奇偶著色 $(x+y)\pmod 2$。</div>
      <div class="para"><strong>P.3 藝術名作</strong>：現代地圖坐標系、復古像素藝術（Pixel Art）與歐普藝術棋盤波浪。</div>
      <div class="homework-box"><strong>P.4 階梯作業【棋盤坐標尋寶圖：畫出我的像素徽章】</strong>：在 $8\times 8$ 方格紙上，依坐標指令填色，精確浮現工整的復古像素愛心圖騰與黑白交替幾何。</div>
    </div>

    <div class="lesson-card">
      <div class="lesson-header">
        <span class="lesson-pill">第 2 堂</span>
        <div class="lesson-title">點與面的哲學：圍棋交叉點 vs 象棋向量步法</div>
      </div>
      <div class="para"><strong>P.1 視覺動機</strong>：輪廓線是「點」拉出來的，色彩是填在「面」裡的；斜線的角度由什麼決定？</div>
      <div class="para"><strong>P.2 幾何推導</strong>：點（0 維）、線（1 維）、面（2 維）；圍棋落子在交點；象棋向量位移 $(\Delta x, \Delta y)$：「馬走日」橫 1 縱 2、「象走田」橫 2 縱 2；楚河漢界是水平鏡射對稱軸。</div>
      <div class="para"><strong>P.3 藝術名作</strong>：蒙德里安《紅黃藍構圖》的黑線交點與色塊平衡。</div>
      <div class="homework-box"><strong>P.4 階梯作業【象棋幾何星芒與蒙德里安格子畫】</strong>：從坐標 $(5, 5)$ 的馬出發，畫出 8 條向量斜射線連成八邊形星芒；並用三原色填充幾何色塊面。</div>
    </div>

    <div class="lesson-card">
      <div class="lesson-header">
        <span class="lesson-pill">第 3 堂</span>
        <div class="lesson-title">打破四邊形：六角棋盤（Hex Grid）與大自然蜂巢</div>
      </div>
      <div class="para"><strong>P.1 視覺動機</strong>：為什麼除了正方形棋盤，世界上還有六角棋盤？蜜蜂為什麼不用正方形做蜂巢？</div>
      <div class="para"><strong>P.2 幾何推導</strong>：六角網格（Hex Grid）；三軸向坐標系 $(u, v, w)$；周長最小而面積最大的等周定理；每個格子有 6 個等距鄰居。</div>
      <div class="para"><strong>P.3 藝術名作</strong>：大自然蜂巢幾何結構與現代戰略遊戲（《文明帝國》、《卡坦島》）的六角地圖美學。</div>
      <div class="homework-box"><strong>P.4 階梯作業【繪製六角棋盤與蜂巢紋樣】</strong>：用圓規半徑六等分步進法，精確畫出正六邊形，並向外擴展拼貼出一片緊密咬合的六角棋盤並著色。</div>
    </div>

    <div class="lesson-card">
      <div class="lesson-header">
        <span class="lesson-pill">第 4 堂</span>
        <div class="lesson-title">誰能鋪滿地面？正多邊形繪製與平面密鋪公理</div>
      </div>
      <div class="para"><strong>P.1 視覺動機</strong>：鋪地磚時，為什麼可以用正三角形、正方形、正六邊形，卻從來沒有人用正五邊形？</div>
      <div class="para"><strong>P.2 幾何推導</strong>：正多邊形內角公式；頂點周圍角和整除公理（必須等於 $360^\circ$）：$60^\circ\times 6=360^\circ$、$90^\circ\times 4=360^\circ$、$120^\circ\times 3=360^\circ$；五邊形 $108^\circ$ 不能整除必留縫隙！</div>
      <div class="para"><strong>P.3 藝術名作</strong>：西班牙阿罕布拉宮阿拉伯鑲嵌磁磚與埃舍爾密鋪幾何。</div>
      <div class="homework-box"><strong>P.4 階梯作業【幾何地磚拼圖工程報告】</strong>：尺規繪製正三角形、正方形、正六邊形剪紙拼貼，驗證三種正多邊形能完美密鋪，五邊形必定留縫隙。</div>
    </div>
  </div>

  <!-- STAGE 2 (PAGE 7) -->
  <div class="page-break-before" id="ch4-2">
    <div class="section-top-brand">
      <span class="brand-subtext">24-LESSON MATRIX · STAGE 2</span>
      <img src="{logo_data_uri}" class="header-mini-logo" alt="Logo" />
    </div>

    <div class="stage-banner">
      <h3>【第二階段：漢字間架結構與寫字坐標學（第 5–8 堂）】</h3>
    </div>

    <div class="lesson-card">
      <div class="lesson-header">
        <span class="lesson-pill">第 5 堂</span>
        <div class="lesson-title">田字格的四個象限：漢字的初級居中與對稱中心</div>
      </div>
      <div class="para"><strong>P.1 視覺動機</strong>：寫「十、口、日」時東倒西歪、散架偏離中心。</div>
      <div class="para"><strong>P.2 幾何推導</strong>：中心空間約束；田字格是漢字以原點 $(0, 0)$ 為中心的四象限平衡系統；橫豎主筆精準壓在坐標軸上。</div>
      <div class="para"><strong>P.3 藝術名作</strong>：古代印章篆刻的四象限對稱布局美學。</div>
      <div class="homework-box"><strong>P.4 階梯作業【坐標守衛戰：穩如泰山的「十」與「口」】</strong>：在田字格中寫出端正的「十」與「口」，四個象限留白面積完全相等。</div>
    </div>

    <div class="lesson-card">
      <div class="lesson-header">
        <span class="lesson-pill">第 6 堂</span>
        <div class="lesson-title">書法九宮格與中宮收緊：三分除法與字形重心</div>
      </div>
      <div class="para"><strong>P.1 視覺動機</strong>：寫「中、東、果」時肚子太大像大西瓜，整個人散架癱掉。</div>
      <div class="para"><strong>P.2 幾何推導</strong>：長寬各三等分（除以 3）；九宮格第 5 宮（中宮）；重心鉛垂線；「中宮緊密，四肢開張」公理。</div>
      <div class="para"><strong>P.3 藝術名作</strong>：歐陽詢《九成宮醴泉銘》的重心結構解析。</div>
      <div class="homework-box"><strong>P.4 階梯作業【中宮鎖定法：寫出挺拔的「中」與「果」】</strong>：將 $6\text{cm}\times 6\text{cm}$ 外框三等分畫九宮格，扁口鎖死在中心宮，長豎筆挺貫穿上下。</div>
    </div>

    <div class="lesson-card">
      <div class="lesson-header">
        <span class="lesson-pill">第 7 堂</span>
        <div class="lesson-title">筆畫的等距除法：歐陽詢排疊公理與棋盤平行線</div>
      </div>
      <div class="para"><strong>P.1 視覺動機</strong>：寫「三、目、春、重」時橫線忽密忽疏，像被踩爛的百葉窗。</div>
      <div class="para"><strong>P.2 幾何推導</strong>：線段除法等分；平行線族；筆畫留白間隙相等公理（歐陽詢排疊公理）。</div>
      <div class="para"><strong>P.3 藝術名作</strong>：現代字體設計（Typography，黑體、明體）的等距幾何規範。</div>
      <div class="homework-box"><strong>P.4 階梯作業【除法尺寫字：完美等距的「目」與「春」】</strong>：外框高 6cm，內有 2 橫，切出 3 個均等空白（$6 \div 3 = 2\text{cm}$）。用直尺量測間距，誤差小於 1.5 毫米即滿分。</div>
    </div>

    <div class="lesson-card">
      <div class="lesson-header">
        <span class="lesson-pill">第 8 堂</span>
        <div class="lesson-title">上下 1:2 與左右穿插避讓：坐標空間的禮讓美學</div>
      </div>
      <div class="para"><strong>P.1 視覺動機</strong>：寫「花、青」大頭娃娃，「林、明」左右打架或分家。</div>
      <div class="para"><strong>P.2 幾何推導</strong>：垂直高度比例切分（$1:1, 1:2, 2:1$）；水平寬度避讓穿插（凸包互補讓位）。</div>
      <div class="para"><strong>P.3 藝術名作</strong>：《歐陽詢間架結構九十二法》的避讓幾何。</div>
      <div class="homework-box"><strong>P.4 階梯作業【部件讓位拼圖：寫出優雅的「花」與「林」】</strong>：「花」草字頭佔上 $\frac{1}{3}$，化佔下 $\frac{2}{3}$；「林」左木捺變點，讓出空間給右木長撇穿插。</div>
    </div>
  </div>

  <!-- STAGE 3 (PAGE 8) -->
  <div class="page-break-before" id="ch4-3">
    <div class="section-top-brand">
      <span class="brand-subtext">24-LESSON MATRIX · STAGE 3</span>
      <img src="{logo_data_uri}" class="header-mini-logo" alt="Logo" />
    </div>

    <div class="stage-banner">
      <h3>【第三階段：空間升維——正多面體與曲面解構（動物與衣物合流）（第 9–12 堂）】</h3>
    </div>

    <div class="lesson-card">
      <div class="lesson-header">
        <span class="lesson-pill">第 9 堂</span>
        <div class="lesson-title">正多面體宇宙：柏拉圖五大立體的展開與摺疊</div>
      </div>
      <div class="para"><strong>P.1 空間動機</strong>：古希臘柏拉圖認為宇宙由 5 種最完美立體構成；為什麼世界上「只有 5 種」正多面體？</div>
      <div class="para"><strong>P.2 幾何推導</strong>：頂點角虧損公理（$\sum\alpha<360^\circ$ 才能折疊出立體）；正四面體、正六面體、正八面體、正十二面體、正二十面體；歐拉示性數 $V - E + F = 2$。</div>
      <div class="para"><strong>P.3 藝術名作</strong>：達文西為《神聖比例》繪製的正多面體幾何木刻插圖。</div>
      <div class="homework-box"><strong>P.4 階梯作業【親手摺出幾何水晶：正八面體與立方體展開圖】</strong>：在卡紙上畫出正八面體與立方體展開圖，剪下、壓折痕、黏合出兩座實體幾何水晶。</div>
    </div>

    <div class="lesson-card">
      <div class="lesson-header">
        <span class="lesson-pill">第 10 堂</span>
        <div class="lesson-title">角虧損與曲率生成：動物切面與衣物打版的本質同一性</div>
      </div>
      <div class="para"><strong>P.1 造型哲學</strong>：動物的皮膚與人類的衣服，在數學上是完全同一件事！平坦的布料（曲率 0）如何包裹 3D 人體？平坦的卡紙如何包裹 3D 動物？</div>
      <div class="para"><strong>P.2 幾何推導</strong>：角虧損產生曲率；剪掉夾角 $\Delta\theta$ 縫合隆起（服裝上的省道 Darts，多面體上的角虧）；接縫與稜線拓撲。</div>
      <div class="para"><strong>P.3 藝術對接</strong>：現代高訂時裝立體剪裁（Patternmaking）與 Low-Poly 幾何多面體紙雕。</div>
      <div class="homework-box"><strong>P.4 階梯作業【實體雙重拼裝：多面半寫實靈狐頭部 ＋ 立體連帽小斗篷】</strong>：剪紙拼裝出 3D 幾何靈狐頭雕，並在平面布料上剪開肩膀省道，做出一件立體服貼的連帽斗篷！</div>
    </div>

    <div class="lesson-card">
      <div class="lesson-header">
        <span class="lesson-pill">第 11 堂</span>
        <div class="lesson-title">多面動物結構素描：用幾何切面畫出野生獵豹</div>
      </div>
      <div class="para"><strong>P.1 視覺動機</strong>：畫動物最怕毛茸茸一團、結構鬆散；大師一眼能看透皮毛下的幾何切面骨架。</div>
      <div class="para"><strong>P.2 幾何推導</strong>：動物頭骨五大主切面；法向量點積與光影三大面：垂直最亮、傾斜為灰、背光為暗。</div>
      <div class="para"><strong>P.3 藝術名作</strong>：古典解剖學大師 Bridgman 的塊面人體與野生動物結構素描。</div>
      <div class="homework-box"><strong>P.4 階梯作業【半寫實幾何獵豹頭部結構素描】</strong>：勾勒獵豹頭部 12 個主要切面，設定光線角度，依照三大明暗面排線，畫出一隻大理石雕刻般的幾何獵豹！</div>
    </div>

    <div class="lesson-card">
      <div class="lesson-header">
        <span class="lesson-pill">第 12 堂</span>
        <div class="lesson-title">布料衣褶（Drapery）的力學幾何：告別隨手畫泡麵線</div>
      </div>
      <div class="para"><strong>P.1 視覺動機</strong>：學生畫衣服總隨手畫幾根無意義波浪線；大師筆下的布料有重力、有重量、有空間垂墜感！</div>
      <div class="para"><strong>P.2 幾何推導</strong>：衣褶由重力與支撐受力點決定；三大幾何模型：管狀褶（圓柱面）、吊橋褶（懸鏈線拋物線）、Z 字擠壓褶（相扣三角形）。</div>
      <div class="para"><strong>P.3 藝術名作</strong>：達文西《天使報喜》中聖母膝蓋上的極致布料素描研究（Drapery Study）。</div>
      <div class="homework-box"><strong>P.4 階梯作業【為幾何關節人偶穿上垂墜風衣】</strong>：標定肩膀受力點，向後拉出飄揚風衣（畫出管狀圓柱厚度），在手肘處畫出 Z 字褶，完成一幅力學真實的服裝素描。</div>
    </div>
  </div>

  <!-- STAGE 4 (PAGE 9) -->
  <div class="page-break-before" id="ch4-4">
    <div class="section-top-brand">
      <span class="brand-subtext">24-LESSON MATRIX · STAGE 4</span>
      <img src="{logo_data_uri}" class="header-mini-logo" alt="Logo" />
    </div>

    <div class="stage-banner">
      <h3>【第四階段：相機光學、錯位裁切與單點透視（第 13–16 堂）】</h3>
    </div>

    <div class="lesson-card">
      <div class="lesson-header">
        <span class="lesson-pill">第 13 堂</span>
        <div class="lesson-title">相機裡的九宮格：拍照三分構圖與照片裁切的幾何魔術</div>
      </div>
      <div class="para"><strong>P.1 視覺動機</strong>：拍照總是把主體放在正中央像證件照；裁切照片為什麼會帶來震撼的幾何新發現？</div>
      <div class="para"><strong>P.2 幾何推導</strong>：相機九宮格輔助線；三分法則（Rule of Thirds）4 個黃金焦點；裁切即「坐標原點平移」與「消除參照物提純幾何引導線」；長寬比（$1:1, 4:3, 16:9$ 電影感）。</div>
      <div class="para"><strong>P.3 藝術名作</strong>：頂級街頭攝影大師布列松（Cartier-Bresson）「決定性瞬間」幾何構圖。</div>
      <div class="homework-box"><strong>P.4 階梯作業【我是國家地理雜誌裁切師】</strong>：用手機拍一張凌亂房間，裁掉雜物將主體移到九宮格黃金焦點，壓窄成 $16:9$ 電影比例，對比前後震撼變化。</div>
    </div>

    <div class="lesson-card">
      <div class="lesson-header">
        <span class="lesson-pill">第 14 堂</span>
        <div class="lesson-title">比薩斜塔的除法魔術：好萊塢「錯位攝影（Forced Perspective）」實戰</div>
      </div>
      <div class="para"><strong>P.1 視覺動機</strong>：比薩斜塔為什麼能被手推住？電影《魔戒》哈比人為什麼看起來那麼矮小？</div>
      <div class="para"><strong>P.2 幾何推導</strong>：角大小公式 $\theta = H/D$；相似三角形除法等式 $\frac{H}{D}=\frac{h}{d}$；相機單鏡頭 2D 投影抹殺深度軸 $Z$；小光圈大景深；裁切消除路人參照物。</div>
      <div class="para"><strong>P.3 藝術名作</strong>：《魔戒》哈比人與甘道夫同桌進餐的強迫透視實景拍攝解密。</div>
      <div class="homework-box"><strong>P.4 階梯作業【客廳裡的巨獸與小小人】</strong>：恐龍放 50cm，家人站 250cm（縮小 5 倍！），對位手腳踩頭頂，裁掉多餘雜物，完成好萊塢級錯位大片。</div>
    </div>

    <div class="lesson-card">
      <div class="lesson-header">
        <span class="lesson-pill">第 15 堂</span>
        <div class="lesson-title">西洋棋盤推倒了！視平線、消失點與單點透視空間盒</div>
      </div>
      <div class="para"><strong>P.1 視覺動機</strong>：透視不是玄學，透視就是把前兩階段學的棋盤坐標紙『推倒在腳下』！</div>
      <div class="para"><strong>P.2 幾何推導</strong>：中心射影；視平線（Horizon Line = 眼睛高度）；平行的縱向線向無窮遠點（消失點 VP）收斂；單點透視三大公理（橫平、豎直、深聚滅點）。</div>
      <div class="para"><strong>P.3 藝術名作</strong>：維梅爾《音樂課》中的黑白棋盤地面與深邃室內空間。</div>
      <div class="homework-box"><strong>P.4 階梯作業【棋盤地面的臥室設計圖】</strong>：畫正後方那堵牆，引出 4 條透視射線貫穿到紙邊。地面畫收斂棋盤線，左側順著射線畫床，右側畫書桌，線條嚴密對齊滅點。</div>
    </div>

    <div class="lesson-card">
      <div class="lesson-header">
        <span class="lesson-pill">第 16 堂</span>
        <div class="lesson-title">棋盤地磚的非線性收縮：對角線空間測深神技</div>
      </div>
      <div class="para"><strong>P.1 視覺動機</strong>：西洋棋盤地磚越遠越窄，到底該窄多少？不用猜，用對角線連出來！</div>
      <div class="para"><strong>P.2 幾何推導</strong>：矩形對角線平分空間；透視下等距棋盤的幾何作圖法；視平線高度切割法則（遠近人物眼睛恆在視平線上）。</div>
      <div class="para"><strong>P.3 藝術名作</strong>：達文西《最後的晚餐》天花板方格凹槽的對角線測深幾何。</div>
      <div class="homework-box"><strong>P.4 階梯作業【精確數學作圖：無失真透視黑白棋盤與行人】</strong>：畫出第 1 塊地磚深度，用對角線交點精確決定第 2、3、4 排地磚深度線，塗黑白棋盤色，並立上遠近眼睛皆穿過視平線的行人。</div>
    </div>
  </div>

  <!-- STAGE 5 (PAGE 10) -->
  <div class="page-break-before" id="ch4-5">
    <div class="section-top-brand">
      <span class="brand-subtext">24-LESSON MATRIX · STAGE 5</span>
      <img src="{logo_data_uri}" class="header-mini-logo" alt="Logo" />
    </div>

    <div class="stage-banner">
      <h3>【第五階段：旋轉的立體方塊——兩點透視與萬物方塊法（第 17–20 堂）】</h3>
    </div>

    <div class="lesson-card">
      <div class="lesson-header">
        <span class="lesson-pill">第 17 堂</span>
        <div class="lesson-title">旋轉的坐標方塊：兩點透視的雙滅點法則</div>
      </div>
      <div class="para"><strong>P.1 視覺動機</strong>：物體水平旋轉時，正面不再平行於畫布，出現左右兩個消失點（$V_L, V_R$）。</div>
      <div class="para"><strong>P.2 幾何推導</strong>：垂直稜線保持垂直；頂底邊緣分別連向左右滅點；頂面交叉封閉。</div>
      <div class="para"><strong>P.3 藝術名作</strong>：現代概念藝術（Concept Art）中的幾何城市街景與積木方塊。</div>
      <div class="homework-box"><strong>P.4 階梯作業【漂浮的兩點透視大方塊】</strong>：畫視平線與左右滅點 $V_L, V_R$。立垂直稜線，端點連向左右滅點，切出寬度，交叉封閉頂面，完成立體大方塊。</div>
    </div>

    <div class="lesson-card">
      <div class="lesson-header">
        <span class="lesson-pill">第 18 堂</span>
        <div class="lesson-title">【神級作圖】在兩點透視中畫出魔術方塊！</div>
      </div>
      <div class="para"><strong>P.1 視覺動機</strong>：99% 的孩子畫魔方裡面的 9 個格子全是瞎畫的；如何在透視斜面上切出精確的 $3\times 3$ 九宮格？</div>
      <div class="para"><strong>P.2 幾何推導</strong>：【核心技術】透視梯形面的<strong>對角線三等分除法作圖法</strong>；在空間中不靠尺量，僅憑幾何交點切出近寬遠窄的 3 等分！</div>
      <div class="para"><strong>P.3 藝術名作</strong>：超現實主義大師將魔術方塊作為空間幾何圖騰的當代畫作。</div>
      <div class="homework-box"><strong>P.4 階梯作業【神級作圖：兩點透視立體魔術方塊】</strong>：畫兩點透視立方體，在左面、右面、頂面上運用對角線等分法各切出 9 個透視小方塊，塗上經典紅白藍魔方貼紙與黑接縫！</div>
    </div>

    <div class="lesson-card">
      <div class="lesson-header">
        <span class="lesson-pill">第 19 堂</span>
        <div class="lesson-title">萬物皆可方塊化（The Box Method）：畫家具、寶箱與汽車</div>
      </div>
      <div class="para"><strong>P.1 視覺動機</strong>：複雜物體（椅子、汽車、寶箱）太難畫？大師秘訣：萬物不過是切削過的魔術方塊！</div>
      <div class="para"><strong>P.2 幾何推導</strong>：三維包圍盒（Bounding Box）；幾何形體減法切割。</div>
      <div class="para"><strong>P.3 藝術名作</strong>：工業設計手繪草圖（Scott Robertson《How to Draw》方塊建模體系）。</div>
      <div class="homework-box"><strong>P.4 階梯作業【用透視方塊雕刻一把扶手椅】</strong>：畫兩點透視長方盒，前切座墊厚度、後留椅背、底切椅腳，擦去輔助線，椅子自然立體成型。</div>
    </div>

    <div class="lesson-card">
      <div class="lesson-header">
        <span class="lesson-pill">第 20 堂</span>
        <div class="lesson-title">棋子上的圓與圓柱體：透視橢圓法則</div>
      </div>
      <div class="para"><strong>P.1 視覺動機</strong>：畫西洋棋的「車」或水杯時，為什麼畫出來的橢圓總是兩頭尖尖像顆橄欖球？</div>
      <div class="para"><strong>P.2 幾何推導</strong>：正方形內切圓透視變形；長軸與短軸；圓柱體短軸永遠指向消失點鐵律。</div>
      <div class="para"><strong>P.3 藝術名作</strong>：古羅馬圓形競技場與古典圓柱長廊素描。</div>
      <div class="homework-box"><strong>P.4 階梯作業【透視棋盤上的立體西洋棋「車」】</strong>：在透視棋盤方塊底面切出飽滿圓潤的橢圓（短軸指向滅點），頂面切出另一個橢圓，相切連成圓柱體，頂部加上城堡鋸齒。</div>
    </div>
  </div>

  <!-- STAGE 6 (PAGE 11) -->
  <div class="page-break-before" id="ch4-6">
    <div class="section-top-brand">
      <span class="brand-subtext">24-LESSON MATRIX · STAGE 6</span>
      <img src="{logo_data_uri}" class="header-mini-logo" alt="Logo" />
    </div>

    <div class="stage-banner">
      <h3>【第六階段：光影空間、綜合大創作與全域策展（第 21–24 堂）】</h3>
    </div>

    <div class="lesson-card">
      <div class="lesson-header">
        <span class="lesson-pill">第 21 堂</span>
        <div class="lesson-title">棋盤、魔方與多面體的光影射線：光源立足點與精確影子作圖</div>
      </div>
      <div class="para"><strong>P.1 視覺動機</strong>：光線是空間射線；點光源照在物體上，地面影子的大小長度怎麼精確畫出來？</div>
      <div class="para"><strong>P.2 幾何推導</strong>：光源點 $L$、光源地面垂直投影點（立足點）$L_g$；兩條射線相交決定陰影頂點。</div>
      <div class="para"><strong>P.3 藝術名作</strong>：林布蘭畫作中戲劇性的明暗幾何射線。</div>
      <div class="homework-box"><strong>P.4 階梯作業【多面體與魔術方塊在棋盤上的影子】</strong>：在棋盤上方點光源 $L$，地面點 $L_g$。從 $L_g$ 引射線穿過魔方底角，從 $L$ 引射線穿過魔方頂角，兩線交點勾勒出精確的投影形狀。</div>
    </div>

    <div class="lesson-card">
      <div class="lesson-header">
        <span class="lesson-pill">第 22 堂</span>
        <div class="lesson-title">人體的立體坐標化：方塊人（The Mannequin）與透視縮短</div>
      </div>
      <div class="para"><strong>P.1 視覺動機</strong>：告別平面的火柴人，像 3D 動畫師一樣用「方塊盒子」組裝出有空間朝向的人體！</div>
      <div class="para"><strong>P.2 幾何推導</strong>：頭部（球體）、胸腔（方塊盒子）、骨盆（楔形盒子）、四肢（圓柱體）；英雄出拳的透視縮短（Foreshortening）。</div>
      <div class="para"><strong>P.3 藝術名作</strong>：漫威/DC 超級英雄人體動態結構手稿。</div>
      <div class="homework-box"><strong>P.4 階梯作業【在棋盤上奔跑的透視方塊人】</strong>：用兩點透視畫向前傾斜的胸腔方塊與反向扭轉的骨盆方塊，關節用球體連接，畫出奔跑擺動的手臂與腿部圓柱。</div>
    </div>

    <div class="lesson-card">
      <div class="lesson-header">
        <span class="lesson-pill">第 23 堂</span>
        <div class="lesson-title">終極繪畫大創作：走進達利的超現實棋局、浮空多面體與守衛獸</div>
      </div>
      <div class="para"><strong>P.1 視覺動機</strong>：將全套課程學到的棋盤密鋪、正多面體、魔方、多面獵豹、飄逸衣褶、透視與光影，融為一幅震撼人心的巨作！</div>
      <div class="para"><strong>P.2 幾何推導</strong>：單點透視、兩點透視、對角線測深、多面體網格切面、光影投射大綜合。</div>
      <div class="para"><strong>P.3 藝術名作</strong>：薩爾瓦多·達利（Salvador Dalí）超現實主義空間構圖。</div>
      <div class="homework-box"><strong>P.4 階梯作業【超現實巨型透視空間大創作】</strong>：畫延伸至地平線的黑白棋盤地面；空中浮著巨大的兩點透視魔方與正八面體；地面站著穿風衣的方塊人，身旁伏臥幾何獵豹，夕陽拉出幾何長影。</div>
    </div>

    <div class="lesson-card">
      <div class="lesson-header">
        <span class="lesson-pill">第 24 堂</span>
        <div class="lesson-title">全域策展發布：我的《美術中的數學大師手冊》成果展</div>
      </div>
      <div class="para"><strong>P.1 知識閉環</strong>：24 堂課「坐標地址 $\to$ 多邊形密鋪 $\to$ 漢字間架 $\to$ 正多面體 $\to$ 動物與衣物曲面 $\to$ 錯位攝影 $\to$ 棋盤透視 $\to$ 兩點魔方」全景總結。</div>
      <div class="para"><strong>P.2 成果檢定</strong>：6 道涵蓋六角平鋪、書法等分、角虧損展開、錯位除法、透視測深、魔方切分的綜合測驗題。</div>
      <div class="para"><strong>P.3 策展專案</strong>：裝訂個人的《iPad 出版級：美術中的數學大師手冊》，展出自己的實體多面體、靈狐紙雕、連帽斗篷與終極透視大畫，蓋上 `woieyufan` 專屬認證徽章。</div>
      <div class="homework-box"><strong>P.4 銜接未來</strong>：通往國高中高階公理演繹與空間幾何之門。</div>
    </div>
  </div>

  <!-- ==================== CHAPTER 5: SCHOOL SUBMISSION (PAGE 12) ==================== -->
  <div class="page-break-before" id="ch5">
    <div class="section-top-brand">
      <span class="brand-subtext">SCHOOL SUBMISSION ROADMAP</span>
      <img src="{logo_data_uri}" class="header-mini-logo" alt="Logo" />
    </div>

    <div class="chapter-header-box">
      <div class="chapter-title">第五章：學校作業直交方案與階段成品清冊</div>
    </div>

    <div class="para">
      本課程規劃了 <strong>7 大「學校直交級（School-Ready Grade A+）」實體作品</strong>，涵蓋平面美勞、立體紙雕、硬筆書法、生活攝影與建築透視，隨學隨交，完美對接學校各學科作業與評量：
    </div>

    <div class="table-container">
      <table class="doc-table">
        <thead>
          <tr>
            <th>課堂節點</th>
            <th>作品名稱</th>
            <th>作品實體形態</th>
            <th>對接學校學科</th>
            <th>評量拿下 A+ 核心亮點</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>第 4 堂完結</strong></td>
            <td>《蜂巢與伊斯蘭密鋪地磚》</td>
            <td>8 開彩色幾何裝飾畫</td>
            <td>美勞「平面幾何設計」、數學「多邊形密鋪」</td>
            <td>圓規六等分步進作圖，嚴絲合縫無縫隙，超越隨意塗鴉。</td>
          </tr>
          <tr>
            <td><strong>第 7 堂完結</strong></td>
            <td>《歐陽詢楷書間架解碼帖》</td>
            <td>米字格硬筆書法展示卡</td>
            <td>國語每週「硬筆字作業」、校內語文競賽</td>
            <td>標註中宮收緊紅框與排疊等距線，字形挺拔如範本。</td>
          </tr>
          <tr>
            <td><strong>第 9 堂完結</strong></td>
            <td>《幾何水晶：正多面體展》</td>
            <td>正八面體/十二面體立體模型</td>
            <td>美勞「立體造型」、寒假自主學習手作</td>
            <td>純手工卡紙立體摺紙，稜角硬挺如寶石，教室展覽桌焦點。</td>
          </tr>
          <tr>
            <td><strong>第 10-11 堂</strong></td>
            <td>《3D 幾何靈狐 ＆ 獵豹素描》</td>
            <td>3D 動物頭雕 ＋ 4開素描大畫</td>
            <td>學生美展「立體雕塑類 / 素描類」</td>
            <td><strong>全校轟動款！</strong> 國際流行 Low-Poly 雕塑，體積感震撼。</td>
          </tr>
          <tr>
            <td><strong>第 14 堂完結</strong></td>
            <td>《客廳巨獸：強迫透視攝影》</td>
            <td>A4 攝影輸出 ＋ 幾何解說卡</td>
            <td>資訊/綜合「數位攝影」、寒假科學探究</td>
            <td>解密好萊塢《魔戒》特效，相似三角形除法計算幽默嚴謹。</td>
          </tr>
          <tr>
            <td><strong>第 15-18 堂</strong></td>
            <td>《我的房間 ＆ 透視魔方》</td>
            <td>4 開單雙點透視專業素描</td>
            <td>美勞必修「室內透視圖 / 我的房間」</td>
            <td>地磚對角線空間測深無懈可擊，精準切出兩點透視魔方。</td>
          </tr>
          <tr>
            <td><strong>第 21-22 堂</strong></td>
            <td>《迷你立體斗篷 ＆ 奔跑人物》</td>
            <td>立體打版小斗篷 ＋ 風衣素描</td>
            <td>美勞「服裝立體設計」、動態素描作業</td>
            <td>展示省道幾何縫合弧度，告別泡麵線，畫出真實重力垂墜。</td>
          </tr>
          <tr>
            <td><strong>第 24 堂完結</strong></td>
            <td>《美術中的數學大師手冊》</td>
            <td>精裝出版級個人作品集 (Portfolio)</td>
            <td>小學畢業專題、美術班/資優班升學面試</td>
            <td><strong>終極殺手鐧！</strong> 完整學術級作品集，面試評審驚嘆。</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>

  <!-- ==================== CHAPTER 6 & 7 (PAGE 13 & 14) ==================== -->
  <div class="page-break-before" id="ch6">
    <div class="section-top-brand">
      <span class="brand-subtext">PUBLICATION SPECIFICATION</span>
      <img src="{logo_data_uri}" class="header-mini-logo" alt="Logo" />
    </div>

    <div class="chapter-header-box">
      <div class="chapter-title">第六章：iPad 出版級交付規範與 woieyufan 視覺資產綁定</div>
    </div>

    <div class="section-title">6.1 視覺與排版標準</div>
    <div class="bullet-item"><span class="bullet-dot">•</span><div class="bullet-content"><strong>版面視口比例</strong>：鎖定 iPad 4:3 比例容器（iPad Pro 11"/12.9"、iPad Air 最佳化），主版心最大寬度 <code>max-width: 920px</code>，內邊距 <code>35px 55px</code>。</div></div>
    <div class="bullet-item"><span class="bullet-dot">•</span><div class="bullet-content"><strong>品牌標準色盤</strong>：主品牌色霓虹青（<code>#00e5ff</code>）、學術深藍（<code>#1e3a8a</code>）、深邃科技黑（<code>#080a0f</code>）、紙面純白底色（<code>#ffffff</code>）。</div></div>
    <div class="bullet-item"><span class="bullet-dot">•</span><div class="bullet-content"><strong>高精度字體排印</strong>：系統原生 Apple SF Pro Text + 蘋方體，數學公式與坐標標記全數採用 KaTeX 向量排版引擎。</div></div>
    <div class="bullet-item"><span class="bullet-dot">•</span><div class="bullet-content"><strong>強制分頁控制</strong>：寫入 <code>.page-break-before {{ page-break-before: always; break-before: page; }}</code>，確保在 GoodNotes / Notability / Apple Books 中維持印刷級單頁裝訂體驗。</div></div>

    <div class="section-title">6.2 品牌資產載入定位</div>
    <div class="bullet-item"><span class="bullet-dot">•</span><div class="bullet-content"><strong>頁首專屬徽章</strong>：右上方嵌入 <code>woieyufan-logo-transparent-300dpi.png</code>，搭配霓虹青（<code>#00e5ff</code>）高對比邊框。</div></div>
    <div class="bullet-item"><span class="bullet-dot">•</span><div class="bullet-content"><strong>防偽背景浮水印</strong>：全域背景居中壓印 <code>woieyufan-logo_downward.svg</code>，透明度壓制為 <code>opacity: 0.035</code>，既具備防偽識別，又不干擾閱覽。</div></div>
  </div>

  <div class="page-break-before" id="ch7">
    <div class="section-top-brand">
      <span class="brand-subtext">ASSESSMENT RUBRICS</span>
      <img src="{logo_data_uri}" class="header-mini-logo" alt="Logo" />
    </div>

    <div class="chapter-header-box">
      <div class="chapter-title">第七章：評量規準與成果檢定試卷架構</div>
    </div>

    <div class="section-title">7.1 三層次能力檢定指標（Three-Tier Rubrics）</div>
    <div class="rubric-card">
      <div class="rubric-title">Level 1：識坐標（Coordinate Precision）</div>
      <div class="para">檢驗標準：能否精確在網格上標出點位地址，掌握田字格四象限與書法九宮格中宮重心鎖定，用尺規完成正多邊形與六角棋盤繪製。</div>
    </div>
    <div class="rubric-card">
      <div class="rubric-title">Level 2：推透視（Perspective Logic）</div>
      <div class="para">檢驗標準：能否不靠尺量、僅憑幾何對角線作出正確的空間深度收縮（地磚、魔方），嚴格落實視平線高度切割法則與橢圓短軸指向鐵律。</div>
    </div>
    <div class="rubric-card">
      <div class="rubric-title">Level 3：創作品（Creative Synthesis）</div>
      <div class="para">檢驗標準：能否靈活運用攝影視角、比薩斜塔錯位除法、角虧損展開（動物/衣服）、萬物方塊法與光影射線，獨立建構出完整的超現實大場景。</div>
    </div>

    <div class="section-title">7.2 成果檢定試卷命題架構（6 大題型規格）</div>
    <div class="bullet-item"><span class="bullet-dot">•</span><div class="bullet-content"><strong>題型一（棋盤與密鋪）</strong>：六角棋盤軸向坐標判定，與正多邊形頂點角和 $360^\circ$ 密鋪算式證明。（15%）</div></div>
    <div class="bullet-item"><span class="bullet-dot">•</span><div class="bullet-content"><strong>題型二（漢字排疊等距）</strong>：給定外框尺寸，利用歐陽詢排疊公理除法計算橫線間隔，修復失衡漢字。（15%）</div></div>
    <div class="bullet-item"><span class="bullet-dot">•</span><div class="bullet-content"><strong>題型三（角虧損與多面體）</strong>：分析正方體真偽展開圖，並計算圓柱水杯長方形側面的精確周長公式。（15%）</div></div>
    <div class="bullet-item"><span class="bullet-dot">•</span><div class="bullet-content"><strong>題型四（錯位攝影除法）</strong>：利用角大小除法公式計算 10cm 玩具在不同距離下的視角縮放倍數，並標註裁切方案。（15%）</div></div>
    <div class="bullet-item"><span class="bullet-dot">•</span><div class="bullet-content"><strong>題型五（單雙點透視作圖）</strong>：在給定視平線與雙滅點的立方體上，精確利用對角線三等分法畫出立體魔術方塊。（20%）</div></div>
    <div class="bullet-item"><span class="bullet-dot">•</span><div class="bullet-content"><strong>題型六（光影與人體方塊）</strong>：由光源點與地面投影點做出幾何陰影，並搭建穿著垂墜風衣的奔跑方塊人。（20%）</div></div>
  </div>

</div>

<!-- Auto-render KaTeX -->
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
    f.write(html_content)

print(f"Step 2: Clean HTML compiled successfully: {output_html} ({len(html_content)} bytes)")
