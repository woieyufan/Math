# -*- coding: utf-8 -*-
"""
Front pages (Page 1 to Page 3) for
《看見幾何：從寫字、拍照、剪衣服到文藝復興名畫的視覺解密》
Grounded in Elementary School (K-9) Mathematical Tools.
"""

def get_page_1():
    return r'''
  <!-- PAGE 1: BOOK COVER -->
  <div class="cover-wrapper">
    <img class="cover-watermark" src="__SVG_DATA_URI__" alt="Watermark">
    
    <div class="cover-header-brand">
      <img class="brand-logo-img" src="__LOGO_DATA_URI__" alt="woieyufan Logo">
      <div class="brand-text-col">
        <span class="brand-title">woieyufan SCIENCE & HUMANITIES PRESS</span>
        <span class="brand-sub">ADVANCED STEM/STEAM VISUAL MATHEMATICS SERIES</span>
      </div>
    </div>

    <div class="cover-main">
      <div class="cover-badge">★ 青少年進階視覺數學科普典藏版 ★</div>
      <h1 class="doc-title">看見幾何：從寫字、拍照、剪衣服<br>到文藝復興名畫的視覺解密</h1>
      <p class="doc-subtitle">
        全面立足小學數學工具庫！從除法餘數畫出發光星星、九宮格坐標平衡漢字、<br>
        相似形借位推倒比薩斜塔、衣服打版製造笛卡兒角虧，到破解躺著巨人的調和平均數
      </p>

      <div class="meta-grid">
        <div class="meta-item">
          <span class="meta-label">適讀年段</span>
          <span class="meta-val">小學中高年級至國中先修</span>
        </div>
        <div class="meta-item">
          <span class="meta-label">核心哲學</span>
          <span class="meta-val">小學數學工具 ➜ 視覺探案</span>
        </div>
        <div class="meta-item">
          <span class="meta-label">全書規格</span>
          <span class="meta-val">五大卷 ｜ 24 個探案主題</span>
        </div>
        <div class="meta-item">
          <span class="meta-label">出版單位</span>
          <span class="meta-val">woieyufan 數學教研工坊</span>
        </div>
      </div>
    </div>

    <div class="cover-footer">
      <span>FIRST EDITION ｜ ADVANCED EXTRACURRICULAR READER</span>
      <span>ISBN 978-986-000-GEOM-1 ｜ ALL RIGHTS RESERVED</span>
    </div>
  </div>
'''

def get_page_2():
    return r'''
  <!-- PAGE 2: EDITORIAL MANIFESTO -->
  <div class="section-page">
    <div class="page-top-header">
      <span class="header-left">EDITORIAL MANIFESTO ｜ 主編致讀者</span>
      <div class="header-right">
        <img class="header-logo-mini" src="__LOGO_DATA_URI__" alt="Mini Logo">
        <span>woieyufan BOOKS</span>
      </div>
    </div>

    <div class="chapter-header-box">
      <div class="chapter-tag">PROLOGUE</div>
      <div class="chapter-title">世界背後，藏著一張看不見的幾何網</div>
      <div class="para">
        親愛的好奇少年：你是否也曾在學校課堂上感到疑惑——<strong>為什麼我們要算那麼多枯燥的除法餘數？為什麼要背九九乘法和最大公因數？為什麼要在方格紙上標數對 $(x, y)$？</strong>這些考卷上的題目，難道長大後除了應付考試，就真的毫無用處嗎？這本書要告訴你一個驚天大秘密：<strong>全世界最頂級的藝術家、建築師、服裝設計師與攝影師，每天都在使用你手裡的這套小學數學工具！</strong>
      </div>
    </div>

    <div class="card-pane" style="margin-bottom: 10px; border-left: 4px solid var(--accent); background: #f0fdf4;">
      <div style="font-weight: 800; color: #166534; font-size: 12.5px; margin-bottom: 3px;">小學數學工具的降維打擊：捅破課本沒講透的窗戶紙！</div>
      <div style="font-size: 11px; color: #14532d; line-height: 1.55;">
        學校課堂為了評量，往往只教機械式計算，淺嚐輒止。但在這本書裡，我們把課本的窗戶紙徹底捅破：<strong>除法餘數變成了國旗星星的一筆畫密碼；生字簿九宮格變成了控制漢字不倒的坐標系；內角和小於 $360^\circ$ 的角虧變成了裁縫師把平面的布剪成立體衣服的神奇剪刀！</strong>
      </div>
    </div>

    <div class="section-title" style="font-size: 12px; font-weight: 800; color: var(--primary); margin: 6px 0 4px 0;">全書五大卷對應的小學數學工具矩陣</div>
    <div class="doc-table-wrapper">
      <table class="doc-table">
        <tr>
          <th style="width: 25%;">卷別名稱</th>
          <th style="width: 45%;">探索的日常生活與名畫謎題</th>
          <th style="width: 30%;">底層小學數學工具對接</th>
        </tr>
        <tr>
          <td><strong>卷一：筆尖與餘數星星</strong></td>
          <td>漢字九宮格重心、火柴人到幾何骨架、時鐘一筆畫五角星、棋盤網格</td>
          <td>數對 $(x,y)$、除法餘數、公因數、互質</td>
        </tr>
        <tr>
          <td><strong>卷二：自然演算法與密鋪</strong></td>
          <td>長頸鹿斑紋、向日葵種子排列、艾雪蜥蜴剪紙、巴黎聖母院玫瑰花窗</td>
          <td>中垂線、線對稱、圓心角、正多邊形</td>
        </tr>
        <tr>
          <td><strong>卷三：多面體與立體裁縫</strong></td>
          <td>衣服打版省道（Dart）、柏拉圖正多面體、正方體 11 種皮、3D 紙雕動物</td>
          <td>笛卡兒角虧、展開圖、歐拉公式 $V-E+F=2$</td>
        </tr>
        <tr>
          <td><strong>卷四：鏡頭光影與透視大案</strong></td>
          <td>影子測高、手電筒圓錐光斑、比薩斜塔借位拍照、名畫消失點、哀悼基督</td>
          <td>相似三角形、中心投影、反比調和平均數</td>
        </tr>
        <tr>
          <td><strong>卷五：極限色彩與終極大作</strong></td>
          <td>A4 紙裝下無限長海岸線、秀拉視網膜向量混色、RGB 色彩立方體</td>
          <td>等比極限、自相似、向量加法與重心</td>
        </tr>
      </table>
    </div>

    <div class="secret-box" style="margin-top: 6px;">
      <div class="secret-title">★ 給家長與老師的話：讓數學從考卷走向現實</div>
      <div class="secret-desc">
        這本書精準對接國小中高年級到國中必學的數學工具。我們不強加大學高深的抽象概念，而是用最迷人的生活現象與名畫，讓孩子看見手中數學工具的威力，建立受用一生的幾何直覺。
      </div>
    </div>
  </div>
'''

def get_page_3():
    return r'''
  <!-- PAGE 3: COMPLETE 24-CHAPTER TOC -->
  <div class="section-page">
    <div class="page-top-header">
      <span class="header-left">COMPLETE TABLE OF CONTENTS ｜ 24 個幾何探案目錄</span>
      <div class="header-right">
        <img class="header-logo-mini" src="__LOGO_DATA_URI__" alt="Mini Logo">
        <span>woieyufan BOOKS</span>
      </div>
    </div>

    <div class="chapter-header-box" style="margin-bottom: 6px;">
      <div class="chapter-tag">CONTENTS</div>
      <div class="chapter-title">全書目錄：小學數學工具出發的 24 個視覺探案</div>
    </div>

    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 10px; align-items: start;">
      <!-- COLUMN 1: VOL 1, 2, 3 (PART) -->
      <div>
        <!-- VOL 1 -->
        <div class="toc-vol-box">
          <div class="toc-vol-head">
            <span>【卷一：筆尖、格子與餘數星星】坐標與整數</span>
            <span style="color: var(--neon-cyan);">CH 01–05</span>
          </div>
          <div class="toc-chap-row">
            <span class="toc-chap-title">第 01 章 寫字也是算幾何？——漢字九宮格與坐標重心</span>
            <span class="toc-chap-math">數對 $(x,y)$ / 重心平衡</span>
          </div>
          <div class="toc-chap-row">
            <span class="toc-chap-title">第 02 章 火柴人的進化論——從小學生塗鴉到幾何骨架人體</span>
            <span class="toc-chap-math">幾何模組 / 比例線段</span>
          </div>
          <div class="toc-chap-row">
            <span class="toc-chap-title">第 03 章 時鐘上的流星雨——除法餘數、互質與一筆畫五角星</span>
            <span class="toc-chap-math">模運算 / 最大公因數</span>
          </div>
          <div class="toc-chap-row">
            <span class="toc-chap-title">第 04 章 黑白格子的暗算——圍棋、象棋、六角蜂巢網格距離</span>
            <span class="toc-chap-math">網格距離 / 六角密鋪</span>
          </div>
          <div class="toc-chap-row">
            <span class="toc-chap-title">第 05 章 只用一把直尺織出平滑曲線！——弦絲畫包絡線</span>
            <span class="toc-chap-math">一次函數切線 / 拋物線</span>
          </div>
        </div>

        <!-- VOL 2 -->
        <div class="toc-vol-box">
          <div class="toc-vol-head">
            <span>【卷二：大自然演算法與平面密鋪】中垂線與角度</span>
            <span style="color: var(--neon-cyan);">CH 06–09</span>
          </div>
          <div class="toc-chap-row">
            <span class="toc-chap-title">第 06 章 長頸鹿的斑紋是算出來的！——沃羅諾伊圖分割</span>
            <span class="toc-chap-math">垂直平分線全域劃分</span>
          </div>
          <div class="toc-chap-row">
            <span class="toc-chap-title">第 07 章 爬滿牆壁的蜥蜴——艾雪剪紙、滑移反射與面積守恆</span>
            <span class="toc-chap-math">平面剛體變換 / 密鋪</span>
          </div>
          <div class="toc-chap-row">
            <span class="toc-chap-title">第 08 章 太陽向日葵的採光算術——137.5 度黃金角奇蹟</span>
            <span class="toc-chap-math">費氏數列 / 極坐標螺線</span>
          </div>
          <div class="toc-chap-row">
            <span class="toc-chap-title">第 09 章 巴黎聖母院的十二芒星——圓規等分圓周玫瑰花窗</span>
            <span class="toc-chap-math">正多邊形 / 圓心角</span>
          </div>
        </div>

        <!-- VOL 3 -->
        <div class="toc-vol-box" style="margin-bottom: 0;">
          <div class="toc-vol-head">
            <span>【卷三：多面體王國與立體打版】角虧與展開圖</span>
            <span style="color: var(--neon-cyan);">CH 10–14</span>
          </div>
          <div class="toc-chap-row">
            <span class="toc-chap-title">第 10 章 神聖五大多面體——柏拉圖立體與達文西鏤空木架</span>
            <span class="toc-chap-math">角虧定理 / 凸多面體</span>
          </div>
          <div class="toc-chap-row">
            <span class="toc-chap-title">第 11 章 正方體的 11 張皮——展開圖拓撲爬行法與幾何燈罩</span>
            <span class="toc-chap-math">正方體展開圖拓撲</span>
          </div>
          <div class="toc-chap-row">
            <span class="toc-chap-title">第 12 章 為什麼足球是 12 塊五邊形？——阿基米德截角多面體</span>
            <span class="toc-chap-math">半正多面體 / 截角</span>
          </div>
          <div class="toc-chap-row">
            <span class="toc-chap-title">第 13 章 打版師的幾何剪刀——平面布料如何穿成立體衣服？</span>
            <span class="toc-chap-math">省道 (Darts) / 圓錐展開</span>
          </div>
          <div class="toc-chap-row">
            <span class="toc-chap-title">第 14 章 Low Poly 半寫實動物紙雕——三維三角網格摺紙</span>
            <span class="toc-chap-math">歐拉公式 $V-E+F=2$</span>
          </div>
        </div>
      </div>

      <!-- COLUMN 2: VOL 4, 5 & SAMPLE GUIDE -->
      <div>
        <!-- VOL 4 -->
        <div class="toc-vol-box">
          <div class="toc-vol-head">
            <span>【卷四：鏡頭光影與透視大案】相似形與投影</span>
            <span style="color: var(--neon-cyan);">CH 15–22</span>
          </div>
          <div class="toc-chap-row">
            <span class="toc-chap-title">第 15 章 踩在腳底的巨人——影子幾何、太陽平行光與路燈發散光</span>
            <span class="toc-chap-math">平行投影 / 發散光線</span>
          </div>
          <div class="toc-chap-row">
            <span class="toc-chap-title">第 16 章 手電筒照牆壁的魔法——圓、橢圓、拋物線圓錐截面</span>
            <span class="toc-chap-math">圓錐曲線 / 截面投影</span>
          </div>
          <div class="toc-chap-row">
            <span class="toc-chap-title">第 17 章 推倒比薩斜塔！——相機視錐截線與相似三角形借位</span>
            <span class="toc-chap-math">相似三角形 $\frac{h}{d}=\frac{H}{D}$</span>
          </div>
          <div class="toc-chap-row">
            <span class="toc-chap-title">第 18 章 照片怎麼裁最好看？——相機九宮格取景、三分法構圖</span>
            <span class="toc-chap-math">黃金分割 / 視覺重心</span>
          </div>
          <div class="toc-chap-row">
            <span class="toc-chap-title">第 19 章 耶穌額頭上的十字星——《最後晚餐》天花板一次方程</span>
            <span class="toc-chap-math">一次函數斜率 / 消失點</span>
          </div>
          <div class="toc-chap-row">
            <span class="toc-chap-title">第 20 章 地板瓷磚的溜滑梯——阿爾伯蒂地坪網格平行截比例線</span>
            <span class="toc-chap-math">平行線截比例線段</span>
          </div>
          <div class="toc-chap-row">
            <span class="toc-chap-title">第 21 章 走不出的城堡——《紀念碑谷》30 度等角軸測視錯覺</span>
            <span class="toc-chap-math">Isometric 軸測 / 三視圖</span>
          </div>
          <div class="toc-chap-row">
            <span class="toc-chap-title">第 22 章 躺著的巨人——曼特尼亞《哀悼基督》與調和平均數</span>
            <span class="toc-chap-math">調和平均 $H = \frac{2ab}{a+b}$</span>
          </div>
        </div>

        <!-- VOL 5 -->
        <div class="toc-vol-box">
          <div class="toc-vol-head">
            <span>【卷五：極限色彩與終極大作】向量與極限</span>
            <span style="color: var(--neon-cyan);">CH 23–24</span>
          </div>
          <div class="toc-chap-row">
            <span class="toc-chap-title">第 23 章 A4 紙裝下無限海岸線——科赫雪花與秀拉向量光學混色</span>
            <span class="toc-chap-math">等比數列 / 向量加法</span>
          </div>
          <div class="toc-chap-row">
            <span class="toc-chap-title">第 24 章 全域幾何終極大解密：創作屬於你的文藝復興大畫作！</span>
            <span class="toc-chap-math">全域綜合設計實踐</span>
          </div>
        </div>

        <!-- SAMPLE READING GUIDE -->
        <div style="padding: 6px 10px; background: #eff6ff; border: 1px dashed #93c5fd; border-radius: 5px; font-size: 9.5px; color: #1e40af; line-height: 1.45;">
          <strong>★ 本冊精選 5 大示範樣章試讀索引（循序漸進爬坡）：</strong><br>
          • P. 04–05：【樣章 1 / 第 01 章】漢字九宮格坐標系與不倒翁重心力矩<br>
          • P. 06–07：【樣章 2 / 第 03 章】時鐘上的流星雨：除法餘數與一筆畫星形<br>
          • P. 08–09：【樣章 3 / 第 17 章】推倒比薩斜塔！相似三角形借位攝影方程<br>
          • P. 10–11：【樣章 4 / 第 13 章】打版師的幾何剪刀：衣服省道、圓錐與角虧<br>
          • P. 12–13：【樣章 5 / 第 22 章】曼特尼亞《哀悼基督》與調和平均數透視
        </div>
      </div>
    </div>
  </div>
'''
