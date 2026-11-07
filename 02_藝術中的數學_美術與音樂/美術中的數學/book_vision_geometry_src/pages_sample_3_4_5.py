# -*- coding: utf-8 -*-
"""
Sample Chapters 3, 4 & 5 (Pages 8 to 13) for
《看見幾何：從寫字、拍照、剪衣服到文藝復興名畫的視覺解密》

Page 8-9: Sample Chapter 3 (TOC Ch 17) - 推倒比薩斜塔！相似三角形借位攝影方程
Page 10-11: Sample Chapter 4 (TOC Ch 13) - 打版師的幾何剪刀：衣服省道、圓錐與角虧
Page 12-13: Sample Chapter 5 (TOC Ch 22) - 躺著的巨人：曼特尼亞《哀悼基督》與調和平均數
"""

def get_page_8():
    return r'''
  <!-- PAGE 8: CHAPTER 17 (SPREAD LEFT) -->
  <div class="section-page">
    <div class="page-top-header">
      <span class="header-left">VOL 4 ｜ CHAPTER 17：推倒比薩斜塔！（PART 1）</span>
      <div class="header-right">
        <img class="header-logo-mini" src="__LOGO_DATA_URI__" alt="Mini Logo">
        <span>woieyufan BOOKS</span>
      </div>
    </div>

    <div class="chapter-header-box">
      <div class="chapter-tag">CASE FILE #17 ｜ 鏡頭光影與透視大案</div>
      <div class="chapter-title">推倒比薩斜塔！攝影師的「相似三角形」借位懸案</div>
      <div class="para">
        在義大利比薩奇蹟廣場上，每天都有成千上萬名遊客做出滑稽的姿勢：有人側身雙手使勁往前推，有人伸出食指捏住半空中。而在他們的相機螢幕裡，出現了一個不可思議的畫面——<strong>身高 1.4 公尺的小學生，竟然用兩根手指輕鬆捏住了高達 56 公尺、重達 14,000 噸的千年中世紀鐘樓！</strong>為什麼一個普通人能在照片裡瞬間變成「頂天立地的巨靈神」？
      </div>
    </div>

    <!-- MYSTERY BOX -->
    <div class="mystery-box">
      <div class="mystery-title">
        <span>🔍 視覺懸案：三維空間被相機「拍扁」時，遺失了什麼重要信息？</span>
      </div>
      <div class="mystery-desc">
        真實世界有長、寬、高三個維度（$X, Y, Z$）。但是，不論是相機的感光元件、你的手機螢幕，還是古代畫家的畫布，都只是<strong>「二維平面（Flat 2D）」</strong>！相機的小孔成像透鏡，把來自遠處的光線匯聚於一點。在這個過程中，物體離鏡頭的「深度距離 $Z$」被強制抹平了——在二維照片上，距離鏡頭 30 公分的手掌，和距離鏡頭 100 公尺的大塔，共享完全相同的成像截面！
      </div>
    </div>

    <!-- SVG VISUAL DEMO -->
    <div class="card-pane" style="text-align: center; margin-bottom: 8px; padding: 6px 12px; background: #f8fafc;">
      <svg width="100%" height="140" viewBox="0 0 600 140" xmlns="http://www.w3.org/2000/svg" style="max-width: 580px;">
        <g transform="translate(10, 8)">
          <rect x="0" y="0" width="580" height="122" fill="#f0fdf4" rx="6" stroke="#bbf7d0"/>
          
          <!-- Camera / Eye -->
          <circle cx="40" cy="85" r="5" fill="#0284c7"/>
          <text x="40" y="105" text-anchor="middle" font-size="8.5" font-weight="bold" fill="#0369a1">相機透鏡 (O)</text>
          
          <!-- Sight Cone Rays -->
          <line x1="40" y1="85" x2="520" y2="18" stroke="#0284c7" stroke-width="1.6" stroke-dasharray="4,2"/>
          <line x1="40" y1="85" x2="520" y2="105" stroke="#0284c7" stroke-width="1.6"/>

          <!-- Close Hand (Finger) -->
          <line x1="160" y1="85" x2="160" y2="62" stroke="#e11d48" stroke-width="3.5" stroke-linecap="round"/>
          <circle cx="160" cy="62" r="3.5" fill="#e11d48"/>
          <text x="160" y="55" text-anchor="middle" font-size="8.5" font-weight="bold" fill="#9f1239">人手手指 ($h$)</text>
          <text x="160" y="98" text-anchor="middle" font-size="8" fill="#64748b">距離 $d$</text>

          <!-- Far Tower (Pisa) -->
          <g transform="translate(480, 18)">
            <polygon points="10,87 26,87 38,0 22,0" fill="#cbd5e1" stroke="#475569" stroke-width="1.4"/>
            <line x1="14" y1="67" x2="30" y2="67" stroke="#64748b"/>
            <line x1="18" y1="47" x2="34" y2="47" stroke="#64748b"/>
            <line x1="22" y1="27" x2="38" y2="27" stroke="#64748b"/>
          </g>
          <text x="515" y="13" text-anchor="middle" font-size="8.5" font-weight="bold" fill="#334155">比薩斜塔 ($H=56\text{m}$)</text>
          <text x="515" y="116" text-anchor="middle" font-size="8" fill="#64748b">距離 $D=100\text{m}$</text>

          <path d="M 40,85 L 160,62 L 160,85 Z" fill="rgba(225, 29, 72, 0.15)"/>
          <path d="M 40,85 L 510,18 L 510,85 Z" fill="rgba(2, 132, 199, 0.1)"/>
          
          <text x="290" y="42" font-size="10.5" font-weight="bold" fill="#1e3a8a">視錐頂角 $\theta$ 保持一致：$\tan \theta = \frac{h}{d} = \frac{H}{D}$</text>
          <text x="290" y="62" font-size="9" fill="#0f766e">近處小三角形 $\triangle OAB$ 與 遠處大三角形 $\triangle OCD$ 為 AAA 相似形！</text>
        </g>
      </svg>
    </div>

    <!-- WORKSHOP BOX -->
    <div class="workshop-box">
      <div class="workshop-title">
        <span>🛠️ 親手解剖：用一枚 10 元硬幣遮蔽天上的滿月</span>
      </div>
      <div class="workshop-steps">
        <ol>
          <li><strong>準備道具：</strong>一枚直徑 $h \approx 2.6\text{ cm}$ 的十元硬幣。</li>
          <li><strong>等待滿月：</strong>在晴朗的滿月夜，月球直徑高達 $H \approx 3,474,000\text{ 公尺}$，離地球 $D \approx 384,400,000\text{ 公尺}$。</li>
          <li><strong>伸直手臂：</strong>閉上一隻眼睛，單手捏住硬幣移向眼前約 $d \approx 2.87\text{ 公尺}$（或手持一元硬幣於手臂長度）。</li>
          <li><strong>小學數學工具解密：</strong>手裡幾公克的金屬圓片，竟然百分之百完全遮蓋住了宇宙中直徑三千多公里的巨大天體！這就是比例式（Angular Diameter）的本質！</li>
        </ol>
      </div>
    </div>
  </div>
'''

def get_page_9():
    return r'''
  <!-- PAGE 9: CHAPTER 17 (SPREAD RIGHT) -->
  <div class="section-page">
    <div class="page-top-header">
      <span class="header-left">VOL 4 ｜ CHAPTER 17：推倒比薩斜塔！（PART 2）</span>
      <div class="header-right">
        <img class="header-logo-mini" src="__LOGO_DATA_URI__" alt="Mini Logo">
        <span>woieyufan BOOKS</span>
      </div>
    </div>

    <div class="chapter-header-box">
      <div class="chapter-tag">MATHEMATICAL ENGINE ｜ 幾何引擎</div>
      <div class="chapter-title">相似三角形方程：借位攝影師的「空間精算表」</div>
    </div>

    <!-- ENGINE BOX -->
    <div class="engine-box">
      <div class="engine-title">
        <span>⚙️ 小學核心數學工具：比、比例式與相似三角形（AAA 相似定理）</span>
      </div>
      <div class="engine-desc">
        在小學六年級，我們學會了「比與比例尺」：$a:b = c:d \iff \frac{a}{b} = \frac{c}{d}$。<br>
        相機成像是一束以鏡頭為頂點的光線錐。物體在底片上的成像高度，完全由<strong>物體真實尺寸與其到鏡頭距離的比值（視角正切值 $\tan\theta$）</strong>決定：
        $$\frac{h_{\text{手}}}{d_{\text{手}}} = \frac{H_{\text{塔}}}{D_{\text{塔}}} \iff d_{\text{手}} = D_{\text{塔}} \times \frac{h_{\text{手}}}{H_{\text{塔}}}$$
        只要這個等式成立，無論物體的真實物理質量相差幾千萬倍，在二維照片上看來都「一樣大」！
      </div>
    </div>

    <!-- NUMERICAL EXPERIMENT TABLE -->
    <div style="margin-bottom: 8px;">
      <table class="doc-table">
        <thead>
          <tr>
            <th style="width: 22%;">被借位目標</th>
            <th style="width: 26%;">目標數據 ($H, D$)</th>
            <th style="width: 24%;">前景道具 ($h$)</th>
            <th style="width: 28%;">攝影師指令：手伸出的距離 ($d$)</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>比薩斜塔（托塔天王）</strong></td>
            <td>塔高 $56\text{ m}$<br>距離鏡頭 $100\text{ m}$</td>
            <td>手掌垂直張開<br>$h = 18\text{ cm} = 0.18\text{ m}$</td>
            <td>$d = 100 \times \frac{0.18}{56} \approx \mathbf{0.32\text{ m} (32\text{ cm})}$<br>手肘微彎，正好在胸前！</td>
          </tr>
          <tr>
            <td><strong>巴黎艾菲爾鐵塔（捏塔尖）</strong></td>
            <td>塔高 $330\text{ m}$<br>距離鏡頭 $600\text{ m}$</td>
            <td>食指與拇指捏住<br>$h = 4\text{ cm} = 0.04\text{ m}$</td>
            <td>$d = 600 \times \frac{0.04}{330} \approx \mathbf{0.073\text{ m} (7.3\text{ cm})}$<br>手指必須極度貼近相機鏡頭！</td>
          </tr>
          <tr>
            <td><strong>遠處好朋友（踩在腳底）</strong></td>
            <td>身高 $150\text{ cm}$<br>站在後方 $30\text{ m}$ 處</td>
            <td>鞋底長度<br>$h = 25\text{ cm} = 0.25\text{ m}$</td>
            <td>$d = 30 \times \frac{0.25}{1.5} = \mathbf{5.0\text{ m}}$<br>攝影師距離前面拍照者 5 公尺！</td>
          </tr>
        </tbody>
      </table>
    </div>

    <div class="card-pane" style="margin-bottom: 8px; background: #fff1f2; border-left: 4px solid var(--ruby);">
      <div style="font-weight: 800; color: #9f1239; font-size: 11.5px; margin-bottom: 3px;">光學死穴：為什麼有的借位照一眼就「穿幫」？</div>
      <div style="font-size: 10.5px; color: #881337; line-height: 1.5;">
        很多新手拍借位照片失敗，不是因為三角形算錯，而是因為<strong>「景深（Depth of Field）」穿幫</strong>！如果相機開大光圈（如 f/1.8），手指清晰，背景的斜塔卻變成模糊光斑；人腦立刻依據模糊度判定「手指在近處，塔在極遠處」，立體視覺拒絕上當！必須縮小光圈（f/16）才能全景深騙過大腦！
      </div>
    </div>

    <!-- MASTER'S SECRET BOX -->
    <div class="secret-box">
      <div class="secret-title">
        <span>🔑 大師暗門：好萊塢電影的「強迫透視（Forced Perspective）」佈景</span>
      </div>
      <div class="secret-desc">
        在電影《魔戒》中，高大的巫師甘道夫和身材只有一半的哈比人佛羅多並肩坐在一張馬車桌旁聊天。導演彼得·傑克森根本沒有用電腦特效，而是打造了一張<strong>特殊梯形透視桌</strong>！哈比人演員實際坐在甘道夫後方整整 1.2 公尺處，配合超小光圈全景深，大腦被徹底欺騙！
      </div>
    </div>

    <div style="margin-top: 8px; padding: 6px 12px; background: #fefce8; border: 1px dashed #eab308; border-radius: 5px; font-size: 10px; color: #854d0e;">
      <strong>💡 今日相機實戰任務：</strong>拿出手機，找一面白牆或草地。請同伴後退 10 步，你在前排伸出手掌。調整手掌位置，直到手機螢幕裡同伴正好「站在你的掌心」。拍下照片，並用皮尺量出你與相機、同伴與相機的距離，驗算比例是否符合 $\frac{h_1}{d_1} = \frac{h_2}{d_2}$！
    </div>
  </div>
'''

def get_page_10():
    return r'''
  <!-- PAGE 10: CHAPTER 13 (SPREAD LEFT) -->
  <div class="section-page">
    <div class="page-top-header">
      <span class="header-left">VOL 3 ｜ CHAPTER 13：打版師的幾何剪刀（PART 1）</span>
      <div class="header-right">
        <img class="header-logo-mini" src="__LOGO_DATA_URI__" alt="Mini Logo">
        <span>woieyufan BOOKS</span>
      </div>
    </div>

    <div class="chapter-header-box">
      <div class="chapter-tag">CASE FILE #13 ｜ 多面體王國與立體打版</div>
      <div class="chapter-title">打版師的幾何剪刀：衣服如何把平面的布，穿成三維的身體？</div>
      <div class="para">
        當你走進服飾店，看到一件輪廓挺拔的西裝外套或優雅收腰的洋裝時，你有沒有想過：<strong>世界上所有的布料，在織布機上織出來的時候，全都是平平整整的一大張「二維平面（Flat Surface）」！</strong>但是，人體卻是一個布滿凸起與起伏的「三維曲面」——有圓拱的肩膀、鼓起的胸脯與內縮的腰線。裁縫師是怎樣不用膠水、光靠一把剪刀和幾根線，就強迫平坦的布料變成貼合人體的球面的？
      </div>
    </div>

    <!-- MYSTERY BOX -->
    <div class="mystery-box">
      <div class="mystery-title">
        <span>🔍 視覺懸案：如果直接拿一張紙包裹橘子，為什麼必定滿是皺褶？</span>
      </div>
      <div class="mystery-desc">
        試著拿一張平整的 A4 紙緊緊包裹一個圓滾滾的橘子或籃球。你會絕望地發現：無論你多小心，紙張表面必然產生醜陋的隆起和皺褶！偉大的數學家高斯（Gauss）用定理證明：<strong>平面的內蘊曲率為 0，而球面的內蘊曲率為正數；你永遠無法把一個零曲率的平面，在不剪開的前提下無皺貼合到球面上！</strong>
      </div>
    </div>

    <!-- SVG VISUAL DEMO -->
    <div class="card-pane" style="text-align: center; margin-bottom: 8px; padding: 6px 12px; background: #f8fafc;">
      <svg width="100%" height="140" viewBox="0 0 600 140" xmlns="http://www.w3.org/2000/svg" style="max-width: 580px;">
        <!-- Left: Dart Cutting -->
        <g transform="translate(15, 8)">
          <rect x="0" y="0" width="265" height="122" fill="#eff6ff" rx="6" stroke="#bfdbfe"/>
          <text x="132" y="16" text-anchor="middle" font-size="10.5" font-weight="bold" fill="#1e3a8a">步驟一：在二維布料上剪去 V 形缺角（省道）</text>
          
          <rect x="35" y="26" width="195" height="70" fill="#dbeafe" stroke="#3b82f6" stroke-width="1.4" rx="3"/>
          <polygon points="132,26 115,68 149,68" fill="#ef4444" opacity="0.3"/>
          <line x1="132" y1="26" x2="115" y2="68" stroke="#dc2626" stroke-width="1.8"/>
          <line x1="132" y1="26" x2="149" y2="68" stroke="#dc2626" stroke-width="1.8"/>
          <circle cx="132" cy="26" r="3" fill="#dc2626"/>
          <text x="132" y="21" text-anchor="middle" font-size="8" fill="#dc2626" font-weight="bold">頂點 P（胸高點 BP）</text>
          <text x="132" y="58" text-anchor="middle" font-size="8.5" fill="#b91c1c" font-weight="bold">剪除角 $\theta$</text>
          <text x="132" y="112" text-anchor="middle" font-size="8.5" fill="#1e40af">剪除角 $\theta$ 使得頂點周圍的總角度 &lt; 360°</text>
        </g>

        <!-- Right: 3D Cone Emergence -->
        <g transform="translate(310, 8)">
          <rect x="0" y="0" width="275" height="122" fill="#fefce8" rx="6" stroke="#fef08a"/>
          <text x="137" y="16" text-anchor="middle" font-size="10.5" font-weight="bold" fill="#854d0e">步驟二：縫合邊界，平面瞬間「隆起」成立體圓錐！</text>
          
          <ellipse cx="137" cy="92" rx="60" ry="16" fill="#fef3c7" stroke="#d97706" stroke-width="1.4"/>
          <line x1="137" y1="30" x2="77" y2="92" stroke="#d97706" stroke-width="1.4"/>
          <line x1="137" y1="30" x2="197" y2="92" stroke="#d97706" stroke-width="1.4"/>
          <line x1="137" y1="30" x2="137" y2="108" stroke="#dc2626" stroke-width="1.8" stroke-dasharray="3,2"/>
          <circle cx="137" cy="30" r="3.5" fill="#d97706"/>
          <text x="137" y="24" text-anchor="middle" font-size="8" fill="#b45309" font-weight="bold">圓錐頂點（立體空間）</text>
          <text x="145" y="75" text-anchor="start" font-size="8" fill="#dc2626">縫合縫線 (Seam)</text>
          <text x="137" y="114" text-anchor="middle" font-size="8.5" fill="#713f12">角虧定理：消失的角度轉化為隆起高度 $H$</text>
        </g>
      </svg>
    </div>

    <!-- WORKSHOP BOX -->
    <div class="workshop-box">
      <div class="workshop-title">
        <span>🛠️ 親手解剖：10 秒鐘自製「紙上胸省（Bust Dart）」</span>
      </div>
      <div class="workshop-steps">
        <ol>
          <li><strong>畫一個圓：</strong>在一張卡紙上用圓規畫一個半徑 $R = 8\text{ cm}$ 的圓並剪下來。</li>
          <li><strong>切出一個扇形：</strong>從圓心向邊緣畫兩條半徑，夾角剪去一個 $\theta = 45^\circ$ 的小扇形（像切下一小塊披薩）。</li>
          <li><strong>閉合邊界：</strong>用手指拉攏切開的兩條邊，用膠帶黏合。</li>
          <li><strong>小學數學工具解密：</strong>平坦紙片黏合瞬間<strong>轟然隆起成立體圓錐！</strong>因為內角和少於 $360^\circ$，消失的角度逼它只能朝第三維度生長！</li>
        </ol>
      </div>
    </div>
  </div>
'''

def get_page_11():
    return r'''
  <!-- PAGE 11: CHAPTER 13 (SPREAD RIGHT) -->
  <div class="section-page">
    <div class="page-top-header">
      <span class="header-left">VOL 3 ｜ CHAPTER 13：打版師的幾何剪刀（PART 2）</span>
      <div class="header-right">
        <img class="header-logo-mini" src="__LOGO_DATA_URI__" alt="Mini Logo">
        <span>woieyufan BOOKS</span>
      </div>
    </div>

    <div class="chapter-header-box">
      <div class="chapter-tag">MATHEMATICAL ENGINE ｜ 幾何引擎</div>
      <div class="chapter-title">角虧定理與圓錐高度：衣服隆起深度的精密算式</div>
    </div>

    <!-- ENGINE BOX -->
    <div class="engine-box">
      <div class="engine-title">
        <span>⚙️ 小學核心數學工具：內角和、笛卡兒角虧（Angular Defect）與立體高度方程</span>
      </div>
      <div class="engine-desc">
        在平面上，繞著任何一點旋轉一圈是 $360^\circ$。當打版師剪掉角度為 $\theta$ 的扇形缺口（省道）並縫合時，總角度變成了 $360^\circ - \theta$。<br>
        這個「消失的角度」$\theta$ 被稱為<strong>角虧（Angular Defect）</strong>！正是角虧強迫布料在第三維度（$Z$ 軸）拱起：
        $$\text{錐底半徑 } r = R \left(1 - \frac{\theta}{360^\circ}\right), \quad \text{立體拱起高度 } H = \sqrt{R^2 - r^2}$$
        這也是為什麼五大多面體每個頂點內角和必須小於 $360^\circ$（留出角虧）才能成為立體多面體！
      </div>
    </div>

    <!-- NUMERICAL EXPERIMENT TABLE -->
    <div style="margin-bottom: 8px;">
      <table class="doc-table">
        <thead>
          <tr>
            <th style="width: 20%;">省道剪除角 $\theta$</th>
            <th style="width: 25%;">展開剩餘角度</th>
            <th style="width: 25%;">錐底半徑 $r$ ($R=10\text{ cm}$)</th>
            <th style="width: 30%;">立體隆起深度 $H$ 與服裝對應部位</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>$15^\circ$（小省）</strong></td>
            <td>$345^\circ$ ($95.8\%$)</td>
            <td>$9.58\text{ cm}$</td>
            <td>$H \approx 2.86\text{ cm}$ ｜ 輕微弧度（後肩蝴蝶骨斜度）</td>
          </tr>
          <tr>
            <td><strong>$30^\circ$（標準胸省）</strong></td>
            <td>$330^\circ$ ($91.7\%$)</td>
            <td>$9.17\text{ cm}$</td>
            <td>$H \approx 4.00\text{ cm}$ ｜ 標準女裝胸省（罩杯貼合）</td>
          </tr>
          <tr>
            <td><strong>$60^\circ$（大角度省）</strong></td>
            <td>$300^\circ$ ($83.3\%$)</td>
            <td>$8.33\text{ cm}$</td>
            <td>$H \approx 5.53\text{ cm}$ ｜ 高挺隆起（貝雷帽頂、立體肩墊）</td>
          </tr>
          <tr>
            <td><strong>$90^\circ$（直角省）</strong></td>
            <td>$270^\circ$ ($75.0\%$)</td>
            <td>$7.50\text{ cm}$</td>
            <td>$H \approx 6.61\text{ cm}$ ｜ 尖銳小丑帽、露營帳篷頂部</td>
          </tr>
        </tbody>
      </table>
    </div>

    <div class="card-pane" style="margin-bottom: 8px; background: #fdf2f8; border-left: 4px solid var(--ruby);">
      <div style="font-weight: 800; color: #9f1239; font-size: 11.5px; margin-bottom: 3px;">高斯的「絕妙定理」與多面體網格</div>
      <div style="font-size: 10.5px; color: #881337; line-height: 1.5;">
        高斯證明：當一個曲面彎曲但不拉伸時，高斯曲率 $K$ 保持不變！平坦布料 $K=0$。當你把紙捲成圓柱體時高斯曲率仍為 0，所以圓柱體可以被完美攤平；但人體是雙曲面或球形（$K \ne 0$）。裁縫師用剪刀剪出角虧，本質上就是用**「多面體三角網格逼近曲面」**的幾何壯舉！
      </div>
    </div>

    <!-- MASTER'S SECRET BOX -->
    <div class="secret-box">
      <div class="secret-title">
        <span>🔑 大師暗門：打版師的省道旋轉魔法（Dart Manipulation）</span>
      </div>
      <div class="secret-desc">
        高級時裝設計師常常在女裝胸前看不到任何剪痕，難道不用省道嗎？不！他們使用的是<strong>「省道旋轉變換群」</strong>！只要保持頂點（胸高點 BP）不動與總角虧 $\theta$ 不變，打版師可以把腰部省道旋轉轉移到腋下或領口！在數學上這是一次<strong>全等剛體旋轉變換</strong>，外觀變成了時尚褶皺，立體容積分毫不差！
      </div>
    </div>

    <div style="margin-top: 8px; padding: 6px 12px; background: #ecfdf5; border: 1px dashed #34d399; border-radius: 5px; font-size: 10px; color: #065f46;">
      <strong>💡 裁縫師幾何挑戰：</strong>回家觀察你的牛仔褲或運動外套。找找看手肘或膝蓋處是不是也有兩道不起眼的小縫線？量量看它們的角度是不是大約 $10^\circ \sim 15^\circ$？正是這微小的角虧，讓你的手肘在彎曲時不會感到布料緊繃！
    </div>
  </div>
'''

def get_page_12():
    return r'''
  <!-- PAGE 12: CHAPTER 22 (SPREAD LEFT) -->
  <div class="section-page">
    <div class="page-top-header">
      <span class="header-left">VOL 4 ｜ CHAPTER 22：躺著的巨人（PART 1）</span>
      <div class="header-right">
        <img class="header-logo-mini" src="__LOGO_DATA_URI__" alt="Mini Logo">
        <span>woieyufan BOOKS</span>
      </div>
    </div>

    <div class="chapter-header-box">
      <div class="chapter-tag">CASE FILE #22 ｜ 終極壓軸・鏡頭與透視大案</div>
      <div class="chapter-title">躺著的巨人：曼特尼亞《哀悼基督》的透視懸案</div>
      <div class="para">
        當你平躺在沙發上，請朋友站在你的正腳底朝你的頭部拍照——拍出來的照片一定會讓你驚恐大叫：<strong>你的兩隻腳掌巨大如熊掌，直接遮擋了半個胸膛，而你的腦袋小得像一顆彈珠！</strong>這叫「近大遠小」的幾何透視。但在文藝復興名畫《哀悼基督》（Lamentation of Christ）中，大師曼特尼亞也畫了一具正對著觀者躺著的軀體，但為什麼你一眼看去，卻覺得無比神聖莊嚴，絲毫沒有「巨腳怪人」的滑稽感？
      </div>
    </div>

    <!-- MYSTERY BOX -->
    <div class="mystery-box">
      <div class="mystery-title">
        <span>🔍 視覺懸案：如果嚴格按數學幾何透視，這幅畫會徹底崩塌！</span>
      </div>
      <div class="mystery-desc">
        義大利畫家曼特尼亞（Andrea Mantegna, 1431–1506）是透視法的狂熱信徒。但在這幅名畫中，他做了一件極其大膽的「數學背叛」：如果按照光學小孔成像的射線幾何，站在死者腳前 1.5 公尺處觀察，<strong>腳底到眼睛的距離（1.5m）只有頭頂到眼睛距離（3.3m）的一半不到！</strong>腳掌應該比頭顱大上整整 2.2 倍！曼特尼亞到底動了什麼手腳？
      </div>
    </div>

    <!-- SVG VISUAL DEMO -->
    <div class="card-pane" style="text-align: center; margin-bottom: 8px; padding: 6px 12px; background: #f8fafc;">
      <svg width="100%" height="140" viewBox="0 0 600 140" xmlns="http://www.w3.org/2000/svg" style="max-width: 580px;">
        <!-- Left: Rigid geometric perspective -->
        <g transform="translate(10, 8)">
          <rect x="0" y="0" width="270" height="122" fill="#fff1f2" rx="6" stroke="#fecdd3"/>
          <text x="135" y="16" text-anchor="middle" font-size="10.5" font-weight="bold" fill="#9f1239">嚴格剛性幾何透視（真實相機鏡頭）</text>
          
          <circle cx="20" cy="65" r="4.5" fill="#e11d48"/>
          <text x="20" y="80" text-anchor="middle" font-size="8.5" fill="#9f1239">眼睛 (O)</text>
          
          <line x1="20" y1="65" x2="80" y2="30" stroke="#fb7185" stroke-dasharray="3,3"/>
          <line x1="20" y1="65" x2="80" y2="100" stroke="#fb7185" stroke-dasharray="3,3"/>
          <line x1="20" y1="65" x2="240" y2="50" stroke="#fda4af" stroke-dasharray="2,2"/>
          <line x1="20" y1="65" x2="240" y2="80" stroke="#fda4af" stroke-dasharray="2,2"/>
          
          <rect x="80" y="30" width="16" height="70" fill="#e11d48" rx="2"/>
          <text x="88" y="68" text-anchor="middle" font-size="8.5" fill="#fff" font-weight="bold">巨腳</text>
          
          <circle cx="240" cy="65" r="13" fill="#9f1239"/>
          <text x="240" y="68" text-anchor="middle" font-size="7.5" fill="#fff">微型頭顱</text>
          <text x="135" y="114" text-anchor="middle" font-size="8.5" fill="#881337">視覺效果：腳丫遮蔽軀幹，像滑稽矮人</text>
        </g>

        <!-- Right: Mantegna's Dampened Perspective -->
        <g transform="translate(300, 8)">
          <rect x="0" y="0" width="280" height="122" fill="#f0fdf4" rx="6" stroke="#bbf7d0"/>
          <text x="140" y="16" text-anchor="middle" font-size="10.5" font-weight="bold" fill="#166534">曼特尼亞《哀悼基督》的幾何阻尼修正</text>
          
          <circle cx="20" cy="65" r="4.5" fill="#16a34a"/>
          <text x="20" y="80" text-anchor="middle" font-size="8.5" fill="#166534">觀者眼睛</text>
          
          <ellipse cx="75" cy="65" rx="8" ry="22" fill="#22c55e"/>
          <text x="75" y="68" text-anchor="middle" font-size="8.5" fill="#fff">調和縮腳</text>
          <rect x="110" y="48" width="70" height="34" fill="#86efac" rx="4"/>
          <text x="145" y="68" text-anchor="middle" font-size="8.5" fill="#14532d">伸展胸膛</text>
          <circle cx="225" cy="65" r="20" fill="#15803d"/>
          <text x="225" y="69" text-anchor="middle" font-size="8.5" fill="#fff" font-weight="bold">神聖莊嚴頭顱</text>
          <text x="140" y="114" text-anchor="middle" font-size="8.5" fill="#14532d">非線性調和平均修正：保留尊嚴與安詳</text>
        </g>
      </svg>
    </div>

    <!-- WORKSHOP BOX -->
    <div class="workshop-box">
      <div class="workshop-title">
        <span>🛠️ 親手解剖：拿起鉛筆做「透視縮短（Foreshortening）」小實驗</span>
      </div>
      <div class="workshop-steps">
        <ol>
          <li><strong>準備道具：</strong>一枝全新長約 18 公分的鉛筆、一把直尺。</li>
          <li><strong>平行視線：</strong>將鉛筆橫放在桌面上正對側面，你看到的是完整的 18 公分（投影夾角 $\theta = 0^\circ$）。</li>
          <li><strong>對準自己：</strong>將鉛筆轉動 90 度，筆尖正對眼珠，筆尾朝後。在你的視野投影中，<strong>長達 18 公分的鉛筆瞬間「縮短」成了一個只有 0.7 公分直徑的小圓點！</strong></li>
          <li><strong>小學數學工具解密：</strong>一米七的人體平躺時在視網膜上的幾何長度被大幅壓縮；如果完全依照剛性光學，大腦的恆常性神經會崩潰。大師必須找到一種過渡平均數！</li>
        </ol>
      </div>
    </div>
  </div>
'''

def get_page_13():
    return r'''
  <!-- PAGE 13: CHAPTER 22 (SPREAD RIGHT) -->
  <div class="section-page">
    <div class="page-top-header">
      <span class="header-left">VOL 4 ｜ CHAPTER 22：躺著的巨人（PART 2）</span>
      <div class="header-right">
        <img class="header-logo-mini" src="__LOGO_DATA_URI__" alt="Mini Logo">
        <span>woieyufan BOOKS</span>
      </div>
    </div>

    <div class="chapter-header-box">
      <div class="chapter-tag">MATHEMATICAL ENGINE ｜ 幾何引擎</div>
      <div class="chapter-title">調和平均數：眼睛視野裡的「非線性減速檔」</div>
    </div>

    <!-- ENGINE BOX -->
    <div class="engine-box">
      <div class="engine-title">
        <span>⚙️ 小學進階數學工具：算術平均數 vs. 調和平均數（Harmonic Mean）</span>
      </div>
      <div class="engine-desc">
        在學校裡，我們最常學到的是<strong>算術平均數</strong>：$A = \frac{a+b}{2}$。例如 20 和 60 的算術平均是 40。但在物理速度、電阻並聯，以及<strong>透視投影的空間深度</strong>中，主宰一切的是<strong>調和平均數</strong>：
        $$\text{調和平均數 } H = \frac{2}{\frac{1}{a} + \frac{1}{b}} = \frac{2ab}{a+b}$$
        調和平均數永遠小於或等於幾何平均數和算術平均數（$H \le G \le A$）。它的本質，就是<strong>「對倒數求平均再倒回來」</strong>！
      </div>
    </div>

    <!-- NUMERICAL EXPERIMENT TABLE -->
    <div style="margin-bottom: 8px;">
      <table class="doc-table">
        <thead>
          <tr>
            <th style="width: 22%;">平均數類型</th>
            <th style="width: 28%;">計算公式</th>
            <th style="width: 22%;">數值示例 (a=2, b=6)</th>
            <th style="width: 28%;">在視覺藝術中的幾何物理意義</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>算術平均數 (A)</strong></td>
            <td>$A = \frac{a+b}{2}$</td>
            <td>$\frac{2+6}{2} = 4.0$</td>
            <td>長度等差切分（如畫一條均勻等分的斑馬線）</td>
          </tr>
          <tr>
            <td><strong>幾何平均數 (G)</strong></td>
            <td>$G = \sqrt{a \times b}$</td>
            <td>$\sqrt{2 \times 6} \approx 3.46$</td>
            <td>面積守恆變換、連續等比縮放</td>
          </tr>
          <tr>
            <td><strong>調和平均數 (H)</strong></td>
            <td>$H = \frac{2ab}{a+b}$</td>
            <td>$\frac{24}{8} = 3.0$</td>
            <td><strong>透視深度非線性衰減！</strong>靠近相機處急遽壓縮，深處平緩</td>
          </tr>
        </tbody>
      </table>
    </div>

    <div class="card-pane" style="margin-bottom: 8px; background: #eff6ff; border-left: 4px solid var(--accent);">
      <div style="font-weight: 800; color: var(--primary); font-size: 11.5px; margin-bottom: 3px;">透視坐標為什麼與「調和平均」密不可分？</div>
      <div style="font-size: 10.5px; color: #1e3a8a; line-height: 1.5;">
        當你看著一排間距相等的電線桿向遠方延伸時，第一根與第二根在畫布上的間距很大，而第五根與第六根在畫布上的間距極小。電線桿在畫布上的成像坐標 $y'$ 與真實距離 $x$ 成反比：$y' = f \cdot \frac{Y}{x}$。當你在處理「反比量」的中間點時，幾何投影的中心點坐標，恰好就是前點與後點距離的<strong>調和平均數</strong>，而不是算術平均數！
      </div>
    </div>

    <!-- MASTER'S SECRET BOX -->
    <div class="secret-box">
      <div class="secret-title">
        <span>🔑 大師暗門：曼特尼亞的「視覺補償調和係數」</span>
      </div>
      <div class="secret-desc">
        曼特尼亞在創作《哀悼基督》時，做了一個天才的數學折衷：他沒有採用絕對的相機光學透視（比值約 2.2:1），也沒有採用中世紀完全忽視深度的平面投影（比值 1:1），而是巧妙地將腳部與頭部的尺寸比錨定在<strong>調和中介區間（約 1.25:1）</strong>。他既給了觀者身歷其境的震撼感，又透過調和阻尼讓救世主面容保持莊嚴完整——這是數學與神學美感最完美的一次聯姻！
      </div>
    </div>

    <div style="margin-top: 8px; padding: 6px 12px; background: #faf5ff; border: 1px dashed #c084fc; border-radius: 5px; font-size: 10px; color: #581c87;">
      <strong>💡 終極壓軸挑戰（國中物理跨界）：</strong>在高速公路上搭車，去程時速 60 km/h，回程原路時速 100 km/h，全程平均速度是多少？千萬別回答 80 km/h！因為兩段路程相等，平均速度是調和平均數 $\frac{2 \times 60 \times 100}{60 + 100} = 75\text{ km/h}$！空間透視與時間速度，共用著完全相同的數學靈魂。
    </div>
  </div>
'''
