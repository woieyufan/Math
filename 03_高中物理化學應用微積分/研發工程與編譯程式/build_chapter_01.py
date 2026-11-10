# -*- coding: utf-8 -*-
"""
Generate Chapter 1 text for the precollege calculus monograph according to Blue Paper Book & Dojo specs.
"""

ch01_content = r"""# 第一章：無窮小量階數與極限定義（代數非零與極限為零的本質破局）
**Chapter 1: Orders of Infinitesimals and the Limit Definition: Resolving the Non-Zero Algebraic and Zero Limit Duality**

---

## 導讀手札（Prologue）
中學物理與幾何中，所有關於「瞬時」與「平滑」的直觀，最終都匯聚於一個核心的矛盾：一個處於運動中的物體，在「某一瞬間」究竟有沒有速度？
如果「瞬間」意味著時間間隔為零，那麼位移也是零，速度似乎變成毫無意義的 $0/0$；如果時間間隔不為零，那麼測得的永遠只是「一段時間內的平均速度」，而非「當下那一瞬間的真實狀態」。

這個困擾了人類兩千年的「芝諾佯謬」，正是微積分誕生的產房。本章不追求抽象無味的符號遊戲，而是回歸笛卡兒座標系與伽利略運動學的第一性原理，剖析割線如何旋轉貼合為切線，破除「$0/0$ 未定式是除以零」的直觀誤解，並以嚴密的「無窮小量階數比較」，為整座微積分大廈奠定第一塊堅不可摧的基石。

---

## 1.1 割線斜率之代數商：變化的平均度量

考慮笛卡兒坐標系中的一條連續光滑曲線 $y = f(x)$。在曲線上任取一點 $P(x_0, f(x_0))$。為了探索曲線在 $P$ 點附近的彎曲走勢，我們在鄰近處取另一點 $Q(x_0 + \Delta x, f(x_0 + \Delta x))$，其中 $\Delta x$ 代表自變量的微小增量，且嚴格滿足 $\Delta x \neq 0$。

連接 $P$、$Q$ 兩點的直線稱為曲線的**割線（Secant Line）**。根據解析幾何，割線的斜率 $m_{\text{sec}}$ 即為函數增量 $\Delta y = f(x_0 + \Delta x) - f(x_0)$ 與自變量增量 $\Delta x$ 的代數比值：

$$\mathbf{Eq\ 1.1}\quad m_{\text{sec}} = \frac{f(x_0 + \Delta x) - f(x_0)}{\Delta x} \quad (\Delta x \neq 0)$$

```
[幾何圖規指示：Fig 1.1 割線斜率逼近與切線極限定義圖]
坐標系：橫軸 x，縱軸 y。
主曲線：拋物線 y = x^2。標定定點 P(1, 1)。
動點序列：標定 Q1(2, 4), Q2(1.5, 2.25), Q3(1.1, 1.21)。
動態軌跡：繪製連接 P 與各 Q 點的虛線割線，並用弧形箭頭標註割線繞 P 點逆時針旋轉，最終嚴密貼合為實線切線 T（斜率為 2）。
```

> **側欄手札 1.1【幾何量綱提示】**  
> 割線斜率是「商」而非純數。如果縱軸是位移（公尺），橫軸是時間（秒），則斜率的物理量綱為 $\mathrm{m/s}$。微分學的本質，是用兩個可觀測幾何量增量的比值，去逼近一個不可直接觀測的局域變化率。

---

## 1.2 破除幽靈微元：代數非零與極限為零的對立統一

在微積分誕生初期，哲學家貝克萊主教曾提出尖銳的質疑：「這些消失的微元是什麼？它們既不是有窮量，也不是無窮小，更不是無。難道它們是早已死去的量的幽靈嗎？」

貝克萊的質疑切中了舊微積分的邏輯漏洞：在推導切線斜率時，推導者往往在第一步將 $\Delta x$ 當作非零量放在分母進行約分，而在最後一步又將 $\Delta x$ 視為零直接拋棄。這種「任意變換假設」在邏輯學上被稱為**偷換假定（Fallacy of Equivocation）**。

現代極限論徹底終結了這一混亂。解決問題的關鍵在於將計算過程劃分為兩大嚴格的獨立階段：

1. **第一階段（代數除法階段，$\Delta x \neq 0$）**：此時 $\Delta x$ 是真實存在的非零實數，無論它多麼微小，只要 $\Delta x \neq 0$，將它放在分母作為除數完全合法，分子分母同除 $\Delta x$ 的因式分解在代數上無懈可擊。
2. **第二階段（極限定義階段，$\Delta x \to 0$）**：極限算子 $\lim_{\Delta x \to 0}$ 並非要求我們將 $\Delta x = 0$ 強行代入表達式，而是探詢當 $\Delta x$ 無限接近於零時，整個比值整體趨向的「目標數值」。

所謂的 $0/0$ 型未定式，絕不是數學上被嚴格禁止的「除以零」，而是指**分子與分母兩個變量同時趨向於零時，它們動態壓縮的比值收斂到某個確定的有限實數**。

由此，我們給出切線斜率的算子定義：

$$\mathbf{Eq\ 1.3}\quad f'(x_0) = \left. \frac{\mathrm{d}f}{\mathrm{d}x} \right|_{x=x_0} = \lim_{\Delta x \to 0} \frac{f(x_0 + \Delta x) - f(x_0)}{\Delta x}$$

> **側欄手札 1.2【思維陷阱警示】**  
> 絕不要把極限理解為「無限逼近但永遠達不到」的時間過程。極限是一個靜態且精確的實數。對於函數 $f(x)=c$（常數），其割線斜率恆為 0，極限也是 0。極限描述的是一種結構性的數值歸宿，而非物理上的奔跑。

---

## 1.3 無窮小量階數比較：誰消失得更快？

為了精準掌握極限過程中各項微元的命運，我們必須對「趨於零的速率」進行嚴格的度量。

設 $\alpha(\Delta x)$ 與 $\beta(\Delta x)$ 是當 $\Delta x \to 0$ 時極限均為零的兩個變量（稱為無窮小量）。若比值 $\alpha / \beta$ 在極限下仍為零，說明 $\alpha$ 趨於零的速度遠快於 $\beta$。我們將 $\alpha$ 稱為 $\beta$ 的**高階無窮小量**，記作 $\alpha = o(\beta)$：

$$\mathbf{Eq\ 1.2}\quad \lim_{\Delta x \to 0} \frac{o((\Delta x)^k)}{(\Delta x)^k} = 0 \quad (k \in \mathbb{N}^+)$$

```
[幾何圖規指示：Fig 1.2 高階無窮小幾何矩形面積壓縮圖]
坐標系：幾何圖形對比。
基準圖形：邊長為 1 與 Δx 的細長矩形，其面積為 Δx（一階無窮小）。
高階圖形：邊長為 Δx 與 Δx 的小正方形，其面積為 (Δx)^2（二階無窮小）。
動態縮放：展示當 Δx 從 0.1 縮小至 0.01 時，細長矩形面積縮小至 1/10，而小正方形面積劇烈縮小至 1/100，視覺化展示高階小量在面積意義上的微縮消融。
```

這項概念揭示了導數存在的本質：**光滑曲線的局域增量中，只有一階無窮小量能與自變量 $\Delta x$ 形成平衡的有限比值；所有二階及更高階小量，在除以 $\Delta x$ 之後全部坍縮為零。**

反之，若增量中包含低階無窮小量（例如 $\sqrt{\Delta x}$），則導數將發生發散：

$$\mathbf{Eq\ 1.7}\quad \lim_{\Delta x \to 0} \frac{\sqrt{\Delta x}}{\Delta x} = \lim_{\Delta x \to 0} \frac{1}{\sqrt{\Delta x}} = \infty$$

低階無窮小的存在意味著變化率無窮大，對應幾何上垂直切線或尖銳頂點（尖點、角點），此時函數不可導。

---

## 1.4 局部仿射線性逼近：微積分的工程靈魂

將導數定義式移項整理，我們可以得到微積分學中最具威力的結構式——**局部仿射線性逼近展開式（Local Affine Approximation）**：

$$\mathbf{Eq\ 1.4}\quad f(x_0 + \Delta x) = f(x_0) + f'(x_0)\Delta x + o(\Delta x)$$

這個公式告訴我們：在切點 $x_0$ 充分小的鄰域內，任意複雜的光滑非線性函數 $f(x)$，都可以拆解為三個部分：
1. **零階項 $f(x_0)$**：函數在當前點的靜態基準值；
2. **一階主部 $f'(x_0)\Delta x$**：切線帶來的線性增量修正（以固定斜率 $f'$ 延伸）；
3. **高階殘差 $o(\Delta x)$**：真實曲線與切線之間的偏差，其大小隨 $\Delta x \to 0$ 以平方甚至更高階的速度衰減。

```
[幾何圖規指示：Fig 1.3 局部仿射線性逼近與切線局部貼合圖]
主圖：非線性三次曲線 y = x^3 - x 在 x0 = 1 附近的起伏。
切線：直線 y = 2x - 1 精確切於 (1, 0)。
放大鏡視圖：以 (1, 0) 為中心畫出圓形放大鏡。鏡內展示局部視野放大 100 倍後的景象，非線性曲線與直線切線在肉眼上完全重合，視覺化論證「局部看，任何光滑曲線都是直線」。
```

工程與物理學中大量使用的「微小量近似公式」（例如 $\sqrt{1+x} \approx 1 + \frac{1}{2}x$、$\sin x \approx x$、$(1+x)^n \approx 1 + nx$），全部都是局部仿射線性逼近展開式的直接推論。微積分的核心靈魂，就是**「以直代曲，抓住一階主部，忽略高階微縮」**。

> **側欄手札 1.3【大一統視角】**  
> 線性代數研究的是平坦的線性空間，而微積分則是將彎曲的世界在局域切空間中「線性化」。微分不是別的，它正是非線性映射在局部切空間的最佳線性逼近算子。

---

## 1.5 物理落地：瞬時速度與自由落體加速度

在中學物理中，勻速直線運動的速度定義為 $v = \frac{\Delta x}{\Delta t}$。但當質點做變速運動（例如自由落體、彈簧振子、阻尼擺動）時，這個比值只能代表一段時間內的平均速度 $\bar{v}$。

如果我們想知道汽車在某一確切秒數瞬間時速表上的指針讀數，就必須將測量時間區間 $\Delta t$ 壓縮至極限。瞬時速度的嚴格定義，就是位置函數對時間的微商：

$$\mathbf{Eq\ 1.5}\quad v(t_0) = \lim_{\Delta t \to 0} \frac{x(t_0 + \Delta t) - x(t_0)}{\Delta t} = \left. \frac{\mathrm{d}x}{\mathrm{d}t} \right|_{t=t_0}$$

```
[幾何圖規指示：Fig 1.4 自由落體運動 s-t 拋物線與瞬時速度斜率圖]
坐標系：橫軸時間 t，縱軸位移 s。
軌跡：二次拋物線 s = (1/2)gt^2。
推導動線：在 t0 處作割線到 t0 + Δt，標註割線斜率 v_avg = gt0 + (1/2)gΔt。箭頭標註當 Δt 趨向 0 時，割線旋轉為切線，斜率收斂至精確數值 gt0。
```

現在，我們以第一性原理正面擊潰高中物理第一個核心公式——伽利略自由落體運動。
已知自由落體運動的位置方程為 $x(t) = \frac{1}{2}gt^2$。我們計算時間由 $t$ 到 $t + \Delta t$ 的位置增量：

$$\begin{aligned}
\Delta x &= x(t + \Delta t) - x(t) \\
&= \frac{1}{2}g(t + \Delta t)^2 - \frac{1}{2}gt^2 \\
&= \frac{1}{2}g\left(t^2 + 2t\Delta t + (\Delta t)^2\right) - \frac{1}{2}gt^2 \\
&= gt\Delta t + \frac{1}{2}g(\Delta t)^2
\end{aligned}$$

注意這裏的代數結構：增量由兩項組成，第一項 $gt\Delta t$ 是一階無窮小量，第二項 $\frac{1}{2}g(\Delta t)^2$ 是二階無窮小量。
現在計算平均速度（此時 $\Delta t \neq 0$）：

$$\bar{v} = \frac{\Delta x}{\Delta t} = \frac{gt\Delta t + \frac{1}{2}g(\Delta t)^2}{\Delta t} = gt + \frac{1}{2}g\Delta t$$

最後，讓極限算子作用於此代數商：

$$\mathbf{Eq\ 1.6}\quad v(t) = \lim_{\Delta t \to 0} \bar{v} = \lim_{\Delta t \to 0} \left(gt + \frac{1}{2}g\Delta t\right) = gt + 0 = gt$$

高中課本要求學生死記的「速度 $v = gt$」，在微積分框架下沒有任何神秘黑盒子。它不過是二項式展開中一次項係數的自然湧現，而殘留的二階項 $\frac{1}{2}g\Delta t$ 則在極限壓縮中無害地消融為零。

---

## 1.6 公理建構示範例題（Worked Examples）

### 例題 1.1（二階多項式導數之第一性原理推演）
**【題目】** 設函數 $f(x) = x^2$。請完全依據割線極限定義，給出求導的每一步嚴格無跳步推導，並驗證代數約分的合法性。

**【詳解】**
1. 設自變量有微小增量 $\Delta x$。在第一階段，嚴格保證 $\Delta x \neq 0$。
2. 計算函數值增量：
   $$\Delta y = f(x + \Delta x) - f(x) = (x + \Delta x)^2 - x^2 = x^2 + 2x\Delta x + (\Delta x)^2 - x^2 = 2x\Delta x + (\Delta x)^2$$
3. 建立割線斜率之差商（Difference Quotient）。由於 $\Delta x \neq 0$，分母非零，代數除法合法：
   $$m_{\text{sec}} = \frac{\Delta y}{\Delta x} = \frac{2x\Delta x + (\Delta x)^2}{\Delta x} = \frac{\Delta x (2x + \Delta x)}{\Delta x} = 2x + \Delta x$$
4. 引入極限算子。此時探求當 $\Delta x \to 0$ 時該差商之數值歸宿：
   $$f'(x) = \lim_{\Delta x \to 0} m_{\text{sec}} = \lim_{\Delta x \to 0} (2x + \Delta x) = 2x + \lim_{\Delta x \to 0}\Delta x = 2x + 0 = 2x$$
5. 結論：$(x^2)' = 2x$。推導過程中絕無「除以零」之謬誤，完全自洽。

---

### 例題 1.2（自由落體瞬時速度與二階小量分析）
**【題目】** 某物體從高塔自由墜落，運動規律為 $s(t) = 4.9t^2$（距離單位為公尺，時間單位為秒）。請計算其在 $t = 2\,\mathrm{s}$ 瞬時的速度，並證明在時間增量 $\Delta t = 0.001\,\mathrm{s}$ 時，二階小量殘差對真實速度的相對誤差小於 $0.03\%$。

**【詳解】**
1. 計算 $t = 2$ 時的平均速度表達式（$\Delta t \neq 0$）：
   $$\begin{aligned}
   \Delta s &= 4.9(2 + \Delta t)^2 - 4.9(2)^2 = 4.9(4 + 4\Delta t + (\Delta t)^2) - 19.6 \\
   &= 19.6\Delta t + 4.9(\Delta t)^2
   \end{aligned}$$
2. 計算差商：
   $$\bar{v} = \frac{\Delta s}{\Delta t} = 19.6 + 4.9\Delta t$$
3. 取極限得出瞬時速度：
   $$v(2) = \lim_{\Delta t \to 0} (19.6 + 4.9\Delta t) = 19.6\,\mathrm{m/s}$$
4. 當 $\Delta t = 0.001\,\mathrm{s}$ 時，實際平均速度為：
   $$\bar{v} = 19.6 + 4.9(0.001) = 19.6049\,\mathrm{m/s}$$
5. 殘差項為 $4.9\Delta t = 0.0049\,\mathrm{m/s}$。相對誤差為：
   $$\text{Relative Error} = \frac{0.0049}{19.6} = 0.00025 = 0.025\% < 0.03\%$$
   證畢。這定量證明了高階小量在極短時間內的物理影響完全可忽略。

---

### 例題 1.3（局部仿射逼近手算高精度根號值）
**【題目】** 利用局部仿射線性逼近公式 $f(x_0 + \Delta x) \approx f(x_0) + f'(x_0)\Delta x$，在不使用計算機的情況下手算估計 $\sqrt{101}$ 的數值，並分析誤差量階。

**【詳解】**
1. 選取母函數 $f(x) = \sqrt{x}$。
2. 尋找鄰近最容易精確求解的「基準點」：選取 $x_0 = 100$，此時 $f(x_0) = \sqrt{100} = 10$。
3. 計算增量：$\Delta x = 101 - 100 = 1$。
4. 依微商定義求 $f'(x) = \frac{1}{2\sqrt{x}}$ 在 $x_0 = 100$ 處的值：
   $$f'(100) = \frac{1}{2\sqrt{100}} = \frac{1}{20} = 0.05$$
5. 代入仿射逼近公式：
   $$\sqrt{101} = f(100 + 1) \approx f(100) + f'(100) \cdot (1) = 10 + 0.05 \cdot 1 = 10.05$$
6. 誤差分析：真實值平方檢驗 $(10.05)^2 = 101.0025$。誤差僅約 $0.0025/20 \approx 0.000124$，屬於 $(\Delta x)^2$ 階的高階無窮小量。

---

## 1.7 邊欄 Socratic 思辨深入剖析

### 思辨 1.1【破除分母為零的佯謬】
> **問**：若 $\Delta x$ 最終等於 $0$，為何開局可置於分母？若 $\Delta x \neq 0$，憑何在結尾直接令其為 $0$？  
> **答**：這是混淆了「運算變量」與「極限目標」。極限運算 $\lim_{\Delta x \to 0}$ 中的「$\to$」是單向逼近算子，不是等號。在整個代數簡化過程中，$\Delta x$ 恆為非零實數，因此分母非零合法；在最後一步，我們並非令 $\Delta x = 0$，而是求多項式 $2x + \Delta x$ 當 $\Delta x$ 無限趨近於 0 時的數值下確界與上確界之交集，該收斂值唯一確定為 $2x$。

### 思辨 1.2【「無限接近但不等於」的語言毒害】
> **問**：中學常說「極限就是無限接近但不等於」，這句話有何致命漏洞？  
> **答**：此話若成立，常數函數 $f(x) = 5$ 的極限將崩潰。當 $x \to 2$ 時，$f(x)$ 恆等於 5，它「等於」5 而不是「無限接近但不等於 5」。極限的真實數學定義是：只要給定任意小的容許誤差 $\epsilon > 0$，皆能找到自變量鄰域 $\delta > 0$，使函數值落入目標點的 $\epsilon$ 鄰域內。極限是完全可以「達到」的靜態實數。

### 思辨 1.3【切線的真正幾何定義】
> **問**：為何切線不能定義為「與曲線只交於一點的直線」？  
> **答**：初中圓幾何的經驗在此處是嚴重的認知障礙。考慮三次曲線 $y = x^3$，直線 $y = 0$ 在原點與曲線相交，且「直接穿透」曲線兩側。但 $y=0$ 依然是 $y=x^3$ 在原點的唯一真切線！切線的真正第一性原理是**「割線旋轉的極限位置」**，或是代數上**「聯立差式必定含有至少二重根」**。單點相交既非切線的充分條件，亦非必要條件。

---

## 1.8 課後階梯習題庫（Problem Ladder）

### Level 1: 基礎公理默寫與純數變換（Foundational Drills）

#### P1 1.1
請在白紙上閉卷默寫導數的極限定義式，並用文字嚴格解釋式中「$\Delta x \neq 0$」與「$\lim_{\Delta x \to 0}$」各自生效的代數時機。

#### P1 1.2
使用導數極限定義式，完全不跳步求函數 $f(x) = 3x^2 - 5x + 2$ 在 $x = 1$ 處的導數值。

#### P1 1.3
設無窮小量 $\alpha(\Delta x) = 3(\Delta x)^2 + 5\Delta x$。請判定當 $\Delta x \to 0$ 時，$\alpha(\Delta x)$ 相對於基準無窮小量 $\Delta x$ 是高階、同階還是低階無窮小，並求出極限值 $\lim_{\Delta x \to 0} \frac{\alpha(\Delta x)}{\Delta x}$。

#### P1 1.4
利用局部仿射線性逼近公式，手算估計 $(1.003)^{10}$ 的一階近似值，並指出其忽略的殘差項相對於 $0.003$ 的無窮小階數。

---

### Level 2: 自然科學跨學科實戰（Interdisciplinary Applications）

#### P2 1.1【古典力學：軌跡折返點判定】
一質點沿直線做一維運動，其位置函數為 $x(t) = t^3 - 6t^2 + 9t$（$t \ge 0$，長度單位為 $\mathrm{m}$，時間為 $\mathrm{s}$）。  
(1) 完全依據導數極限定義，推導速度函數 $v(t) = \frac{\mathrm{d}x}{\mathrm{d}t}$；  
(2) 求質點在哪些時刻瞬時速度為零，並從相空間位移變化解釋其物理上的「折返」意義。

#### P2 1.2【幾何光學：光程差極限變化率】
一束光自空氣射向平面玻璃界面。設光源位於坐標 $(0, h)$，動態觀測點沿界面移動，其橫坐標為 $x$。光程函數為 $S(x) = \sqrt{h^2 + x^2}$。  
(1) 利用微商定義求 $\frac{\mathrm{d}S}{\mathrm{d}x}$；  
(2) 解釋當 $x \gg h$ 時，該變化率的極限物理含義。

#### P2 1.3【熱學工程：金屬線膨脹微商定義】
已知金屬棒長度 $L$ 隨溫度 $T$ 變化。在參考溫度 $T_0$ 附近，長度增量表示為 $\Delta L = L_0 \alpha \Delta T + o(\Delta T)$。  
(1) 寫出線膨脹係數 $\alpha$ 的微商定義式；  
(2) 進行量綱檢驗，說明 $\alpha$ 的物理單位為何是 $\mathrm{K}^{-1}$。

#### P2 1.4【流體力學：圓柱水箱底孔漏水瞬時速率】
高度為 $H$、底面積為 $A$ 的圓柱形水箱，底部開孔放水。托里拆利定律導出水位隨時間變化規律為 $h(t) = H\left(1 - \frac{t}{T}\right)^2 \quad (0 \le t \le T)$，其中 $T$ 為排空總時間。  
(1) 利用極限定義計算任意時刻 $t$ 的瞬時水位下降速率 $-\frac{\mathrm{d}h}{\mathrm{d}t}$；  
(2) 比較剛開始放水（$t=0$）與即將排空（$t=T$）時的瞬時漏水速率比值。

---

### Level 3: 邊界奇異點與深水區挑戰（Deepwater Challenges）

#### P3 1.1【病態函數：處處不連續但在單點可導】
定義修改版狄利克雷函數如下：
$$f(x) = \begin{cases} x^2, & x \in \mathbb{Q} \\ 0, & x \notin \mathbb{Q} \end{cases}$$
該函數在除原點外所有點皆處處不連續。請嚴格利用導數極限定義，證明 $f(x)$ 在 $x = 0$ 處完全可導，並求出 $f'(0)$ 的確切數值。

#### P3 1.2【無窮小階數失守：高頻振盪奇異性】
考慮函數：
$$g(x) = \begin{cases} x \sin\left(\frac{1}{x}\right), & x \neq 0 \\ 0, & x = 0 \end{cases}$$
(1) 證明 $g(x)$ 在 $x=0$ 處連續；  
(2) 計算差商 $\frac{g(\Delta x) - g(0)}{\Delta x}$，並證明該差商在 $\Delta x \to 0$ 時極限不存在，從而論證 $g(x)$ 在原點不可導。

---

## 1.9 官方解答密鑰庫（Official Solutions Key）

### P1 1.1 解答
- **核心公式**：$f'(x_0) = \lim_{\Delta x \to 0} \frac{f(x_0+\Delta x) - f(x_0)}{\Delta x}$。
- **生效時機解密**：在計算比值 $\frac{\Delta y}{\Delta x}$ 期間，$\Delta x \neq 0$ 保證代數運算分母不為零，因式分解約分合法；在完成純代數化簡後，極限算子 $\lim_{\Delta x \to 0}$ 作用，求取無窮小逼近下的數值歸宿，並非代數代入。

### P1 1.2 解答
- **增量式**：
  $$\begin{aligned}
  f(1+\Delta x) - f(1) &= [3(1+\Delta x)^2 - 5(1+\Delta x) + 2] - [3(1)^2 - 5(1) + 2] \\
  &= [3(1 + 2\Delta x + (\Delta x)^2) - 5 - 5\Delta x + 2] - 0 \\
  &= 6\Delta x + 3(\Delta x)^2 - 5\Delta x = \Delta x + 3(\Delta x)^2
  \end{aligned}$$
- **差商計算**（$\Delta x \neq 0$）：$\frac{\Delta y}{\Delta x} = \frac{\Delta x (1 + 3\Delta x)}{\Delta x} = 1 + 3\Delta x$。
- **求極限**：$f'(1) = \lim_{\Delta x \to 0} (1 + 3\Delta x) = 1 + 0 = 1$。

### P1 1.3 解答
- **極限商**：$\lim_{\Delta x \to 0} \frac{3(\Delta x)^2 + 5\Delta x}{\Delta x} = \lim_{\Delta x \to 0} (3\Delta x + 5) = 5$。
- **階數判定**：由於極限為有限非零常數 $5 \neq 0$，$\alpha(\Delta x)$ 與 $\Delta x$ 屬於**同階無窮小量**（First-Order Infinitesimal）。

### P1 1.4 解答
- **仿射模型**：取 $f(x) = x^{10}$，基準點 $x_0 = 1$，增量 $\Delta x = 0.003$。
- **微商**：$f'(1) = 10(1)^9 = 10$。
- **一階估算**：$(1.003)^{10} \approx f(1) + f'(1)\Delta x = 1 + 10(0.003) = 1 + 0.03 = 1.03$。
- **殘差階數**：根據二項式定理，下一項為 $\binom{10}{2}(0.003)^2 = 45 \times 9 \times 10^{-6} \approx 0.000405$，為 $o(\Delta x)$ 即二階無窮小量。

### P2 1.1 解答
- **(1) 速度推導**：
  $$\begin{aligned}
  \Delta x &= (t+\Delta t)^3 - 6(t+\Delta t)^2 + 9(t+\Delta t) - (t^3 - 6t^2 + 9t) \\
  &= [3t^2\Delta t + 3t(\Delta t)^2 + (\Delta t)^3] - [12t\Delta t + 6(\Delta t)^2] + 9\Delta t \\
  &= (3t^2 - 12t + 9)\Delta t + o(\Delta t)
  \end{aligned}$$
  除以 $\Delta t$ 取極限得：$v(t) = 3t^2 - 12t + 9 = 3(t-1)(t-3)$。
- **(2) 折返時刻**：令 $v(t) = 0$，得 $t_1 = 1\,\mathrm{s}$ 與 $t_2 = 3\,\mathrm{s}$。在 $t \in [0, 1)$，速度為正（向前運動）；$t \in (1, 3)$，速度為負（向後運動，位移減小）；$t > 3$，速度重新為正（再次向前）。$t=1, 3$ 是速度變號的軌跡幾何折返點。

### P2 1.2 解答
- **(1) 微商推導**：
  $$\frac{\mathrm{d}S}{\mathrm{d}x} = \lim_{\Delta x \to 0} \frac{\sqrt{h^2 + (x+\Delta x)^2} - \sqrt{h^2 + x^2}}{\Delta x}$$
  分子有理化：
  $$\frac{2x\Delta x + (\Delta x)^2}{\Delta x \left(\sqrt{h^2 + (x+\Delta x)^2} + \sqrt{h^2 + x^2}\right)} = \frac{2x + \Delta x}{\sqrt{h^2 + (x+\Delta x)^2} + \sqrt{h^2 + x^2}} \to \frac{2x}{2\sqrt{h^2+x^2}} = \frac{x}{\sqrt{h^2+x^2}}$$
- **(2) 物理含義**：$\frac{x}{\sqrt{h^2+x^2}} = \cos\theta$（$\theta$ 為光線與界面的夾角）。當 $x \gg h$ 時，$x/\sqrt{h^2+x^2} \to 1$。這說明在遠距離處，光程增加率與水平位移完全等同（光線近乎平行於界面傳播）。

### P2 1.3 解答
- **(1) 微商定義**：$\alpha = \frac{1}{L_0} \left. \frac{\mathrm{d}L}{\mathrm{d}T} \right|_{T_0} = \frac{1}{L_0} \lim_{\Delta T \to 0} \frac{L(T_0+\Delta T) - L(T_0)}{\Delta T}$。
- **(2) 量綱檢驗**：$\frac{\mathrm{d}L}{\mathrm{d}T}$ 量綱為 $\mathrm{m/K}$，前面乘以 $\frac{1}{L_0}$（量綱為 $\mathrm{m}^{-1}$），兩者相乘 $\mathrm{m}^{-1} \cdot (\mathrm{m/K}) = \mathrm{K}^{-1}$。長度量綱完全消去，驗證膨脹係數為純溫度倒數量綱。

### P2 1.4 解答
- **(1) 漏水速率**：
  $$\begin{aligned}
  \Delta h &= H\left(1 - \frac{t+\Delta t}{T}\right)^2 - H\left(1 - \frac{t}{T}\right)^2 \\
  &= H\left[ \left(1 - \frac{t}{T}\right) - \frac{\Delta t}{T} \right]^2 - H\left(1 - \frac{t}{T}\right)^2 \\
  &= H\left[ -2\left(1 - \frac{t}{T}\right)\frac{\Delta t}{T} + \frac{(\Delta t)^2}{T^2} \right]
  \end{aligned}$$
  除以 $\Delta t$ 取極限：
  $$\frac{\mathrm{d}h}{\mathrm{d}t} = -\frac{2H}{T}\left(1 - \frac{t}{T}\right) \implies -\frac{\mathrm{d}h}{\mathrm{d}t} = \frac{2H}{T}\left(1 - \frac{t}{T}\right)$$
- **(2) 比值**：$t=0$ 時速率為 $\frac{2H}{T}$；$t=T$ 時速率為 $0$。剛開始放水時速率最大，隨水位降低水壓減小，漏水速率呈線性衰減至零。

### P3 1.1 解答
- **極限差商**：在原點處，$f(0) = 0$。任取增量 $\Delta x \neq 0$：
  $$\frac{f(0 + \Delta x) - f(0)}{\Delta x} = \frac{f(\Delta x)}{\Delta x}$$
- **分類討論**：
  - 當 $\Delta x \in \mathbb{Q}$ 時，$\frac{f(\Delta x)}{\Delta x} = \frac{(\Delta x)^2}{\Delta x} = \Delta x$；
  - 當 $\Delta x \notin \mathbb{Q}$ 時，$\frac{f(\Delta x)}{\Delta x} = \frac{0}{\Delta x} = 0$。
- **夾擠定理**：無論 $\Delta x$ 是有理數還是無理數，皆恆有 $0 \le \left|\frac{f(\Delta x)}{\Delta x}\right| \le |\Delta x|$。
- **極限收斂**：因為 $\lim_{\Delta x \to 0} |\Delta x| = 0$，由夾擠定理（Squeeze Theorem）必有：
  $$f'(0) = \lim_{\Delta x \to 0} \frac{f(\Delta x) - f(0)}{\Delta x} = 0$$
- **哲學啟示**：一個處處不連續的函數，可以在單點極其平滑且導數為零！這證明了可導性是純粹的局域極限性質。

### P3 1.2 解答
- **(1) 連續性證明**：因為 $|\sin(1/x)| \le 1$，所以 $|g(x) - g(0)| = |x \sin(1/x)| \le |x|$。由夾擠定理，$\lim_{x \to 0} g(x) = 0 = g(0)$，故 $g(x)$ 在原點嚴格連續。
- **(2) 差商求極限**：
  $$\frac{g(\Delta x) - g(0)}{\Delta x} = \frac{\Delta x \sin(1/\Delta x) - 0}{\Delta x} = \sin\left(\frac{1}{\Delta x}\right)$$
  當 $\Delta x \to 0$ 時，$1/\Delta x \to \infty$，$\sin(1/\Delta x)$ 在 $[-1, 1]$ 區間內進行無窮劇烈的高頻震盪，不存在單一收斂極限。
- **結論**：極限不存在，故 $g(x)$ 在原點不可導。這論證了「連續是可導的必要條件，但絕非充分條件」。
"""

# File paths
base_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(base_dir, '..'))
text_dir = os.path.join(project_dir, '專著正文與詳細解答')

book_ch01_md = os.path.join(text_dir, "中學微積分先修專著_第01章.md")
book_ch01_txt = os.path.join(text_dir, "中學微積分先修專著_第01章.txt")

with open(book_ch01_md, "w", encoding="utf-8") as f:
    f.write(ch01_content)

with open(book_ch01_txt, "w", encoding="utf-8") as f:
    f.write(ch01_content)

print(f"Chapter 1 monograph successfully generated! Length: {len(ch01_content)} characters.")
