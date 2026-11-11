# -*- coding: utf-8 -*-
"""
Pedagogy & Research pages (Page 13 to Page 15) for Gifted Math White Paper V4.0
Covers:
- Page 13: Gifted Pedagogy & Bridging Inquiry Model (Tax Optimization & Factorization Game)
- Page 14: Five-Stage Independent Research Framework (National Science Fair & Paper Mentoring)
- Page 15: Chung-Hsiao 43-Set Test Papers & Handouts Panoramic Matrix
"""

def get_page_13():
    return r'''
  <!-- PAGE 13: GIFTED PEDAGOGY -->
  <div class="section-page">
    <div class="page-top-header">
      <span class="header-left">PEDAGOGICAL INNOVATION ｜ 資優教法：情境創設與搭橋提問模型</span>
      <div class="header-right">
        <img class="header-logo-mini" src="__LOGO_DATA_URI__" alt="Mini Logo">
        <span>woieyufan EDUCATION</span>
      </div>
    </div>

    <div class="chapter-header-box">
      <span class="chapter-tag">教法篇 ｜ 課堂創新</span>
      <div class="chapter-title">搭橋式提問法與高層次情境任務設計</div>
      <p class="chapter-desc">解密《資優數學教材與教法示例》：以「節稅高手任務」引導因數倍數之圖論與極值優化</p>
    </div>

    <div class="hero-statement">
      ★ 資優班教學最高原則：<br>
      普通班已經教過的基礎知識，資優班只需應用，絕不重複死練！課程是層層堆砌的概念階梯，切忌過河拆橋或難度跳躍過猛。教師的責任是創造「認知衝突」，提供學生體會數學之美與策略優化的舞台！
    </div>

    <div class="two-col-grid">
      <!-- TAX OPTIMIZATION TASK -->
      <div class="concept-card concept-card-emerald">
        <div class="card-title">1. 經典案例拆解：節稅高手任務 (Tax Master)</div>
        <p style="font-size: 11.5px; margin: 0; line-height: 1.5; color: #334155;">
          • <strong>任務情境</strong>：1 到 15 的 15 張收入卡，總和 120 萬元。<br>
          • <strong>規則</strong>：選取某數 $N$ 為收入時，$N$ 的所有<strong>尚未被扣過的真因數</strong>必須繳為政府稅金。<br>
          • <strong>特例懲罰</strong>：若選取之數的所有真因數先前均已被繳稅，則該數全額充公為稅金！<br>
          • <strong>核心目標</strong>：尋求取數順序，使得<strong>個人總收入最大化（節稅最多）</strong>。
        </p>
      </div>

      <!-- BRIDGING MODEL -->
      <div class="concept-card concept-card-indigo">
        <div class="card-title">2. 四階搭橋式提問梯隊</div>
        <p style="font-size: 11.5px; margin: 0; line-height: 1.5; color: #334155;">
          • <strong>第一階（直覺衝撞）</strong>：學生先挑大數（如 15、14），發現稅金高達 1+3+5=9 萬。<br>
          • <strong>第二階（質數保護）</strong>：選大質數 13、11，稅金僅有 1 萬元！<br>
          • <strong>第三階（因數鏈雪崩）</strong>：1 已被繳走，後續選其他合數時「1 免稅」，大幅降低扣除額！<br>
          • <strong>第四階（模型抽象）</strong>：將數群建模為<strong>有向無環圖 (DAG)</strong>，求最大獨立權重。
        </p>
      </div>
    </div>

    <div class="section-title">3. 課堂實作：因倍數接龍（師生思維博弈）</div>
    <div class="para">
      數字介於 1 到 50，輪流說出前一個數的因數或倍數，每個數字只能使用一次。此遊戲看似簡單，實則蘊含「質數死胡同」、「完全平方式分岔節點」與「哈密頓路徑 (Hamiltonian Path)」等高等圖論概念。目前全國資優班最佳紀錄為串接 38 個數字！
    </div>

    <div class="problem-box">
      <div class="problem-header"><span class="annot-target" id="annot-p13">【課堂提問對話示範】</span> 教師如何引導學生跳出死胡同</div>
      <div class="proof-box" style="font-size: 11.5px;">
        <div><strong>教師提問</strong>：「如果我們先拿 9，大家覺得好不好？」</div>
        <div><strong>資優生 A</strong>：「9 的因數是 1 和 3，交完 4 萬稅，自己拿 9 萬，淨賺 5 萬，好像還不錯？」</div>
        <div><strong>資優生 B（深入質疑）</strong>：「不對！如果前面已經把 1 和 3 繳掉了，這時選 9 會觸發『無因數可繳』規則，9 萬會全額充公！所以 9 必須在 1 或 3 還在的時候優先處理！」</div>
        <div><strong>教師總結</strong>：「太棒了！這就是<strong>因數拓撲依賴</strong>——在博弈中，合數的選取時機直接取決於前置因數的存活狀態！」</div>
      </div>
    </div>

    <div class="page-bottom-footer">
      <span>中學數理資優教研白皮書 ｜ woieyufan EDUCATION</span>
      <span class="footer-center">第十二篇：資優班教學與搭橋模型</span>
      <span>PAGE 13</span>
    </div>
  </div>
'''

def get_page_14():
    return r'''
  <!-- PAGE 14: FIVE-STAGE INDEPENDENT RESEARCH -->
  <div class="section-page">
    <div class="page-top-header">
      <span class="header-left">RESEARCH METHODOLOGY ｜ 獨立研究：國中數學科研五部曲實施指引</span>
      <div class="header-right">
        <img class="header-logo-mini" src="__LOGO_DATA_URI__" alt="Mini Logo">
        <span>woieyufan EDUCATION</span>
      </div>
    </div>

    <div class="chapter-header-box">
      <span class="chapter-tag">研究篇 ｜ 科研素養</span>
      <div class="chapter-title">國中數學獨立研究五步法架構</div>
      <p class="chapter-desc">解密《國中數學獨立研究第一階段教材》：系統化引領七至八年級資優生完成科展與學術論文</p>
    </div>

    <div class="hero-statement">
      ★ 獨立研究核心定位：<br>
      培養資優生在八年級獨立主導並完成數學專題之關鍵能力。將科研程序科學拆解為時間序列五大主題，化解中學生知識儲備不足的痛點，建立「猜想 ➜ 反例 ➜ 修正 ➜ 證明」之學術品格！
    </div>

    <!-- 5 STAGES TABLE -->
    <table class="doc-table">
      <thead>
        <tr>
          <th style="width: 18%;">研究五部曲</th>
          <th style="width: 32%;">中學資優課堂實施細則</th>
          <th style="width: 30%;">指導教師核心提問與引導</th>
          <th style="width: 20%;">核心產出成果</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>第一步：尋找問題<br>(Find Focus)</strong></td>
          <td>從棋盤遊戲、幾何對稱折紙、費波那契數列或課本定理之邊界拓展發掘靈感。</td>
          <td>「如果把條件從『正三角形』放寬至『任意三角形』，結果還會成立嗎？」</td>
          <td>研究動機說明書<br>研究目的條列</td>
        </tr>
        <tr>
          <td><strong>第二步：補足知識<br>(Acquire Know)</strong></td>
          <td>針對選題自學微積分基礎、初等數論、線性代數矩陣或圖論符號語言。</td>
          <td>「現有初中工具無法描述此動態，我們需要引入什麼數學語言？」</td>
          <td>數學術語符號表<br>先備知識筆記</td>
        </tr>
        <tr>
          <td><strong>第三步：文獻探討<br>(Literature)</strong></td>
          <td>檢索中華民國中小學科學展覽歷屆作品與國際競賽題目，建立查重與文獻引用。</td>
          <td>「前人已經做到哪裡？我們的研究有什麼獨特的新角度與推廣價值？」</td>
          <td>文獻比較架構圖<br>研究獨創性陳述</td>
        </tr>
        <tr>
          <td><strong>第四步：問題探究<br>(Inquiry & Proof)</strong></td>
          <td>小數據實驗（$n=1,2,3$）尋找規律，構造幾何輔助線或數學歸納法形式證明。</td>
          <td>「這個猜想有沒有反例？在極端邊界情況下公式是否依然強健？」</td>
          <td>引理與定理推導<br>反例排除記錄簿</td>
        </tr>
        <tr>
          <td><strong>第五步：書面口頭報告<br>(Paper/Oral)</strong></td>
          <td>按照標準學術格式排版（摘要、緒論、定義、正文證明、討論、參考文獻）。</td>
          <td>「如何用 5 分鐘清晰向評審闡述核心突破與研究價值？」</td>
          <td>完整科展報告書<br>專題答辯簡報</td>
        </tr>
      </tbody>
    </table>

    <div class="two-col-grid" style="margin-top: 10px;">
      <div class="concept-card concept-card-emerald">
        <div class="card-title">★ 科研素養與學術倫理教育</div>
        <p style="font-size: 11px; margin: 0; line-height: 1.5; color: #475569;">
          培養嚴格的學術倫理：文獻引用註明出處、不偽造數據、不抄襲前人成果；培養「面對卡關時的學術堅毅 (Resilience)」，理解失敗是探究不可或缺的基石。
        </p>
      </div>

      <div class="concept-card concept-card-indigo">
        <div class="card-title">★ 評審答辯演練與同儕質詢</div>
        <p style="font-size: 11px; margin: 0; line-height: 1.5; color: #475569;">
          組織課堂模擬發表會，由同儕資優生擔任嚴苛的「同儕審查員 (Peer Reviewers)」，就證明的每一步邏輯跳躍與邊界特例提出質詢，磨礪口語表達與邏輯防禦力。
        </p>
      </div>
    </div>

    <div class="page-bottom-footer">
      <span>中學數理資優教研白皮書 ｜ woieyufan EDUCATION</span>
      <span class="footer-center">第十三篇：獨立研究五步法</span>
      <span>PAGE 14</span>
    </div>
  </div>
'''

def get_page_15():
    return r'''
  <!-- PAGE 15: CHUNG-HSIAO 43-SET TEST PAPERS MATRIX -->
  <div class="section-page">
    <div class="page-top-header">
      <span class="header-left">TEST PAPER ARCHIVES ｜ 題庫檔案：忠孝國中 43 套歷年數理資優講義全覽</span>
      <div class="header-right">
        <img class="header-logo-mini" src="__LOGO_DATA_URI__" alt="Mini Logo">
        <span>woieyufan EDUCATION</span>
      </div>
    </div>

    <div class="chapter-header-box">
      <span class="chapter-tag">題庫篇 ｜ 實戰矩陣</span>
      <div class="chapter-title">忠孝國中數理資優實體課程試卷庫</div>
      <p class="chapter-desc">完整收錄 96-97 學年度數理資優全學期週考、段考專卷、奧賽真題與詳解手冊</p>
    </div>

    <!-- ARCHIVE MATRIX TABLE -->
    <table class="doc-table">
      <thead>
        <tr>
          <th style="width: 22%;">專卷分類</th>
          <th style="width: 32%;">試卷檔案清單（精選代表）</th>
          <th style="width: 28%;">核心考察思維與題型</th>
          <th style="width: 18%;">解答配備情況</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>97 學年第一學期<br>週考與加強卷</strong><br>(17 套 PDF)</td>
          <td>
            • 97-1 數理資優 0920, 0927一次版, 1004<br>
            • 97-1 數理資優 1025, 1101, 1115, 1122<br>
            • 97-1 數理資優 1129, 1213, 1220, 1227
          </td>
          <td>
            因數與倍數素因子分解、同餘方程模運算、三角形外心與內心性質、二次函數極值
          </td>
          <td>
            配備 1025-ans, 1115-ans, 1122-ans, 1129-ans, 1213-ans, 1220-ans 完整官方解答
          </td>
        </tr>
        <tr>
          <td><strong>97 學年第二學期<br>週考與加強卷</strong><br>(6 套 PDF)</td>
          <td>
            • 97-2 數理資優 0307, 0321, 0418<br>
            • 97-2 數理資優 0502-1, 0509-1
          </td>
          <td>
            圓方冪、四點共圓判定、塞瓦定理比例計算、空間幾何展開圖與截面
          </td>
          <td>
            配備 0509-1-ans 詳盡步驟解答卷
          </td>
        </tr>
        <tr>
          <td><strong>96 學年第二學期<br>實體課堂系列</strong><br>(10 套 PDF)</td>
          <td>
            • 忠孝96-2 二年級資優 0301, 0315, 0426<br>
            • 忠孝96-2 二年級資優 0503, 0531, 0531-1<br>
            • 忠孝96-2 二年級資優 0614, 0614-1~3
          </td>
          <td>
            等差等比數列高次求和、柯西不等式向量法、幾何旋轉全等構造、鴿籠原理
          </td>
          <td>
            課堂完整題本與教師原版板書推導
          </td>
        </tr>
        <tr>
          <td><strong>知己知己<br>專項訓練系列</strong><br>(2 套 PDF)</td>
          <td>
            • 忠孝96-2 知己知己練習卷 0315<br>
            • 忠孝96-2 知己知己練習卷-2-0315
          </td>
          <td>
            分層階梯訓練、弱點專項診斷、分類討論思維、極端值反證法
          </td>
          <td>
            含各題組分步引導式提示
          </td>
        </tr>
        <tr>
          <td><strong>競賽真題與<br>教研示例專卷</strong><br>(8 套 PDF)</td>
          <td>
            • 第九屆國中二年級數學奧林匹克試題<br>
            • 第十五屆希望杯初一第 1 試<br>
            • 國中數學老師來不及教的內容20071124<br>
            • 國中數學獨立研究第一階段教材<br>
            • 資優數學教材與教法示例(講義用)
          </td>
          <td>
            全國大賽真題對決、國高中知識斷崖銜接、獨立研究五步法、因倍數接龍與節稅高手任務
          </td>
          <td>
            附帶完整評析、歷年選手答題失分點分析與名師導讀
          </td>
        </tr>
      </tbody>
    </table>

    <div class="problem-box" style="margin-top: 8px;">
      <div class="problem-header"><span class="annot-target" id="annot-p15">【題庫教學建議】</span> 如何最高效利用 43 套真題資料庫</div>
      <p style="margin: 0; font-size: 11.5px; color: #475569;">
        建議自學學生與指導教師以「知識點模組」橫向串聯試卷：先研讀《資優數學核心思維手冊》掌握四大支柱理論，再按本白皮書矩陣挑選對應日期的忠孝週考卷進行限時模擬訓練，最後比對 ans 解答卷進行深度覆盤，形成自主學習的強大飛輪。
      </p>
    </div>

    <div class="page-bottom-footer">
      <span>中學數理資優教研白皮書 ｜ woieyufan EDUCATION</span>
      <span class="footer-center">第十四篇：忠孝國中43套題庫總覽</span>
      <span>PAGE 15</span>
    </div>
  </div>
'''
