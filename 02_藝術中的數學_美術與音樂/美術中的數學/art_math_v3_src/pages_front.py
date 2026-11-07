# -*- coding: utf-8 -*-
"""
Front pages (Page 1 to Page 8) for Visual Geometry & Art Engineering White Paper V4.0
iPad 4:3 / A4 Publication Specifications.
Unified under the Single Core Philosophy:
【小學數學工具的本質加深：從小學生手裡有的工具出發，捅破課本窗戶紙，直通真實世界】
Each page is balanced, airy, and equipped with an executive bottom footer.
"""

def get_page_1():
    return r'''
  <!-- PAGE 1: COVER -->
  <div class="cover-wrapper">
    <img class="cover-watermark" src="__SVG_DATA_URI__" alt="Watermark">
    
    <div class="cover-header-brand">
      <img class="brand-logo-img" src="__LOGO_DATA_URI__" alt="woieyufan Logo">
      <div class="brand-text-col">
        <span class="brand-title">woieyufan EDUCATION</span>
        <span class="brand-sub">K-9 VISUAL MATHEMATICS & ARTISTIC ENGINEERING SPECIFICATION</span>
      </div>
    </div>

    <div class="cover-main">
      <div class="cover-badge">K-9 CURRICULUM RECONSTRUCTION & EXTENSION WHITE PAPER 4.0</div>
      <h1 class="doc-title">小學全域：視覺幾何與藝術工程<br>體系建構與課外讀物企劃白皮書</h1>
      <p class="doc-subtitle">
        全面立足小學數學工具庫，捅破應試死算窗戶紙，在真實世界中完成認知加深<br>
        從除法餘數、數對坐標、角度量測到展開圖：以自然光學、生活工藝、名畫透視與極簡程式為驗證舞台
      </p>

      <div class="meta-grid">
        <div class="meta-item">
          <span class="meta-label">唯一核心出發點</span>
          <span class="meta-val">小學工具原點 ➜ 捅破窗戶紙 ➜ 現實本質加深</span>
        </div>
        <div class="meta-item">
          <span class="meta-label">跨界定位</span>
          <span class="meta-val">自然科與名畫為舞台，程式為輔助驗證工具</span>
        </div>
        <div class="meta-item">
          <span class="meta-label">適讀對象</span>
          <span class="meta-val">國小中高年級至國中先修</span>
        </div>
        <div class="meta-item">
          <span class="meta-label">體系規格</span>
          <span class="meta-val">七大維度全景題庫 ｜ 舒展版 iPad 4:3 典藏白皮書</span>
        </div>
      </div>
    </div>

    <div class="cover-footer">
      <span>CONFIDENTIAL & PROPRIETARY ｜ ADVANCED EDUCATIONAL SPECIFICATION</span>
      <span>VERSION 4.0 ｜ VERIFIED FOR K-9 ACADEMIC & EXTRACURRICULAR DEPLOYMENT</span>
    </div>
  </div>
'''

def get_page_2():
    return r'''
  <!-- PAGE 2: EXECUTIVE ARCHITECTURE & CORE PHILOSOPHY -->
  <div class="section-page">
    <div class="page-top-header">
      <span class="header-left">EXECUTIVE ARCHITECTURE & CORE PHILOSOPHY ｜ 體系定位與唯一核心綱領</span>
      <div class="header-right">
        <img class="header-logo-mini" src="__LOGO_DATA_URI__" alt="Mini Logo">
        <span>woieyufan EDUCATION</span>
      </div>
    </div>

    <div class="chapter-header-box">
      <div class="chapter-title">唯一核心出發點：小學數學工具的本質加深</div>
    </div>

    <div class="hero-statement">
      ★ 本白皮書唯一核心宣言：<br>
      小學生在學校學的數學工具，本來就威力無窮！課本為了應試，往往在最精彩、最通往真實世界的地方「淺嚐輒止」。我們唯一的出發點，就是從小學生手裡已經掌握的工具起步，把沒講透的窗戶紙捅破，帶他們在真實世界裡看見數學的真實威力！
    </div>

    <div class="para">
      在過往的教學實踐中，跨學科教育往往陷入兩種極端：一種是<strong>「為了學畫畫而附庸風雅借用數學」</strong>，把數學當作零碎的點綴；另一種是<strong>「高深大學抽象概念的強行下放」</strong>，用小學生完全無法理解的拓撲與群論名詞堆砌門面。本白皮書堅決摒棄這兩種歧途，確立了純粹而堅定的單一主幹：
    </div>

    <!-- 6 CORE ELEMENTARY TOOLS DEEPENING TABLE -->
    <div style="margin: 10px 0;">
      <table class="doc-table">
        <thead>
          <tr>
            <th style="width: 20%;">小學必學工具</th>
            <th style="width: 28%;">課本應試痛點（盲點死算）</th>
            <th style="width: 32%;">真實世界跨界舞台（物理/名畫）</th>
            <th style="width: 20%;">本質認知加深</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>除法餘數與因倍數</strong></td>
            <td>直式除法算式反覆求商與餘數，枯燥刷題</td>
            <td>時鐘流星雨、萬花尺花瓣齒輪、提花織布</td>
            <td><strong>模運算 $\pmod m$</strong> 週期密碼</td>
          </tr>
          <tr>
            <td><strong>平面坐標與數對</strong></td>
            <td>空白方格紙上標點 $(x, y)$，毫無空間意義</td>
            <td>書法九宮格質心、向量動態捕捉、螢幕像素</td>
            <td><strong>質心力矩與向量</strong> 空間控制</td>
          </tr>
          <tr>
            <td><strong>量角器與角度量測</strong></td>
            <td>拿量角器量測靜態三角形內角，枯燥乏味</td>
            <td>撞球兩次反射、萬花筒鏡面夾角、色相環</td>
            <td><strong>光線幾何與對稱群</strong> 映射</td>
          </tr>
          <tr>
            <td><strong>柱錐展開圖與面積</strong></td>
            <td>考卷摺紙盒判斷哪一面相對，應試死記</td>
            <td>柏拉圖多面體、服裝立體打版省道、足球截角</td>
            <td><strong>高斯曲率與笛卡兒角虧</strong></td>
          </tr>
          <tr>
            <td><strong>比、連比與比例式</strong></td>
            <td>計算 $a:b=c:d$ 內外項相乘，脫離物體結構</td>
            <td>古希臘《持矛者》7.5頭身、透視調和數列</td>
            <td><strong>模矩系統與透視投影</strong></td>
          </tr>
          <tr>
            <td><strong>小數、分數與百分比</strong></td>
            <td>反覆進行小數與分數相互轉換直式練習</td>
            <td>RGB 光源刺激 vs CMYK 減法吸光、大氣散射</td>
            <td><strong>光學衰減與能量守恆</strong></td>
          </tr>
        </tbody>
      </table>
    </div>

    <div class="callout-box" style="margin-top: 8px;">
      <div class="callout-title">★ 三大從屬檢驗準繩（Subordinate Verification Criteria）</div>
      <div class="callout-content">
        <strong>① 必須能親手算得出</strong>：拒絕玄學比喻，小學生學過四則運算，就能親手代數算出 CMYK 吸收率與齒輪圈數。<br>
        <strong>② 必須符合真實物理</strong>：調動小學自然科光與影子、大氣與視力常識，揭示大師調色與透視的客觀自然法則。<br>
        <strong>③ 程式純為現代數位圓規</strong>：不搞繁瑣程式教學，3～5 行極簡 Code Lab 僅作為動態放大鏡驗證幾何閉合。
      </div>
    </div>

    <div class="page-bottom-footer">
      <span class="footer-left">小學全域：視覺幾何與藝術工程 ｜ 企劃白皮書</span>
      <span class="footer-center">第 2 頁 / 共 24 頁</span>
      <span class="footer-right">woieyufan EDUCATION ｜ 內部專利發行規範</span>
    </div>
  </div>
'''

def get_page_3():
    return r'''
  <!-- PAGE 3: TABLE OF CONTENTS -->
  <div class="section-page">
    <div class="page-top-header">
      <span class="header-left">COMPLETE ARCHITECTURE & TOC ｜ 白皮書全卷規劃地圖</span>
      <div class="header-right">
        <img class="header-logo-mini" src="__LOGO_DATA_URI__" alt="Mini Logo">
        <span>woieyufan EDUCATION</span>
      </div>
    </div>

    <div class="chapter-header-box">
      <div class="chapter-title">白皮書全卷規劃地圖與導讀導覽</div>
      <div class="para">
        本白皮書共分為七大章節與附錄，系統化規範教育哲學、知識地圖、核心公理、24 模組實戰矩陣、實施標準與評量規準。
      </div>
    </div>

    <div class="toc-grid">
      <div class="toc-item">
        <div class="toc-item-title">第一章：體系定位與教育哲學宣言</div>
        <div class="toc-item-sub">P. 4–5 ｜ 唯一核心立論、小學工具淺嚐痛點診斷、自然科物理還原與輔助程式定位</div>
      </div>
      <div class="toc-item">
        <div class="toc-item-title">第二章：小學數學工具對接與七大幾何維度地圖</div>
        <div class="toc-item-sub">P. 6 ｜ 數與運算、平面坐標、光譜色彩、密鋪、多面體、射影透視與碎形力學</div>
      </div>
      <div class="toc-item">
        <div class="toc-item-title">第三章：核心跨界幾何與硬核科學公理</div>
        <div class="toc-item-sub">P. 7–8 ｜ 光學吸光方程、莫內天光散射、笛卡兒角虧、相機中央射影、齒輪模數與極限</div>
      </div>
      <div class="toc-item">
        <div class="toc-item-title">第四章：全模組探案課程工程矩陣</div>
        <div class="toc-item-sub">P. 9–20 ｜ 24 模組實戰設計、K-9 課本數學錨點與尺規作圖工程矩陣（每頁舒展 2 堂課）</div>
      </div>
      <div class="toc-item">
        <div class="toc-item-title">第五章：課堂實施標準與實體成果清冊</div>
        <div class="toc-item-sub">P. 21 ｜ 120 分鐘五段式模組、6 大實體成果清冊（模矩尺/艾雪印章/透視板）</div>
      </div>
      <div class="toc-item">
        <div class="toc-item-title">第六章與第七章：出版規格、評量規準與附錄</div>
        <div class="toc-item-sub">P. 22–24 ｜ iPad 出版級規範、四維度獨立 Rubrics 規準、人體調和縮短與密鋪嚴格證明</div>
      </div>
    </div>

    <div class="section-title">全卷三大閱讀與研析路徑指南（Reading Pathways）</div>
    <table class="doc-table">
      <tr>
        <th style="width: 25%;">讀者角色</th>
        <th style="width: 40%;">推薦研讀路徑</th>
        <th style="width: 35%;">核心收穫與落地指引</th>
      </tr>
      <tr>
        <td><strong>家長與自學學生</strong></td>
        <td>P. 2 (核心宣言) ➜ P. 6 (七大維度地圖) ➜ P. 9–20 (24 堂實戰矩陣)</td>
        <td>打破對數學的枯燥恐懼，理解學校工具如何玩轉名畫透視與光學色彩。</td>
      </tr>
      <tr>
        <td><strong>數學與美術教研團隊</strong></td>
        <td>P. 4–5 (哲學宣言) ➜ P. 7–8 (科學公理) ➜ P. 21 (120分五段式實施)</td>
        <td>掌握跨領域課程的底層邏輯，建立尺規重構與五段式教學標竿標準。</td>
      </tr>
      <tr>
        <td><strong>出版編輯與課程開發</strong></td>
        <td>P. 9–20 (模組矩陣) ➜ P. 22 (出版標準) ➜ P. 23 (評量規準)</td>
        <td>獲取每堂課的 Before/After 嚴格對照、實體成果定義與四階評分標準。</td>
      </tr>
    </table>

    <div class="page-bottom-footer">
      <span class="footer-left">小學全域：視覺幾何與藝術工程 ｜ 企劃白皮書</span>
      <span class="footer-center">第 3 頁 / 共 24 頁</span>
      <span class="footer-right">woieyufan EDUCATION ｜ 內部專利發行規範</span>
    </div>
  </div>
'''

def get_page_4():
    return r'''
  <!-- PAGE 4: CHAPTER 1 (PART 1): PHILOSOPHY & TOOL ORIGIN -->
  <div class="section-page">
    <div class="page-top-header">
      <span class="header-left">ACADEMIC PHILOSOPHY & SPECIFICATION ｜ 第一章：體系定位與教育哲學宣言（上）</span>
      <div class="header-right">
        <img class="header-logo-mini" src="__LOGO_DATA_URI__" alt="Mini Logo">
        <span>woieyufan EDUCATION</span>
      </div>
    </div>

    <div class="chapter-header-box">
      <div class="chapter-title">第一章：體系定位與教育哲學宣言</div>
    </div>

    <div class="section-title">1.1 兒童數學與視覺藝術的割裂痛點：被閹割的小學工具</div>
    <div class="para">
      在當前學校教學中，數學與美術陷入了嚴重的「學科孤島」困境：數學課充斥著脫離現實的解題死算（如反覆計算「內外項相乘」、「求商與餘數」、「追趕問題」），把鮮活的空間幾何與代數思維閹割成了枯燥的考卷分數。學生日復一日地套公式，卻完全不知道自己手裡算過成百上千次的工具，在真實世界裡究竟有何威力。
    </div>
    <div class="para">
      與此同時，美術課則往往淪為純粹的感官塗鴉與主觀模仿，缺乏嚴謹的幾何骨骼。學生畫人體不知比例規律，畫風景不知透視截線，畫色彩不知光譜吸收。我們主張：<strong>「視覺藝術是最高維度的數學可視化實驗室，數學是藝術與自然的隱形工程龍骨。」</strong>
    </div>

    <div class="section-title">1.2 唯一的核心出發點：小學生學過什麼，我們就從哪裡起跳</div>
    <div class="para">
      本體系絕不空降高中大學的高深抽象符號。本書所有主題的唯一及格線只有一條：<strong>這是不是小學生課本裡必然會學到的工具？小學生的認知能不能在這裡被狠狠加深？</strong>
    </div>

    <div class="callout-box" style="background: #f8fafc; border-left: 4px solid var(--primary);">
      <div class="callout-title" style="color: var(--primary);">★ 捅破課本沒講透的「三層窗戶紙」：</div>
      <div class="callout-content" style="color: #334155;">
        <p style="margin: 0 0 8px 0;"><strong>① 除法餘數的昇華</strong>：課本只考直式算式的商與餘數，我們揭密餘數正是國旗五角星一筆畫閉合、時鐘流星雨與萬花尺花瓣的生成密碼！</p>
        <p style="margin: 0 0 8px 0;"><strong>② 生字九宮格的昇華</strong>：課本只拿九宮格來練字，我們揭密數對坐標 $(x, y)$ 是控制漢字結構「險絕不倒」的質心力矩工程！</p>
        <p style="margin: 0;"><strong>③ 柱錐展開圖的昇華</strong>：課本只考紙盒折疊，我們揭密剪掉的角度（角虧）正是服裝打版師把平面布料穿成立體衣服的神奇剪刀！</p>
      </div>
    </div>

    <div class="hero-statement">
      教育本質：不是給孩子塞入更多深奧的公式，而是把他們手裡原本看似平淡無奇的工具，擦拭出照亮大自然與名畫的鋒芒！
    </div>

    <div class="page-bottom-footer">
      <span class="footer-left">小學全域：視覺幾何與藝術工程 ｜ 企劃白皮書</span>
      <span class="footer-center">第 4 頁 / 共 24 頁</span>
      <span class="footer-right">woieyufan EDUCATION ｜ 內部專利發行規範</span>
    </div>
  </div>
'''

def get_page_5():
    return r'''
  <!-- PAGE 5: CHAPTER 1 (PART 2): NATURE, PHYSICS & AUXILIARY CODE -->
  <div class="section-page">
    <div class="page-top-header">
      <span class="header-left">ACADEMIC PHILOSOPHY & SPECIFICATION ｜ 第一章：體系定位與教育哲學宣言（下）</span>
      <div class="header-right">
        <img class="header-logo-mini" src="__LOGO_DATA_URI__" alt="Mini Logo">
        <span>woieyufan EDUCATION</span>
      </div>
    </div>

    <div class="chapter-header-box">
      <div class="chapter-title">第一章：體系定位與教育哲學宣言（續）</div>
    </div>

    <div class="section-title">1.3 自然科與大師名畫是舞台，絕非附庸風雅的拼貼</div>
    <div class="para">
      為什麼本體系必須深度注入自然科物理、光譜與神經生理？因為小學自然科教了光與影子、認識三原色與視覺，但學校課堂從未用嚴謹的數學工具把兩者串聯起來：
    </div>

    <div class="callout-box" style="background: #eff6ff; border-left: 4px solid #0284c7; border-color: #bfdbfe;">
      <div class="callout-title" style="color: #1e40af;">★ 自然科物理聯動之硬核實例：</div>
      <div class="callout-content" style="color: #1e3a8a;">
        <p style="margin: 0 0 8px 0;"><strong>① 螢幕 RGB vs 顏料 CMYK</strong>：螢幕是特定波長（紅 625nm、綠 530nm、藍 450nm）對視網膜 S/M/L 錐細胞的加法刺激；顏料則是化學染料對色光的減法吸收。小學生學過小數百分比，就能親手代數換算！</p>
        <p style="margin: 0;"><strong>② 莫內相反色陰影</strong>：晴天直射陽光被遮擋處並非黑色或灰色，而是被大氣瑞立散射天光藍（450nm）漫射照亮，疊加視網膜神經側抑制，必然在生理上誘發互補色相 $\theta_{\text{shadow}} = (\theta_{\text{light}} + 180^\circ) \pmod{360^\circ}$。大師不過是精確遵循了客觀物理！</p>
      </div>
    </div>

    <div class="section-title">1.4 程式是現代孩子的「數位圓規」，而非喧賓奪主的主角</div>
    <div class="para">
      我們不是要開程式設計課。3～5 行隨處可跑的極簡 Code Lab（p5.js / Python），是為了給孩子一把「動態幾何放大鏡」：
    </div>
    <div class="para">
      幾何不該永遠困在靜態紙筆。萬花筒兩面鏡子夾角為什麼必須整除 $360^\circ$？孩子在程式裡把夾角改成 $50^\circ$，畫面上立刻親眼看到邊界撕裂與黑縫；改變齒輪齒數，動態花瓣瞬間根據最小公倍數完美閉合。程式作為輔助工具，讓數學定律化為親手操控、即時反饋的可驗證世界。
    </div>

    <div class="hero-statement">
      總結：小學數學工具是骨骼，自然科物理是真實，大師名畫是舞台，程式是數位放大鏡。<br>
      四者全部為「加深小學生的幾何直覺」這一單一目標服務！
    </div>

    <div class="page-bottom-footer">
      <span class="footer-left">小學全域：視覺幾何與藝術工程 ｜ 企劃白皮書</span>
      <span class="footer-center">第 5 頁 / 共 24 頁</span>
      <span class="footer-right">woieyufan EDUCATION ｜ 內部專利發行規範</span>
    </div>
  </div>
'''

def get_page_6():
    return r'''
  <!-- PAGE 6: CHAPTER 2: K-9 KNOWLEDGE TOPOGRAPHY & 7 DIMENSIONS -->
  <div class="section-page">
    <div class="page-top-header">
      <span class="header-left">KNOWLEDGE TOPOGRAPHY ｜ 第二章：小學數學工具對接與七大幾何維度地圖</span>
      <div class="header-right">
        <img class="header-logo-mini" src="__LOGO_DATA_URI__" alt="Mini Logo">
        <span>woieyufan EDUCATION</span>
      </div>
    </div>

    <div class="chapter-header-box">
      <div class="chapter-title">第二章：小學數學工具對接與七大幾何維度地圖</div>
      <div class="para">
        本體系全面啟動小學中高年級必學的數學工具，向上建構出七大主題幾何維度，構成完整的視覺幾何心智地圖。
      </div>
    </div>

    <div class="ba-container" style="gap: 14px; margin-bottom: 12px;">
      <div class="ba-col" style="background: #f0fdf4; border: 1px solid #bbf7d0; padding: 12px 14px;">
        <div class="ba-head" style="color: #15803d; font-size: 13px; margin-bottom: 6px;">軌道 A：代數規律、平面坐標與密鋪（平面幾何與代數）</div>
        <p style="color: #334155; font-size: 12px; margin: 4px 0; line-height: 1.5;"><strong>模組一：數與運算・週期規律</strong>（除法餘數、因倍數）：時鐘流星雨一筆畫星形 $\{n/k\}$、萬花尺 $\text{lcm}$ 齒輪花瓣、提花織布互質步長二進位矩陣。</p>
        <p style="color: #334155; font-size: 12px; margin: 4px 0; line-height: 1.5;"><strong>模組二：平面坐標・格網力學</strong>（數對 $(x,y)$、線段比例）：漢字九宮格質心力矩平衡、曼哈頓正方形「圓」、像素反鋸齒小數覆蓋率、鋼筆貝茲曲線比例插值、AI動捕向量夾角。</p>
        <p style="color: #334155; font-size: 12px; margin: 4px 0; line-height: 1.5;"><strong>模組四：平面分割・密鋪拓撲</strong>（垂直平分線、面積守恆）：長頸鹿斑紋 Voronoi 全域分割、艾雪蜥蜴剪紙滑移反射面積守恆、七巧板 13 種凸多邊形極限定理。</p>
      </div>

      <div class="ba-col" style="background: #fdf2f8; border: 1px solid #fbcfe8; padding: 12px 14px;">
        <div class="ba-head" style="color: #9d174d; font-size: 13px; margin-bottom: 6px;">軌道 B：三維空間、光影色彩與物理極限（立體、光學與力學）</div>
        <p style="color: #334155; font-size: 12px; margin: 4px 0; line-height: 1.5;"><strong>模組三：光學色彩・神經生理</strong>（角度量測、平角 $180^\circ$）：萬花筒像數 $N=360/\theta-1$、RGB 刺激錐細胞 vs CMYK 吸光代數、莫內天光散射相反色陰影、手電筒圓錐截面。</p>
        <p style="color: #334155; font-size: 12px; margin: 4px 0; line-height: 1.5;"><strong>模組五：立體多面體・空間裁縫</strong>（柱錐展開圖、立體折疊）：柏拉圖多面體角虧、正方體 11 皮爬行法、世足足球截角二十面體、服裝打版省道（Dart）圓錐高 $H=\sqrt{R^2-r^2}$、莫比烏斯環。</p>
        <p style="color: #334155; font-size: 12px; margin: 4px 0; line-height: 1.5;"><strong>模組六：比例透視・中央射影</strong>（相似形、三視圖）：相機中央射影一體論、比薩斜塔借位相似形 $\frac{h}{d}=\frac{H}{D}$、哀悼基督調和平均數透視阻尼、紀念碑谷等角軸測盲區。</p>
        <p style="color: #334155; font-size: 12px; margin: 4px 0; line-height: 1.5;"><strong>模組七：極限碎形・結構力學</strong>（等比規律、吸管搭接）：科赫雪花周長發散面積收斂、巴恩斯利蕨類 IFS、向日葵黃金角 $137.5^\circ$、肥皂泡 $120^\circ$ 極小曲面、三角形桁架剛性。</p>
      </div>
    </div>

    <div class="callout-box" style="background: #f8fafc; border: 1px dashed var(--primary-border); margin: 10px 0;">
      <div class="callout-title" style="color: var(--primary);">★ 「先全放，後面再刪」的題庫蓄水池理念（The Grand Reservoir）</div>
      <div class="callout-content" style="color: #475569;">
        本體系確立**「題庫先行、儲備極大化」**的研發方針。先期將所有能被小學數學加深的跨界題材（目前已聚積 39 案）全景納入儲備池，不急於人為閹割篇幅。章節只是教學與排版的載體，最重要的是給孩子一張橫跨幾何、光學、物理、藝術與程式運算的完整世界觀地圖。後續出版或開課時，可根據不同年段學情靈活剪裁！
      </div>
    </div>

    <div class="page-bottom-footer">
      <span class="footer-left">小學全域：視覺幾何與藝術工程 ｜ 企劃白皮書</span>
      <span class="footer-center">第 6 頁 / 共 24 頁</span>
      <span class="footer-right">woieyufan EDUCATION ｜ 內部專利發行規範</span>
    </div>
  </div>
'''

def get_page_7():
    return r'''
  <!-- PAGE 7: CHAPTER 3 (PART 1): CORE SCIENTIFIC AXIOMS -->
  <div class="section-page">
    <div class="page-top-header">
      <span class="header-left">CORE AXIOMS & HARD SCIENCE ｜ 第三章：核心跨界幾何與硬核科學公理（上）</span>
      <div class="header-right">
        <img class="header-logo-mini" src="__LOGO_DATA_URI__" alt="Mini Logo">
        <span>woieyufan EDUCATION</span>
      </div>
    </div>

    <div class="chapter-header-box">
      <div class="chapter-title">第三章：核心跨界幾何與硬核科學公理</div>
    </div>

    <div class="section-title">3.1 視網膜光學刺激 vs 光譜減法吸光公理（Retinal Stimulation & Absorption）</div>
    <div class="para">
      【小學數學對接：小數百分比換算與四則運算】<br>
      螢幕 RGB 是光源色，分別激發視網膜 S-錐細胞（420nm）、M-錐細胞（530nm）、L-錐細胞（560nm）；印刷 CMYK 是化學染料對色光的減法吸收（青吸紅 625~740nm、洋紅吸綠 500~565nm、黃吸藍 450~485nm）。換算代數方程式如下：
    </div>
    <div class="formula-box">
      $$K = 1 - \max(R', G', B'), \quad C = \frac{1 - R' - K}{1 - K}, \quad M = \frac{1 - G' - K}{1 - K}, \quad Y = \frac{1 - B' - K}{1 - K}$$
    </div>

    <div class="section-title">3.2 莫內互補色陰影的大氣天光散射與側抑制公理（Rayleigh & Lateral Inhibition）</div>
    <div class="para">
      【小學數學對接：平角 $180^\circ$、色相環對面】<br>
      日光（暖黃 580nm）直射被阻擋的陰影區，受到大氣分子瑞立散射（$\propto 1/\lambda^4$）的天光藍（450nm）漫射照亮；同時人類視網膜中心-周圍拮抗產生側向抑制，神經系統自動誘導對立互補色相。大師塗相反色是客觀物理與神經感官的雙重必然：
    </div>
    <div class="formula-box">
      $$\theta_{\text{shadow}} = (\theta_{\text{light}} + 180^\circ) \pmod{360^\circ}$$
    </div>

    <div class="section-title">3.3 笛卡兒頂點角虧與曲率成錐公理（Angular Defect & Conical Curvature）</div>
    <div class="para">
      【小學數學對接：正多邊形內角相加、柱錐展開圖】<br>
      平面高斯曲率 $K=0$。立體角閉合頂點內角和必須嚴格小於 $360^\circ$，代數窮舉正多邊形組合證明凸正多面體有且僅有 5 種；平面布料穿在人體身上剪掉的角虧省道（Dart）$\Delta\theta$，決定底圓半徑與人體立體隆起高度：
    </div>
    <div class="formula-box">
      $$r = R \cdot \frac{360^\circ - \Delta\theta}{360^\circ}, \quad H = \sqrt{R^2 - r^2}$$
    </div>

    <div class="page-bottom-footer">
      <span class="footer-left">小學全域：視覺幾何與藝術工程 ｜ 企劃白皮書</span>
      <span class="footer-center">第 7 頁 / 共 24 頁</span>
      <span class="footer-right">woieyufan EDUCATION ｜ 內部專利發行規範</span>
    </div>
  </div>
'''

def get_page_8():
    return r'''
  <!-- PAGE 8: CHAPTER 3 (PART 2): PROJECTION, GEARS & FRACTALS -->
  <div class="section-page">
    <div class="page-top-header">
      <span class="header-left">CORE AXIOMS & HARD SCIENCE ｜ 第三章：核心跨界幾何與硬核科學公理（下）</span>
      <div class="header-right">
        <img class="header-logo-mini" src="__LOGO_DATA_URI__" alt="Mini Logo">
        <span>woieyufan EDUCATION</span>
      </div>
    </div>

    <div class="chapter-header-box">
      <div class="chapter-title">第三章：核心跨界幾何與硬核科學公理（續）</div>
    </div>

    <div class="section-title">3.4 中央射影與相機視錐光學一體公理（Central Projection & Lens Optics）</div>
    <div class="para">
      【小學數學對接：相似三角形、反比除法、調和平均數】<br>
      相機焦點與畫家視點在幾何上完全等價。視錐截線 AAA 相似形方程式決定借位拍照站位；透視縱深地磚間距呈調和級數收縮 $z \propto \frac{1}{Z}$，調和平均數構成透視非線性阻尼，破解曼特尼亞《哀悼基督》的空間修正：
    </div>
    <div class="formula-box">
      $$\frac{h}{d} = \frac{H}{D}, \quad H_{\text{harmonic}} = \frac{2ab}{a+b}$$
    </div>

    <div class="section-title">3.5 模運算閉合與齒輪傳動比公理（Modular Arithmetic & Spirograph LCM）</div>
    <div class="para">
      【小學數學對接：除法餘數、最大公因數 $\gcd$、最小公倍數 $\text{lcm}$】<br>
      施萊夫利符號 $\{n/k\}$ 在 $\gcd(n,k)=1$ 時一筆畫閉合成正星形，$\gcd(n,k)=d>1$ 時分裂為 $d$ 個交疊多邊形；萬花尺內外齒輪嚙合，花瓣數與閉合旋轉圈數由最小公倍數唯一鎖死：
    </div>
    <div class="formula-box">
      $$P = \frac{R}{\gcd(R,r)}, \quad N_{\text{laps}} = \frac{\text{lcm}(R,r)}{R} = \frac{r}{\gcd(R,r)}$$
    </div>

    <div class="section-title">3.6 碎形自相似與等比數列無窮極限公理（Fractal Dimension & Infinite Limits）</div>
    <div class="para">
      【小學數學對接：等邊三角形周長與面積、乘法規律數列】<br>
      科赫雪花每次迭代邊長乘 $\frac{1}{3}$、邊數乘 4，總周長按等比數列趨向無窮大；而面積收斂至有限極限。證明有限紙張內可包容無限周長，揭示海岸線、浪花與蕨類生長的碎形本質：
    </div>
    <div class="formula-box">
      $$P_n = 3 \cdot \left(\frac{4}{3}\right)^n \to \infty, \quad S_\infty = \frac{8}{5} S_0$$
    </div>

    <div class="page-bottom-footer">
      <span class="footer-left">小學全域：視覺幾何與藝術工程 ｜ 企劃白皮書</span>
      <span class="footer-center">第 8 頁 / 共 24 頁</span>
      <span class="footer-right">woieyufan EDUCATION ｜ 內部專利發行規範</span>
    </div>
  </div>
'''
