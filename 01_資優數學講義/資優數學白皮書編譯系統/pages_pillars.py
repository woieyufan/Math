# -*- coding: utf-8 -*-
"""
Four Pillars pages (Page 5 to Page 12) for Gifted Math White Paper V4.0
Covers:
- Page 5: Number Theory I (Divisibility, Euclidean Algorithm, Bézout's Identity, Congruence)
- Page 6: Number Theory II (Fermat, Euler, Order & Primitive Roots, Legendre's Formula, Diophantine Problem)
- Page 7: Algebra I (Vieta's Formulas, Newton's Sums, Symmetric Polynomials, High-Degree Factorization)
- Page 8: Algebra II (Cauchy-Schwarz Vector Geometry, AM-GM Forward-Backward Induction, Nesbitt Inequality)
- Page 9: Geometry I (Ceva & Menelaus Theorems, Projective Ratio, Unification of Triangle Centers)
- Page 10: Geometry II (Power of a Point, Radical Axis & Center, Ptolemy's Theorem, Circle Inversion)
- Page 11: Combinatorics I (Pigeonhole Generalized & Continuous, Double Counting, Graph Handshaking)
- Page 12: Combinatorics II (Invariants, Monovariant Energy Function, Mutilated Chessboard Proof)
"""

def get_page_5():
    return r'''
  <!-- PAGE 5: NUMBER THEORY I -->
  <div class="section-page">
    <div class="page-top-header">
      <span class="header-left">PILLAR I: NUMBER THEORY ｜ 數論支柱（上）：除法、同餘與不定方程</span>
      <div class="header-right">
        <img class="header-logo-mini" src="__LOGO_DATA_URI__" alt="Mini Logo">
        <span>woieyufan EDUCATION</span>
      </div>
    </div>

    <div class="chapter-header-box">
      <span class="chapter-tag">支柱一 ｜ 數論基石</span>
      <div class="chapter-title">帶餘除法、輾轉相除與模環 $\mathbb{Z}_m$</div>
      <p class="chapter-desc">跳脫十進制表層計算，建立離散整數環之代數對稱與同餘分類結構</p>
    </div>

    <div class="hero-statement">
      ★ 數論第一性原理：<br>
      整數的核心在於「整除與餘數」。所有複雜的數論競賽題，本質上都是將無限的整數空間 $\mathbb{Z}$，通過除法餘數折疊至有限的模剩餘環 $\mathbb{Z}_m$ 中考察守恆性！
    </div>

    <div class="two-col-grid">
      <!-- DIVISION & EUCLIDEAN -->
      <div class="concept-card concept-card-indigo">
        <div class="card-title">1. 帶餘除法與歐幾里得輾轉相除</div>
        <p style="font-size: 12px; margin: 0; line-height: 1.5; color: #334155;">
          <strong>定理 1.1（帶餘除法）</strong>：對任意 $a, b \in \mathbb{Z}$ ($b > 0$)，存在唯一整數對 $(q, r)$ 使得 $a = bq + r$ ($0 \le r < b$)。<br><br>
          <strong>定理 1.2（歐幾里得輾轉相除）</strong>：若 $a = bq + r$，則 $\gcd(a, b) = \gcd(b, r)$。<br>
          <em>證明</em>：設 $d$ 為 $a, b$ 公因數，則 $d \mid (a - bq) = r$，故 $d \mid \gcd(b, r)$。同理可證逆向整除，證畢。
        </p>
      </div>

      <!-- BEZOUT IDENTITY -->
      <div class="concept-card concept-card-emerald">
        <div class="card-title">2. 貝祖等式 (Bézout's Identity)</div>
        <p style="font-size: 12px; margin: 0; line-height: 1.5; color: #334155;">
          <strong>定理 1.3（Bézout 等式）</strong>：對任意 $a, b \in \mathbb{Z}^+$，存在整數 $x, y$ 使得：
          $$ax + by = \gcd(a, b)$$
          <strong>線性不定方程充要條件</strong>：方程 $ax + by = c$ 有整數解 $\iff \gcd(a, b) \mid c$。<br>
          <em>解的構造</em>：若 $(x_0, y_0)$ 為特解，則通解為 $x = x_0 + k\frac{b}{d}, y = y_0 - k\frac{a}{d}$ ($k \in \mathbb{Z}$)。
        </p>
      </div>
    </div>

    <div class="section-title">3. 同餘算術與環 $\mathbb{Z}_m$ 的運算規律</div>
    <div class="para">
      定義：若 $m \mid (a - b)$，記作 $a \equiv b \pmod{m}$。同餘是整數集合上的等價關係，具自反、對稱、傳遞性。
    </div>

    <table class="doc-table">
      <thead>
        <tr>
          <th style="width: 25%;">運算性質</th>
          <th style="width: 40%;">代數表達式</th>
          <th style="width: 35%;">競賽避坑指南與關鍵細節</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>線性加減乘</strong></td>
          <td>若 $a \equiv b, c \equiv d \implies a \pm c \equiv b \pm d, ac \equiv bd$</td>
          <td>可自由代換同餘項，大幅化簡多項式餘數</td>
        </tr>
        <tr>
          <td><strong>同餘除法約束</strong></td>
          <td>$ca \equiv cb \pmod{m} \iff a \equiv b \pmod{\frac{m}{\gcd(c, m)}}$</td>
          <td><strong>嚴禁盲目消去常數！</strong>只有當 $\gcd(c, m)=1$ 時才能直接同除 $c$</td>
        </tr>
        <tr>
          <td><strong>模逆元構造</strong></td>
          <td>若 $\gcd(a, m) = 1$，存在唯一的 $a^{-1} \in \mathbb{Z}_m$ 使 $a a^{-1} \equiv 1$</td>
          <td>利用擴展歐幾里得演算法求解 $ax + my = 1$</td>
        </tr>
      </tbody>
    </table>

    <div class="problem-box">
      <div class="problem-header"><span class="annot-target" id="annot-p5">【經典真題 1.1】</span> 模逆元與整除週期構造</div>
      <p style="margin: 0 0 4px 0;">求最小的正整數 $x$，使得 $17x \equiv 1 \pmod{43}$。</p>
      <div class="proof-box">
        <div class="proof-step"><span class="step-num">Step 1：</span> 運用歐幾里得輾轉除法：$43 = 17 \times 2 + 9$，$17 = 9 \times 1 + 8$，$9 = 8 \times 1 + 1$。</div>
        <div class="proof-step"><span class="step-num">Step 2：</span> 倒推 Bézout 等式：$1 = 9 - 8 = 9 - (17 - 9) = 2 \times 9 - 17 = 2(43 - 17 \times 2) - 17 = 2 \times 43 - 5 \times 17$。</div>
        <div class="proof-step"><span class="step-num">Step 3：</span> 模 43 取同餘：$-5 \times 17 \equiv 1 \pmod{43} \implies 17 \times (-5 + 43) = 17 \times 38 \equiv 1 \pmod{43}$。故 $x = 38$。</div>
      </div>
    </div>

    <div class="page-bottom-footer">
      <span>中學數理資優教研白皮書 ｜ woieyufan EDUCATION</span>
      <span class="footer-center">第四篇：數論與構造（上）</span>
      <span>PAGE 05</span>
    </div>
  </div>
'''

def get_page_6():
    return r'''
  <!-- PAGE 6: NUMBER THEORY II -->
  <div class="section-page">
    <div class="page-top-header">
      <span class="header-left">PILLAR I: NUMBER THEORY ｜ 數論支柱（下）：費馬、歐拉與素因子階乘</span>
      <div class="header-right">
        <img class="header-logo-mini" src="__LOGO_DATA_URI__" alt="Mini Logo">
        <span>woieyufan EDUCATION</span>
      </div>
    </div>

    <div class="chapter-header-box">
      <span class="chapter-tag">支柱一 ｜ 數論高階</span>
      <div class="chapter-title">指數同餘循環、原根與勒讓德公式</div>
      <p class="chapter-desc">解密質數密碼、階乘素因數分解與高難度指數不定方程之排除法構造</p>
    </div>

    <div class="two-col-grid">
      <!-- FERMAT & EULER -->
      <div class="concept-card concept-card-indigo">
        <div class="card-title">1. 費馬小定理與歐拉定理</div>
        <p style="font-size: 12px; margin: 0; line-height: 1.5; color: #334155;">
          <strong>費馬小定理</strong>：若 $p$ 為質數，$\gcd(a, p) = 1$，則：
          $$a^{p-1} \equiv 1 \pmod{p}$$
          <strong>歐拉定理</strong>：對任意正整數 $m$ 及 $\gcd(a, m) = 1$：
          $$a^{\phi(m)} \equiv 1 \pmod{m}$$
          其中歐拉函數 $\phi(m) = m \prod_{p \mid m} \left(1 - \frac{1}{p}\right)$ 為小於等於 $m$ 且與 $m$ 互質的正整數個數。
        </p>
      </div>

      <!-- LEGENDRE FORMULA -->
      <div class="concept-card concept-card-emerald">
        <div class="card-title">2. 勒讓德階乘素因數公式</div>
        <p style="font-size: 12px; margin: 0; line-height: 1.5; color: #334155;">
          <strong>定理 1.4（Legendre's Formula）</strong>：階乘 $n!$ 質因數分解中，質數 $p$ 的最高冪次 $v_p(n!)$ 為：
          $$v_p(n!) = \sum_{k=1}^{\infty} \left\lfloor \frac{n}{p^k} \right\rfloor = \frac{n - S_p(n)}{p - 1}$$
          其中 $S_p(n)$ 為整數 $n$ 在 $p$ 進制下的各位數字之和。此公式是研究二項式係數整除性之核武。
        </p>
      </div>
    </div>

    <div class="section-title">3. 階 (Order) 與原根 (Primitive Root) 循環密碼</div>
    <div class="para">
      定義：使 $a^d \equiv 1 \pmod{m}$ 成立之最小正整數 $d$ 稱為 $a$ 模 $m$ 的階，記為 $\operatorname{ord}_m(a)$。
      <strong>關鍵性質</strong>：若 $a^k \equiv 1 \pmod{m}$，則 $\operatorname{ord}_m(a) \mid k$；且必有 $\operatorname{ord}_m(a) \mid \phi(m)$。當階恰好等於 $\phi(m)$ 時，$a$ 稱為模 $m$ 的<strong>原根</strong>。
    </div>

    <div class="problem-box">
      <div class="problem-header"><span class="annot-target" id="annot-p6">【奧林匹克真題 1.2】</span> 模 3 與模 4 交叉排除法求解指數不定方程</div>
      <p style="margin: 0 0 4px 0;">求所有正整數對 $(x, y)$ 使得 $3^x + 55 = y^2$。</p>
      <div class="proof-box">
        <div class="proof-step"><span class="step-num">Step 1（模 4 奇偶性鎖定）：</span> 
          考察 $3^x \pmod{4}$。由於 $3 \equiv -1 \pmod{4}$，故 $3^x \equiv (-1)^x \pmod{4}$。已知 $55 \equiv 3 \pmod{4}$。<br>
          完全平方數 $y^2 \equiv 0$ 或 $1 \pmod{4}$。若 $x$ 為奇數，則 $3^x + 55 \equiv -1 + 3 \equiv 2 \pmod{4}$，矛盾！故 $x$ 必為<strong>偶數</strong>。
        </div>
        <div class="proof-step"><span class="step-num">Step 2（平方差因式分解構造）：</span> 
          設 $x = 2k$ ($k \in \mathbb{Z}^+$)，原式變為 $55 = y^2 - (3^k)^2 = (y - 3^k)(y + 3^k)$。<br>
          由於 $y + 3^k > y - 3^k > 0$，因數分解 55 僅有兩組：$(1, 55)$ 與 $(5, 11)$。
        </div>
        <div class="proof-step"><span class="step-num">Step 3（精確求值）：</span>
          解聯立方程：A組 $\begin{cases} y+3^k=55 \\ y-3^k=1 \end{cases} \implies 2\cdot 3^k = 54 \implies 3^k = 27 \implies k=3, y=28, x=6$。<br>
          B組 $\begin{cases} y+3^k=11 \\ y-3^k=5 \end{cases} \implies 2\cdot 3^k = 6 \implies 3^k = 3 \implies k=1, y=8, x=2$。<br>
          <strong>結論</strong>：正整數解僅有 $(x, y) \in \{(2, 8), (6, 28)\}$。證畢。
        </div>
      </div>
    </div>

    <div class="page-bottom-footer">
      <span>中學數理資優教研白皮書 ｜ woieyufan EDUCATION</span>
      <span class="footer-center">第五篇：數論與構造（下）</span>
      <span>PAGE 06</span>
    </div>
  </div>
'''

def get_page_7():
    return r'''
  <!-- PAGE 7: ALGEBRA I -->
  <div class="section-page">
    <div class="page-top-header">
      <span class="header-left">PILLAR II: ALGEBRA ｜ 代數支柱（上）：多項式、韋達定理與牛頓和</span>
      <div class="header-right">
        <img class="header-logo-mini" src="__LOGO_DATA_URI__" alt="Mini Logo">
        <span>woieyufan EDUCATION</span>
      </div>
    </div>

    <div class="chapter-header-box">
      <span class="chapter-tag">支柱二 ｜ 代數結構</span>
      <div class="chapter-title">韋達定理推廣、初等對稱多項式與牛頓和</div>
      <p class="chapter-desc">以根與係數全局對稱結構，解構高次方程、對稱式降維與數列遞迴關係</p>
    </div>

    <div class="hero-statement">
      ★ 代數第一性原理：<br>
      方程的本質是「對稱的投影」。不必求解出每一個具體複數根，透過根與係數的整體關係（初等對稱多項式 $e_k$），即可完全控制所有高次冪和 $p_k = \sum x_i^k$ 的演化軌跡！
    </div>

    <div class="two-col-grid">
      <!-- VIETA FORMULA -->
      <div class="concept-card concept-card-emerald">
        <div class="card-title">1. 高次方程韋達定理 (Vieta's Formulas)</div>
        <p style="font-size: 12px; margin: 0; line-height: 1.5; color: #334155;">
          設 $P(x) = a_n x^n + a_{n-1} x^{n-1} + \dots + a_0 = a_n \prod_{i=1}^n (x - x_i)$。<br>
          展開後對比同次項係數，定義初等對稱多項式：
          $$e_1 = \sum_{i=1}^n x_i = -\frac{a_{n-1}}{a_n}, \quad e_2 = \sum_{i<j} x_i x_j = \frac{a_{n-2}}{a_n}$$
          $$e_k = \sum_{1 \le i_1 < \dots < i_k \le n} x_{i_1}\cdots x_{i_k} = (-1)^k \frac{a_{n-k}}{a_n}$$
        </p>
      </div>

      <!-- NEWTON SUMS -->
      <div class="concept-card concept-card-indigo">
        <div class="card-title">2. 牛頓和公式 (Newton's Sums)</div>
        <p style="font-size: 12px; margin: 0; line-height: 1.5; color: #334155;">
          定義根的 $k$ 次冪和 $p_k = x_1^k + x_2^k + \dots + x_n^k$。則對任意首一多項式 $x^n - e_1 x^{n-1} + \dots + (-1)^n e_n = 0$，有遞迴關係：
          $$p_1 - e_1 = 0$$
          $$p_2 - e_1 p_1 + 2e_2 = 0$$
          $$p_k - e_1 p_{k-1} + e_2 p_{k-2} - \dots + (-1)^k k e_k = 0 \quad (k \le n)$$
        </p>
      </div>
    </div>

    <div class="section-title">3. 高中銜接：立方和差與高次因式分解（忠孝國中加強專題）</div>
    <div class="para">
      超越課綱平方差公式，資優生必須熟練運用高階因式分解恆等式：
    </div>

    <table class="doc-table">
      <thead>
        <tr>
          <th style="width: 30%;">公式名稱</th>
          <th style="width: 45%;">因式分解代數恆等式</th>
          <th style="width: 25%;">重要應用情境</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>立方和與差公式</strong></td>
          <td>$a^3 \pm b^3 = (a \pm b)(a^2 \mp ab + b^2)$</td>
          <td>三次對稱方程、根式有理化</td>
        </tr>
        <tr>
          <td><strong>高次二項差推廣</strong></td>
          <td>$x^n - 1 = (x - 1)(x^{n-1} + x^{n-2} + \dots + x + 1)$</td>
          <td>等比數列求和、梅森質數判別</td>
        </tr>
        <tr>
          <td><strong>三元三次古典對稱式</strong></td>
          <td>$a^3 + b^3 + c^3 - 3abc = (a+b+c)(a^2+b^2+c^2 - ab - bc - ca)$</td>
          <td>條件等式：若 $a+b+c=0$，則 $a^3+b^3+c^3 = 3abc$</td>
        </tr>
      </tbody>
    </table>

    <div class="problem-box">
      <div class="problem-header"><span class="annot-target" id="annot-p7">【經典真題 2.1】</span> 牛頓和與高次對稱聯立方程組</div>
      <p style="margin: 0 0 4px 0;">設實數 $x, y, z$ 滿足 $x+y+z = 3$，$x^2+y^2+z^2 = 9$，$x^3+y^3+z^3 = 27$。求 $x^4+y^4+z^4$ 之值。</p>
      <div class="proof-box">
        <div class="proof-step"><span class="step-num">Step 1：</span> 設 $x, y, z$ 為三次多項式 $P(t) = t^3 - e_1 t^2 + e_2 t - e_3 = 0$ 的三根。已知 $p_1 = 3, p_2 = 9, p_3 = 27$。</div>
        <div class="proof-step"><span class="step-num">Step 2：</span> 由韋達與牛頓和：$e_1 = p_1 = 3$。又 $p_2 - e_1 p_1 + 2e_2 = 0 \implies 9 - 3(3) + 2e_2 = 0 \implies e_2 = 0$。</div>
        <div class="proof-step"><span class="step-num">Step 3：</span> 再看三次牛頓和：$p_3 - e_1 p_2 + e_2 p_1 - 3e_3 = 0 \implies 27 - 3(9) + 0 - 3e_3 = 0 \implies e_3 = 0$。</div>
        <div class="proof-step"><span class="step-num">Step 4：</span> 故此方程為 $t^3 - 3t^2 = t^2(t - 3) = 0$。其三根為 $3, 0, 0$。因此 $x^4+y^4+z^4 = 3^4 + 0^4 + 0^4 = 81$。證畢。</div>
      </div>
    </div>

    <div class="page-bottom-footer">
      <span>中學數理資優教研白皮書 ｜ woieyufan EDUCATION</span>
      <span class="footer-center">第六篇：代數結構與多項式（上）</span>
      <span>PAGE 07</span>
    </div>
  </div>
'''

def get_page_8():
    return r'''
  <!-- PAGE 8: ALGEBRA II -->
  <div class="section-page">
    <div class="page-top-header">
      <span class="header-left">PILLAR II: ALGEBRA ｜ 代數支柱（下）：經典競賽不等式大一統</span>
      <div class="header-right">
        <img class="header-logo-mini" src="__LOGO_DATA_URI__" alt="Mini Logo">
        <span>woieyufan EDUCATION</span>
      </div>
    </div>

    <div class="chapter-header-box">
      <span class="chapter-tag">支柱二 ｜ 不等式鏈</span>
      <div class="chapter-title">柯西-施瓦茨幾何視角與 AM-GM 構造</div>
      <p class="chapter-desc">以 $n$ 維歐氏向量空間內積為幾何核心，大一統代數不等式之局部化與齊次化技巧</p>
    </div>

    <div class="two-col-grid">
      <!-- CAUCHY SCHWARZ -->
      <div class="concept-card concept-card-emerald">
        <div class="card-title">1. 柯西-施瓦茨不等式 (Cauchy-Schwarz)</div>
        <p style="font-size: 12px; margin: 0; line-height: 1.5; color: #334155;">
          對任意實數 $a_i, b_i$：
          $$\left(\sum_{i=1}^n a_i^2\right)\left(\sum_{i=1}^n b_i^2\right) \ge \left(\sum_{i=1}^n a_i b_i\right)^2$$
          <strong>幾何內積視角</strong>：設 $\vec{u} = (a_1, \dots, a_n), \vec{v} = (b_1, \dots, b_n)$。由 $\vec{u}\cdot\vec{v} = \|\vec{u}\|\|\vec{v}\|\cos\theta$ 且 $|\cos\theta| \le 1$ 立得！等號成立 $\iff \vec{u} \parallel \vec{v}$。
        </p>
      </div>

      <!-- BERGSTROM / FRONTAL CAUCHY -->
      <div class="concept-card concept-card-indigo">
        <div class="card-title">2. 安杜因柯西分式形式 (Bergström)</div>
        <p style="font-size: 12px; margin: 0; line-height: 1.5; color: #334155;">
          對任意實數 $x_i$ 與正實數 $y_i > 0$：
          $$\frac{x_1^2}{y_1} + \frac{x_2^2}{y_2} + \dots + \frac{x_n^2}{y_n} \ge \frac{(x_1 + x_2 + \dots + x_n)^2}{y_1 + y_2 + \dots + y_n}$$
          此形式是解決競賽中「分母為多項和、分子為單項」對稱分式不等式的終極武器。
        </p>
      </div>
    </div>

    <div class="section-title">3. 算幾不等式 (AM-GM) 及其柯西倒推歸納法</div>
    <div class="para">
      對任意非負實數 $a_1, \dots, a_n \ge 0$：$\frac{a_1 + \dots + a_n}{n} \ge \sqrt[n]{a_1 \cdots a_n}$。柯西獨創的<strong>「倒推歸納法 (Forward-Backward Induction)」</strong>是資優證明思維之典範：先證明 $n=2$，再推導 $n=2^k$（前向倍增），最後藉由設 $a_n = \text{前 } n-1 \text{ 項算術平均}$ 逆向回推至任意 $n-1$！
    </div>

    <div class="problem-box">
      <div class="problem-header"><span class="annot-target" id="annot-p8">【奧林匹克經典名題 2.2】</span> 分子補全與安杜因分式柯西證明 Nesbitt 不等式</div>
      <p style="margin: 0 0 4px 0;">設 $a, b, c > 0$，求證：$\frac{a}{b + c} + \frac{b}{c + a} + \frac{c}{a + b} \ge \frac{3}{2}$。</p>
      <div class="proof-box">
        <div class="proof-step"><span class="step-num">Step 1（分子補全構造）：</span>
          左式各項加 1：$\left(\frac{a}{b+c} + 1\right) + \left(\frac{b}{c+a} + 1\right) + \left(\frac{c}{a+b} + 1\right) = (a+b+c)\left(\frac{1}{b+c} + \frac{1}{c+a} + \frac{1}{a+b}\right)$。
        </div>
        <div class="proof-step"><span class="step-num">Step 2（應用安杜因分式柯西）：</span>
          $$\frac{1^2}{b+c} + \frac{1^2}{c+a} + \frac{1^2}{a+b} \ge \frac{(1+1+1)^2}{(b+c)+(c+a)+(a+b)} = \frac{9}{2(a+b+c)}$$
        </div>
        <div class="proof-step"><span class="step-num">Step 3（整體代回）：</span>
          $$(a+b+c)\left(\frac{1}{b+c} + \frac{1}{c+a} + \frac{1}{a+b}\right) \ge (a+b+c) \cdot \frac{9}{2(a+b+c)} = \frac{9}{2}$$
          兩邊同時減去 3，即得：$\frac{a}{b+c} + \frac{b}{c+a} + \frac{c}{a+b} \ge \frac{9}{2} - 3 = \frac{3}{2}$。等號成立 $\iff a = b = c$。證畢。
        </div>
      </div>
    </div>

    <div class="page-bottom-footer">
      <span>中學數理資優教研白皮書 ｜ woieyufan EDUCATION</span>
      <span class="footer-center">第七篇：代數結構與不等式（下）</span>
      <span>PAGE 08</span>
    </div>
  </div>
'''

def get_page_9():
    return r'''
  <!-- PAGE 9: GEOMETRY I -->
  <div class="section-page">
    <div class="page-top-header">
      <span class="header-left">PILLAR III: GEOMETRY ｜ 幾何支柱（上）：塞瓦、梅涅勞斯與共點共線</span>
      <div class="header-right">
        <img class="header-logo-mini" src="__LOGO_DATA_URI__" alt="Mini Logo">
        <span>woieyufan EDUCATION</span>
      </div>
    </div>

    <div class="chapter-header-box">
      <span class="chapter-tag">支柱三 ｜ 射影幾何</span>
      <div class="chapter-title">塞瓦定理、梅涅勞斯定理與幾何中心大一統</div>
      <p class="chapter-desc">以射影積比代數化幾何構型，一統三角形三中線、三高線與三角平分線之共點性質</p>
    </div>

    <div class="hero-statement">
      ★ 幾何第一性原理：<br>
      共點與共線不是幾何的巧合，而是「長度有向比之乘積守恆」。塞瓦 (Ceva) 與梅涅勞斯 (Menelaus) 是射影幾何的孿生雙子星，將複雜的輔助線作圖轉化為代數連乘積！
    </div>

    <div class="two-col-grid">
      <!-- CEVA THEOREM -->
      <div class="concept-card concept-card-amber">
        <div class="card-title">1. 塞瓦定理 (Ceva's Theorem - 共點)</div>
        <p style="font-size: 12px; margin: 0; line-height: 1.5; color: #334155;">
          在 $\triangle ABC$ 中，點 $D, E, F$ 分別在邊 $BC, CA, AB$ 上。線段 $AD, BE, CF$ <strong>交於同一點 $P$ 的充要條件</strong>為：
          $$\frac{AF}{FB} \cdot \frac{BD}{DC} \cdot \frac{CE}{EA} = 1$$
          <em>角元形式 (Trig Ceva)</em>：$\frac{\sin\angle BAD}{\sin\angle CAD}\cdot\frac{\sin\angle CBE}{\sin\angle ABE}\cdot\frac{\sin\angle ACF}{\sin\angle BCF} = 1$。
        </p>
      </div>

      <!-- MENELAUS THEOREM -->
      <div class="concept-card concept-card-indigo">
        <div class="card-title">2. 梅涅勞斯定理 (Menelaus's Theorem - 共線)</div>
        <p style="font-size: 12px; margin: 0; line-height: 1.5; color: #334155;">
          若一條直線截 $\triangle ABC$ 的三邊直線 $BC, CA, AB$ 於點 $D, E, F$，則：
          $$\frac{AF}{FB} \cdot \frac{BD}{DC} \cdot \frac{CE}{EA} = 1$$
          <em>注意</em>：三交點中必有 1 個或 3 個點位於三角形邊的外延長線上。
        </p>
      </div>
    </div>

    <div class="section-title">3. 塞瓦定理一統三角形三大心共點之嚴密推導</div>
    <table class="doc-table">
      <thead>
        <tr>
          <th style="width: 20%;">幾何中心</th>
          <th style="width: 32%;">分比條件與幾何性質</th>
          <th style="width: 28%;">塞瓦積比計算</th>
          <th style="width: 20%;">共點結論</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>重心 $G$</strong><br>(Centroid)</td>
          <td>三邊中點：$AF=FB, BD=DC, CE=EA$</td>
          <td>$\frac{1}{1} \cdot \frac{1}{1} \cdot \frac{1}{1} = 1$</td>
          <td>三中線必共點於 $G$</td>
        </tr>
        <tr>
          <td><strong>內心 $I$</strong><br>(Incenter)</td>
          <td>內角平分線定理：$\frac{BD}{DC}=\frac{c}{b}, \frac{CE}{EA}=\frac{a}{c}, \frac{AF}{FB}=\frac{b}{a}$</td>
          <td>$\frac{b}{a} \cdot \frac{c}{b} \cdot \frac{a}{c} = 1$</td>
          <td>三內角平分線必共點於 $I$</td>
        </tr>
        <tr>
          <td><strong>垂心 $H$</strong><br>(Orthocenter)</td>
          <td>直角射影：$AF=b\cos A, FB=a\cos B$<br>$BD=c\cos B, DC=b\cos C$<br>$CE=a\cos C, EA=c\cos A$</td>
          <td>$\frac{b\cos A}{a\cos B}\cdot\frac{c\cos B}{b\cos C}\cdot\frac{a\cos C}{c\cos A} = 1$</td>
          <td>三高線必共點於 $H$</td>
        </tr>
      </tbody>
    </table>

    <div class="problem-box">
      <div class="problem-header"><span class="annot-target" id="annot-p9">【真題示範 3.1】</span> 塞瓦逆定理快速破解幾何比例問題</div>
      <p style="margin: 0 0 4px 0;">在 $\triangle ABC$ 中，$D$ 在 $BC$ 上滿足 $BD:DC = 2:3$，$E$ 在 $AC$ 上滿足 $CE:EA = 1:2$。$AD$ 與 $BE$ 交於點 $P$，$CP$ 延長線交 $AB$ 於 $F$。求 $AF:FB$ 之值。</p>
      <div class="proof-box">
        <div class="proof-step"><span class="step-num">Step 1：</span> 因 $AD, BE, CF$ 共點於 $P$，由塞瓦定理：$\frac{AF}{FB} \cdot \frac{BD}{DC} \cdot \frac{CE}{EA} = 1$。</div>
        <div class="proof-step"><span class="step-num">Step 2：</span> 代入已知數值：$\frac{AF}{FB} \cdot \left(\frac{2}{3}\right) \cdot \left(\frac{1}{2}\right) = 1 \implies \frac{AF}{FB} \cdot \frac{1}{3} = 1 \implies \frac{AF}{FB} = 3$。即 $AF:FB = 3:1$。快速破局！</div>
      </div>
    </div>

    <div class="page-bottom-footer">
      <span>中學數理資優教研白皮書 ｜ woieyufan EDUCATION</span>
      <span class="footer-center">第八篇：幾何與變換思維（上）</span>
      <span>PAGE 09</span>
    </div>
  </div>
'''

def get_page_10():
    return r'''
  <!-- PAGE 10: GEOMETRY II -->
  <div class="section-page">
    <div class="page-top-header">
      <span class="header-left">PILLAR III: GEOMETRY ｜ 幾何支柱（下）：圓冪、根軸與反演幾何</span>
      <div class="header-right">
        <img class="header-logo-mini" src="__LOGO_DATA_URI__" alt="Mini Logo">
        <span>woieyufan EDUCATION</span>
      </div>
    </div>

    <div class="chapter-header-box">
      <span class="chapter-tag">支柱三 ｜ 圓冪系統</span>
      <div class="chapter-title">圓方冪、根軸根心與幾何反演變換</div>
      <p class="chapter-desc">解密四點共圓判定終極工具，利用根軸連心垂直性與反演變換實現幾何降維</p>
    </div>

    <div class="two-col-grid">
      <!-- POWER OF A POINT -->
      <div class="concept-card concept-card-amber">
        <div class="card-title">1. 圓冪定理 (Power of a Point)</div>
        <p style="font-size: 12px; margin: 0; line-height: 1.5; color: #334155;">
          過點 $P$ 引圓 $O$（半徑 $R$）的任一割線交圓於 $A, B$。定義點 $P$ 關於圓 $O$ 的<strong>方冪</strong>為：
          $$\mathcal{P}(P) = \vec{PA}\cdot\vec{PB} = d^2 - R^2 \quad (d = PO)$$
          • 若 $P$ 在圓外，$\mathcal{P}(P) = PT^2$（切線長平方）。<br>
          • <strong>相交弦定理與割線定理</strong>均為圓冪定理的直接特例！
        </p>
      </div>

      <!-- RADICAL AXIS & CENTER -->
      <div class="concept-card concept-card-indigo">
        <div class="card-title">2. 根軸 (Radical Axis) 與根心定理</div>
        <p style="font-size: 12px; margin: 0; line-height: 1.5; color: #334155;">
          <strong>根軸定理</strong>：對兩圓 $\omega_1, \omega_2$ 方冪相等的點的軌跡為一條直線，且<strong>垂直於兩圓連心線 $O_1O_2$</strong>。若兩圓相交，根軸即為公共弦！<br>
          <strong>根心定理</strong>：三個圓心不共線的圓，其兩兩之根軸共點，該點稱為<strong>根心</strong>。
        </p>
      </div>
    </div>

    <div class="section-title">3. 托勒密定理 (Ptolemy's Theorem) 與反演變換 (Inversion)</div>
    <div class="para">
      <strong>托勒密定理</strong>：圓內接四邊形 $ABCD$ 兩對角線乘積等於兩組對邊乘積之和：$AC \cdot BD = AB \cdot CD + BC \cdot DA$。若四點不共圓，則嚴格大於（托勒密不等式）。  
      <strong>反演變換 (Circle Inversion)</strong>：以 $O$ 為反演中心、半徑 $R$ 的反演變換將過 $O$ 的圓映為直線，將不過 $O$ 的圓映為圓。反演將共圓問題降維為共線問題，是 IMO 幾何競賽之終極大招。
    </div>

    <div class="problem-box">
      <div class="problem-header"><span class="annot-target" id="annot-p10">【第九屆國中奧林匹克真題 3.2】</span> 根軸系統證明四點共圓</div>
      <p style="margin: 0 0 4px 0;">在銳角 $\triangle ABC$ 中，$BE, CF$ 為兩高。$M$ 為 $BC$ 中點。試證明：$E, F, M$ 與 $\triangle ABC$ 垂心 $H$ 之相關圓共點性質。</p>
      <div class="proof-box">
        <div class="proof-step"><span class="step-num">Step 1：</span> 考察四邊形 $BCEF$。因 $\angle BEC = \angle BFC = 90^\circ$，$B, C, E, F$ 四點共圓於 $\omega_1$（以直角三角形斜邊中點 $M$ 為圓心，$BC$ 為直徑）。</div>
        <div class="proof-step"><span class="step-num">Step 2：</span> 考察四邊形 $AFHE$。因 $\angle AFH + \angle AEH = 90^\circ+90^\circ = 180^\circ$，$A, F, H, E$ 四點共圓於 $\omega_2$（以 $AH$ 為直徑）。</div>
        <div class="proof-step"><span class="step-num">Step 3：</span> 兩圓 $\omega_1, \omega_2$ 的公共弦為 $EF$。由圓冪定理，過 $A$ 點的直線滿足 $AF \cdot AB = AE \cdot AC$。這正是點 $A$ 對兩圓方冪相等之體現，根軸 $EF \perp AH$！證畢。</div>
      </div>
    </div>

    <div class="page-bottom-footer">
      <span>中學數理資優教研白皮書 ｜ woieyufan EDUCATION</span>
      <span class="footer-center">第九篇：幾何與變換思維（下）</span>
      <span>PAGE 10</span>
    </div>
  </div>
'''

def get_page_11():
    return r'''
  <!-- PAGE 11: COMBINATORICS I -->
  <div class="section-page">
    <div class="page-top-header">
      <span class="header-left">PILLAR IV: COMBINATORICS ｜ 組合支柱（上）：鴿籠原理與雙重計數</span>
      <div class="header-right">
        <img class="header-logo-mini" src="__LOGO_DATA_URI__" alt="Mini Logo">
        <span>woieyufan EDUCATION</span>
      </div>
    </div>

    <div class="chapter-header-box">
      <span class="chapter-tag">支柱四 ｜ 離散組合</span>
      <div class="chapter-title">狄利克雷抽屜原理、連續度量覆蓋與算兩次</div>
      <p class="chapter-desc">超越枚舉計數，建立存在性證明、等價分類構造與圖論關聯矩陣 Fubini 思想</p>
    </div>

    <div class="hero-statement">
      ★ 組合第一性原理：<br>
      組合問題的本質是「有限容量與無限映射的衝突」。狄利克雷鴿籠原理不直接計算個體，而是以測度的有限性鎖定「碰撞必然發生」；算兩次則透過不同維度的對稱統計，恆等消去中間變數！
    </div>

    <div class="two-col-grid">
      <!-- PIGEONHOLE EXTENSION -->
      <div class="concept-card concept-card-rose">
        <div class="card-title">1. 鴿籠原理推廣與連續形式</div>
        <p style="font-size: 12px; margin: 0; line-height: 1.5; color: #334155;">
          <strong>廣義形式</strong>：若 $N$ 個物體放入 $k$ 個盒子，則至少有一個盒子含有 $\lceil \frac{N}{k} \rceil$ 個物體。<br>
          <strong>連續度量形式</strong>：若測度為 $L$ 的幾何區域被 $n$ 個子區域覆蓋，則至少存在一個子區域測度 $\ge \frac{L}{n}$。<br>
          <em>難點所在</em>：題目從不點明鴿子與籠子，勝負全在<strong>構造適當的分類等價關係</strong>。
        </p>
      </div>

      <!-- DOUBLE COUNTING -->
      <div class="concept-card concept-card-indigo">
        <div class="card-title">2. 算兩次 (Double Counting / Fubini)</div>
        <p style="font-size: 12px; margin: 0; line-height: 1.5; color: #334155;">
          同一個二元關係矩陣，按「行」求和與按「列」求和總量必相等：
          $$\sum_{x \in X} \deg(x) = \sum_{y \in Y} \deg(y)$$
          <strong>圖論握手定理 (Handshaking Lemma)</strong>：任何無向圖中，所有頂點度數之和等於邊數的 2 倍（$\sum \deg(v) = 2|E|$）。推論：<strong>奇數度頂點必為偶數個</strong>！
        </p>
      </div>
    </div>

    <div class="section-title">3. 經典專題：數集整除性構造（Erdős 經典鴿籠問題）</div>
    <div class="para">
      <strong>【定理】</strong> 從數集 $\{1, 2, 3, \dots, 2n\}$ 中任意取出 $n+1$ 個數，必定存在兩個數 $a, b$ 使得 $a \mid b$。
    </div>

    <div class="proof-box">
      <div class="proof-step"><span class="step-num">Step 1（構造等價類 - 籠子）：</span>
        利用算術基本定理，任意正整數 $x \in \{1, \dots, 2n\}$ 皆可唯一表示為 $x = 2^k \cdot m$，其中 $k \ge 0$，$m$ 為奇數。
      </div>
      <div class="proof-step"><span class="step-num">Step 2（統計籠子個數）：</span>
        在 $1$ 到 $2n$ 之間，奇數恰好為 $1, 3, 5, \dots, 2n-1$，共計恰有 $n$ 個相異奇數。以這 $n$ 個奇數作為 $n$ 個籠子的標籤。
      </div>
      <div class="proof-step"><span class="step-num">Step 3（應用鴿籠原理）：</span>
        從集合中取出 $n+1$ 個數（$n+1$ 隻鴿子）。由鴿籠原理，必有至少兩個數 $x_1, x_2$ 落入同一個奇數籠中，即：$x_1 = 2^{k_1} m, x_2 = 2^{k_2} m$。不妨設 $k_1 < k_2$，則顯然 $x_1 \mid x_2$！證畢。
      </div>
    </div>

    <div class="problem-box">
      <div class="problem-header"><span class="annot-target" id="annot-p11">【幾何幾值範例 4.1】</span> 單位正方形中 5 個點的直徑極值</div>
      <p style="margin: 0 0 4px 0;">在邊長為 1 的正方形內任取 5 個點，證明必存在兩點距離不大於 $\frac{\sqrt{2}}{2}$。</p>
      <div class="proof-box">
        將正方形四等分為 4 個邊長為 $\frac{1}{2}$ 的全等小正方形。由鴿籠原理，5 個點放入 4 個小正方形，必有兩點在同一個小正方形內。小正方形內兩點最大距離為對角線長度：$d_{\max} = \sqrt{(1/2)^2 + (1/2)^2} = \frac{\sqrt{2}}{2}$。證畢。
      </div>
    </div>

    <div class="page-bottom-footer">
      <span>中學數理資優教研白皮書 ｜ woieyufan EDUCATION</span>
      <span class="footer-center">第十篇：組合與極值思維（上）</span>
      <span>PAGE 11</span>
    </div>
  </div>
'''

def get_page_12():
    return r'''
  <!-- PAGE 12: COMBINATORICS II -->
  <div class="section-page">
    <div class="page-top-header">
      <span class="header-left">PILLAR IV: COMBINATORICS ｜ 組合支柱（下）：不變量原理與離散博弈</span>
      <div class="header-right">
        <img class="header-logo-mini" src="__LOGO_DATA_URI__" alt="Mini Logo">
        <span>woieyufan EDUCATION</span>
      </div>
    </div>

    <div class="chapter-header-box">
      <span class="chapter-tag">支柱四 ｜ 動態演化</span>
      <div class="chapter-title">不變量、半不變量勢能函數與極值原理</div>
      <p class="chapter-desc">掌握在動態狀態轉移中提煉守恆量之核心技巧，一招破解染色覆蓋與演算法終止性</p>
    </div>

    <div class="two-col-grid">
      <!-- INVARIANTS -->
      <div class="concept-card concept-card-rose">
        <div class="card-title">1. 不變量原理 (Invariant Principle)</div>
        <p style="font-size: 12px; margin: 0; line-height: 1.5; color: #334155;">
          在離散變換進程中，定義狀態函數 $I(S)$。若在每一步允許的操作下，始終有 $I(S_{t+1}) = I(S_t)$，則 $I(S)$ 為<strong>不變量</strong>。<br>
          <strong>不可達性判定</strong>：若目標狀態 $S^*$ 的 $I(S^*) \ne I(S_0)$，則<strong>目標狀態絕對不可達</strong>！常見不變量：奇偶性、模餘數、代數交叉積。
        </p>
      </div>

      <!-- MONOVARIANTS -->
      <div class="concept-card concept-card-emerald">
        <div class="card-title">2. 半不變量 (Monovariant / 勢能法)</div>
        <p style="font-size: 12px; margin: 0; line-height: 1.5; color: #334155;">
          構造映射至有下界非負整數的勢能函數 $\Phi(S)$。若每次操作滿足 $\Phi(S_{t+1}) < \Phi(S_t)$，則：<br>
          1. <strong>有限步終止性</strong>：此動態進程必在有限步內停止。<br>
          2. <strong>終態特徵</strong>：當無法再操作時，系統必處於 $\Phi$ 之局部極小態。
        </p>
      </div>
    </div>

    <div class="section-title">3. 經典名題精解：殘缺棋盤骨牌覆蓋之不可行性證明</div>
    <div class="problem-box">
      <div class="problem-header"><span class="annot-target" id="annot-p12">【不變量經典名題 4.2】</span> $8 \times 8$ 殘缺棋盤與黑白染色不變量</div>
      <p style="margin: 0 0 4px 0;">從 $8 \times 8$ 棋盤中剪去對角線上的兩個角落格子（剩餘 62 格）。問：是否能用 31 塊 $1 \times 2$ 的骨牌完全覆蓋？</p>
      <div class="proof-box">
        <div class="proof-step"><span class="step-num">Step 1（構造黑白染色幾何模型）：</span>
          標準 $8 \times 8$ 棋盤黑白相間著色，恰有 32 個黑格與 32 個白格。
        </div>
        <div class="proof-step"><span class="step-num">Step 2（考察被剪角落格之顏色）：</span>
          主對角線上的格子顏色相同（座標 $(1,1)$ 與 $(8,8)$ 之和 $1+1=2, 8+8=16$ 均為偶數，屬同色）。因此剪去的兩個格子必全為<strong>同色</strong>（設為黑格）。
        </div>
        <div class="proof-step"><span class="step-num">Step 3（統計剩餘格子）：</span>
          殘缺棋盤中，黑格僅剩 $32 - 2 = 30$ 個，白格仍有 32 個。
        </div>
        <div class="proof-step"><span class="step-num">Step 4（提煉骨牌覆蓋不變量）：</span>
          任意一塊 $1 \times 2$ 骨牌放置於棋盤上，無論橫向或豎向，<strong>必然恰好覆蓋 1 個黑格與 1 個白格</strong>。
          若 31 塊骨牌能夠覆蓋，則其覆蓋的黑格數必為 31，白格數必為 31。
        </div>
        <div class="proof-step"><span class="step-num">Step 5（導出矛盾）：</span>
          但殘缺棋盤只有 30 個黑格，需要 31 個黑格方能覆蓋。矛盾！故<strong>絕對不可能完全覆蓋</strong>。證畢。
        </div>
      </div>
    </div>

    <div class="page-bottom-footer">
      <span>中學數理資優教研白皮書 ｜ woieyufan EDUCATION</span>
      <span class="footer-center">第十一篇：組合與極值思維（下）</span>
      <span>PAGE 12</span>
    </div>
  </div>
'''
