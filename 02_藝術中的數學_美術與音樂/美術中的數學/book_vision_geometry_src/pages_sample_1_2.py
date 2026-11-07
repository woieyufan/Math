# -*- coding: utf-8 -*-
"""
Sample Chapters 1 & 2 (Pages 4 to 7) for
《看見幾何：從寫字、拍照、剪衣服到文藝復興名畫的視覺解密》

Page 4-5: Sample Chapter 1 (TOC Ch 01) - 寫字也是算幾何？漢字九宮格坐標系與不倒翁重心
Page 6-7: Sample Chapter 2 (TOC Ch 03) - 時鐘上的流星雨：除法餘數、互質與一筆畫五角星
"""

def get_page_4():
    return r'''
  <!-- PAGE 4: CHAPTER 01 (SPREAD LEFT) -->
  <div class="section-page">
    <div class="page-top-header">
      <span class="header-left">VOL 1 ｜ CHAPTER 01：寫字也是算幾何？（PART 1）</span>
      <div class="header-right">
        <img class="header-logo-mini" src="__LOGO_DATA_URI__" alt="Mini Logo">
        <span>woieyufan BOOKS</span>
      </div>
    </div>

    <div class="chapter-header-box">
      <div class="chapter-tag">CASE FILE #01 ｜ 平面坐標與筆尖</div>
      <div class="chapter-title">寫字也是算幾何？書法家是隱藏的幾何學家</div>
      <div class="para">
        當你讀小學第一天坐進教室，老師發給你的第一本生字簿，上面印的一定是紅色的<strong>「田字格」</strong>或<strong>「米字格」</strong>。長大一點去書法班，老師又會給你一張大大的<strong>「九宮格」</strong>紙。你有沒有想過：為什麼老祖宗不給我們一張乾淨無瑕的白紙，非要用八條線把一個正方形切成九個格子？難道寫書法不是隨性抒發情感的文人遊戲，而是一場錙銖必較的「平面坐標計算」嗎？
      </div>
    </div>

    <!-- MYSTERY BOX -->
    <div class="mystery-box">
      <div class="mystery-title">
        <span>🔍 視覺懸案：為什麼明明筆畫歪斜，整座字卻「穩如泰山」？</span>
      </div>
      <div class="mystery-desc">
        看唐代楷書四大家之首歐陽詢寫的《九成宮醴泉銘》中的「戈」字或「成」字，那一筆長長的斜鉤（戈勾）筆鋒極端傾斜，如果它是一根柱子，早就該轟然傾倒了！但奇怪的是，任何一個懂美感的人站在石碑前，都會覺得這個字剛勁挺拔、巍然屹立。書法大師在無意識間，到底動用了什麼神奇的力學與幾何天平？
      </div>
    </div>

    <!-- SVG VISUAL DEMO -->
    <div class="card-pane" style="text-align: center; margin-bottom: 8px; padding: 6px 12px; background: #f8fafc;">
      <svg width="100%" height="140" viewBox="0 0 600 140" xmlns="http://www.w3.org/2000/svg" style="max-width: 580px;">
        <!-- Left: Nine-Fold Grid Coordinates -->
        <g transform="translate(15, 8)">
          <rect x="0" y="0" width="265" height="122" fill="#fefce8" rx="6" stroke="#fef08a"/>
          <text x="132" y="16" text-anchor="middle" font-size="10.5" font-weight="bold" fill="#854d0e">九宮格：世界上最早的平面直角坐標系</text>
          
          <!-- Nine Grid Box -->
          <g transform="translate(80, 22)">
            <rect x="0" y="0" width="105" height="84" fill="#ffffff" stroke="#b45309" stroke-width="1.5"/>
            <!-- Grid Lines -->
            <line x1="35" y1="0" x2="35" y2="84" stroke="#f59e0b" stroke-dasharray="2,2"/>
            <line x1="70" y1="0" x2="70" y2="84" stroke="#f59e0b" stroke-dasharray="2,2"/>
            <line x1="0" y1="28" x2="105" y2="28" stroke="#f59e0b" stroke-dasharray="2,2"/>
            <line x1="0" y1="56" x2="105" y2="56" stroke="#f59e0b" stroke-dasharray="2,2"/>
            <!-- Center Cross Point (Origin) -->
            <circle cx="52.5" cy="42" r="3.5" fill="#dc2626"/>
            <text x="56" y="38" font-size="8" fill="#dc2626" font-weight="bold">原點 (0,0)</text>
          </g>

          <text x="132" y="115" text-anchor="middle" font-size="8.5" fill="#78350f">歐陽詢發明「九宮格」，本質是笛卡兒二維直角坐標網格！</text>
        </g>

        <!-- Right: Physics Center of Gravity in Character '永' -->
        <g transform="translate(305, 8)">
          <rect x="0" y="0" width="280" height="122" fill="#f1f5f9" rx="6" stroke="#cbd5e1"/>
          <text x="140" y="16" text-anchor="middle" font-size="10.5" font-weight="bold" fill="#1e293b">漢字「永」的幾何重心（Center of Mass）平衡</text>

          <!-- Character 'Yong' vector representation -->
          <g transform="translate(87, 22)">
            <rect x="0" y="0" width="105" height="84" fill="#ffffff" stroke="#94a3b8" stroke-width="1"/>
            <!-- Center of Mass crosshairs -->
            <line x1="52.5" y1="0" x2="52.5" y2="84" stroke="#e2e8f0"/>
            <line x1="0" y1="42" x2="105" y2="42" stroke="#e2e8f0"/>
            
            <!-- Strokes of 永 -->
            <ellipse cx="52.5" cy="16" rx="5" ry="3.5" fill="#0f172a"/>
            <path d="M 25,28 L 75,28 Q 80,28 80,34 L 78,44" fill="none" stroke="#0f172a" stroke-width="4.5" stroke-linecap="round"/>
            <path d="M 52.5,28 L 52.5,76 L 40,70" fill="none" stroke="#0f172a" stroke-width="5" stroke-linecap="round"/>
            <path d="M 25,50 L 45,40" fill="none" stroke="#0f172a" stroke-width="3.5" stroke-linecap="round"/>
            <path d="M 45,50 L 20,74" fill="none" stroke="#0f172a" stroke-width="4" stroke-linecap="round"/>
            <path d="M 60,40 L 85,72" fill="none" stroke="#0f172a" stroke-width="5" stroke-linecap="round"/>

            <!-- Center of Gravity Spot -->
            <circle cx="53" cy="42" r="4" fill="#e11d48"/>
            <circle cx="53" cy="42" r="7.5" fill="none" stroke="#e11d48" stroke-width="1.2" stroke-dasharray="2,2"/>
          </g>

          <text x="140" y="115" text-anchor="middle" font-size="8.5" fill="#334155">墨跡質量力矩總和 $\sum \vec{r}_i m_i = 0$：漢字有「不倒翁」力學中心</text>
        </g>
      </svg>
    </div>

    <!-- WORKSHOP BOX -->
    <div class="workshop-box">
      <div class="workshop-title">
        <span>🛠️ 親手解剖：用剪刀和針線找出漢字的「物理重心」</span>
      </div>
      <div class="workshop-steps">
        <ol>
          <li><strong>準備厚卡紙：</strong>在一張 $10 \times 10\text{ cm}$ 的厚紙板上，用粗奇異筆寫一個大大的「木」字。</li>
          <li><strong>精確剪出字形：</strong>用美工刀將「木」字沿著黑墨邊緣完整刻下來，形成一個獨立的鏤空紙片。</li>
          <li><strong>懸掛吊針法：</strong>在十字交叉處刺一個小孔穿過細線懸掛，你會發現——<strong>整個「木」字竟然水平懸空在半空中，既不往左傾，也不往右翻！</strong></li>
          <li><strong>小學數學工具解密：</strong>寫字時大腦每秒都在計算數對 $(x, y)$ 的加權平均數，這叫動態力矩平衡！</li>
        </ol>
      </div>
    </div>
  </div>
'''

def get_page_5():
    return r'''
  <!-- PAGE 5: CHAPTER 01 (SPREAD RIGHT) -->
  <div class="section-page">
    <div class="page-top-header">
      <span class="header-left">VOL 1 ｜ CHAPTER 01：寫字也是算幾何？（PART 2）</span>
      <div class="header-right">
        <img class="header-logo-mini" src="__LOGO_DATA_URI__" alt="Mini Logo">
        <span>woieyufan BOOKS</span>
      </div>
    </div>

    <div class="chapter-header-box">
      <div class="chapter-tag">MATHEMATICAL ENGINE ｜ 幾何引擎</div>
      <div class="chapter-title">數對坐標與質量矩：書法字體美感的定量方程式</div>
    </div>

    <!-- ENGINE BOX -->
    <div class="engine-box">
      <div class="engine-title">
        <span>⚙️ 小學核心數學工具：平面數對 $(x, y)$ 與二維質心平衡公式</span>
      </div>
      <div class="engine-desc">
        在小學四年級，我們學會了用數對 $(x, y)$ 來定位方格紙上的點。在九宮格中，中心交點就是原點 $(0,0)$。<br>
        如果漢字由 $n$ 個墨跡筆劃微元組成，每個點坐標為 $(x_i, y_i)$，面積為 $m_i$，整座字的<strong>幾何重心 $(\bar{X}, \bar{Y})$</strong> 嚴格滿足：
        $$\bar{X} = \frac{\sum_{i=1}^n m_i x_i}{\sum_{i=1}^n m_i}, \quad \bar{Y} = \frac{\sum_{i=1}^n m_i y_i}{\sum_{i=1}^n m_i}$$
        一幅字之所以耐看，是因為書法大師巧妙讓重心 $\bar{X}$ 嚴格落在中心中軸線（$X=0$）正負 $2\%$ 容差內！
      </div>
    </div>

    <!-- NUMERICAL EXPERIMENT TABLE -->
    <div style="margin-bottom: 8px;">
      <table class="doc-table">
        <thead>
          <tr>
            <th style="width: 22%;">漢字結構力學</th>
            <th style="width: 28%;">幾何數學原理</th>
            <th style="width: 24%;">書法代表碑帖</th>
            <th style="width: 26%;">視覺美學效果</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>中宮緊收，四肢舒展</strong></td>
            <td>質心處墨跡密度極高<br>四周筆劃向外延伸半徑極大</td>
            <td>歐陽詢《九成宮醴泉銘》</td>
            <td>像芭蕾舞者收緊核心轉圈，極具張力與精神</td>
          </tr>
          <tr>
            <td><strong>黃金分割主橫 (0.618)</strong></td>
            <td>主筆橫劃不落在 $50\%$ 正中<br>而是落在 $61.8\%$ 黃金分割點</td>
            <td>柳公權《玄秘塔碑》</td>
            <td>避免「上下均分」的死板呆滯，視覺輕盈優雅</td>
          </tr>
          <tr>
            <td><strong>計白當黑 (布白均勻)</strong></td>
            <td>封閉白色多邊形區域<br>面積方差 $\sigma^2 \to 0$ 最小化</td>
            <td>顏真卿《多寶塔碑》</td>
            <td>字體內部的虛空間均勻呼吸，寬博大氣</td>
          </tr>
        </tbody>
      </table>
    </div>

    <div class="card-pane" style="margin-bottom: 8px; background: #f0fdf4; border-left: 4px solid var(--emerald);">
      <div style="font-weight: 800; color: #166534; font-size: 11.5px; margin-bottom: 3px;">歐陽詢《三十六法》：中國古代的計算幾何演算法</div>
      <div style="font-size: 10.5px; color: #14532d; line-height: 1.5;">
        一千多年前，歐陽詢寫下「避就、排疊、穿插、向背」。用現代計算機圖形學翻譯，這些全都是<strong>「排斥力向量場（Repulsive Potential Field）」</strong>！相鄰筆劃不能碰撞，長劃要為短劃讓出安全距離，多條平行線等距排疊——古代書法家，其實是第一代手動演算的坐標演算法工程師！
      </div>
    </div>

    <!-- MASTER'S SECRET BOX -->
    <div class="secret-box">
      <div class="secret-title">
        <span>🔑 大師暗門：數位字體設計師的 1000×1000 向量坐標網格</span>
      </div>
      <div class="secret-desc">
        今天你在手機上看到的「蘋方黑體」或「微軟正黑體」，在字型軟體中都是由標準的 $1000 \times 1000$ 單位 Em-Square 坐標系定義的。字型設計師用貝茲曲線控制點坐標微調重心高低。小學的九宮格，就是這套掌控數位排版的幾何系統起點！
      </div>
    </div>

    <div style="margin-top: 8px; padding: 6px 12px; background: #eff6ff; border: 1px dashed #3b82f6; border-radius: 5px; font-size: 10px; color: #1d4ed8;">
      <strong>💡 書法幾何探案小作業：</strong>翻開國語課本找到「月」字和「夕」字。「月」字方正對稱，重心在正中；而「夕」字只有左下方有筆劃，右上方全是空白！仔細看設計師怎麼寫「夕」字最後那一筆點——是不是寫得特別厚重、往右下角延伸？那就是在為傾斜的重心增加「力矩（Torque）」平衡！
    </div>
  </div>
'''

def get_page_6():
    return r'''
  <!-- PAGE 6: CHAPTER 03 (SPREAD LEFT) -->
  <div class="section-page">
    <div class="page-top-header">
      <span class="header-left">VOL 1 ｜ CHAPTER 03：時鐘上的流星雨（PART 1）</span>
      <div class="header-right">
        <img class="header-logo-mini" src="__LOGO_DATA_URI__" alt="Mini Logo">
        <span>woieyufan BOOKS</span>
      </div>
    </div>

    <div class="chapter-header-box">
      <div class="chapter-tag">CASE FILE #03 ｜ 除法餘數與星形多邊形</div>
      <div class="chapter-title">時鐘上的流星雨：除法餘數、互質與一筆畫五角星</div>
      <div class="para">
        每個人小時候都曾在筆記本空白處畫過一顆美麗的<strong>「五角星」</strong>——筆尖落在紙上，刷刷刷五筆一氣呵成，一秒鐘連回起點，既流暢又神奇！但是，當你試著用同樣的方法畫一顆<strong>「六角星（大衛之星）」</strong>時，你會震驚地發現：<strong>你永遠不可能一筆畫連完六角星！</strong>你畫了三筆就會撞回原點卡死，必須把筆抬起來，在另一處重新畫一個倒三角！為什麼五角星能一筆畫到底，六角星卻會被殘酷「腰斬」？
      </div>
    </div>

    <!-- MYSTERY BOX -->
    <div class="mystery-box">
      <div class="mystery-title">
        <span>🔍 視覺懸案：誰在暗中操控星星的筆尖軌跡？</span>
      </div>
      <div class="mystery-desc">
        把圓周均分成 5 個點或 6 個點，每次跳 2 步連線。五角星是 $0 \to 2 \to 4 \to 1 \to 3 \to 0$ 一筆畫穿越所有頂點；而六角星卻是 $0 \to 2 \to 4 \to 0$ 提早封閉！這根本不是巧合，而是小學除法算術裡最深奧的秘密：<strong>除法留下來的「餘數」，正在圓形時鐘上跳舞！</strong>
      </div>
    </div>

    <!-- SVG VISUAL DEMO -->
    <div class="card-pane" style="text-align: center; margin-bottom: 8px; padding: 6px 12px; background: #f8fafc;">
      <svg width="100%" height="140" viewBox="0 0 600 140" xmlns="http://www.w3.org/2000/svg" style="max-width: 580px;">
        <!-- Left: Five-pointed Star {5/2} Coprime -->
        <g transform="translate(20, 8)">
          <rect x="0" y="0" width="260" height="122" fill="#fff7ed" rx="6" stroke="#fed7aa"/>
          <text x="130" y="16" text-anchor="middle" font-size="10.5" font-weight="bold" fill="#c2410c">五角星 {5/2}：5 與 2 互質 ➜ 一筆畫貫穿！</text>
          
          <!-- Circle Clock with 5 points -->
          <g transform="translate(130, 65)">
            <circle cx="0" cy="0" r="42" fill="#fff" stroke="#fdba74" stroke-dasharray="2,2"/>
            <!-- 5 Points (Angles: -90, -18, 54, 126, 198) -->
            <!-- Path of 5-star: 0 -> 2 -> 4 -> 1 -> 3 -> 0 -->
            <polygon points="0,-40 38,27 -38,-12 38,-12 -38,27" fill="rgba(249, 115, 22, 0.15)" stroke="#ea580c" stroke-width="2"/>
            <!-- Dots -->
            <circle cx="0" cy="-40" r="3" fill="#ea580c"/>
            <text x="0" y="-44" text-anchor="middle" font-size="7.5" fill="#c2410c" font-weight="bold">點0</text>
            <circle cx="38" cy="-12" r="3" fill="#ea580c"/>
            <text x="46" y="-12" text-anchor="start" font-size="7.5" fill="#c2410c">點1</text>
            <circle cx="23" cy="33" r="3" fill="#ea580c"/>
            <text x="28" y="38" text-anchor="start" font-size="7.5" fill="#c2410c">點2</text>
            <circle cx="-23" cy="33" r="3" fill="#ea580c"/>
            <text x="-30" y="38" text-anchor="end" font-size="7.5" fill="#c2410c">點3</text>
            <circle cx="-38" cy="-12" r="3" fill="#ea580c"/>
            <text x="-44" y="-12" text-anchor="end" font-size="7.5" fill="#c2410c">點4</text>
          </g>
          <text x="130" y="116" text-anchor="middle" font-size="8.5" fill="#9a3412">gcd(5, 2) = 1（互質）：步步留下不重複餘數，一筆畫完成</text>
        </g>

        <!-- Right: Six-pointed Star {6/2} Non-Coprime -->
        <g transform="translate(310, 8)">
          <rect x="0" y="0" width="270" height="122" fill="#eff6ff" rx="6" stroke="#bfdbfe"/>
          <text x="135" y="16" text-anchor="middle" font-size="10.5" font-weight="bold" fill="#1e40af">六角星 {6/2}：gcd(6, 2) = 2 ➜ 分裂為 2 個三角形！</text>

          <!-- Circle Clock with 6 points -->
          <g transform="translate(135, 65)">
            <circle cx="0" cy="0" r="42" fill="#fff" stroke="#93c5fd" stroke-dasharray="2,2"/>
            <!-- Triangle 1: 0 -> 2 -> 4 -> 0 -->
            <polygon points="0,-40 34.6,20 -34.6,20" fill="rgba(37, 99, 235, 0.15)" stroke="#2563eb" stroke-width="2"/>
            <!-- Triangle 2: 1 -> 3 -> 5 -> 1 -->
            <polygon points="34.6,-20 0,40 -34.6,-20" fill="rgba(239, 68, 68, 0.15)" stroke="#dc2626" stroke-width="2" stroke-dasharray="3,2"/>
            <!-- Labels -->
            <circle cx="0" cy="-40" r="3" fill="#2563eb"/>
            <text x="0" y="-44" text-anchor="middle" font-size="7.5" fill="#1e40af" font-weight="bold">點0</text>
            <circle cx="34.6" cy="-20" r="3" fill="#dc2626"/>
            <text x="42" y="-20" text-anchor="start" font-size="7.5" fill="#b91c1c" font-weight="bold">點1(抬筆)</text>
          </g>
          <text x="135" y="116" text-anchor="middle" font-size="8.5" fill="#1e3a8a">gcd(6, 2) = 2（公因數為2）：必分裂為 2 個封閉正三角形</text>
        </g>
      </svg>
    </div>

    <!-- WORKSHOP BOX -->
    <div class="workshop-box">
      <div class="workshop-title">
        <span>🛠️ 親手解剖：拿起 12 小時的時鐘圓盤做「除法跳步實驗」</span>
      </div>
      <div class="workshop-steps">
        <ol>
          <li><strong>畫一個時鐘：</strong>在白紙上用圓規畫一個圓，標上 1 到 12 的時鐘刻度（把 12 點當作 0）。</li>
          <li><strong>實驗一（跳 5 步）：</strong>從 0 點出發，每次順時針走 5 小時連線：$0 \to 5 \to 10 \to 3 \to 8 \to 1 \to 6 \dots$ 你會驚喜地畫出一顆<strong>完美的十二角星，而且一筆畫連完 12 個點！</strong>因為 $\gcd(12, 5) = 1$！</li>
          <li><strong>實驗二（跳 4 步）：</strong>從 0 點出發，每次跳 4 小時：$0 \to 4 \to 8 \to 0$。天啊！才三筆就撞回原點變成正三角形！因為 $\gcd(12, 4) = 4$，它分裂成了 4 個獨立三角形！</li>
        </ol>
      </div>
    </div>
  </div>
'''

def get_page_7():
    return r'''
  <!-- PAGE 7: CHAPTER 03 (SPREAD RIGHT) -->
  <div class="section-page">
    <div class="page-top-header">
      <span class="header-left">VOL 1 ｜ CHAPTER 03：時鐘上的流星雨（PART 2）</span>
      <div class="header-right">
        <img class="header-logo-mini" src="__LOGO_DATA_URI__" alt="Mini Logo">
        <span>woieyufan BOOKS</span>
      </div>
    </div>

    <div class="chapter-header-box">
      <div class="chapter-tag">MATHEMATICAL ENGINE ｜ 幾何引擎</div>
      <div class="chapter-title">模運算與最大公因數：主宰全宇宙星形的生死算式</div>
    </div>

    <!-- ENGINE BOX -->
    <div class="engine-box">
      <div class="engine-title">
        <span>⚙️ 小學核心數學工具：除法餘數（同餘運算）與互質定理（Coprime Theorem）</span>
      </div>
      <div class="engine-desc">
        在圓周上平均分佈 $n$ 個頂點，每次跳躍步長為 $k$。每次落點坐標為當前點數加 $k$ 後<strong>除以 $n$ 的「餘數」</strong>：
        $$\text{新落點} = (x + k) \pmod n \iff x_{\text{新}} = (x + k) - n \cdot q$$
        數學家施萊夫利（Schläfli）將這種星形記為 $\{n/k\}$。<strong>最大公因數定理：</strong><br>
        1. 若 $\gcd(n, k) = 1$（$n$ 與 $k$ 互質），軌跡必然遍歷全體 $n$ 個頂點，形成<strong>一筆畫正星形</strong>！<br>
        2. 若 $\gcd(n, k) = d > 1$，軌跡必在 $n/d$ 步後提早撞回起點，退化為 <strong>$d$ 個獨立多邊形複合交疊</strong>！
      </div>
    </div>

    <!-- NUMERICAL EXPERIMENT TABLE -->
    <div style="margin-bottom: 8px;">
      <table class="doc-table">
        <thead>
          <tr>
            <th style="width: 20%;">頂點數與步長</th>
            <th style="width: 26%;">最大公因數 $\gcd(n, k)$</th>
            <th style="width: 26%;">除法餘數運算特徵</th>
            <th style="width: 28%;">視覺幾何成果與代表象徵</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>$\{5/2\}$ 五角星</strong></td>
            <td>$\gcd(5, 2) = 1$（互質）</td>
            <td>餘數軌跡：$0, 2, 4, 1, 3, 0$</td>
            <td><strong>一筆畫五角星</strong> ｜ 中華民國國徽、美國國旗</td>
          </tr>
          <tr>
            <td><strong>$\{6/2\}$ 六角星</strong></td>
            <td>$\gcd(6, 2) = \mathbf{2}$（不互質）</td>
            <td>第 3 步餘數撞零：$0, 2, 4, 0$</td>
            <td><strong>2 個正三角形交疊</strong> ｜ 以色列國旗大衛之星</td>
          </tr>
          <tr>
            <td><strong>$\{8/2\}$ 八角星</strong></td>
            <td>$\gcd(8, 2) = \mathbf{2}$（不互質）</td>
            <td>分裂為 2 個步長為 4 的迴路</td>
            <td><strong>2 個正方形交疊</strong> ｜ 伊斯蘭幾何八角星 (۞)</td>
          </tr>
          <tr>
            <td><strong>$\{8/3\}$ 尖銳八角星</strong></td>
            <td>$\gcd(8, 3) = 1$（互質）</td>
            <td>餘數：$0, 3, 6, 1, 4, 7, 2, 5, 0$</td>
            <td><strong>一筆畫超尖銳八角星</strong> ｜ 羅盤星象圖</td>
          </tr>
        </tbody>
      </table>
    </div>

    <div class="card-pane" style="margin-bottom: 8px; background: #fffbeb; border-left: 4px solid var(--gold);">
      <div style="font-weight: 800; color: #92400e; font-size: 11.5px; margin-bottom: 3px;">為什麼國旗上的星星絕大多數是「五角星」？</div>
      <div style="font-size: 10.5px; color: #78350f; line-height: 1.5;">
        因為 5 是最小的奇數質數！$n=5$ 的時候，步長 $k=2$ 自然與 5 互質。五角星是幾何學中結構最簡潔、最穩定的一筆畫星形。五角星每一條線段相交處，恰好被彼此切成 $\frac{\sqrt{5}-1}{2} \approx 0.618$ 的<strong>黃金分割比</strong>！小學的除法餘數，在此刻與宇宙最美黃金比完美相遇。
      </div>
    </div>

    <!-- MASTER'S SECRET BOX -->
    <div class="secret-box">
      <div class="secret-title">
        <span>🔑 大師暗門：從餘數加法到「模乘法心臟線（Cardioid）」</span>
      </div>
      <div class="secret-desc">
        如果在時鐘上我們不跳步加法，而是做乘法表：把每個點 $x$ 連線到 $2x \pmod{60}$（取除以 60 的餘數），你會被眼前的畫面震撼到說不出話來——幾十條直尺線條交織在一起，圓圈中心竟然不可思議地浮現出了一條光滑極致的<strong>「心臟線（Cardioid）」</strong>！這正是陽光照進圓形馬克杯咖啡表面時，浮現的光斑包絡線！
      </div>
    </div>

    <div style="margin-top: 8px; padding: 6px 12px; background: #ecfdf5; border: 1px dashed #10b981; border-radius: 5px; font-size: 10px; color: #047857;">
      <strong>💡 今日小小數學家挑戰：</strong>找一張空白圓形紙盤，點上 7 個等距刻度（0 到 6）。因為 7 是質數，它和 2、3 都互質！試著分別用步長 2（$\{7/2\}$）和步長 3（$\{7/3\}$）連線，你會畫出兩種完全不同銳度的七角星！澳洲國旗上的聯邦之星，就是由此誕生的！
    </div>
  </div>
'''
