# -*- coding: utf-8 -*-
"""
Compile the publication-grade White Paper v6.0 PDF with:
1. High-resolution transparent brand LOGO embedded in the cover header
2. Running headers on all pages with document title, divider, and small logo badge
3. Running footers with hairline divider, English academic subtitle, and dynamic Page X of Y numbering
4. KaTeX mathematical typesetting
5. Mermaid vector diagrams
"""

import os
import subprocess
import base64
import fitz

# Paths
svg_path = r"C:\Users\user\Documents\woieyufan-logo_downward.svg"
badge_png = r"C:\Users\user\.gemini\antigravity\brain\17c5c8ea-1f34-4270-a5e4-410bdd5037d4\scratch\clean_logo.png"
raw_pdf = r"C:\Users\user\.gemini\antigravity\brain\17c5c8ea-1f34-4270-a5e4-410bdd5037d4\scratch\whitepaper_raw.pdf"
final_pdf = r"C:\Users\user\Documents\中學超前自學_微積分先修體系白皮書.pdf"
html_path = r"C:\Users\user\.gemini\antigravity\brain\17c5c8ea-1f34-4270-a5e4-410bdd5037d4\scratch\whitepaper_branded.html"
chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
cjk_font_path = r"C:\Windows\Fonts\msjh.ttc"

# Encode Logo to Base64
with open(badge_png, "rb") as f:
    logo_b64 = base64.b64encode(f.read()).decode("utf-8")
logo_data_uri = f"data:image/png;base64,{logo_b64}"

html_content = f"""<!DOCTYPE html>
<html lang="zh-TW">
<head>
<meta charset="utf-8">
<title>中學超前自學·微積分先修體系白皮書：第一性原理綱領與認知架構</title>
<!-- KaTeX -->
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.css">
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.js"></script>
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/contrib/auto-render.min.js"></script>
<!-- Mermaid -->
<script src="https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.min.js"></script>
<!-- Google Fonts -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Noto+Serif+TC:wght@400;600;700;900&family=Noto+Sans+TC:wght@400;500;700&display=swap" rel="stylesheet">

<style>
  @page {{
    size: A4;
    margin: 26mm 18mm 22mm 18mm;
  }}

  body {{
    font-family: 'Noto Serif TC', 'Songti SC', 'SimSun', serif;
    font-size: 10pt;
    line-height: 1.75;
    color: #2d3748;
    background-color: #ffffff;
    margin: 0;
    padding: 0;
  }}

  /* Top Branded Cover Header */
  .brand-bar {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 20px;
    padding-bottom: 12px;
    border-bottom: 2px solid #2b6cb0;
  }}

  .brand-logo-img {{
    height: 48px;
    width: auto;
    object-fit: contain;
  }}

  .brand-tag {{
    font-family: 'Noto Sans TC', sans-serif;
    font-size: 8pt;
    font-weight: 700;
    letter-spacing: 1.5px;
    color: #2b6cb0;
    background-color: #ebf8ff;
    border: 1px solid #bee3f8;
    padding: 5px 12px;
    border-radius: 4px;
    text-transform: uppercase;
  }}

  .doc-title {{
    font-size: 21pt;
    font-weight: 900;
    color: #1a365d;
    line-height: 1.32;
    margin: 0 0 8px 0;
    letter-spacing: -0.5px;
  }}

  .doc-subtitle {{
    font-family: 'Noto Sans TC', sans-serif;
    font-size: 10.5pt;
    font-weight: 500;
    color: #4a5568;
    margin: 0 0 16px 0;
    letter-spacing: 0.2px;
  }}

  .doc-meta {{
    font-family: 'Noto Sans TC', sans-serif;
    font-size: 8.5pt;
    background-color: #f7fafc;
    border-left: 3.5px solid #3182ce;
    padding: 8px 14px;
    color: #4a5568;
    line-height: 1.6;
    border-radius: 0 4px 4px 0;
    margin-bottom: 24px;
  }}

  .doc-meta strong {{
    color: #2b6cb0;
  }}

  /* Headings */
  h2 {{
    font-family: 'Noto Serif TC', serif;
    font-size: 13pt;
    font-weight: 700;
    color: #1a365d;
    border-left: 4px solid #2b6cb0;
    padding-left: 10px;
    margin-top: 26px;
    margin-bottom: 12px;
    page-break-after: avoid;
  }}

  h3 {{
    font-family: 'Noto Sans TC', sans-serif;
    font-size: 10.5pt;
    font-weight: 700;
    color: #2c5282;
    margin-top: 18px;
    margin-bottom: 8px;
    page-break-after: avoid;
  }}

  h4 {{
    font-family: 'Noto Sans TC', sans-serif;
    font-size: 9.5pt;
    font-weight: 700;
    color: #2b6cb0;
    margin-top: 14px;
    margin-bottom: 6px;
    page-break-after: avoid;
  }}

  p {{
    margin: 0 0 10px 0;
    text-align: justify;
    text-justify: inter-ideograph;
  }}

  /* Blockquotes & Principles */
  blockquote {{
    font-family: 'Noto Sans TC', sans-serif;
    font-size: 9pt;
    background-color: #ebf8ff;
    border-left: 3.5px solid #3182ce;
    color: #2b6cb0;
    margin: 12px 0;
    padding: 10px 14px;
    border-radius: 0 6px 6px 0;
    page-break-inside: avoid;
  }}

  blockquote p {{
    margin: 0;
  }}

  /* Lists */
  ul, ol {{
    margin: 0 0 10px 0;
    padding-left: 20px;
  }}

  li {{
    margin-bottom: 4px;
  }}

  li strong {{
    color: #1a365d;
  }}

  /* Mermaid Diagrams */
  .mermaid {{
    display: flex;
    justify-content: center;
    margin: 16px 0;
    page-break-inside: avoid;
  }}

  /* KaTeX Math */
  .katex {{
    font-size: 1.05em !important;
  }}

  .katex-display {{
    margin: 10px 0 !important;
    page-break-inside: avoid;
  }}

  /* Conclusion Box */
  .conclusion-box {{
    background-color: #f7fafc;
    border: 1px solid #cbd5e0;
    border-top: 3px solid #2b6cb0;
    border-radius: 4px;
    padding: 14px 18px;
    margin-top: 22px;
    page-break-inside: avoid;
  }}

  .conclusion-box p {{
    font-style: italic;
    color: #2d3748;
    margin-bottom: 6px;
  }}
</style>
</head>
<body>

<div class="brand-bar">
  <img src="{logo_data_uri}" alt="Logo" class="brand-logo-img">
  <div class="brand-tag">First-Principles Monograph · Academic Specification</div>
</div>

<div class="doc-title">中學超前自學·微積分先修體系白皮書</div>
<div class="doc-subtitle">第一性原理綱領與認知架構 (First-Principles Doctrine & Cognitive Architecture)</div>

<div class="doc-meta">
  <div><strong>版本標識</strong>：v6.0（典範審定版）</div>
  <div><strong>適用對象</strong>：國二升國三、國三升高一具備深刻求知熱忱與數學天賦之超前自學者</div>
  <div><strong>核心使命</strong>：依循第一性原理，以微積分作為跨學科共通語言，融會貫通中學數學、物理、化學、統計大一統認知疆界。</div>
</div>

<h2>序言：以理性與和諧之美，致敬求知的心智</h2>
<p>在青少年向更高階科學探索的歷程中，心智最渴望的不是機械記憶零散孤立的結論，而是看見真理如何在第一性原理的自洽演繹中自然生長。</p>
<p>微積分誕生於人類對「運動、變化、能量與形貌」的深邃探究。從牛頓的萬有引力與動態天體，到萊布尼茨的幾何切線與微分算子，微積分從一開始便是自然哲學最生機勃勃的共通語言。然而，在過往的學習路徑中，求知者往往在「零碎公式的死記硬背」與「過於抽象枯燥的純符號公理」之間徘徊，難以一窺其宏大的全景。</p>
<p>本體系立足於<strong>第一性原理（First Principles）</strong>，以嚴謹、自洽且充滿幾何直觀的視角，為青年自學者重塑一條完整、通透的科學探索階梯。</p>
<p>本白皮書是本體系的<strong>綱領性文獻（Foundational Doctrine）</strong>。它不羅列繁瑣的教務流水帳，而是確立整個微積分先修體系的<strong>四大基石原則、資優認知心流地圖、以及專著與研討道場的雙軌實踐哲學</strong>。後續所有藍皮書的章節劃分、公式推導鏈、題庫與板書設計，皆本於本白皮書四大憲章之思想基石。</p>

<h2>第一憲章：立論宗旨與資優心智特性</h2>
<h3>1.1 求知天性與第一性原理的渴望</h3>
<p>青少年中具備數學與科學稟賦的心智，天生具備強烈的「邏輯自洽需求」。他們對於「定理為何成立」、「公式背後的物理機制究竟是什麼」擁有不懈的追問本能。當面對動能定理、克卜勒第三定律、交流電有效值或常態分佈時，他們所追尋的並非應試套題的捷徑，而是現象背後的底層因果鏈條。本體系的存在，旨在完全尊重這份求知本能，引領學習者親手推開第一性原理的大門。</p>

<h3>1.2 幾何直觀與空間心智旋轉</h3>
<p>在建立嚴密的符號推導之前，空間與幾何直觀是理解連續變化的重要泉源。無論是割線逼近切線的動態極限、微元累積成整體的體積切片、高爾頓板長條圖坍縮為連續曲線的過程，抑或是二重積分在極座標下的扇形掃描，幾何直觀都能在符號演算之外，賦予數學概念強烈的空間生命力。本體系始終堅持「幾何先行，代數隨後，物理落地」的認知進路。</p>

<h3>1.3 概念自洽：拒絕孤立的公式記憶</h3>
<p>微積分不是一組彼此割裂的解題技巧，而是一個高度內聚的有機思想整體。從單變數微分、反導累積、常微分方程，再到多變數幾何與場論微元，每一個新概念的湧現，都應當是前序概念為解決真實問題時的自然演化。唯有確保理論生長過程中的「步步有著落、處處可溯源」，學習者才能建立真正穩固且具有遷移能力的科學世界觀。</p>

<h2>第二憲章：微積分先修體系的四大基石原則</h2>

<div class="mermaid">
flowchart TD
    subgraph Principles["微積分先修體系四大基石原則"]
        P1["【原則一：因果自洽與零賒帳原則】<br>概念生長零斷層，對數與自然底e及時確立"]
        P2["【原則二：大一統融會原則】<br>微積分作為共通語言，串聯運動、熱力、電磁與統計"]
        P3["【原則三：螺旋式認知深化原則】<br>連續機率直觀伏筆 -> 二重極座標高斯積分終局清償"]
        P4["【原則四：分析力學升維原則】<br>常微分方程刻畫動態，尤拉-拉格朗日方程展現純量之美"]
    end
</div>

<h3>2.1 原則一：因果自洽與零賒帳原則（The Principle of Self-Consistency & Zero Debt）</h3>
<blockquote>
  <p><strong>「凡出現在學習路徑中的關鍵概念，皆應在最合理的臨界節點自然誕生，具備嚴密的幾何與純數合法性，使知識大廈每一步都踏在堅實的地基之上。」</strong></p>
</blockquote>
<p><strong>推論：對數與自然底 $e$ 的及時確立</strong><br>
在微積分基本定理（FTC）解決了所有冪函數 $\\int x^n \\mathrm{{d}}x = \\frac{{x^{{n+1}}}}{{n+1}}$ 的積分之後，整個人類數學面臨 $n = -1$ 的反導空缺。本體系堅持在理論地基完備後，立即迎向這一挑戰。<br>
因此，<strong>對數與自然底 $e$ 緊隨 FTC 之後（Chapter 14）水到渠成地誕生</strong>：以雙曲線下方面積 $A(x) = \\int_1^x \\frac{{1}}{{t}}\\mathrm{{d}}t$ 定義對數，由其伸降不變性嚴謹推導加法同態性質 $A(ab) = A(a) + A(b)$，並藉由面積反函數確立自然底 $e$。在純數地基上及時補齊此一拼圖，使後續所有的常微分方程、流體黏滯阻力、火箭噴射與熱力學等溫過程，皆能在純粹嚴整的數學支持下展開。</p>

<h3>2.2 原則二：大一統融會原則（The Principle of Unified Synthesis）</h3>
<blockquote>
  <p><strong>「微積分是自然哲學的通用語言；高中理化中看似繁複的各類規律，皆可在微積分的統一視角下融會貫通。」</strong></p>
</blockquote>
<p><strong>推論：高中理化規律的源頭溯源</strong><br>
從運動學中速度與位移的微元聯繫 $v\\mathrm{{d}}v = a\\mathrm{{d}}s$、彈簧彈力儲能 $\\frac{{1}}{{2}}kx^2$、克卜勒第三定律的幾何引力積分，到球體積 $\\frac{{4}}{{3}}\\pi R^3$ 與球表面積 $4\\pi R^2$ 的切片對偶關係，乃至電容儲能 $\\frac{{1}}{{2}}CV^2$、電感儲能 $\\frac{{1}}{{2}}LI^2$ 與交流電有效值 RMS $\\frac{{V_0}}{{\\sqrt{{2}}}}$。<br>
當學習者看見這些分散在不同學科的公式，實質上皆源於同一套微積分演算法在不同物理邊界下的具體實現時，孤立記憶的沉重將轉化為通透理解的喜悅。</p>

<h3>2.3 原則三：螺旋式認知深化原則（The Principle of Spiral Deepening）</h3>
<blockquote>
  <p><strong>「深刻的科學理解遵循螺旋式上升規律：由直觀啟發埋設伏筆，經由知識積累與時間沉澱，最終在更高維度完成優雅的數學閉環。」</strong></p>
</blockquote>
<p><strong>推論：機率統計的雙重螺旋穿透</strong></p>
<ul>
  <li><strong>上冊直觀啟發（Chapter 15）</strong>：利用高爾頓板（Galton Board）將離散二項分佈直方圖無限細分，在長條圖平滑坍縮為連續曲線的極限過程中，直觀引入連續機率密度 $\\mathrm{{d}}P = f(x)\\mathrm{{d}}x$ 與全機率歸一化條件 $\\int_{{-\\infty}}^{{\\infty}} f(x)\\mathrm{{d}}x = 1$。導師在此時引出高斯常態分佈的形式 $\\frac{{1}}{{\\sqrt{{2\\pi}}}}\\exp(-x^2/2)$，並在黑板一側留下思考問題：<em>「這裏的常數 $\\sqrt{{2\\pi}}$，究係源於何種幾何對稱性？」</em></li>
  <li><strong>下冊幾何終局（Chapter 27）</strong>：當課程推進至下冊多變數微積分，二重積分在極座標下的面積元 $\\mathrm{{d}}A = r\\mathrm{{d}}r\\mathrm{{d}}\\theta$ 正式確立。學習者藉由將兩個獨立的一維高斯積分轉化為二重平面積分 $\\iint e^{{-(x^2+y^2)}}\\mathrm{{d}}x\\mathrm{{d}}y$，在旋轉對稱性的極座標變換下，常數 $\\pi$ 與 $2$ 自然顯露！</li>
</ul>
<p>常態分佈的 68-95-99.7% 法則與統計物理中的「馬克士威-波茲曼氣體分子速率分佈」在此處完美閉環，讓學習者深刻體會數學與物理在深層結構上的和諧共鳴。</p>

<h3>2.4 原則四：分析力學升維原則（The Principle of Analytical Mechanics Elevation）</h3>
<blockquote>
  <p><strong>「常微分方程是動態物理的精確畫筆；而分析力學則為理解多維物理系統提供了無與倫比的對稱之美。」</strong></p>
</blockquote>
<p><strong>推論：微分方程刻畫動態，尤拉-拉格朗日方程展現純量之美</strong><br>
簡諧運動的本質是二階常微分方程 $\\frac{{\\mathrm{{d}}^2 x}}{{\\mathrm{{d}}t^2}} + \\omega^2 x = 0$ 的解析解。<br>
更進一步，在 Chapter 19 作為上冊的高潮總結，體系引入分析力學的經典工具——<strong>拉格朗日量（Lagrangian）$L = T - V$</strong> 與 <strong>尤拉-拉格朗日方程</strong>：</p>
<p>$$\\frac{{\\mathrm{{d}}}}{{\\mathrm{{d}}t}}\\left(\\frac{{\\partial L}}{{\\partial \\dot{{q}}}}\\right) - \\frac{{\\partial L}}{{\\partial q}} = 0$$</p>
<p>面對滑塊、單擺或耦合質點等複雜力學系統，學習者不再局限於分解受力向量與隔離受力圖，而是立足於系統動能 $T$ 與位能 $V$ 的純量之差，通過偏導演算直接寫出系統動力學方程。這引導學習者跨越牛頓力學的向量視角，領略最小作用量原理與分析力學的極致簡約。</p>

<h2>第三憲章：超前自學者的認知階梯與雙卷演進全景</h2>

<div class="mermaid">
flowchart LR
    S1["【態一：幾何與物理直觀】<br>動態逼近、幾何切片、物理相空間"]
    S2["【態二：微積分演算法則】<br>極限算子、微分方程、分部換元、面積元"]
    S3["【態三：大一統代數結論】<br>理化公式溯源、對稱性提煉、宏觀定律"]

    S1 ==>|"激發求知渴望"| S2
    S2 ==>|"提供分析工具"| S3
</div>

<h3>3.1 頓悟階梯三態躍遷模型</h3>
<p>為引導自學者順利跨越抽象門檻，體系各模組均遵循<strong>「三態躍遷」</strong>的認知動線：由現象與幾何切片出發建立直觀猜想，透過微積分微元與算子進行精確量化，最終沉澱為具備普適解釋力的高階代數定律。</p>

<h3>3.2 雙卷 28 個有機生長模組架構</h3>
<p>本體系打破人為行政課時的死板限制，完全順應高中數學與物理公式的內在深度，自然生長為 <strong>28 個完整模組（共 56 小時高強度研學）</strong>：</p>

<h4>上冊【純數脊椎骨、單變數積分與常微分方程實戰】（Chapters 1–19，約 420 頁）</h4>
<ul>
  <li><strong>Stage I：微分學幾何起源（Ch 1–3）</strong>：極限割線、冪法則、多項式切線與重根判別式；</li>
  <li><strong>Stage II：複合映射與相空間（Ch 4–6）</strong>：連鎖律、隱函數圓錐曲線、相空間速度場 $v\\mathrm{{d}}v=a\\mathrm{{d}}s$；</li>
  <li><strong>Stage III：三角震盪與極值本質（Ch 7–9）</strong>：無量綱弧度制、向心加速度 $a=v^2/R$、費馬最短時間原理；</li>
  <li><strong>Stage IV：累積的度量與對數奠基（Ch 10–14）</strong>：黎曼和、微積分基本定理、第一面積矩、換元分部、<strong>對數與自然底 $e$ 的幾何發明（填補 $x^{{-1}}$ 反導空缺，自洽奠基）</strong>；</li>
  <li><strong>Stage V：動態物理與常微分方程（Ch 15–19）</strong>：
    <ul>
      <li><em>Ch 15</em>：<strong>機率統計的連續跨越</strong>（高爾頓板坍縮、連續機率密度 $\\mathrm{{d}}P=f(x)\\mathrm{{d}}x$、記帳 $\\sqrt{{2\\pi}}$ 懸念）；</li>
      <li><em>Ch 16–18</em>：一階 ODE（牛頓冷卻定律、流體終端速度、齊奧爾科夫斯基火箭方程、RC 電路暫態與 50% 能量轉換）；</li>
      <li><em>Ch 19</em>：二階 ODE 與簡諧運動（阻尼振動判別式）兼 <strong>拉格朗日量分析力學專題</strong>（尤拉-拉格朗日方程輸出運動方程）。</li>
    </ul>
  </li>
</ul>

<h4>下冊【物理場域實戰、多變數幾何、統計終局與量子大一統】（Chapters 20–28，約 380 頁）</h4>
<ul>
  <li><strong>Stage VI：古典物理場域實戰（Ch 20–23）</strong>：熱力學第一定律與絕熱膨脹 $PV^\\gamma=C$、電磁三大位能三位一體 $\\frac{{1}}{{2}}$ 幾何本質、畢奧-薩伐爾定律磁場積分、剛體轉動慣量與平行軸定理；</li>
  <li><strong>Stage VII：級數逼近、多變數微積分與統計量子終局（Ch 24–28）</strong>：
    <ul>
      <li><em>Ch 24–26</em>：泰勒級數逼近、全微分與實驗誤差傳播、二重積分極座標面積元 $\\mathrm{{d}}A = r\\mathrm{{d}}r\\mathrm{{d}}\\theta$；</li>
      <li><em>Ch 27</em>：<strong>高斯常態分佈終局清償與氣體速率</strong>（極座標擊破高斯積分，清償 Ch 15 之 $\\sqrt{{2\\pi}}$ 借條，解析常態分佈法則與馬克士威-波茲曼分佈）；</li>
      <li><em>Ch 28</em>：<strong>正交函數系、傅立葉展開與量子力學閉環</strong>（交流電有效值 RMS $\\frac{{1}}{{\\sqrt{{2}}}}$ 嚴格推導、海森堡測不準原理 $\\Delta x \\Delta p \\ge \\frac{{\\hbar}}{{2}}$ 的波包微積分本質）。</li>
    </ul>
  </li>
</ul>

<h2>第四憲章：出版專著與黑板道場的雙軌實踐</h2>

<div class="mermaid">
flowchart TD
    subgraph Track1["【軌道一：出版級案頭專著《書籍篇》】"]
        T1_1["定位：案頭良師，安靜自學時的嚴密演繹"]
        T1_2["特徵：100% 零跳步推導鏈，高精度幾何向量圖繪製"]
        T1_3["邊欄：80~120字側欄手札（直觀啟發、思維辨析、統一視角）"]
        T1_4["載體：7大階段28章、196條公式鏈、448道階梯練習、112幅向量圖規"]
    end

    subgraph Track2["【軌道二：黑板研討道場《課堂篇》】"]
        T2_1["定位：思維工坊，生長式黑板板書與深度研討"]
        T2_2["特徵：重回黑板四分區與粉筆手寫推導的生長節奏"]
        T2_3["機制：蘇格拉底啟發式提問、即席推演、深入辨析、簡約破局"]
        T2_4["載體：28場研討（56小時）、196條板書、252道攻防實彈、五維雷達評量"]
    end

    Track1 ==>|"提供完備自學儲備"| Track2
    Track2 ==>|"反饋思維啟發，重讀專著"| Track1
</div>

<h3>4.1 案頭專著《書籍篇》的使命：嚴謹自洽的純粹演繹</h3>
<p>專著是自學者深度閱讀的案頭夥伴：零跳步原則保護自學者的邏輯自洽感；每章配備嚴格 80～120 字的啟發性邊欄手札，點破幾何本質；階梯式習題系統包含基礎工具練習、跨學科物理應用與深水探索挑戰，構建 448 道層次豐富的思考題庫。</p>

<h3>4.2 黑板研討《課堂篇》的靈魂：手寫推導與啟發對話</h3>
<p>課堂篇倡導以黑板手寫取代預製幻燈片。在粉筆書寫的時間節奏中，學生得以同步觀摩「公式如何從物理圖像中逐步生長為代數式」。黑板劃分為四分區動線：先驗概念區、核心微積分推導區、中學物理定律演繹區，以及研討記帳區。導師透過蘇格拉底式啟發提問，啟發學生獨立思考與即席表達。</p>

<h3>4.3 研習成效五維能力雷達標竿</h3>
<p>完成本體系研習的自學者，將在五大維度建立紮實的能力基礎（滿分 25 分）：<strong>第一性原理溯源力</strong>、<strong>符號與幾何心智旋轉力</strong>、<strong>綜合問題分析力</strong>、<strong>極限與量綱守恆敏銳度</strong>，以及<strong>即席板書與學術表達力</strong>。</p>

<div class="conclusion-box">
  <p><strong>結語：在理性與自然的對稱中前行</strong></p>
  <p>這套微積分先修體系，本質上是一次引領青年學子走向科學純粹美感的邀約。</p>
  <p>真正的科學探索，是一場在簡約與和諧中發現秩序的旅程。當學習者在 Chapter 14 親眼見證自然底 $e$ 如何優雅地填補反導空缺，在 Chapter 19 體會拉格朗日量以純量統合複雜動力學的從容，在 Chapter 27 藉極座標高斯積分揭開常態分佈 $\\sqrt{{2\\pi}}$ 的幾何面紗——在那一刻，他們所獲得的，不僅是跨越學科的分析工具，更是一種對自然規律深層對稱性的敬畏與終生受用的理性自信。</p>
  <p>願每一位懷抱求知熱忱的自學者，皆能在這座理性的階梯上，踏出屬於自己的堅實步伐。</p>
</div>

<script>
  document.addEventListener("DOMContentLoaded", function() {{
    renderMathInElement(document.body, {{
      delimiters: [
        {{left: '$$', right: '$$', display: true}},
        {{left: '$', right: '$', display: false}}
      ],
      throwOnError : false
    }});
    mermaid.initialize({{
      startOnLoad: true,
      theme: 'neutral',
      flowchart: {{ useMaxWidth: true, htmlLabels: true, curve: 'basis' }}
    }});
  }});
</script>

</body>
</html>
"""

# Write HTML
with open(html_path, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"Branded HTML written to: {html_path}")

# Run Chrome Headless to generate raw PDF
cmd = [
    chrome_path,
    "--headless=new",
    "--disable-gpu",
    "--run-all-compositor-stages-before-draw",
    "--virtual-time-budget=8000",
    "--no-pdf-header-footer",
    f"--print-to-pdf={raw_pdf}",
    html_path
]

res = subprocess.run(cmd, capture_output=True, text=True)
if res.returncode != 0 or not os.path.exists(raw_pdf):
    print("Error in Chrome PDF rendering:", res.stderr)
    exit(1)

print(f"Raw PDF generated ({os.path.getsize(raw_pdf)} bytes). Now stamping headers, footers and logo...")

# Post-processing with PyMuPDF (fitz)
doc = fitz.open(raw_pdf)
total_pages = len(doc)
margin_x = 51.0 # pt (about 18mm)
header_y = 22.0 # pt
badge_w = 26.0
badge_h = 25.0

# Prepare CJK font for Chinese running headers
doc[0].insert_font(fontname="cjk_header", fontfile=cjk_font_path)

for page_idx in range(total_pages):
    page = doc[page_idx]
    w = page.rect.width
    h = page.rect.height

    # Register font on every page
    page.insert_font(fontname="cjk_header", fontfile=cjk_font_path)

    # Header Stamping
    if page_idx == 0:
        # Cover page: HTML already has the large logo in the brand bar.
        # Add subtle top hairline
        pass
    else:
        # Running header on pages 2+
        # Left header text
        header_text = "中學超前自學 · 微積分先修體系白皮書（第一性原理綱領與認知架構）"
        page.insert_text(fitz.Point(margin_x, header_y + 16), header_text, fontname="cjk_header", fontsize=8.5, color=(0.28, 0.35, 0.44))

        # Right header logo badge
        badge_rect = fitz.Rect(w - margin_x - badge_w, header_y, w - margin_x, header_y + badge_h)
        page.insert_image(badge_rect, filename=badge_png, overlay=True)

        # Hairline divider under header
        divider_y = header_y + badge_h + 5
        page.draw_line(fitz.Point(margin_x, divider_y), fitz.Point(w - margin_x, divider_y), color=(0.80, 0.84, 0.89), width=0.6)

    # Footer Stamping on all pages
    footer_divider_y = h - 38.0
    page.draw_line(fitz.Point(margin_x, footer_divider_y), fitz.Point(w - margin_x, footer_divider_y), color=(0.80, 0.84, 0.89), width=0.6)

    # Left footer: English Monograph Title / Spec
    left_footer = "The Precollege Calculus Monograph · First-Principles Doctrine & Cognitive Architecture"
    page.insert_text(fitz.Point(margin_x, footer_divider_y + 18), left_footer, fontname="helv", fontsize=8.0, color=(0.45, 0.52, 0.60))

    # Right footer: Page numbering
    page_str = f"Page {page_idx + 1} of {total_pages}"
    page.insert_text(fitz.Point(w - margin_x - 56, footer_divider_y + 18), page_str, fontname="helv", fontsize=8.0, color=(0.35, 0.40, 0.48))

temp_final = raw_pdf.replace(".pdf", "_stamped.pdf")
doc.save(temp_final)
doc.close()

import shutil
shutil.move(temp_final, final_pdf)
print(f"SUCCESS! Branded PDF generated at: {final_pdf}")
print(f"Total Pages: {total_pages}, Size: {os.path.getsize(final_pdf)} bytes")
