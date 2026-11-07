# -*- coding: utf-8 -*-
"""
stage2_data.py: 第二階：複合映射、隱函數與相空間（第 4–6 堂）
包含：
- 第 4 堂：尺度轉換齒輪與量綱連鎖律
- 第 5 堂：隱函數微分法與高階幾何切線
- 第 6 堂：消去時間的狀態空間微商
每堂課配賦：7 條核心公式鏈 + 25 道階梯題庫（書籍 16 + 道場 9）
"""

STAGE_2 = {
    "title": "第二階：複合映射、隱函數與相空間（第 4–6 堂）",
    "theme": "變量依賴的幾何齒輪咬合，擺脫單變量束縛，直面相空間與非顯式代數軌跡",
    "lessons": [
        {
            "id": 4,
            "title": "尺度轉換齒輪與量綱連鎖律（尺規比率與連乘本質）",
            "book_blueprint": "將複合函數導數詮釋為傳動齒輪的角速度之比；以萊布尼茲微分符號的消去直觀與量綱鏈條為雙核；徹底拆解複合函數求導漏乘內層微商的通病。",
            "dojo_core": "黑板直擊：以不同坐標系尺規轉換（英吋對公分、攝氏對華氏、空間尺度收縮）現場搭建連鎖微商矩陣，導師當場抓捕學員漏乘內層導數的隱性思維惰性。",
            "formulas": [
                {"id": "Eq 4.1", "name": "複合映射連鎖律核心定理式", "latex": "\\frac{\\mathrm{d}}{\\mathrm{d}x} f\\big(g(x)\\big) = f'\\big(g(x)\\big) \\cdot g'(x)"},
                {"id": "Eq 4.2", "name": "萊布尼茲齒輪微商消去式", "latex": "\\frac{\\mathrm{d}y}{\\mathrm{d}x} = \\frac{\\mathrm{d}y}{\\mathrm{d}u} \\cdot \\frac{\\mathrm{d}u}{\\mathrm{d}x}"},
                {"id": "Eq 4.3", "name": "多重齒輪鏈條相乘傳動式", "latex": "\\frac{\\mathrm{d}y}{\\mathrm{d}t} = \\frac{\\mathrm{d}y}{\\mathrm{d}u_1} \\cdot \\frac{\\mathrm{d}u_1}{\\mathrm{d}u_2} \\cdots \\frac{\\mathrm{d}u_n}{\\mathrm{d}t}"},
                {"id": "Eq 4.4", "name": "廣義冪函數複合微分法則", "latex": "\\frac{\\mathrm{d}}{\\mathrm{d}x} \\big(u(x)\\big)^n = n \\big(u(x)\\big)^{n-1} \\cdot \\frac{\\mathrm{d}u}{\\mathrm{d}x}"},
                {"id": "Eq 4.5", "name": "物理量綱連鎖相乘守恆式", "latex": "\\left[\\frac{\\mathrm{d}A}{\\mathrm{d}C}\\right] = \\left[\\frac{\\mathrm{d}A}{\\mathrm{d}B}\\right] \\cdot \\left[\\frac{\\mathrm{d}B}{\\mathrm{d}C}\\right] = \\frac{[A]}{[B]} \\cdot \\frac{[B]}{[C]} = \\frac{[A]}{[C]}"},
                {"id": "Eq 4.6", "name": "球體膨脹體積對時間微商關係式", "latex": "\\frac{\\mathrm{d}V}{\\mathrm{d}t} = \\frac{\\mathrm{d}V}{\\mathrm{d}r} \\cdot \\frac{\\mathrm{d}r}{\\mathrm{d}t} = 4\\pi r^2 \\frac{\\mathrm{d}r}{\\mathrm{d}t}"},
                {"id": "Eq 4.7", "name": "反函數導數倒數關係式", "latex": "\\frac{\\mathrm{d}x}{\\mathrm{d}y} = \\frac{1}{\\frac{\\mathrm{d}y}{\\mathrm{d}x}} \\quad \\left(\\frac{\\mathrm{d}y}{\\mathrm{d}x} \\neq 0\\right)"}
            ],
            "problems": {
                "worked_examples": [
                    {"id": "Ex 4.1", "desc": "設 $y = (3x^2 - 5x + 1)^4$，令 $u = 3x^2 - 5x + 1$，利用齒輪消去式 $\\frac{\\mathrm{d}y}{\\mathrm{d}x} = \\frac{\\mathrm{d}y}{\\mathrm{d}u}\\frac{\\mathrm{d}u}{\\mathrm{d}x}$ 完整展示換元與回代，證明內層微商 $(6x-5)$ 的必然存在。"},
                    {"id": "Ex 4.2", "desc": "一球形氣球以恆定速率 $100\\,\\mathrm{cm^3/s}$ 充氣。當氣球半徑為 $10\\,\\mathrm{cm}$ 時，計算其半徑膨脹的瞬時速率 $\\frac{\\mathrm{d}r}{\\mathrm{d}t}$ 與表面積增長速率 $\\frac{\\mathrm{d}S}{\\mathrm{d}t}$。"},
                    {"id": "Ex 4.3", "desc": "利用反函數導數定理 $\\frac{\\mathrm{d}x}{\\mathrm{d}y} = 1/\\frac{\\mathrm{d}y}{\\mathrm{d}x}$，從 $y = x^3$ 的導函數 $y'=3x^2$ 嚴格推導其反函數 $x = y^{1/3}$ 的導數，並說明在原點處切線垂直之幾何意義。"}
                ],
                "margin_inquiries": [
                    {"id": "Th 4.1", "desc": "【深水思辨】萊布尼茲將導數寫作微商符號 $\\frac{\\mathrm{d}y}{\\mathrm{d}x}$，讓連鎖律看起來就像普通的『分數乘法約分』。這究竟是純粹的符號巧合，還是無窮小幾何本質的深刻反映？什麼情況下不能當成分數隨意約分？"},
                    {"id": "Th 4.2", "desc": "【體制內盲點】中學生在求導 $y = (2x+1)^3$ 時經常寫成 $3(2x+1)^2$，忘記乘 $2$。從齒輪傳動比率的角度，如何用通俗語言向初學者徹底糾正這一思維盲區？"},
                    {"id": "Th 4.3", "desc": "【量綱審查】如果某化學反應中物質濃度 $C$ 的單位是 $\\mathrm{mol/L}$，溫度 $T$ 的單位是 $\\mathrm{K}$，時間 $t$ 的單位是 $\\mathrm{s}$，寫出 $\\frac{\\mathrm{d}C}{\\mathrm{d}t} = \\frac{\\mathrm{d}C}{\\mathrm{d}T}\\frac{\\mathrm{d}T}{\\mathrm{d}t}$ 各項的單位，說明連鎖律在量綱分析中的自洽性。"}
                ],
                "foundational_drills": [
                    {"id": "P1 4.1", "desc": "閉卷默寫複合函數連鎖律公式，並標明外層函數與內層函數的定義域銜接要求。"},
                    {"id": "P1 4.2", "desc": "無跳步求導：$f(x) = \\sqrt{x^3 + 2x - 1}$，寫出中間變量 $u(x)$ 與每一步鏈式展開。"},
                    {"id": "P1 4.3", "desc": "求三重複合函數 $y = \\big((x^2+1)^3 + 5\\big)^2$ 的一階導數 $\\frac{\\mathrm{d}y}{\\mathrm{d}x}$。"},
                    {"id": "P1 4.4", "desc": "已知函數 $f(u) = u^2 + 3u$，$u(v) = \\frac{1}{v}$，$v(x) = 2x+1$，求 $\\left.\\frac{\\mathrm{d}f}{\\mathrm{d}x}\\right|_{x=1}$。"}
                ],
                "interdisciplinary_applications": [
                    {"id": "P2 4.1", "desc": "【熱力學絕熱過程】理想氣體絕熱膨脹滿足 $P V^\\gamma = C$。若氣體體積以恆定速率增長 $\\frac{\\mathrm{d}V}{\\mathrm{d}t} = v_0$，利用連鎖律求壓強下降速率 $\\frac{\\mathrm{d}P}{\\mathrm{d}t}$。"},
                    {"id": "P2 4.2", "desc": "【幾何運動學】一架飛機在高度 $h=3000\\,\\mathrm{m}$ 處以水平速度 $v=200\\,\\mathrm{m/s}$ 等速飛過觀測站正上方。求當飛機與觀測站直線距離為 $5000\\,\\mathrm{m}$ 時，仰角隨時間變化的角速度。"},
                    {"id": "P2 4.3", "desc": "【電路學動態功率】非線性電阻兩端電壓隨電流變化為 $V(I) = k I^2$。若交流電路中電流隨時間變化 $I(t) = I_0 \\sin(\\omega t)$，求瞬時功率隨時間變化的變化率 $\\frac{\\mathrm{d}P}{\\mathrm{d}t}$。"},
                    {"id": "P2 4.4", "desc": "【化學動力學】若生成物濃度 $x(t)$ 與未反應物濃度 $(a-x)$ 的反應速率滿足 $\\frac{\\mathrm{d}x}{\\mathrm{d}t} = k(a-x)^2$，求反應速率對時間的二階微商 $\\frac{\\mathrm{d}^2x}{\\mathrm{d}t^2}$。"}
                ],
                "deepwater_challenges": [
                    {"id": "P3 4.1", "desc": "【多變數連鎖律雛形】設 $z = f(u, v)$，而 $u = x+y$，$v = x-y$。利用微元關係證明 $\\frac{\\partial z}{\\partial x} = \\frac{\\partial z}{\\partial u} + \\frac{\\partial z}{\\partial v}$，展示偏微商的齒輪分配。"},
                    {"id": "P3 4.2", "desc": "【不可微內層病態陷阱】構造外層函數 $f(u) = u^2$ 與內層函數 $g(x) = x^{1/3}$，探討複合函數 $h(x) = f(g(x))$ 在 $x=0$ 處的可微性，剖析外層『零導數』如何挽救內層『奇異發散』。"}
                ],
                "dojo_defense_tasks": [
                    {"id": "D1 4.1", "desc": "學員甲在黑板求導 $y = (x^2+1)^{-1}$，寫出 $-1(x^2+1)^{-2}$ 後停止。導師冷酷走上黑板，在後面畫了一個巨大的齒輪並質詢：『內層的 $x^2+1$ 難道是靜止不動的嗎？它旋轉的速率去哪裡了？』"},
                    {"id": "D1 4.2", "desc": "學員乙被要求推導反函數二階導數公式 $\\frac{\\mathrm{d}^2x}{\\mathrm{d}y^2} = -\\frac{y''}{(y')^3}$，導師質詢：『為什麼對 $\\frac{1}{y'}$ 求導不能直接對 $y$ 求導？連鎖律在換元時是怎樣將 $\\frac{\\mathrm{d}}{\\mathrm{d}y}$ 轉化為 $\\frac{\\mathrm{d}x}{\\mathrm{d}y}\\frac{\\mathrm{d}}{\\mathrm{d}x}$ 的？』"},
                    {"id": "D1 4.3", "desc": "學員丙上黑板分析『相關變化率（Related Rates）』問題，長度為 $L$ 的梯子靠牆滑落，底端以 $v$ 等速移開，求頂端滑落速度。導師詰問：當梯子即將完全著地時，頂端速度趨向無窮大，這是否違反相對論？物理破局點何在？"}
                ],
                "unseen_sandbox_scenarios": [
                    {"id": "D2 4.1", "desc": "光線穿透大氣層，折射率隨高度分佈 $n(z)$，光線路徑滿足斯涅爾定律微分形式 $n(z)\\sin\\theta(z) = \\text{const}$，現場構造傳播角對高度的微商 $\\frac{\\mathrm{d}\\theta}{\\mathrm{d}z}$。"},
                    {"id": "D2 4.2", "desc": "黑洞視界吸積盤物質旋入，質量隨半徑增加，角動量轉移速率滿足微分連鎖關係，現場推導能量輻射效率微商。"},
                    {"id": "D2 4.3", "desc": "受控核融合托卡馬克磁面幾何中，磁通量隨多角半徑變化，構造截面形變因子對磁場梯度的連鎖算子。"}
                ],
                "system_trivialization_arsenal": [
                    {"id": "D3 4.1", "desc": "高中指考物理難題：人以等速 $v$ 透過定滑輪拉繩提升地面上的小車，求小車前進速度隨繩長與夾角的變化關係。傳統運動分解極易出錯，設位移幾何勾股定理後對時間求導，1 行得出 $v_{\\text{car}} = v/\\cos\\theta$。"},
                    {"id": "D3 4.2", "desc": "高二數甲模擬題：曲線參數方程 $x = t^2+1, y = t^3-t$，求 $t=1$ 處的切線斜率。無需消去參數 $t$，直接以微商商數 $\\frac{\\mathrm{d}y}{\\mathrm{d}x} = \\frac{y'(t)}{x'(t)}$ 兩行秒殺。"},
                    {"id": "D3 4.3", "desc": "物理競賽題：倒圓錐容器注入液體，液面上升速率與液體體積增長率的幾何比例，用體積連鎖律 10 秒內得出答案。"}
                ]
            }
        },
        {
            "id": 5,
            "title": "隱函數微分法與高階幾何切線（軌跡代數直接求導）",
            "book_blueprint": "打破『必須將 $y$ 寫成 $x$ 的顯式表達式才能求導』的幼稚禁錮；直接在方程式 $F(x, y) = 0$ 兩側施加微分算子；掌握圓、橢圓、雙曲線及葉形線的高階幾何曲率。",
            "dojo_core": "黑板直擊：在笛卡兒葉形線 $x^3 + y^3 = 3axy$ 上實彈演示全方程逐項微分，要求學生在黑板上求出水平切線與鉛直切點，體驗不解方程而控制曲線的代數力量。",
            "formulas": [
                {"id": "Eq 5.1", "name": "隱函數方程微分算子作用式", "latex": "\\frac{\\mathrm{d}}{\\mathrm{d}x} F(x, y) = 0 \\iff \\frac{\\partial F}{\\partial x} + \\frac{\\partial F}{\\partial y}\\frac{\\mathrm{d}y}{\\mathrm{d}x} = 0"},
                {"id": "Eq 5.2", "name": "隱函數一階微商標準解", "latex": "\\frac{\\mathrm{d}y}{\\mathrm{d}x} = -\\frac{F_x}{F_y} \\quad (F_y \\neq 0)"},
                {"id": "Eq 5.3", "name": "圓軌跡幾何正交求導式", "latex": "x^2 + y^2 = R^2 \\implies 2x + 2y y' = 0 \\implies y' = -\\frac{x}{y}"},
                {"id": "Eq 5.4", "name": "圓的向心加速度幾何曲率二階式", "latex": "y'' = \\frac{\\mathrm{d}}{\\mathrm{d}x}\\left(-\\frac{x}{y}\\right) = -\\frac{y - x y'}{y^2} = -\\frac{y - x(-x/y)}{y^2} = -\\frac{x^2+y^2}{y^3} = -\\frac{R^2}{y^3}"},
                {"id": "Eq 5.5", "name": "橢圓切線點斜式代數閉環式", "latex": "\\frac{x^2}{a^2} + \\frac{y^2}{b^2} = 1 \\implies \\frac{x x_0}{a^2} + \\frac{y y_0}{b^2} = 1 \\quad (\\text{切線方程直接映射})"},
                {"id": "Eq 5.6", "name": "鉛直切線奇異性判據式", "latex": "F_y(x_0, y_0) = 0 \\quad \\text{且} \\quad F_x(x_0, y_0) \\neq 0 \\iff \\text{切線斜率發散，切線為垂直直線}"},
                {"id": "Eq 5.7", "name": "二階隱微分曲率分子展開式", "latex": "y'' = -\\frac{F_{xx} F_y^2 - 2F_{xy}F_x F_y + F_{yy}F_x^2}{F_y^3}"}
            ],
            "problems": {
                "worked_examples": [
                    {"id": "Ex 5.1", "desc": "給定圓方程 $x^2 + y^2 = 25$。不解出 $y = \\pm\\sqrt{25-x^2}$，直接用隱函數微分求點 $(3, 4)$ 處的切線斜率，並驗證切線與半徑向量正交（斜率乘積為 $-1$）。"},
                    {"id": "Ex 5.2", "desc": "對笛卡兒葉形線 $x^3 + y^3 = 6xy$，求 $\\frac{\\mathrm{d}y}{\\mathrm{d}x}$ 的表達式；求該曲線在點 $(3, 3)$ 處的切線方程，並求曲線上切線為水平的點。"},
                    {"id": "Ex 5.3", "desc": "已知橢圓 $\\frac{x^2}{a^2} + \\frac{y^2}{b^2} = 1$。利用隱函數求導導出切線斜率 $y' = -\\frac{b^2 x}{a^2 y}$，並證明過橢圓上一點 $(x_0, y_0)$ 的切線方程可整齊寫為 $\\frac{x x_0}{a^2} + \\frac{y y_0}{b^2} = 1$。"}
                ],
                "margin_inquiries": [
                    {"id": "Th 5.1", "desc": "【深水思辨】為什麼我們敢直接對 $F(x, y)=0$ 的兩端對 $x$ 求導？這裡隱含了什麼重大的數學存在性前提？（隱函數存在定理 Cauchy-Dini 定理的直觀幾何意義）。"},
                    {"id": "Th 5.2", "desc": "【體制內盲點】中學教材求圓錐曲線切線時，教了一種把 $x^2$ 換成 $x x_0$、$x$ 換成 $\\frac{x+x_0}{2}$ 的口訣。這個口訣背後的微積分公理本質是什麼？為什麼它只對二次曲線成立？"},
                    {"id": "Th 5.3", "desc": "【幾何奇點】在曲線 $y^2 = x^3$（半立方拋物線）的原點 $(0, 0)$ 處，直接求導會出現什麼情況？如何用幾何上的『尖點（Cusp）』解釋導數的崩潰？"}
                ],
                "foundational_drills": [
                    {"id": "P1 5.1", "desc": "閉卷寫出對二元多項式方程 $F(x, y)=0$ 兩側對 $x$ 求導的連鎖律展開式，標記 $y$ 是 $x$ 的隱函數。"},
                    {"id": "P1 5.2", "desc": "求雙曲線 $x^2 - 4y^2 = 9$ 在點 $(5, 2)$ 處的切線方程與法線方程。"},
                    {"id": "P1 5.3", "desc": "已知 $x^2 y + y^3 = 2$，求 $y'$ 與 $y''$ 在點 $(1, 1)$ 的精確值。"},
                    {"id": "P1 5.4", "desc": "求心臟線（外擺線）變形軌跡方程中某給定點處的隱微分斜率。"}
                ],
                "interdisciplinary_applications": [
                    {"id": "P2 5.1", "desc": "【熱力學狀態方程式】凡得瓦爾方程 $\\left(P + \\frac{a}{V^2}\\right)(V - b) = RT$。保持溫度 $T$ 為常數，利用隱微分法直接求等溫微商 $\\left(\\frac{\\partial P}{\\partial V}\\right)_T$。"},
                    {"id": "P2 5.2", "desc": "【天體運動軌道】行星軌道為橢圓 $\\frac{x^2}{a^2} + \\frac{y^2}{b^2} = 1$，求質點在任意坐標 $(x, y)$ 處速度方向（切線向量）與向心引力向量的夾角。"},
                    {"id": "P2 5.3", "desc": "【電磁等勢面】點電荷與接地導體球形成的平面等勢線為阿波羅尼奧斯圓族，用隱微分證明等勢線與電力線（梯度場）處處正交。"},
                    {"id": "P2 5.4", "desc": "【材料力學莫爾圓】應力圓方程 $(\\sigma - \\sigma_{\\text{avg}})^2 + \\tau^2 = R^2$，用隱微分求解切應力極值點對應的主應力方位角。"}
                ],
                "deepwater_challenges": [
                    {"id": "P3 5.1", "desc": "【奇異分歧點分析】曲線方程 $x^3 + y^3 - 3xy = 0$ 在原點 $(0, 0)$ 處，$F_x = 0$ 且 $F_y = 0$。利用二階小量分析該處的局部幾何逼近，證明原點是兩條切線正交交叉的結點（Node）。"},
                    {"id": "P3 5.2", "desc": "【高階曲率半徑】利用隱微分導出的 $y'$ 與 $y''$，計算橢圓頂點處的幾何曲率半徑 $\\rho = \\frac{(1+y'^2)^{3/2}}{|y''|}$，並驗證其與長短半軸的幾何關係 $\\rho = b^2/a$。"}
                ],
                "dojo_defense_tasks": [
                    {"id": "D1 5.1", "desc": "學員甲在黑板求 $x^2 + y^2 = 1$ 的二階導數，求出 $y'' = -\\frac{y - x y'}{y^2}$ 後就停筆。導師質詢：『為什麼不把一階導數 $y' = -x/y$ 回代？為什麼不把原方程 $x^2+y^2=1$ 簡化？黑板板書必須呈現終極封閉解 $-1/y^3$！』"},
                    {"id": "D1 5.2", "desc": "學員乙被指定在黑板求解雙曲線 $xy = c$ 的切線方程，導師質詢：『證明這條切線與兩條漸近線所圍成的三角形面積是一個與切點位置完全無關的常數！』"},
                    {"id": "D1 5.3", "desc": "學員丙上黑板分析星狀線 $x^{2/3} + y^{2/3} = a^{2/3}$，導師詰問：『這條曲線切線夾在兩坐標軸之間的線段長度是多少？用隱微分向全班證明它恆等於定值 $a$！』"}
                ],
                "unseen_sandbox_scenarios": [
                    {"id": "D2 5.1", "desc": "給定一個流體力學流函數 $\\psi(x, y) = x^2 y - \\frac{1}{3}y^3$，流線方程為 $\\psi(x, y) = C$。現場利用隱微分求任意點流速向量 $\\mathbf{u} = (u, v)$ 並驗證不可壓縮條件。"},
                    {"id": "D2 5.2", "desc": "三維勢能面等高線在二維投影為隱式曲線族，現場構造其沿最速下降路徑的法線微分算子。"},
                    {"id": "D2 5.3", "desc": "光學焦散線（Caustic curve）：光線經圓柱反射後的包絡線滿足隱式方程，現場求其尖角奇異點的切線漸近性。"}
                ],
                "system_trivialization_arsenal": [
                    {"id": "D3 5.1", "desc": "高中聯考解析幾何壓軸：過橢圓外一點引兩條切線，求切點弦方程。傳統聯考解法需設斜率方程並配合韋達定理計算整整一頁紙，利用隱微分相切條件 2 行直接寫出切點弦方程。"},
                    {"id": "D3 5.2", "desc": "高中模擬考題：求曲線 $x^2 - xy + y^2 = 3$ 在哪一點切線斜率為 $0$ 或 $\\infty$。利用隱微分分子分母分別為零，10 秒鎖定頂點坐標。"},
                    {"id": "D3 5.3", "desc": "物理競賽題：證明質點在光滑橢圓形軌道內運動時，軌道支持力（法線方向）沿半徑矢量的投影特性，用隱微分法線斜率一步證畢。"}
                ]
            }
        },
        {
            "id": 6,
            "title": "消去時間的狀態空間微商（相空間運動學求解）",
            "book_blueprint": "摧毀體制內『運動學必須依賴時間參數 $t$』的狹隘思維；利用微商相除建立相空間核心恆等式 $a = v\\frac{\\mathrm{d}v}{\\mathrm{d}x}$；將等加速運動公式、變力做功與保守力相軌跡一網打盡。",
            "dojo_core": "黑板直擊：在黑板上當場封印時間符號 $t$！僅憑 $x$ 與 $v$ 兩條坐標軸，直接推演非線性力場（簡諧振子、引力場、空氣阻力）的狀態微分方程，讓學生體驗相空間分析的上帝視角。",
            "formulas": [
                {"id": "Eq 6.1", "name": "時間微商速度基本定義式", "latex": "v(t) = \\frac{\\mathrm{d}x}{\\mathrm{d}t}"},
                {"id": "Eq 6.2", "name": "時間微商加速度基本定義式", "latex": "a(t) = \\frac{\\mathrm{d}v}{\\mathrm{d}t}"},
                {"id": "Eq 6.3", "name": "消去時間之連鎖微商構造式", "latex": "a = \\frac{\\mathrm{d}v}{\\mathrm{d}t} = \\frac{\\mathrm{d}v}{\\mathrm{d}x} \\cdot \\frac{\\mathrm{d}x}{\\mathrm{d}t} = \\frac{\\mathrm{d}v}{\\mathrm{d}x} \\cdot v"},
                {"id": "Eq 6.4", "name": "狀態相空間微商核心定理式", "latex": "a = v \\frac{\\mathrm{d}v}{\\mathrm{d}x} = \\frac{1}{2} \\frac{\\mathrm{d}(v^2)}{\\mathrm{d}x}"},
                {"id": "Eq 6.5", "name": "相空間分離變量定積分等價式", "latex": "\\int_{x_0}^x a(s)\\,\\mathrm{d}s = \\int_{v_0}^v u\\,\\mathrm{d}u = \\frac{1}{2}v^2 - \\frac{1}{2}v_0^2"},
                {"id": "Eq 6.6", "name": "等加速度運動相空間終極封閉解", "latex": "a = \\text{const} \\implies v^2 - v_0^2 = 2a(x - x_0) \\quad (\\text{體制內第三公式之公理本質})"},
                {"id": "Eq 6.7", "name": "簡諧振子相軌跡橢圓封閉解", "latex": "a(x) = -\\omega^2 x \\implies v\\,\\mathrm{d}v = -\\omega^2 x\\,\\mathrm{d}x \\implies \\frac{v^2}{\\omega^2} + x^2 = A^2"}
            ],
            "problems": {
                "worked_examples": [
                    {"id": "Ex 6.1", "desc": "從連鎖律 $a = \\frac{\\mathrm{d}v}{\\mathrm{d}t} = \\frac{\\mathrm{d}v}{\\mathrm{d}x}\\frac{\\mathrm{d}x}{\\mathrm{d}t} = v\\frac{\\mathrm{d}v}{\\mathrm{d}x}$ 出發，在 $a$ 為常數條件下，嚴格積分推導高中物理等加速第三公式 $v^2 - v_0^2 = 2as$，指出其本質即為相空間中的直線。"},
                    {"id": "Ex 6.2", "desc": "一質點受線性回復力作用，加速度滿足 $a(x) = -k x$（$k > 0$），初始條件為 $x(0) = x_0, v(0) = 0$。在不求解時間三角函數前提下，直接分離變數求解 $v(x)$，並在 $(x, v)$ 相平面上畫出軌跡。"},
                    {"id": "Ex 6.3", "desc": "天體引力場中，加速度為 $a(r) = -\\frac{GM}{r^2}$。一探測器從距天體中心 $R$ 處由靜止自由下落，利用相空間積分直接求質點到達半徑 $r$ 處的速度 $v(r)$，並推導第二宇宙速度。"}
                ],
                "margin_inquiries": [
                    {"id": "Th 6.1", "desc": "【深水思辨】為什麼高中物理教材將 $v^2 - v_0^2 = 2as$ 與 $v = v_0 + at, s = v_0 t + \\frac{1}{2}at^2$ 並列為三個獨立公式？在高等微積分看來，前者是相空間微商積分，後兩者是時間微商積分，它們的幾何投影差別何在？"},
                    {"id": "Th 6.2", "desc": "【體制內盲點】在非定力作用下（例如彈簧振子），很多高中生依然套用 $v^2 - v_0^2 = 2as$，結果慘遭滑鐵盧。用相空間微商指出：只有當 $a(x)$ 可以在積分號外提出來時該式才成立。"},
                    {"id": "Th 6.3", "desc": "【奇異點思考】若質點運動到某點處速度為零 $v=0$，但加速度 $a \\neq 0$，此時 $\\frac{\\mathrm{d}v}{\\mathrm{d}x} = \\frac{a}{v} \\to \\infty$。這在幾何相圖中代表什麼？為什麼相軌跡在 $x$ 軸上的切線必垂直於 $x$ 軸？"}
                ],
                "foundational_drills": [
                    {"id": "P1 6.1", "desc": "閉卷獨立寫出 $a = v\\frac{\\mathrm{d}v}{\\mathrm{d}x} = \\frac{1}{2}\\frac{\\mathrm{d}(v^2)}{\\mathrm{d}x}$ 的兩步無跳步推導。"},
                    {"id": "P1 6.2", "desc": "已知一維運動加速度與位置關係為 $a(x) = 3x^2 + 2x$，$x=0$ 時速度為 $v=2$，求速度隨位置變化的函數 $v(x)$。"},
                    {"id": "P1 6.3", "desc": "設物體加速度與速度成反比 $a(v) = \\frac{k}{v}$，求速度 $v$ 與位置 $x$ 的函數關係式。"},
                    {"id": "P1 6.4", "desc": "在相平面 $(x, v)$ 上，畫出 $v^2 - 4x = 0$ 的幾何曲線，並判定這對應於何種物理受力情境。"}
                ],
                "interdisciplinary_applications": [
                    {"id": "P2 6.1", "desc": "【空氣黏滯阻力】質點受空氣阻力滿足 $a(v) = -g - c v$（鉛直上拋）。利用相空間微商分離積分，求質點上升至速度為零時的最高點位移 $h_{\\max}$。"},
                    {"id": "P2 6.2", "desc": "【非線性分子間作用力】兩個分子間的相互作用加速度滿足 Lennard-Jones 形式 $a(r) = \\frac{A}{r^{13}} - \\frac{B}{r^7}$。求分子自無窮遠處由靜止相互靠近時的相對速度 $v(r)$。"},
                    {"id": "P2 6.3", "desc": "【帶電粒子磁鏡效應】在發散磁場中，軸向加速度 $a_z = -\\frac{\\mu}{m}\\frac{\\partial B_z}{\\partial z}$。將磁場梯度表示為位置的函數，利用相空間求解粒子反射點位置（磁鏡點）。"},
                    {"id": "P2 6.4", "desc": "【軟組織衝擊吸收】安全氣囊受壓時反向加速度為 $a(x) = -k x^3$（非線性剛度），求初速為 $v_0$ 的假人衝入氣囊後的壓縮最大距離 $x_{\\max}$。"}
                ],
                "deepwater_challenges": [
                    {"id": "P3 6.1", "desc": "【相軌跡拓撲分類】分析單擺在相空間中的全微分方程 $\\frac{\\mathrm{d}v}{\\mathrm{d}\\theta} = -\\frac{g}{L} \\frac{\\sin\\theta}{v}$。繪出其在開軌道（旋轉態）與閉軌道（震盪態）之間的臨界分離線（Separatrix）方程。"},
                    {"id": "P3 6.2", "desc": "【李亞普諾夫穩定性雛形】構造阻尼振子相軌跡方程，證明軌跡在相空間中以對數螺線向原點收縮，證明能量微商嚴格負定 $\\frac{\\mathrm{d}E}{\\mathrm{d}t} \\le 0$。"}
                ],
                "dojo_defense_tasks": [
                    {"id": "D1 6.1", "desc": "學員甲上黑板推導引力場 $a(r) = -GM/r^2$ 的逃逸速度，寫出 $\\int v\\,\\mathrm{d}v = -GM \\int r^{-2}\\,\\mathrm{d}r$。導師當面質詢：『你的積分上下限在哪裡？為什麼你可以令末狀態 $r \\to \\infty$ 且 $v=0$？引力勢能的零勢點是如何在相空間定積分中顯現出來的？』"},
                    {"id": "D1 6.2", "desc": "學員乙被要求在黑板繪製加速度與速度平方成正比 $a = -c v^2$ 的相平面軌跡，導師質詢：『當質點運動時，速度會不會在有限位移內降為零？如果不會，極限行為是什麼？用公式 $v(x) = v_0 e^{-cx}$ 說服全班！』"},
                    {"id": "D1 6.3", "desc": "學員丙上黑板論辯：『如果加速度是時間的顯式函數 $a(t)$，相空間微商 $a = v\\frac{\\mathrm{d}v}{\\mathrm{d}x}$ 還能直接分離變量求解嗎？』如果不可以，運動學方程本質上是什麼層次的微分方程？"}
                ],
                "unseen_sandbox_scenarios": [
                    {"id": "D2 6.1", "desc": "電磁軌道砲中洛倫茲力隨位置指數衰減 $F(x) = F_0 e^{-x/L}$，彈丸初速為零，現場利用相空間微分方程推導砲彈出膛口速度 $v_{\\text{exit}}$。"},
                    {"id": "D2 6.2", "desc": "假想穿透地球中心的對穿隧道，重力加速度隨離地心距離線性減小 $a(r) = -g \\frac{r}{R}$。現場求解質點在隧道中的相軌跡與往返週期。"},
                    {"id": "D2 6.3", "desc": "化學自催化反應速率與反應物濃度呈非線性耦合，現場構造濃度-反應速率狀態相空間軌跡。"}
                ],
                "system_trivialization_arsenal": [
                    {"id": "D3 6.1", "desc": "高二物理壓軸題：汽車以恆定功率 $P$ 行駛，受恆定阻力 $f$。求汽車從速度 $v_1$ 加速到 $v_2$ 所行駛的位移 $s$。傳統時間法無法直接做，利用 $a = \\frac{P/v - f}{m} = v\\frac{\\mathrm{d}v}{\\mathrm{d}s}$ 現場分離積分，3 行導出精確位移解析解。"},
                    {"id": "D3 6.2", "desc": "物理競賽題：斜面摩擦係數隨距離增大 $\\mu(x) = k x$，物體滑下，求滑行最大距離。利用相空間積分直接令 $\\int a(x)\\,\\mathrm{d}x = 0$，10 秒求出答案。"},
                    {"id": "D3 6.3", "desc": "聯考多選題：判斷變加速運動的 $v-x$ 圖像面積是否代表任何物理量。以相空間微商指出：$\\int v\\,\\mathrm{d}x$ 無直接定義，但 $\\int v\\,\\mathrm{d}v$ 是比動能變化，一針見血戳破選項陷阱。"}
                ]
            }
        }
    ]
}

if __name__ == "__main__":
    print(f"Loaded {STAGE_2['title']} with {len(STAGE_2['lessons'])} lessons.")
    total_f = sum(len(l['formulas']) for l in STAGE_2['lessons'])
    total_p = sum(
        len(l['problems']['worked_examples']) +
        len(l['problems']['margin_inquiries']) +
        len(l['problems']['foundational_drills']) +
        len(l['problems']['interdisciplinary_applications']) +
        len(l['problems']['deepwater_challenges']) +
        len(l['problems']['dojo_defense_tasks']) +
        len(l['problems']['unseen_sandbox_scenarios']) +
        len(l['problems']['system_trivialization_arsenal'])
        for l in STAGE_2['lessons']
    )
    print(f"Total formulas: {total_f} (Expect 21), Total problems: {total_p} (Expect 75)")
