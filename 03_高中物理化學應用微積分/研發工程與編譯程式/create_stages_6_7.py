# -*- coding: utf-8 -*-
"""
create_stages_6_7.py
構建 Stage 6 (Ch 20-24) 與 Stage 7 (Ch 25-28) 數據模組
完全落實高中必考公式、高斯二重極座標證明、68-95-99.7 經驗法則、馬克士威分佈、ODE 與近代物理
徹底移除希爾伯特/鄧煜等空降內容。
"""

import os
import sys

SCRATCH_DIR = r"C:\Users\user\.gemini\antigravity\brain\17c5c8ea-1f34-4270-a5e4-410bdd5037d4\scratch"

# -------------------------------------------------------------
# STAGE 6 DATA (Ch 20 - 24)
# -------------------------------------------------------------
STAGE_6 = {
    "title": "第六階：超越函數發明、多變數幾何與統計終局大一統（第 20–24 堂）",
    "theme": "對數與指數微積分自指基石，泰勒展開與斯特靈近似，多變數全微分誤差傳播，二重極座標高斯定積分，常態分佈與氣體分子速率終極閉環",
    "lessons": [
        {
            "id": 20,
            "title": "對數微積分發明與自指自然常數 e（連續複利與生長衰變）",
            "book_blueprint": "高中數學強行定義 e = 2.71828...，卻從未向學生解釋為何要發明這個古怪的常數。本章從反導函數的唯一黑洞切入：冪函數積分 int x^n dx = x^{n+1}/(n+1) 在 n = -1 時分母為零崩潰！為填補曲線 1/x 下方幾何面積的空白，人類發明了自然對數定義式 ln(x) = int_1^x (1/t) dt；利用換元法嚴格證明對數性質 ln(ab) = ln(a) + ln(b)；再由反函數定理定義指數函數 y = e^x，其微商 d/dx(e^x) = e^x，具備『變化率恆等於自身』的自指神性！最後以連續複利模型 lim_{n -> inf} (1 + 1/n)^n = e 連接放射性衰變與人口指數增長，完成超越函數微積分基石。",
            "dojo_core": "黑板四分區實彈攻防：一區在黑板畫出雙曲線 y = 1/x，塗滿 [1, x] 區間的面積微元 dt/t；二區利用面積的可加性證明 ln(ab) = ln(a) + ln(b)，展示微積分如何生長出代數法則；三區推導指數函數的自指导數，說明相空間中斜率恆等於縱坐標的幾何含義；四區以複利增長與半衰期實例擊碎死記硬背。",
            "formulas": [
                {"id": "Eq 20.1", "name": "自然對數幾何微積分定義式", "latex": r"\ln x = \int_1^x \frac{1}{t}\,\mathrm{d}t \quad (x > 0)"},
                {"id": "Eq 20.2", "name": "自然對數核心微商算子式", "latex": r"\frac{\mathrm{d}}{\mathrm{d}x} \ln x = \frac{1}{x}"},
                {"id": "Eq 20.3", "name": "自然常數極限定義式", "latex": r"e = \lim_{n \to \infty} \left(1 + \frac{1}{n}\right)^n = \lim_{h \to 0} (1 + h)^{1/h}"},
                {"id": "Eq 20.4", "name": "自指指數函數微商式", "latex": r"\frac{\mathrm{d}}{\mathrm{d}x} e^x = e^x"},
                {"id": "Eq 20.5", "name": "任意底數指數函數求導式", "latex": r"\frac{\mathrm{d}}{\mathrm{d}x} a^x = a^x \ln a \quad (a > 0)"},
                {"id": "Eq 20.6", "name": "對數求導法通用算子式", "latex": r"\frac{\mathrm{d}}{\mathrm{d}x} \ln |y(x)| = \frac{y'(x)}{y(x)}"},
                {"id": "Eq 20.7", "name": "指數生長與衰變模型解析式", "latex": r"\frac{\mathrm{d}y}{\mathrm{d}t} = k y \implies y(t) = y_0 e^{kt}"}
            ],
            "problems": {
                "worked_examples": [
                    {"id": "Ex 20.1", "desc": "純粹利用定義 ln(x) = int_1^x (1/t) dt 與換元積分法，不依賴任何指數假設，無跳步證明 ln(a*b) = ln(a) + ln(b)。"},
                    {"id": "Ex 20.2", "desc": "利用對數求導法求 y = x^x (x > 0) 的導函數，並求其局部極小值點與極小值。"},
                    {"id": "Ex 20.3", "desc": "放射性同位素半衰期為 T_half，列出衰變微分方程并求出衰變常數 lambda = ln(2) / T_half，計算經 3 個半衰期後剩餘質量比例。"}
                ],
                "margin_inquiries": [
                    {"id": "Q1 20.1", "desc": "為什麼在所有指數函數 a^x 中，只有以 e 為底時，在 x=0 處的切線斜率恰好等於 1？"},
                    {"id": "Q2 20.2", "desc": "如果冪法則 int x^n dx 在 n = -1 時直接套公式會出現 1/0，微積分是如何通過面積積分拯救這個奇異點的？"},
                    {"id": "Q3 20.3", "desc": "對數求導法在處理連乘多項式 y = (x-1)(x-2)...(x-n) 時，為何比直接使用乘積法則快得多？"}
                ],
                "foundational_drills": [
                    {"id": "P1 20.1", "desc": "求 f(x) = ln(x + sqrt{x^2 + 1}) 的一階導函數，化簡為最簡式。"},
                    {"id": "P2 20.2", "desc": "求定積分 int_1^e (ln x / x) dx。"},
                    {"id": "P3 20.3", "desc": "利用隱函數與對數求導求方程 e^y + x y = e 在點 (0, 1) 的切線斜率。"},
                    {"id": "P4 20.4", "desc": "計算極限 lim_{x -> 0} (e^x - 1 - x) / x^2。"}
                ],
                "interdisciplinary_applications": [
                    {"id": "P5 20.1", "desc": "【化學一級反應動力學】反應物濃度滿足 d[A]/dt = -k[A]，積分證明濃度半衰期與初始濃度完全無關。"},
                    {"id": "P6 20.2", "desc": "【聲音分貝與對數尺度】聲壓級分貝定義 beta = 10 log_{10}(I / I_0)，利用微分 d(beta) 分析聲強增加 10 倍時分貝的微元增量。"},
                    {"id": "P7 20.3", "desc": "【大氣等溫氣壓公式】結合流體力學 dP = -rho g dz 與理想氣體狀態方程，分離變數法推導氣壓隨高度衰減公式 P(z) = P_0 e^{-M g z / RT}。"},
                    {"id": "P8 20.4", "desc": "【計算機二元檢索樹複雜度】證明平衡二元樹高度隨節點數 N 滿足 h = O(ln N)，並用微積分估算調和級數 sum_{k=1}^N (1/k) approx ln N。"}
                ],
                "deepwater_challenges": [
                    {"id": "P9 20.1", "desc": "嚴格證明歐拉-馬歇羅尼常數 gamma = lim_{n -> inf} (sum_{k=1}^n 1/k - ln n) 的極限存在性，並以幾何曲邊梯形剩餘三角形夾擠之。"},
                    {"id": "P10 20.2", "desc": "非線性生長邏輯斯諦方程式（Logistic Equation）dy/dt = r y (1 - y/K)，利用部分分式分離變數法求出 S 型曲線解析解 y(t)。"}
                ],
                "dojo_defense_tasks": [
                    {"id": "D1 20.1", "desc": "學員求 d/dx(2^x) 寫成 x * 2^{x-1}，導師截停：『這是指數函數，不是冪函數！在黑板寫出化為自然底 e 的標準換底推導！』"},
                    {"id": "D2 20.2", "desc": "學員試圖計算 int (1/x) dx 寫出 ln(x)，導師指出：『x 為負數時怎麼辦？立刻補上絕對值符號並分區間證明！』"},
                    {"id": "D3 20.3", "desc": "學員在黑板推導 lim (1 + 1/n)^n，無法說明為何極限必然介於 2 與 3 之間，要求用二項式定理單調有界定理當場證畢。"}
                ],
                "unseen_sandbox_scenarios": [
                    {"id": "U1 20.1", "desc": "未知破局：設函數 f(x) 滿足 f(xy) = f(x) + f(y) 且在 x=1 可導，求證 f(x) 必然為對數函數 C ln x。"},
                    {"id": "U2 20.2", "desc": "未知破局：一容器內氣體滲漏率正比於容器內外壓差 d(Delta P)/dt = -k Delta P，求解壓差衰減曲線。"},
                    {"id": "U3 20.3", "desc": "未知破局：求方程 e^x = 3x 在實數範圍內的實根個數與近似解。"}
                ],
                "system_trivialization_arsenal": [
                    {"id": "K1 20.1", "desc": "體制內考題秒殺：高中大考指數比較大小題（如 e^pi 與 pi^e），微積分選手考慮 f(x) = ln(x)/x 的單調性，10 秒秒殺。"},
                    {"id": "K2 20.2", "desc": "體制內考題秒殺：放射性剩餘質量計算題，微積分學員直接套用 m = m_0 2^{-t/T} 3 秒心算出答案。"},
                    {"id": "K3 20.3", "desc": "體制內考題秒殺：複雜分式乘積求導，微積分選手取對數求導 1 行列出答案，碾壓死算商法則的學生。"}
                ]
            }
        },
        {
            "id": 21,
            "title": "泰勒級數、馬克勞林級數與斯特靈階乘近似（超越函數多項式化）",
            "book_blueprint": "微積分的核心使命之一：將難以計算的超越函數（sin x, cos x, e^x, ln(1+x)）化為多項式。本章從多項式局部吻合出發，建立高階導數匹配機制，誕生泰勒公式 f(x) = sum_{k=0}^n [f^{(k)}(a)/k!] (x-a)^k + R_n(x)；推導拉格朗日餘項，給出近似截斷誤差的嚴格界限；在此基礎上展示物理學極小參數展開的核心大招：sqrt{1+x} approx 1 + 1/2 x, (1+x)^-1 approx 1 - x, sin x approx x - x^3/6；更進一步，面對高中排列組合中難以計算的階乘 n!，以定積分 int_1^n ln(x) dx 估算 ln(n!) = sum ln k approx n ln n - n + 1，進而導出科學史上的瑰寶——斯特靈公式（Stirling's Approximation）n! approx sqrt{2 pi n} (n/e)^n，為二項分佈向常態分佈的極限躍遷鑄造關鍵數學跳板。",
            "dojo_core": "黑板四分區實彈攻防：一區在黑板以切線（一階）、拋物線（二階）、三階多項式逐層逼近 sin(x) 曲線；二區列出五大經典馬克勞林展開式（e^x, sin x, cos x, 1/(1-x), ln(1+x)）；三區以直方圖面積估算 ln(n!)，推導出 n ln n - n 的階乘對數漸近線；四區以相對論動能低速展開突襲學員，展示物理公式背後的泰勒真身。",
            "formulas": [
                {"id": "Eq 21.1", "name": "泰勒公式與多項式逼近定義式", "latex": r"f(x) = \sum_{k=0}^n \frac{f^{(k)}(a)}{k!} (x - a)^k + R_n(x)"},
                {"id": "Eq 21.2", "name": "拉格朗日餘項精確表達式", "latex": r"R_n(x) = \frac{f^{(n+1)}(\xi)}{(n+1)!} (x - a)^{n+1} \quad (\xi \text{ 介於 } a \text{ 與 } x \text{ 之間})"},
                {"id": "Eq 21.3", "name": "指數函數馬克勞林級數展開式", "latex": r"e^x = \sum_{k=0}^\infty \frac{x^k}{k!} = 1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + \dots"},
                {"id": "Eq 21.4", "name": "正弦與餘弦三角函數級數展開式", "latex": r"\sin x = x - \frac{x^3}{3!} + \frac{x^5}{5!} - \dots, \quad \cos x = 1 - \frac{x^2}{2!} + \frac{x^4}{4!} - \dots"},
                {"id": "Eq 21.5", "name": "歐拉公式神性對偶式", "latex": r"e^{i\theta} = \cos\theta + i\sin\theta \implies e^{i\pi} + 1 = 0"},
                {"id": "Eq 21.6", "name": "階乘對數微積分定積分估算式", "latex": r"\ln(n!) = \sum_{k=1}^n \ln k \approx \int_1^n \ln x\,\mathrm{d}x = n\ln n - n + 1"},
                {"id": "Eq 21.7", "name": "斯特靈階乘漸近展開公式", "latex": r"n! \approx \sqrt{2\pi n} \left(\frac{n}{e}\right)^n \quad (n \to \infty)"}
            ],
            "problems": {
                "worked_examples": [
                    {"id": "Ex 21.1", "desc": "利用相對論質能方程 E = m c^2 = gamma m_0 c^2，將 gamma = (1 - v^2/c^2)^{-1/2} 在 v/c = 0 處進行二階泰勒展開，嚴格導出古典動能 1/2 m_0 v^2 及一階相對論修正項 3/8 m_0 v^4 / c^2。"},
                    {"id": "Ex 21.2", "desc": "利用馬克勞林級數手算 sin(0.1) 的近似值，取前兩項並用拉格朗日餘項估計誤差，證明其誤差小於 10^-6。"},
                    {"id": "Ex 21.3", "desc": "利用梯形數值積分法估算 int_1^n ln(x) dx，無跳步推導出 ln(n!) approx (n + 1/2) ln n - n + C，並闡述常數 C = ln(sqrt{2 pi}) 的來源。"}
                ],
                "margin_inquiries": [
                    {"id": "Q1 21.1", "desc": "為什麼泰勒級數展開的分母上必須有階乘 k!？若沒有 k!，高階導數求導時係數會發生什麼爆炸？"},
                    {"id": "Q2 21.2", "desc": "歐拉公式 e^{ix} = cos x + i sin x 為什麼能將三角函數的旋轉與指數函數的生長統一起來？"},
                    {"id": "Q3 21.3", "desc": "斯特靈公式中的 sqrt{2 pi n} 為何會帶有圓周率 pi？這與高斯積分有何深層淵源？"}
                ],
                "foundational_drills": [
                    {"id": "P1 21.1", "desc": "寫出 f(x) = ln(1 + x) 在 x=0 處的前 4 階泰勒展開多項式。"},
                    {"id": "P2 21.2", "desc": "利用泰勒展開計算未定式極限 lim_{x -> 0} (sin x - x) / x^3。"},
                    {"id": "P3 21.3", "desc": "利用二項式定理展開 (1 + x)^alpha 前三項，導出高中物理常用的 (1 + x)^alpha approx 1 + alpha x。"},
                    {"id": "P4 21.4", "desc": "以斯特靈公式計算 100! 的近似數量級（計算 log_{10}(100!)），比較計算機直接計算的難度。"}
                ],
                "interdisciplinary_applications": [
                    {"id": "P5 21.1", "desc": "【單擺大角度週期修正】單擺恢復力方程中 sin theta approx theta - theta^3 / 6，利用微擾泰勒展開推導單擺週期隨振幅 theta_0 的一階修正公式 T approx 2pi sqrt{L/g} (1 + 1/16 theta_0^2)。"},
                    {"id": "P6 21.2", "desc": "【統計熱力學微觀態數】波茲曼熵公式 S = k ln W，其中微觀態數 W 包含大量粒子數階乘 N!，利用斯特靈公式 d(ln N!)/dN approx ln N 導出化學勢與溫度關係。"},
                    {"id": "P7 21.3", "desc": "【雙電層電容非線性模型】靜電場泊松-玻爾茲曼方程中包含 sinh(e V / kT)，在低電壓極限進行泰勒展開得到線性德拜-休克爾模型。"},
                    {"id": "P8 21.4", "desc": "【黑體輻射普朗克公式退化】普朗克黑體輻射光譜包含 1 / (e^{h nu / kT} - 1)，在長波極限（h nu << kT）展開泰勒級數，完全恢復出經典瑞利-金斯定律。"}
                ],
                "deepwater_challenges": [
                    {"id": "P9 21.1", "desc": "柯西病態光滑函數 f(x) = e^{-1/x^2} (x != 0), f(0) = 0；證明其在 x=0 處任意階導數皆為 0，指出為何其麥克勞林級數收斂半徑無窮但卻不能表示原函數（非解析性）。"},
                    {"id": "P10 21.2", "desc": "利用沃利斯積（Wallis Product）極限 lim_{n -> inf} [ (2n)!! / (2n-1)!! ]^2 * (1 / (2n+1)) = pi / 2，嚴密閉環推導斯特靈公式中的常數 sqrt{2 pi}。"}
                ],
                "dojo_defense_tasks": [
                    {"id": "D1 21.1", "desc": "學員計算 lim (1 - cos x) / x^2，使用兩次洛必達法則耗時 1 分鐘，導師截停：『泰勒展開選手只需 2 秒看穿 cos x = 1 - x^2/2，立刻用泰勒級數秒殺！』"},
                    {"id": "D2 21.2", "desc": "學員推導大角度單擺週期，直接宣稱『sin theta 就等於 theta』，導師在黑板畫出 theta = 60 度時兩者的 15% 誤差，逼問其二階展開項。"},
                    {"id": "D3 21.3", "desc": "學員試圖計算 ln(50!)，在黑板硬算乘積，導師寫下斯特靈公式，要求學員 30 秒內給出數量級估算。"}
                ],
                "unseen_sandbox_scenarios": [
                    {"id": "U1 21.1", "desc": "未知破局：設 f(x) = sqrt{x}，求其在 x=1 處的二階泰勒多項式，並估算 sqrt{1.02} 的數值與誤差限。"},
                    {"id": "U2 21.2", "desc": "未知破局：若已知 sum_{n=0}^inf x^n = 1/(1-x)，逐項求導與逐項積分求出 sum_{n=1}^inf n x^n 與 sum_{n=1}^inf x^n / n 的閉合形式。"},
                    {"id": "U3 21.3", "desc": "未知破局：推導雙曲函數 cosh(x) 與 sinh(x) 的泰勒展開，並驗證其與三角函數級數的複數對偶關係。"}
                ],
                "system_trivialization_arsenal": [
                    {"id": "K1 21.1", "desc": "體制內考題秒殺：高中大考未定式極限壓軸題，微積分選手使用泰勒展開 1 行寫出答案，完全跳過複雜繁複的洛必達法則。"},
                    {"id": "K2 21.2", "desc": "體制內考題秒殺：大考估算題（如 1.003^50 大約多少），微積分學員使用 1 + 50 * 0.003 = 1.15 瞬間心算命中選項。"},
                    {"id": "K3 21.3", "desc": "體制內考題秒殺：高中物理近似題（引力微小變化 Delta g），微積分選手展開 (1 + h/R)^{-2} approx 1 - 2h/R 5 秒秒殺。"}
                ]
            }
        },
        {
            "id": 22,
            "title": "多變數全微分與測量誤差獨立正交合成（BIPM 實驗科學標準）",
            "book_blueprint": "高中物理與化學實驗最大的糊塗帳——『不確定度與誤差傳遞』。課本給出一堆平方和開根號的誤差公式，學生只能依樣畫葫蘆，根本不知其數學本質。本章建立多元函數微積分基石：偏導數（Partial Derivative）partial f / partial x，度量『保持其餘變數不變時對單一變數的變化率』；全微分（Total Differential）dz = (partial f / partial x) dx + (partial f / partial y) dy，揭示多元函數空間切平面的線性近似本質；以此全微分算子切入國際度量衡局（BIPM GUM）誤差傳播律：當自變數測量誤差獨立且服從常態分佈時，協方差為零，誤差正交合成公式 sigma_z^2 = sum (partial f / partial x_i)^2 sigma_{x_i}^2 嚴格浮現！高中實驗所有經典公式：單擺測重力加速度 g = 4 pi^2 L / T^2、歐姆定律電阻 R = V/I、密度測量 rho = M/V 的誤差分析，全部在 3 行全微分求導下徹底降維秒殺。",
            "dojo_core": "黑板四分區實彈攻防：一區在黑板畫出三維空間曲面 z = f(x, y) 及其切平面，標註偏導數的斜率幾何含義；二區推導全微分公式，展示空間長方體微元在切平面上的投影；三區無跳步推導 BIPM 誤差正交合成公式，揭示平方和開根號源於隨機變數獨立時方差可加性；四區以單擺測 g 的真實實驗數據現場攻防，示範全微分如何 3 行秒殺大考實驗誤差題。",
            "formulas": [
                {"id": "Eq 22.1", "name": "多元函數偏導數定義式", "latex": r"\frac{\partial f}{\partial x} = \lim_{\Delta x \to 0} \frac{f(x+\Delta x, y) - f(x, y)}{\Delta x}"},
                {"id": "Eq 22.2", "name": "全微分算子核心公式", "latex": r"\mathrm{d}z = \frac{\partial f}{\partial x}\mathrm{d}x + \frac{\partial f}{\partial y}\mathrm{d}y"},
                {"id": "Eq 22.3", "name": "三維空間切平面幾何方程", "latex": r"z - z_0 = \left(\frac{\partial f}{\partial x}\right)_0 (x - x_0) + \left(\frac{\partial f}{\partial y}\right)_0 (y - y_0)"},
                {"id": "Eq 22.4", "name": "梯度向量算子定義式", "latex": r"\nabla f = \left(\frac{\partial f}{\partial x}, \frac{\partial f}{\partial y}\right)"},
                {"id": "Eq 22.5", "name": "BIPM 獨立測量誤差正交合成公式", "latex": r"\sigma_z = \sqrt{\sum_{i=1}^n \left(\frac{\partial f}{\partial x_i}\right)^2 \sigma_{x_i}^2}"},
                {"id": "Eq 22.6", "name": "乘除運算相對誤差方和根式", "latex": r"z = \frac{x^a y^b}{w^c} \implies \frac{\sigma_z}{z} = \sqrt{a^2 \left(\frac{\sigma_x}{x}\right)^2 + b^2 \left(\frac{\sigma_y}{y}\right)^2 + c^2 \left(\frac{\sigma_w}{w}\right)^2}"},
                {"id": "Eq 22.7", "name": "單擺測重力加速度誤差傳遞式", "latex": r"g = \frac{4\pi^2 L}{T^2} \implies \frac{\sigma_g}{g} = \sqrt{\left(\frac{\sigma_L}{L}\right)^2 + 4\left(\frac{\sigma_T}{T}\right)^2}"}
            ],
            "problems": {
                "worked_examples": [
                    {"id": "Ex 22.1", "desc": "測量圓柱體密度 rho = M / (pi R^2 H)，已知質量 M、半徑 R、高度 H 的測量相對不確定度分別為 1%、2%、1%；利用對數全微分法，無跳步推導出 rho 的相對不確定度為 sqrt{1^2 + 4*(2)^2 + 1^2}% = sqrt{18}% approx 4.24%。"},
                    {"id": "Ex 22.2", "desc": "二元函數 z = x^2 y + sin(x y)，求偏導數 partial z / partial x 與 partial z / partial y，並寫出在點 (1, 0) 處的切平面方程。"},
                    {"id": "Ex 22.3", "desc": "在惠司同電橋測電阻實驗中 R_x = R_2 R_3 / R_1，若已知三隻標準電阻的絕對誤差皆為 0.1 歐姆，利用全微分求 R_x 的最大絕對誤差界限與標準不確定度。"}
                ],
                "margin_inquiries": [
                    {"id": "Q1 22.1", "desc": "為什麼全微分中各個偏導數項代表獨立維度的增量？如果在二維平面上 x 與 y 存在相關性，誤差公式會如何修正？"},
                    {"id": "Q2 22.2", "desc": "在單擺測 g 的相對誤差公式中，週期 T 的相對誤差係數為什麼是 2 而不是 1？這對實驗設計（精測 L 還是精測 T）有何指導意義？"},
                    {"id": "Q3 22.3", "desc": "偏導數 partial f / partial x 與常微分 df/dx 在符號與觀念上有何本質差異？能否隨意約去分母？"}
                ],
                "foundational_drills": [
                    {"id": "P1 22.1", "desc": "求 f(x, y) = e^{x y} ln(x/y) 的兩個一階偏導數。"},
                    {"id": "P2 22.2", "desc": "求曲面 z = x^2 + y^2 在點 (1, 2, 5) 處的切平面方程與法向量。"},
                    {"id": "P3 22.3", "desc": "已知理想氣體狀態方程 P = n R T / V，利用全微分寫出 dP 與 dT, dV 的線性近似關係。"},
                    {"id": "P4 22.4", "desc": "長方形兩邊測得 x = 10 +- 0.1 cm, y = 20 +- 0.2 cm，求面積 A 的不確定度 sigma_A。"}
                ],
                "interdisciplinary_applications": [
                    {"id": "P5 22.1", "desc": "【高中物理電阻率測量】電阻率 rho = R * (pi d^2 / 4) / L，寫出其相對不確定度微積分表達式，分析直徑 d 測量次數對降低總誤差的決定性作用。"},
                    {"id": "P6 22.2", "desc": "【化學滴定濃度誤差】滴定濃度 C_A = C_B V_B / V_A，推導其不確定度合成公式，分析移液管與滴定管誤差的相對佔比。"},
                    {"id": "P7 22.3", "desc": "【熱敏電阻測溫靈敏度】熱敏電阻阻值 R(T) = R_0 e^{B / T}，利用微分求其靈敏度 (1/R)(dR/dT) = -B / T^2，分析高溫區測溫誤差擴大效應。"},
                    {"id": "P8 22.4", "desc": "【全球定位系統 GPS 誤差幾何因子 GDOP】利用三維坐標全微分，分析衛星空間幾何分佈對地面定位坐標誤差橢球的放大機制。"}
                ],
                "deepwater_challenges": [
                    {"id": "P9 22.1", "desc": "克萊羅定理（Schwarz-Clairaut Theorem）：證明若二階混合偏導數連續，則 partial^2 f / (partial x partial y) 恆等於 partial^2 f / (partial y partial x)，並以反例剖析不連續時的不對稱性。"},
                    {"id": "P10 22.2", "desc": "協方差矩陣與誤差橢球：當測量變數 x, y 存在相關係數 rho != 0 時，利用二元常態分佈矩積分推導完整的誤差合成公式 sigma_z^2 = f_x^2 sigma_x^2 + f_y^2 sigma_y^2 + 2 rho f_x f_y sigma_x sigma_y。"}
                ],
                "dojo_defense_tasks": [
                    {"id": "D1 22.1", "desc": "學員推導相對誤差時，將單擺週期 T 的平方項寫成相對誤差相加，導師截停：『指數項求導微元系數是 2！在黑板用對數全微分 d(ln g) 嚴格重推！』"},
                    {"id": "D2 22.2", "desc": "學員計算偏導數時把 y 當作變量一併求導，導師指出：『偏導的核心是凍結其餘變量！在黑板寫出偏導數的極限定義！』"},
                    {"id": "D3 22.3", "desc": "學員宣稱『絕對誤差等於各項絕對誤差之和』，導師在黑板畫出正交隨機向量的幾何合成，質問其為何違背勾股定理。"}
                ],
                "unseen_sandbox_scenarios": [
                    {"id": "U1 22.1", "desc": "未知破局：設焦距公式 1/f = 1/p + 1/q，已知物距 p 與像距 q 的測量誤差，求焦距 f 的絕對誤差傳遞公式。"},
                    {"id": "U2 22.2", "desc": "未知破局：多元復合函數 z = f(u, v)，其中 u = x y, v = x/y，利用鏈鎖律求 partial z / partial x 與 partial z / partial y。"},
                    {"id": "U3 22.3", "desc": "未知破局：求空間曲面 x^2 + 2y^2 + 3z^2 = 6 在點 (1, 1, 1) 處的切平面方程。"}
                ],
                "system_trivialization_arsenal": [
                    {"id": "K1 22.1", "desc": "體制內考題秒殺：高中大考物理實驗『哪一項測量對 g 的誤差影響最大』，微積分選手看係數 2*Delta T/T 瞬間秒判是週期測量。"},
                    {"id": "K2 22.2", "desc": "體制內考題秒殺：求動能 E_k = 1/2 m v^2 的相對誤差，微積分學員 1 行寫出 Delta E/E = Delta m/m + 2 Delta v/v 秒殺。"},
                    {"id": "K3 22.3", "desc": "體制內考題秒殺：歐姆定律 R = V/I 誤差合成題，微積分學員寫下 sqrt{(Delta V/V)^2 + (Delta I/I)^2} 5 秒得出標準答案。"}
                ]
            }
        },
        {
            "id": 23,
            "title": "二重積分、空間體積與極座標變換（多變數降維武器鑄造）",
            "book_blueprint": "如果只停留在單變數微積分，學生的視野就永遠被困在一維數軸上。本章正式鑄造多變數微積分的最強武器——二重積分（Double Integral）與極座標變換。從空間曲頂柱體體積出發，建立二維黎曼和極限 V = iint_R f(x, y) dA；利用富比尼定理（Fubini's Theorem）將二重積分轉化為二次累次積分；直擊二維微積分最大天塹——直角坐標向極座標的轉換：面積微元 dA 在極座標下為什麼不是 dr dtheta，而是 r dr dtheta？利用扇形微元幾何面積或雅可比行列式（Jacobian）dA = |det J| dr dtheta = r dr dtheta 徹底講透！利用極座標武器，輕鬆手算均勻圓盤轉動慣量 I = int_0^{2pi} dtheta int_0^R r^2 (sigma r dr) = 1/2 M R^2，並精確計算半球體積 V = 2/3 pi R^3。此時，屠龍寶刀鑄造完成，為下一章斬斷高斯積分黑盒子提供決定性火力。",
            "dojo_core": "黑板四分區實彈攻防：一區在黑板畫出二維網格分割與三維曲頂柱體，建立 dA = dx dy 的直角幾何圖景；二區畫出極座標扇形微元，清楚標註弧長 r dtheta 與徑向增量 dr，讓學生親手畫出微元矩形 dA = r dr dtheta；三區演示富比尼定理的切片積分動線（先 y 後 x vs 先 x 後 y）；四區以極座標重算圓盤面積與轉動慣量，展示高維微元的降維爆發力。",
            "formulas": [
                {"id": "Eq 23.1", "name": "二重積分二維黎曼和極限定義式", "latex": r"\iint_R f(x, y)\,\mathrm{d}A = \lim_{\Delta A \to 0} \sum_{i} \sum_{j} f(x_i, y_j)\,\Delta A_{ij}"},
                {"id": "Eq 23.2", "name": "直角坐標富比尼累次積分定理", "latex": r"\iint_R f(x, y)\,\mathrm{d}x\mathrm{d}y = \int_a^b \left[ \int_{g_1(x)}^{g_2(x)} f(x, y)\,\mathrm{d}y \right] \mathrm{d}x"},
                {"id": "Eq 23.3", "name": "極座標變換幾何坐標對應式", "latex": r"x = r\cos\theta, \quad y = r\sin\theta \quad (x^2 + y^2 = r^2)"},
                {"id": "Eq 23.4", "name": "極座標面積微元雅可比式", "latex": r"\mathrm{d}A = \mathrm{d}x\mathrm{d}y = \left|\frac{\partial(x, y)}{\partial(r, \theta)}\right|\mathrm{d}r\mathrm{d}\theta = r\,\mathrm{d}r\,\mathrm{d}\theta"},
                {"id": "Eq 23.5", "name": "極座標二重積分通用轉換式", "latex": r"\iint_R f(x, y)\,\mathrm{d}x\mathrm{d}y = \int_{\alpha}^{\beta} \mathrm{d}\theta \int_{r_1(\theta)}^{r_2(\theta)} f(r\cos\theta, r\sin\theta)\,r\,\mathrm{d}r"},
                {"id": "Eq 23.6", "name": "空間球體體積二重積分式", "latex": r"V = 2 \iint_{x^2+y^2 \le R^2} \sqrt{R^2 - (x^2+y^2)}\,\mathrm{d}A = 2 \int_0^{2\pi}\mathrm{d}\theta \int_0^R \sqrt{R^2-r^2}\,r\,\mathrm{d}r = \frac{4}{3}\pi R^3"},
                {"id": "Eq 23.7", "name": "旋轉拋物面體積公式", "latex": r"V = \int_0^{2\pi}\mathrm{d}\theta \int_0^R (H - c r^2)\,r\,\mathrm{d}r = \frac{1}{2}\pi R^2 H"}
            ],
            "problems": {
                "worked_examples": [
                    {"id": "Ex 23.1", "desc": "幾何與代數雙重推導極座標面積微元：法一利用同心圓環扇形微元 dA = (r + dr/2) dtheta dr approx r dr dtheta；法二利用雅可比二階偏導行列式 det [[cos theta, -r sin theta], [sin theta, r cos theta]] = r，無跳步證明 dA = r dr dtheta。"},
                    {"id": "Ex 23.2", "desc": "計算二重積分 iint_D (x^2 + y^2) dx dy，其中 D 為圓域 x^2 + y^2 <= R^2；分別用直角坐標累次積分與極座標積分計算，對比兩者計算量的天壤之別。"},
                    {"id": "Ex 23.3", "desc": "交換積分次序：計算 I = int_0^1 dx int_x^1 e^{y^2} dy；在直角坐標系中畫出積分區域，交換積分次序為先對 x 後對 y，成功積出初等解析解 1/2 (e - 1)。"}
                ],
                "margin_inquiries": [
                    {"id": "Q1 23.1", "desc": "在極座標面積微元 dA = r dr dtheta 中，多出來的這個 r 在幾何上扮演什麼角色？如果半徑 r 很大，相同的角度增量 dtheta 對應的弧長會如何變化？"},
                    {"id": "Q2 23.2", "desc": "為什麼有些在直角坐標系中無法求出原函數的被積函數（如 e^{y^2} 或 e^{-x^2-y^2}），一換到極座標就能瞬間求出解析解？"},
                    {"id": "Q3 23.3", "desc": "富比尼定理允許交換積分次序的充要條件是什麼？如果被積函數在原點發散，交換次序會導致錯誤嗎？"}
                ],
                "foundational_drills": [
                    {"id": "P1 23.1", "desc": "計算直角坐標二重積分 int_0^1 dx int_0^2 (x + 2y) dy。"},
                    {"id": "P2 23.2", "desc": "將積分 int_0^R dx int_0^{sqrt{R^2-x^2}} (x^2+y^2) dy 轉化為極座標積分並求解。"},
                    {"id": "P3 23.3", "desc": "求由拋物面 z = x^2 + y^2 與平面 z = 4 所圍成的空間幾何體體積。"},
                    {"id": "P4 23.4", "desc": "利用二重積分計算心臟線 r = 1 + cos(theta) 所圍成的平面圖形總面積。"}
                ],
                "interdisciplinary_applications": [
                    {"id": "P5 23.1", "desc": "【高斯雷射光束總功率】雷射光強分佈為高斯輪廓 I(r) = I_0 e^{-2r^2 / w_0^2}，在橫截面上進行極座標二重積分 P = int_0^{2pi} dtheta int_0^inf I(r) r dr，求雷射總發射功率。"},
                    {"id": "P6 23.2", "desc": "【行星引力球殼外微積分】利用球座標/柱座標微元二重積分，證明均勻薄球殼對內部任意質點的引力合力嚴格為零（牛頓球殼定理二維展開）。"},
                    {"id": "P7 23.3", "desc": "【半導體晶圓雜質擴散】二維平面上雜質濃度滿足高斯分佈 C(r) = C_0 e^{-r^2 / (4Dt)}，求擴散至半徑 R 範圍內的總雜質原子數。"},
                    {"id": "P8 23.4", "desc": "【流體力學圓管泊肅葉流總流量】圓管截面流速分佈為拋物面 v(r) = v_max (1 - r^2/R^2)，二重積分計算單位時間流體總體積流量 Q = 1/2 pi R^2 v_max。"}
                ],
                "deepwater_challenges": [
                    {"id": "P9 23.1", "desc": "格林定理（Green's Theorem）：推導平面封閉曲線線積分與二重積分的等價轉換 oint (P dx + Q dy) = iint (partial Q / partial x - partial P / partial y) dA，並用以證明任意封閉多邊形面積鞋帶公式。"},
                    {"id": "P10 23.2", "desc": "廣義極座標橢圓面積：針對橢圓區域 (x/a)^2 + (y/b)^2 <= 1，引入變換 x = a r cos(theta), y = b r sin(theta)，計算雅可比行列式 J = a b r，手算證明橢圓面積公式 pi a b。"}
                ],
                "dojo_defense_tasks": [
                    {"id": "D1 23.1", "desc": "學員轉換極座標寫出 dA = dr dtheta，遺漏 r 因子，導師截停：『量綱錯誤！dr 是長度，dtheta 是無量綱，乘起來怎能是面積？在黑板畫出扇形微元補上 r！』"},
                    {"id": "D2 23.2", "desc": "學員在極座標積分時將 theta 的積分上下限寫成 0 到 pi，求整圓面積得出半邊結果，導師要求在黑板重新標註整圓掃描動線。"},
                    {"id": "D3 23.3", "desc": "學員面對無法積出的直角積分發呆，導師截停：『畫出積分區域，立刻交換積分次序！』學員必須在 60 秒內在黑板翻轉切片方向。"}
                ],
                "unseen_sandbox_scenarios": [
                    {"id": "U1 23.1", "desc": "未知破局：計算積分 int_0^2 dx int_0^{sqrt{2x-x^2}} y dy，識別出圓域邊界並轉化為極座標秒殺。"},
                    {"id": "U2 23.2", "desc": "未知破局：求空間曲面 z = x y 在第一象限與圓柱面 x^2 + y^2 = 1 圍成的立體體積。"},
                    {"id": "U3 23.3", "desc": "未知破局：給定一非均勻圓盤面密度 sigma(r) = sigma_0 (1 + r/R)，求該圓盤的總質量與繞中心軸的轉動慣量。"}
                ],
                "system_trivialization_arsenal": [
                    {"id": "K1 23.1", "desc": "體制內考題秒殺：旋轉體體積計算，微積分選手利用二重極座標 1 行寫出體積公式，秒殺體制內繁瑣的圓盤切片法。"},
                    {"id": "K2 23.2", "desc": "體制內考題秒殺：圓形區域物理量積分，微積分學員引入極座標 r dr dtheta 瞬間化為單變數一重積分秒殺。"},
                    {"id": "K3 23.3", "desc": "體制內考題秒殺：立體幾何最大截面與體積估算，微積分選手列出富比尼雙重累次積分 2 分鐘鎖定答案。"}
                ]
            }
        },
        {
            "id": 24,
            "title": "二項分佈極限、高斯常態分佈、68-95-99.7 法則與馬克士威氣體速率大一統（終局收割）",
            "book_blueprint": "本章是全書微積分降維打擊的終極收割聖殿！在第 14 堂課中，我們借用二項分佈長條圖直觀引入了連續機率密度，但在黑板上留下了最大懸念——『鐘形曲線係數為何包含神秘的 1/(sqrt(2pi) sigma)？』今天，所有武器全部就位，這筆數學債將被徹底清償！第一步：由狄莫弗-拉普拉斯定理（de Moivre-Laplace），利用斯特靈公式對二項分佈展開二階泰勒級數，無跳步證明離散組合數在極限下必然收斂為鐘形指數 e^{-(x-mu)^2 / (2 sigma^2)}；第二步：拔出第 23 堂鑄造的二重極座標屠龍刀，計算全域高斯積分 I = int_{-inf}^inf e^{-x^2} dx：利用獨立變數構造平方 I^2 = int e^{-x^2}dx int e^{-y^2}dy = iint e^{-(x^2+y^2)} dA = int_0^{2pi} dtheta int_0^inf r e^{-r^2} dr = 2pi * 1/2 = pi！嚴格開根號導出 I = sqrt{pi}，徹底償清係數 1/(sqrt(2pi) sigma)！第三步：高中統計體制內最痛恨死背的『68–95–99.7% 經驗法則』，本章利用高斯積分手算定積分數值，精確證明 P(mu - sigma <= X <= mu + sigma) = 68.26%、P(mu - 2sigma <= X <= mu + 2sigma) = 95.44%！第四步：降維橫掃高中物理與化學——將高斯積分平移至三維分子速度空間，利用球對稱速度微元 d^3 v = 4 pi v^2 dv，嚴格導出馬克士威-波茲曼速率分佈 f(v) = 4 pi (m / (2 pi k T))^{3/2} v^2 e^{-mv^2 / (2kT)}；定積分手算最概然速率 sqrt{2kT/m}、平均速率 sqrt{8kT/(pi m)}、均方根速率 sqrt{3kT/m}；並秒殺化學阿瑞尼斯方程活化能尾部面積，完成高中數學、物理、化學大一統終極閉環！",
            "dojo_core": "黑板四分區實彈攻防：一區翻開第 14 堂記在黑板上的待付帳單，在黑板正中央寫下 I^2 = iint e^{-(x^2+y^2)} dx dy；二區拔出極座標轉換 dA = r dr dtheta，在全場屏息中積出 2pi * 1/2 = pi，紅粉筆寫下大字 I = sqrt{pi}，全場響起掌聲；三區無跳步推導高中 68-95-99.7 法則的定積分面積；四區平移到三維速度空間，畫出馬克士威速率曲線，推導溫度 T 升高時活化能右側尾部面積的指數暴增，徹底打通理化壁壘。",
            "formulas": [
                {"id": "Eq 24.1", "name": "狄莫弗-拉普拉斯定理二項分佈極限式", "latex": r"\lim_{n \to \infty} \binom{n}{k} p^k (1-p)^{n-k} = \frac{1}{\sqrt{2\pi n p (1-p)}} e^{-\frac{(k - np)^2}{2 n p (1-p)}}"},
                {"id": "Eq 24.2", "name": "高斯積分二重極座標定積分證明式", "latex": r"I^2 = \left(\int_{-\infty}^\infty e^{-x^2}\mathrm{d}x\right)^2 = \iint_{\mathbb{R}^2} e^{-(x^2+y^2)}\,\mathrm{d}A = \int_0^{2\pi}\mathrm{d}\theta \int_0^\infty r e^{-r^2}\,\mathrm{d}r = \pi \implies \int_{-\infty}^\infty e^{-x^2}\mathrm{d}x = \sqrt{\pi}"},
                {"id": "Eq 24.3", "name": "高斯常態分佈全域歸一化標準式", "latex": r"f(x) = \frac{1}{\sqrt{2\pi}\sigma} e^{-\frac{(x-\mu)^2}{2\sigma^2}} \implies \int_{-\infty}^{\infty} f(x)\,\mathrm{d}x = 1"},
                {"id": "Eq 24.4", "name": "高中統計 68-95-99.7 經驗法則定積分式", "latex": r"P(\mu - k\sigma \le X \le \mu + k\sigma) = \frac{1}{\sqrt{2\pi}}\int_{-k}^k e^{-z^2/2}\,\mathrm{d}z \approx \begin{cases} 0.6826 & (k=1) \\ 0.9544 & (k=2) \\ 0.9974 & (k=3) \end{cases}"},
                {"id": "Eq 24.5", "name": "三維速度空間球殼微元式", "latex": r"\mathrm{d}^3\vec{v} = 4\pi v^2\,\mathrm{d}v \quad (v = \sqrt{v_x^2 + v_y^2 + v_z^2})"},
                {"id": "Eq 24.6", "name": "馬克士威-波茲曼速率分佈函數", "latex": r"f(v) = 4\pi \left(\frac{m}{2\pi k T}\right)^{3/2} v^2 e^{-\frac{m v^2}{2 k T}}"},
                {"id": "Eq 24.7", "name": "三種特徵氣體分子速率微積分積分式", "latex": r"v_p = \sqrt{\frac{2kT}{m}}, \quad \bar{v} = \int_0^\infty v f(v)\,\mathrm{d}v = \sqrt{\frac{8kT}{\pi m}}, \quad v_{\text{rms}} = \sqrt{\int_0^\infty v^2 f(v)\,\mathrm{d}v} = \sqrt{\frac{3kT}{m}}"}
            ],
            "problems": {
                "worked_examples": [
                    {"id": "Ex 24.1", "desc": "無跳步推導高斯積分：構造 I^2 = iint_{R^2} e^{-(x^2+y^2)} dx dy，轉換為極座標 int_0^{2pi} dtheta int_0^inf r e^{-r^2} dr，令 u = r^2 完成積分證明 I = sqrt{pi}；進一步換元證明 int_{-inf}^inf e^{-a x^2} dx = sqrt{pi / a}。"},
                    {"id": "Ex 24.2", "desc": "利用馬克勞林級數展開 e^{-z^2/2} = 1 - z^2/2 + z^4/8 - z^6/48，逐項定積分手算驗證常態分佈在 [-1, 1] 區間的累積機率為 (1 / sqrt{2pi}) * 2 * (1 - 1/6 + 1/40 - 1/336) approx 0.6826，徹底破解高中課本 68% 的來源。"},
                    {"id": "Ex 24.3", "desc": "從單粒子馬克士威速度分佈 f(v_x, v_y, v_z) 出發，利用球坐標面積微元 dv_x dv_y dv_z = 4pi v^2 dv，求一階矩積分 int_0^inf v f(v) dv 嚴格導出氣體分子平均速率 v_bar = sqrt{8kT / (pi m)}。"}
                ],
                "margin_inquiries": [
                    {"id": "Q1 24.1", "desc": "為什麼在二維平面上計算 I^2 反而比在一維數軸上計算 I 更容易？微積分在這裡展現了何種『升維破局』的幾何智慧？"},
                    {"id": "Q2 24.2", "desc": "馬克士威速率分佈曲線在原點處 f(0) = 0，而一維速度分佈在原點處有最大值 f(v_x=0) > 0，造成這種差異的幾何微元原因是什麼？"},
                    {"id": "Q3 24.3", "desc": "阿瑞尼斯方程式中反應速率常數隨溫度升高而指數暴增，在馬克士威速率曲線圖上對應哪一塊幾何面積？"}
                ],
                "foundational_drills": [
                    {"id": "P1 24.1", "desc": "求定積分 int_0^inf x e^{-x^2} dx 與 int_0^inf x^2 e^{-x^2} dx。"},
                    {"id": "P2 24.2", "desc": "設隨機變數 X ~ N(100, 16)，利用標準化 Z = (X - 100)/4 與 68-95-99.7 法則，求 P(92 <= X <= 108)。"},
                    {"id": "P3 24.3", "desc": "令馬克士威速率分佈導數 df/dv = 0，無跳步求出最概然速率 v_p = sqrt{2kT/m}。"},
                    {"id": "P4 24.4", "desc": "求均方根速率 v_rms 的微積分定義式，驗證其動能 1/2 m v_rms^2 嚴格等於 3/2 k T。"}
                ],
                "interdisciplinary_applications": [
                    {"id": "P5 24.1", "desc": "【化學阿瑞尼斯活化能尾部】在馬克士威分佈高能尾部，分子動能超過閾值 E_a 的比例為 f_active = int_{E_a}^inf f(E) dE；在高能極限近似證明其面積正比於 e^{-E_a / RT}，解釋為何溫度每升高 10 度反應速率翻倍。"},
                    {"id": "P6 24.2", "desc": "【天文學恆星大氣分子逃逸】計算地球大氣中氫氣（分子量 2）與氮氣（分子量 28）在 300K 時速度大於地球逃逸速度 11.2 km/s 的高斯尾部機率，解釋為何地球大氣存不住氫氣。"},
                    {"id": "P7 24.3", "desc": "【光譜多普勒熱加寬】氣體分子沿視線方向速度分佈服從一維高斯分佈，推導發射光譜線形的常態分佈輪廓及其半高全寬（FWHM）隨溫度 sqrt{T} 增大的公式。"},
                    {"id": "P8 24.4", "desc": "【半導體費米-狄拉克向玻爾茲曼分佈退化】載流子分佈在非簡併半導體中，證明量子統計在 (E - E_F) >> kT 時通過泰勒展開完全退化為經典常態高斯分佈。"}
                ],
                "deepwater_challenges": [
                    {"id": "P9 24.1", "desc": "中心極限定理（Central Limit Theorem）特徵函數證明：設 X_1, ..., X_n 獨立同分佈，利用傅立葉變換與泰勒展開證明其特徵函數收斂於 e^{-t^2/2}，嚴格導出常態分佈的普遍性。"},
                    {"id": "P10 24.2", "desc": "多維速度空間高斯積分：計算 n 維高斯積分 int_{R^n} e^{-sum x_i^2} d^n x = pi^{n/2}，利用球坐標高維幾何證明 n 維超球表面積公式 S_{n-1} = 2 pi^{n/2} / Gamma(n/2)。"}
                ],
                "dojo_defense_tasks": [
                    {"id": "D1 24.1", "desc": "學員推導高斯積分在極座標下忘記乘以 r，寫出 int_0^inf e^{-r^2} dr，導師截停：『如果沒有 r，你的極座標和直角坐標有何區別？在黑板重畫扇形面積微元！』"},
                    {"id": "D2 24.2", "desc": "學員稱『最概然速率、平均速率、均方根速率三個數值是一樣的』，導師要求在黑板畫出馬克士威曲線並標出三者大小順序 v_p < v_bar < v_rms。"},
                    {"id": "D3 24.3", "desc": "學員無法解釋為什麼 68.26% 不是剛好 68%，導師要求在黑板寫出泰勒展開逐項積分前兩項，手算出 0.6826。"}
                ],
                "unseen_sandbox_scenarios": [
                    {"id": "U1 24.1", "desc": "未知破局：設某粒子速度分佈為三角形分佈 f(v) = c(v_0 - v) (0 <= v <= v_0)，求歸一化常數 c、平均速率與最概然速率。"},
                    {"id": "U2 24.2", "desc": "未知破局：計算積分 int_{-inf}^inf x^4 e^{-x^2} dx，利用對參數 a 求導的費曼微積分大招（Feynman's Trick）秒殺。"},
                    {"id": "U3 24.3", "desc": "未知破局：二維平面分子氣體，求二維速度空間中分子速率分佈函數 f_{2D}(v) 的解析表達式。"}
                ],
                "system_trivialization_arsenal": [
                    {"id": "K1 24.1", "desc": "體制內考題秒殺：高中統計常態分佈題『某大考成績服從常態分佈，平均 60，標準差 10，求 80 分以上比例』，微積分選手看 2 個標準差外，直接心算 (1 - 0.9544)/2 = 2.28% 5 秒秒殺。"},
                    {"id": "K2 24.2", "desc": "體制內考題秒殺：物理氣體平均動能題，微積分學員直接引用 1/2 m v_rms^2 = 3/2 kT 1 秒得出答案。"},
                    {"id": "K3 24.3", "desc": "體制內考題秒殺：化學活化能曲線溫度升高題，微積分選手一眼識破為高斯指數尾部積分面積增加，直接秒選正確曲線。"}
                ]
            }
        }
    ]
}

# -------------------------------------------------------------
# STAGE 7 DATA (Ch 25 - 28)
# -------------------------------------------------------------
STAGE_7 = {
    "title": "第七階：常微分方程、動態物理與近代量子微積分終極閉環（第 25–28 堂）",
    "theme": "動態世界微分方程建模，一階分離變數法，RC/RL 暫態電路指數衰減，二階線性簡諧振動淘汰參考圓，交流電網均方根與薛丁格測不準原理大一統閉環",
    "lessons": [
        {
            "id": 25,
            "title": "一階常微分方程分離變數法與反應動力學解析（牛頓冷卻與終端速度）",
            "book_blueprint": "微分方程是自然界譜寫定律的通用語言。高中物理與化學充斥著『速率正比於差距』的動態過程：熱茶冷卻、雨滴下落、化學反應。本章正式開啟常微分方程（ODE）大門：標準一階微分方程 dy/dt = f(t, y)；當函數可分解為 g(t) h(y) 時，採用分離變數法 int (1/h(y)) dy = int g(t) dt 求解；實戰打擊三大高中經典模型：1. 牛頓冷卻定律 dT/dt = -k(T - T_env)，分離變數得 T(t) = T_env + (T_0 - T_env) e^{-kt}，破解降溫指數曲線；2. 空氣阻力下落模型 m dv/dt = mg - kv，導出速度函數 v(t) = (mg/k)(1 - e^{-kt/m})，令 t -> inf 自然浮現終端速度 v_term = mg/k；3. 化學一級反應動力學 d[A]/dt = -k[A]，積分收穫 [A](t) = [A]_0 e^{-kt}，與零級反應、二級反應在相圖上並列對決，完成動力學微積分第一性原理構建。",
            "dojo_core": "黑板四分區實彈攻防：一區在黑板列出一階 ODE 分離變數的四部標準手術刀動線；二區現場推導空氣阻力下落，在黑板畫出 v-t 曲線如何從線性斜率 g 漸近彎折至水平線 mg/k；三區推導牛頓冷卻定律，對比不同介質散熱常數 k 的幾何衰減速度；四區以二級化學反應 1/[A] - 1/[A]_0 = kt 突襲學員，展示非指數型微分方程的特徵。",
            "formulas": [
                {"id": "Eq 25.1", "name": "一階常微分方程分離變數標準式", "latex": r"\frac{\mathrm{d}y}{\mathrm{d}t} = g(t)h(y) \implies \int \frac{1}{h(y)}\,\mathrm{d}y = \int g(t)\,\mathrm{d}t"},
                {"id": "Eq 25.2", "name": "牛頓冷卻定律微分方程", "latex": r"\frac{\mathrm{d}T}{\mathrm{d}t} = -k(T - T_{\text{env}})"},
                {"id": "Eq 25.3", "name": "牛頓冷卻溫度指數衰減解析解", "latex": r"T(t) = T_{\text{env}} + (T_0 - T_{\text{env}}) e^{-kt}"},
                {"id": "Eq 25.4", "name": "線性空氣阻力下落微分方程", "latex": r"m\frac{\mathrm{d}v}{\mathrm{d}t} = mg - kv"},
                {"id": "Eq 25.5", "name": "終端速度與速度演化解析解", "latex": r"v(t) = \frac{mg}{k}\left(1 - e^{-\frac{k}{m}t}\right) \implies v_{\text{term}} = \lim_{t \to \infty} v(t) = \frac{mg}{k}"},
                {"id": "Eq 25.6", "name": "化學一級反應動力學方程與半衰期", "latex": r"\frac{\mathrm{d}[A]}{\mathrm{d}t} = -k[A] \implies [A](t) = [A]_0 e^{-kt}, \quad t_{1/2} = \frac{\ln 2}{k}"},
                {"id": "Eq 25.7", "name": "化學二級反應動力學解析式", "latex": r"\frac{\mathrm{d}[A]}{\mathrm{d}t} = -k[A]^2 \implies \frac{1}{[A](t)} = \frac{1}{[A]_0} + kt"}
            ],
            "problems": {
                "worked_examples": [
                    {"id": "Ex 25.1", "desc": "一杯 90 度的咖啡置於 20 度的室溫環境中，5 分鐘後降溫至 60 度；利用牛頓冷卻定律分離變數求解散熱常數 k，並精確計算降溫至 30 度所需的總時間。"},
                    {"id": "Ex 25.2", "desc": "雨滴在重力與高速空氣二次方阻力 F_d = -c v^2 作用下下落，列出微分方程 m(dv/dt) = mg - c v^2，分離變數法利用部分分式求出速度解析解 v(t) = v_term tanh(gt / v_term)。"},
                    {"id": "Ex 25.3", "desc": "一階線性微分方程 dy/dt + P(t) y = Q(t)，構造積分因子 mu(t) = e^{int P dt}，無跳步推導出通解公式 y(t) = (1/mu) int mu Q dt + C/mu。"}
                ],
                "margin_inquiries": [
                    {"id": "Q1 25.1", "desc": "在線性阻力下落模型中，速度在 t = 0 處的切線斜率（初始加速度）為何恰好是重力加速度 g？"},
                    {"id": "Q2 25.2", "desc": "為什麼化學一級反應的半衰期與反應物初始濃度完全無關，而二級反應的半衰期 t_{1/2} = 1/(k[A]_0) 卻反比於初始濃度？"},
                    {"id": "Q3 25.3", "desc": "積分常數 C 在物理世界中對應什麼？為什麼沒有初始條件（Cauchy 數據），微分方程就無法給出唯一的真實物理軌道？"}
                ],
                "foundational_drills": [
                    {"id": "P1 25.1", "desc": "求解微分方程 dy/dx = 2x y，滿足初始條件 y(0) = 3。"},
                    {"id": "P2 25.2", "desc": "求解微分方程 dy/dt = -y^2，初始條件 y(0) = 1。"},
                    {"id": "P3 25.3", "desc": "某細菌培養物增長速率正比於當前數量 dy/dt = 0.05 y，求數量翻倍所需時間。"},
                    {"id": "P4 25.4", "desc": "物體自靜止下落受線性阻力，求下落距離隨時間變化的函數 x(t) = int v(t) dt。"}
                ],
                "interdisciplinary_applications": [
                    {"id": "P5 25.1", "desc": "【法醫死亡時間推斷】死者體溫測量值隨時間衰減，結合現場環境溫度利用牛頓冷卻方程反推心跳停止的精確時刻。"},
                    {"id": "P6 25.2", "desc": "【跳傘運動員開傘動態】跳傘員自高空俯衝達到第一終端速度 50 m/s，開傘後阻力係數突變，求解降至第二終端速度 5 m/s 的過渡減速曲線與最大過載加速度。"},
                    {"id": "P7 25.3", "desc": "【藥物在人體代謝廓清率】靜脈注射藥物在血液中消除服從一級動力學 dC/dt = -k C，結合連續滴注速率 R_0，求解血液藥物濃度平穩態 C_ss = R_0 / k。"},
                    {"id": "P8 25.4", "desc": "【污染水體自淨自稀釋模型】湖泊體積 V，純淨水以流量 Q 流入並以同流量流出帶走污染物，求解污染物濃度隨時間指數稀釋方程。"}
                ],
                "deepwater_challenges": [
                    {"id": "P9 25.1", "desc": "非線性白努利方程（Bernoulli ODE）：dy/dx + P(x) y = Q(x) y^n，引入變換 u = y^{1-n}，將其化為標準線性微分方程並給出通用積分公式。"},
                    {"id": "P10 25.2", "desc": "可變重力場大氣下落：考慮重力隨高度減小 g(z) = g_0 (R / (R+z))^2 且空氣密度隨高度指數衰減，列出隕石墜入大氣層的非線性二階 ODE 聯立方程。"}
                ],
                "dojo_defense_tasks": [
                    {"id": "D1 25.1", "desc": "學員分離變數直接寫出 int dy/y = int dt，遺漏積分常數 C，導師截停：『常數呢？沒有常數你的初始條件往哪裡代？在黑板補上完整的通解與特解！』"},
                    {"id": "D2 25.2", "desc": "學員求終端速度令 a = 0，導師質問：『速度一直在變，加速度怎麼就變成 0 了？在黑板寫出速度極限 lim_{t -> inf} 的微積分過程！』"},
                    {"id": "D3 25.3", "desc": "學員在牛頓冷卻中寫出 dT/dt = -k T，忽視環境溫度，導師以冰水置於沸水環境為例，要求其寫出溫差驅動項。"}
                ],
                "unseen_sandbox_scenarios": [
                    {"id": "U1 25.1", "desc": "未知破局：設某容器排水孔出流速度服從托里切利定律 v = sqrt{2gh}，求水深 h(t) 隨時間變化的微分方程與排空總時間。"},
                    {"id": "U2 25.2", "desc": "未知破局：雪球在雪地上滾動，質量增長率正比於表面積 dm/dt = k S，求解雪球半徑隨時間的增長規律。"},
                    {"id": "U3 25.3", "desc": "未知破局：求解微分方程 (x + 1) dy/dx = y + 1，滿足 y(0) = 1。"}
                ],
                "system_trivialization_arsenal": [
                    {"id": "K1 25.1", "desc": "體制內考題秒殺：高中大考阻力下落題，體制內學生猜測圖像，微積分選手看 v(t) = v_term(1 - e^{-t/tau}) 5 秒勾出正確漸近曲線。"},
                    {"id": "K2 25.2", "desc": "體制內考題秒殺：化學反應級數判斷，微積分選手觀察半衰期是否恆定，1 秒秒殺一級還是二級反應。"},
                    {"id": "K3 25.3", "desc": "體制內考題秒殺：降溫問題估算，微積分學員利用 Delta T 呈等比數列衰減，10 秒心算答案。"}
                ]
            }
        },
        {
            "id": 26,
            "title": "RC、RL 暫態電路與指數衰減（電容器充放電與 50% 能量佯謬）",
            "book_blueprint": "高中選修物理電學板塊最具思辨性的硬核專題——RC 與 RL 暫態電路。課本只給出充電公式 q(t) = C E (1 - e^{-t/RC}) 與放電公式，卻從不給出克希荷夫電壓定律（KVL）與微積分的結合推導。本章以電路微積分微分方程開篇：充電迴路 E - i R - q/C = 0，代入電流定義 i = dq/dt，誕生一階線性非齊次 ODE：R(dq/dt) + q/C = E；分離變數法分離電荷與時間：dq / (C E - q) = dt / (RC)，積分嚴格導出電荷指數增長 q(t) = C E (1 - e^{-t/tau})，其中時間常數 tau = RC 決定充放電快慢；同理推導 RL 迴路自感漸近電流 i(t) = (E/R)(1 - e^{-Rt/L})；最後，以微積分審判高中物理最震撼的『50% 能量佯謬』：電池輸出總能量 W_bat = int E i dt = C E^2，而電容器終態儲存能量僅為 1/2 C E^2，定積分手算電阻熱損耗 W_R = int_0^inf i^2 R dt = 1/2 C E^2，證明無論電阻 R 多微小，恰好一半的能量必然耗散為焦耳熱，徹底震撼學生的物理認知！",
            "dojo_core": "黑板四分區實彈攻防：一區在黑板畫出 RC 充電迴路圖，列出克希荷夫電壓方程並化為標準 ODE；二區無跳步推導分離變數法，在黑板畫出電荷 q(t) 與電流 i(t) 的對稱反向指數曲線；三區推導 RL 迴路的時間常數 tau = L/R；四區對決 50% 能量佯謬，三條定積分線路現場算平帳單（電池功 = 電容能 + 電阻熱），全場學員震撼受教。",
            "formulas": [
                {"id": "Eq 26.1", "name": "RC 充電迴路克希荷夫微分方程", "latex": r"R\frac{\mathrm{d}q}{\mathrm{d}t} + \frac{q}{C} = \mathcal{E}"},
                {"id": "Eq 26.2", "name": "電容充電電荷與電流指數解析式", "latex": r"q(t) = C\mathcal{E}\left(1 - e^{-\frac{t}{RC}}\right), \quad i(t) = \frac{\mathrm{d}q}{\mathrm{d}t} = \frac{\mathcal{E}}{R} e^{-\frac{t}{RC}}"},
                {"id": "Eq 26.3", "name": "電容放電指數衰減公式", "latex": r"q(t) = Q_0 e^{-\frac{t}{RC}}, \quad i(t) = -\frac{Q_0}{RC} e^{-\frac{t}{RC}}"},
                {"id": "Eq 26.4", "name": "RC 與 RL 電路時間常數定義", "latex": r"\tau_{RC} = RC, \quad \tau_{RL} = \frac{L}{R}"},
                {"id": "Eq 26.5", "name": "RL 電路通電電流增長微分方程與解", "latex": r"L\frac{\mathrm{d}i}{\mathrm{d}t} + i R = \mathcal{E} \implies i(t) = \frac{\mathcal{E}}{R}\left(1 - e^{-\frac{R}{L}t}\right)"},
                {"id": "Eq 26.6", "name": "電源充電輸出總能量定積分式", "latex": r"W_{\text{bat}} = \int_0^\infty \mathcal{E} i(t)\,\mathrm{d}t = \mathcal{E} \int_0^\infty \mathrm{d}q = C\mathcal{E}^2"},
                {"id": "Eq 26.7", "name": "電阻焦耳熱定積分與 50% 能量佯謬閉環", "latex": r"W_R = \int_0^\infty i(t)^2 R\,\mathrm{d}t = \int_0^\infty \frac{\mathcal{E}^2}{R} e^{-\frac{2t}{RC}}\,\mathrm{d}t = \frac{1}{2}C\mathcal{E}^2 = W_{\text{bat}} - E_C"}
            ],
            "problems": {
                "worked_examples": [
                    {"id": "Ex 26.1", "desc": "在 RC 充電電路中，無跳步推導電阻瞬時消耗功率 P_R(t) = i^2 R，求使電阻瞬時功率達到最大的時間點 t_max，並證明該最大功率為 E^2 / (4R)。"},
                    {"id": "Ex 26.2", "desc": "一電感為 L、電阻為 R 的線圈連接至直流電源 E；當電流達到穩定態 E/R 後瞬間短路電源，利用定積分計算磁場能量釋放過程中的總焦耳熱，驗證其等於 1/2 L (E/R)^2。"},
                    {"id": "Ex 26.3", "desc": "雙電容電荷重新分配：一電容 C_1 帶電 Q_0，另一電容 C_2 未充電，兩者通過電阻 R 閉合；列出微分方程求解電流 i(t)，並用微積分證明無論 R 多大，損失的靜電能恆等於 1/2 [C_1 C_2 / (C_1 + C_2)] (Q_0/C_1)^2。"}
                ],
                "margin_inquiries": [
                    {"id": "Q1 26.1", "desc": "在時間常數 t = tau = RC 瞬間，電容器充滿了百分之多少的電荷？（手算 1 - 1/e approx 63.2%）"},
                    {"id": "Q2 26.2", "desc": "如果電路中的電阻 R -> 0（超導電路），50% 的能量損失依然存在嗎？微積分與物理極限在這裡揭示了什麼電磁輻射本質？"},
                    {"id": "Q3 26.3", "desc": "為什麼電感在接通瞬間相當於『斷路』（電流為 0），而電容在接通瞬間相當於『短路』（電壓為 0）？從微積分導數 d/dt 的角度解釋。"}
                ],
                "foundational_drills": [
                    {"id": "P1 26.1", "desc": "電容 C = 10 muF 與電阻 R = 100 kOmega 串聯，計算其時間常數 tau。"},
                    {"id": "P2 26.2", "desc": "若電源電壓為 10V，求上述電路接通後 2 秒時電容器兩端的電壓。"},
                    {"id": "P3 26.3", "desc": "求電容充電至 99% 所需的時間是時間常數 tau 的多少倍？（手算 ln 100）"},
                    {"id": "P4 26.4", "desc": "RL 電路中 L = 2H, R = 10 Omega，求電流上升到最大值一半所需的時間。"}
                ],
                "interdisciplinary_applications": [
                    {"id": "P5 26.1", "desc": "【神經元軸突信號傳導】神經元膜電位被建模為 RC 漏電積分器（Leaky Integrate-and-Fire），突觸電流輸入時膜電位按 V(t) = R I (1 - e^{-t/RC}) 充能，求解達到觸發閾值時的動作電位點火延遲。"},
                    {"id": "P6 26.2", "desc": "【心臟起搏器定時電路】利用 RC 電路充放電週期控制電脈衝釋放頻率，求維持每分鐘 72 次心跳所需調節的電阻阻值。"},
                    {"id": "P7 26.3", "desc": "【相機閃光燈高壓充能】利用升壓變壓器與 RC 電路在 5 秒內將 330 muF 電容充至 300V，計算充電平均功率與閃光瞬間在 1 ms 內的峰值放電功率。"},
                    {"id": "P8 26.4", "desc": "【電源濾波低通濾波器】RC 電路對高頻交流信號呈現衰減，利用微商推導截止頻率 f_c = 1 / (2 pi RC)。"}
                ],
                "deepwater_challenges": [
                    {"id": "P9 26.1", "desc": "RLC 串聯二階暫態電路：L (d^2 q / dt^2) + R (dq/dt) + q/C = E，列出特徵方程並求解欠阻尼（Oscillatory）、臨界阻尼（Critically Damped）、過阻尼（Overdamped）三種情形的臨界電阻 R_c = 2 sqrt{L/C}。"},
                    {"id": "P10 26.2", "desc": "超導雙電容輻射損耗：在無電阻超導電路中，利用麥克斯韋電磁場方程推導電荷重新分配時損失的能量 1/2 C V^2 如何完全以電磁波輻射（坡印廷向量能流積分）散逸至無窮遠。"}
                ],
                "dojo_defense_tasks": [
                    {"id": "D1 26.1", "desc": "學員推導電容充電功寫出 W_bat = 1/2 C E^2，導師截停：『那是電容儲存的能量！電池做了多少功？在黑板寫出 int E i dt 手算給全班看！』"},
                    {"id": "D2 26.2", "desc": "學員稱『只要電阻足夠小，電阻發熱就可以忽略』，導師在黑板手算定積分 W_R = int i^2 R dt，指出 R 在分母與分子相消，結果恆為 1/2 C E^2。"},
                    {"id": "D3 26.3", "desc": "學員在 RL 電路中將時間常數寫成 tau = R L，導師要求用維度分析與微分方程量綱檢查當場修正。"}
                ],
                "unseen_sandbox_scenarios": [
                    {"id": "U1 26.1", "desc": "未知破局：設電源電壓隨時間線性上升 E(t) = alpha t，求解 RC 電路中的電荷 q(t) 響應曲線。"},
                    {"id": "U2 26.2", "desc": "未知破局：電容器漏電模型，極板間存在漏電阻 R_leak，求解斷開電源後電壓的自放電指數曲線。"},
                    {"id": "U3 26.3", "desc": "未知破局：求階躍電壓激勵下，RL 電路電感兩端感應電動勢 V_L(t) 的時間波形。"}
                ],
                "system_trivialization_arsenal": [
                    {"id": "K1 26.1", "desc": "體制內考題秒殺：高中大考電容充電圖像題，微積分學員看 q(t) 指數向上凸、i(t) 指數向下凹，2 秒選中唯一正確圖案。"},
                    {"id": "K2 26.2", "desc": "體制內考題秒殺：電路斷開瞬間反電動勢峰值，微積分選手看 L di/dt 斷開瞬間 dt -> 0 產生高壓電弧，瞬間定性秒答。"},
                    {"id": "K3 26.3", "desc": "體制內考題秒殺：能量損失題，微積分選手直接寫下 Delta E = 1/2 C V^2 1 秒拿滿分。"}
                ]
            }
        },
        {
            "id": 27,
            "title": "二階常係數齊次線性 ODE（簡諧運動解析解，徹底淘汰參考圓）",
            "book_blueprint": "高中物理講簡諧運動（SHM），所有參考書和課本都在畫一個莫名其妙的『參考圓投影』。學生被迫在圓周運動和水平投影之間反覆折磨，卻不知這純粹是微積分未引進前的歷史妥協！本章以微積分第一性原理徹底淘汰參考圓：牛頓第二定律 F = -k x = m (d^2 x / dt^2)，誕生二階常係數齊次線性微分方程 d^2 x / dt^2 + omega^2 x = 0（其中 omega = sqrt{k/m}）；特徵方程 r^2 + omega^2 = 0 誕生虛數根 r = +- i omega；由歐拉公式導出實數通解 x(t) = c_1 cos(omega t) + c_2 sin(omega t) = A cos(omega t + phi)；振幅 A 與初相位 phi 純粹由初始條件（x_0, v_0）自然代數解出，根本不需要畫任何圓！進一步求解單擺非線性方程 d^2 theta / dt^2 + (g/L) sin theta = 0，利用小角度泰勒展開 sin theta approx theta 導出週期 T = 2 pi sqrt{L/g}；最後推導阻尼振盪方程 m x'' + b x' + k x = 0，展現微積分在動力學世界的全域統御力。",
            "dojo_core": "黑板四分區實彈攻防：一區在黑板大字寫下宣言：『今天在黑板上，我們正式為參考圓舉行葬禮！』；二區無跳步推導二階常係數 ODE 特徵方程與歐拉解，展示 A 與 phi 如何由初值條件唯一決定；三區推導單擺小角度泰勒近似，展示大角度下週期拉長的微擾修正；四區對決阻尼振盪的三種判別式，徹底橫掃高難度競賽題。",
            "formulas": [
                {"id": "Eq 27.1", "name": "簡諧運動二階標準微分方程", "latex": r"\frac{\mathrm{d}^2 x}{\mathrm{d}t^2} + \omega^2 x = 0 \quad \left(\omega = \sqrt{\frac{k}{m}}\right)"},
                {"id": "Eq 27.2", "name": "特徵方程與歐拉複數根展開式", "latex": r"r^2 + \omega^2 = 0 \implies r = \pm i\omega \implies x(t) = c_1 e^{i\omega t} + c_2 e^{-i\omega t}"},
                {"id": "Eq 27.3", "name": "簡諧運動實數通用解析解", "latex": r"x(t) = A \cos(\omega t + \phi) = x_0 \cos(\omega t) + \frac{v_0}{\omega} \sin(\omega t)"},
                {"id": "Eq 27.4", "name": "簡諧運動振幅與初相一代數確定式", "latex": r"A = \sqrt{x_0^2 + \left(\frac{v_0}{\omega}\right)^2}, \quad \tan\phi = -\frac{v_0}{\omega x_0}"},
                {"id": "Eq 27.5", "name": "單擺非線性微分方程與小角近似", "latex": r"\frac{\mathrm{d}^2\theta}{\mathrm{d}t^2} + \frac{g}{L}\sin\theta = 0 \xrightarrow{\sin\theta \approx \theta} \frac{\mathrm{d}^2\theta}{\mathrm{d}t^2} + \frac{g}{L}\theta = 0 \implies T = 2\pi\sqrt{\frac{L}{g}}"},
                {"id": "Eq 27.6", "name": "簡諧運動速度與加速度導函數式", "latex": r"v(t) = \frac{\mathrm{d}x}{\mathrm{d}t} = -A\omega\sin(\omega t+\phi), \quad a(t) = \frac{\mathrm{d}^2 x}{\mathrm{d}t^2} = -A\omega^2\cos(\omega t+\phi) = -\omega^2 x"},
                {"id": "Eq 27.7", "name": "阻尼振動特徵微分方程", "latex": r"m\frac{\mathrm{d}^2 x}{\mathrm{d}t^2} + b\frac{\mathrm{d}x}{\mathrm{d}t} + k x = 0 \implies x(t) = A e^{-\gamma t} \cos(\omega' t + \phi) \quad \left(\gamma = \frac{b}{2m}\right)"}
            ],
            "problems": {
                "worked_examples": [
                    {"id": "Ex 27.1", "desc": "質量為 m 的彈簧振子，初始位置 x(0) = x_0，初始速度 v(0) = v_0；不借助參考圓，純粹利用特徵解待定係數法無跳步求出 A 與 phi，並手算驗證機械能守恆 1/2 k A^2 = 1/2 k x_0^2 + 1/2 m v_0^2。"},
                    {"id": "Ex 27.2", "desc": "浮筒垂直振盪：質量為 M、橫截面積為 A 的圓柱形浮筒浮在密度為 rho 的液體中，微小下壓 x 後釋放；列出牛頓第二定律二階 ODE，求振盪固有頻率 omega = sqrt{rho A g / M} 與週期。"},
                    {"id": "Ex 27.3", "desc": "受迫振盪與共振：m x'' + k x = F_0 cos(omega_f t)，利用待定特解法求出穩態振幅 A(omega_f) = (F_0/m) / |omega_0^2 - omega_f^2|，分析驅動頻率接近固有頻率時的共振發散現象。"}
                ],
                "margin_inquiries": [
                    {"id": "Q1 27.1", "desc": "為什麼簡諧運動的速度超前位移 pi/2（90度），而加速度超前位移 pi（180度）？從對正弦函數求導的角度解釋。"},
                    {"id": "Q2 27.2", "desc": "如果彈簧振子受到乾摩擦力（Coulomb Friction）而不是黏性阻力，微分方程的振幅衰減會是指數衰減還是等差線性衰減？"},
                    {"id": "Q3 27.3", "desc": "參考圓在歷史上是誰發明的？為什麼在沒有微積分教學的高中階段，參考圓會成為一種權宜之計？"}
                ],
                "foundational_drills": [
                    {"id": "P1 27.1", "desc": "求解二階微分方程 y'' + 9y = 0，滿足 y(0) = 2, y'(0) = 0。"},
                    {"id": "P2 27.2", "desc": "求質點簡諧運動 x(t) = 5 cos(2t - pi/3) 的振幅、角頻率、頻率、週期與初相位。"},
                    {"id": "P3 27.3", "desc": "長度為 1 米的單擺在月球表面（g = 1.62 m/s^2）的微小擺動週期是多少？"},
                    {"id": "P4 27.4", "desc": "驗證 x(t) = e^{-t} (cos 2t + sin 2t) 是某二階阻尼振盪微分方程的解，求該方程的特徵根。"}
                ],
                "interdisciplinary_applications": [
                    {"id": "P5 27.1", "desc": "【摩天大樓調諧質量阻尼器 TMD】台北 101 大樓風阻尼球被建模為巨型單擺，分析阻尼球與大樓主體雙自由度耦合二階 ODE 的共振消能機制。"},
                    {"id": "P6 27.2", "desc": "【分子雙原子分子震動光譜】HCl 分子共價鍵被近似為微觀量子彈簧，由紅外光譜實測振動頻率反推化學鍵彈簧剛度係數 k。"},
                    {"id": "P7 27.3", "desc": "【汽車懸吊系統避震器】汽車過減速帶模型，由車身質量與彈簧阻尼構成二階方程，求最佳臨界阻尼比 zeta = b / (2 sqrt{k m}) = 0.7 避免車身顛簸晃動。"},
                    {"id": "P8 27.4", "desc": "【LC 迴路電磁振盪對偶】證明 LC 迴路電荷方程 L(d^2 q / dt^2) + q/C = 0 與彈簧振子方程完全同構，列出所有物理量的對偶表（L 對應 m，1/C 對應 k，q 對應 x，i 對應 v）。"}
                ],
                "deepwater_challenges": [
                    {"id": "P9 27.1", "desc": "非線性大角度單擺精確橢圓積分：利用機械能守恆 1/2 m (L dtheta/dt)^2 - m g L cos theta = E，無跳步推導出精確週期第一類完全橢圓積分表達式 T = 4 sqrt{L/g} K(sin(theta_0 / 2))。"},
                    {"id": "P10 27.2", "desc": "相空間相軌跡（Phase Portrait）：在 (x, v) 平面上畫出簡諧運動的閉合橢圓軌跡；證明對於阻尼振盪，相軌跡演化為一條螺旋向內卷吸至原點的吸引子螺旋線。"}
                ],
                "dojo_defense_tasks": [
                    {"id": "D1 27.1", "desc": "學員試圖在黑板畫參考圓算相位，導師截停：『擦掉這個圓！寫出特徵方程，用初值條件直接解出 A 和 phi，展現微積分的尊嚴！』"},
                    {"id": "D2 27.2", "desc": "學員稱『單擺週期恆與振幅無關』，導師在黑板寫出 theta = 90 度，要求學員指證小角度近似 sin theta approx theta 的失效邊界。"},
                    {"id": "D3 27.3", "desc": "學員推導加速度寫出 a = omega^2 x，遺漏負號，導師逼問：『加速度方向與位移同向？那物體豈不是無限加速飛出宇宙了？』"}
                ],
                "unseen_sandbox_scenarios": [
                    {"id": "U1 27.1", "desc": "未知破局：設 U 形管水銀柱長度為 L，將水銀柱輕微壓下一段距離 x 後釋放，求水銀柱微小往復振盪的週期。"},
                    {"id": "U2 27.2", "desc": "未知破局：兩根同軸旋轉的水平滾筒以角速度 omega 反向旋轉，上方放置一根均勻鋼棒，求鋼棒在動摩擦力作用下的簡諧運動週期。"},
                    {"id": "U3 27.3", "desc": "未知破局：求微分方程 y'' - 4y' + 4y = 0 的通解（特徵根重根情形）。"}
                ],
                "system_trivialization_arsenal": [
                    {"id": "K1 27.1", "desc": "體制內考題秒殺：高中簡諧運動位移公式求法，微積分選手由初始位置與速度直接寫出 A 與 phi，10 秒秒殺體制內畫圖 5 分鐘。"},
                    {"id": "K2 27.2", "desc": "體制內考題秒殺：單擺週期變化題（如帶電單擺加電場），微積分學員求出等效 g_eff，1 行寫出新週期。"},
                    {"id": "K3 27.3", "desc": "體制內考題秒殺：彈簧振子動能與位能相等位置，微積分選手看 cos^2(omega t) = sin^2(omega t) 瞬間得出 x = A / sqrt{2}。"}
                ]
            }
        },
        {
            "id": 28,
            "title": "交流電網週期平均值與近代物理波函數終極閉環（全書大一統）",
            "book_blueprint": "這是全書微積分先修體系的終極殿堂與榮譽冠頂！本章跨越宏觀工程與微觀量子兩大極限，完成微積分的最高閉環。第一部分：破局高中電學死背常識——『為什麼台灣與美國家用交流電標稱 110V，但插座的瞬時峰值電壓卻高達 156V？為什麼有效值要除以根號 2？』微積分揭示週期函數均方根（RMS）定義 V_rms = sqrt{(1/T) int_0^T V(t)^2 dt}；對正弦波 V(t) = V_0 sin(omega t)，定積分手算 int_0^T sin^2(omega t) dt = T/2，無跳步證明 V_rms = V_0 / sqrt{2}，秒殺 110V * sqrt{2} approx 155.6V，並推導平均功率 P = V_rms I_rms cos(phi)；第二部分：跨入近代物理與量子力學——微積分如何描繪微觀物質？波恩（Max Born）統計詮釋：微觀粒子狀態由波函數 psi(x) 描述，其機率密度正是模平方 |psi(x)|^2，微元機率 dP = |psi(x)|^2 dx；粒子位置期望值 <x> = int x |psi|^2 dx，動量算子 hat{p} = -i hbar d/dx；最後，以微積分柯西-阿爾茨不等式嚴格證明量子力學第一原理——海森堡測不準原理 Delta x Delta p >= hbar / 2，指出其本質是波函數方差二階矩積分與傅立葉變換頻寬定理的純數推論！至此，全書 28 個章節首尾呼應，從最初的切線微商，歷經物理場域、多變數幾何、常微分方程，終在近代量子機率中達成微積分大一統！",
            "dojo_core": "黑板四分區實彈攻防：一區在黑板推導交流電均方根定積分，畫出 sin^2(omega t) 曲線並計算其對稱均值 1/2，紅粉筆圈出根號 2；二區在黑板畫出薛丁格波函數 psi(x) 及其機率密度模平方曲線 |psi|^2；三區列出量子力學算子矩積分表達式，無跳步推導測不準原理的方差積分展開；四區導師立於黑板前，發表全書結業告學員書：『從無窮小到量子態，你們已經掌握了自然界最底層的源代碼！』全體肅立致敬。",
            "formulas": [
                {"id": "Eq 28.1", "name": "週期信號均方根（RMS）微積分定義式", "latex": r"V_{\text{rms}} = \sqrt{\frac{1}{T}\int_0^T V(t)^2\,\mathrm{d}t}"},
                {"id": "Eq 28.2", "name": "正弦交流電峰值與有效值根號二關係式", "latex": r"\int_0^T \sin^2(\omega t)\,\mathrm{d}t = \frac{T}{2} \implies V_{\text{rms}} = \frac{V_0}{\sqrt{2}} \implies V_0 = 110\sqrt{2} \approx 155.6\,\text{V}"},
                {"id": "Eq 28.3", "name": "交流電網平均功率與功率因數定積分式", "latex": r"P_{\text{avg}} = \frac{1}{T}\int_0^T V(t)I(t)\,\mathrm{d}t = V_{\text{rms}} I_{\text{rms}} \cos\phi"},
                {"id": "Eq 28.4", "name": "量子波函數波恩機率密度統計詮釋式", "latex": r"\mathrm{d}P = |\psi(x)|^2\,\mathrm{d}x, \quad \int_{-\infty}^{\infty} |\psi(x)|^2\,\mathrm{d}x = 1"},
                {"id": "Eq 28.5", "name": "量子力學物理量算子期望值一階矩積分式", "latex": r"\langle x \rangle = \int_{-\infty}^\infty x |\psi(x)|^2\,\mathrm{d}x, \quad \langle p \rangle = \int_{-\infty}^\infty \psi^*(x)\left(-i\hbar\frac{\mathrm{d}}{\mathrm{d}x}\right)\psi(x)\,\mathrm{d}x"},
                {"id": "Eq 28.6", "name": "量子方差二階矩定積分式", "latex": r"(\Delta x)^2 = \langle x^2 \rangle - \langle x \rangle^2 = \int_{-\infty}^\infty (x - \langle x \rangle)^2 |\psi(x)|^2\,\mathrm{d}x"},
                {"id": "Eq 28.7", "name": "海森堡測不準原理微積分大一統式", "latex": r"\Delta x \Delta p \ge \frac{\hbar}{2} \quad (\text{算子不對易性與柯西-施瓦茨方差積分})"}
            ],
            "problems": {
                "worked_examples": [
                    {"id": "Ex 28.1", "desc": "計算半波整流交流電（只有半個週期有信號 V(t) = V_0 sin(omega t)，另外半個週期為 0）的有效值，定積分證明其有效值為 V_0 / 2。"},
                    {"id": "Ex 28.2", "desc": "一維無限深勢阱量子波函數 psi_n(x) = sqrt{2/L} sin(n pi x / L) (0 <= x <= L)；驗證全域機率歸一化 int_0^L |psi_n|^2 dx = 1，並計算粒子位置期望值 <x> = L/2 與不確定度 Delta x。"},
                    {"id": "Ex 28.3", "desc": "基態高斯量子波包 psi(x) = (pi sigma^2)^{-1/4} e^{-x^2 / (2 sigma^2)}；定積分計算 <x>, <x^2>, <p>, <p^2>，嚴格證明其不確定度乘積恰好達到測不準原理的理論下限 Delta x Delta p = hbar / 2。"}
                ],
                "margin_inquiries": [
                    {"id": "Q1 28.1", "desc": "為什麼交流電表的指針讀數是有效值而不是平均值？如果直接對正弦波求一個週期的算術平均，結果會是多少？"},
                    {"id": "Q2 28.2", "desc": "波函數 psi(x) 本身是複數，為什麼微元機率密度模平方 |psi(x)|^2 必然是實數且大於等於 0？"},
                    {"id": "Q3 28.3", "desc": "海森堡測不準原理真的是儀器測量誤差造成的嗎？還是物質波函數在微積分意義上的內在頻寬限制？"}
                ],
                "foundational_drills": [
                    {"id": "P1 28.1", "desc": "求方波交流電（正半週期 +10V，負半週期 -10V）的均方根有效值。"},
                    {"id": "P2 28.2", "desc": "求三角對稱波（峰值 V_0）的有效值，定積分證明其為 V_0 / sqrt{3}。"},
                    {"id": "P3 28.3", "desc": "一維勢阱中第 n=1 能級粒子，求其出現在勢阱中間 [L/4, 3L/4] 區域的定積分機率。"},
                    {"id": "P4 28.4", "desc": "利用動量算子 hat{p} psi = -i hbar (dpsi/dx)，求平面波 psi(x) = A e^{i k x} 的動量本徵值 p = hbar k。"}
                ],
                "interdisciplinary_applications": [
                    {"id": "P5 28.1", "desc": "【特高壓交流輸電線路損耗】在輸電功率固定 P_0 下，熱損耗 P_loss 正比於 I_rms^2 R，利用有效值分析將電壓升至 750 kV 時輸電線路損耗的大幅度抑制。"},
                    {"id": "P6 28.2", "desc": "【掃描隧道顯微鏡 STM 量子穿透】微觀電子穿透勢壘的波函數呈指數衰減 psi(x) = psi_0 e^{-kappa x}，推導穿透機率定積分 T approx e^{-2 kappa d}，解釋 STM 針尖位移 0.1 奈米時電流翻倍的原子級靈敏度。"},
                    {"id": "P7 28.3", "desc": "【核子物理阿爾法衰變半衰期】利用量子穿透波函數微元積分，推導蓋革-努塔爾定律（Geiger-Nuttall Law）中半衰期對阿爾法粒子能量的極端依賴性。"},
                    {"id": "P8 28.4", "desc": "【雷達與通訊時頻不確定度原理】在信號處理中，時間信號持續時間 Delta t 與頻譜頻寬 Delta omega 滿足 Delta t Delta omega >= 1/2，闡述傅立葉變換與量子測不準原理的完全同構性。"}
                ],
                "deepwater_challenges": [
                    {"id": "P9 28.1", "desc": "算子不對易性與柯西-施瓦茨不等式：定義兩個自伴算子 A 與 B，其對易子 [A, B] = A B - B A = i C；構造積分泛函 I(lambda) = int |(Delta A + i lambda Delta B) psi|^2 dx >= 0，利用判別式非正嚴格證明普遍不確定性原理 Delta A Delta B >= 1/2 |<[A, B]>|。"},
                    {"id": "P10 28.2", "desc": "量子諧振子基態薛丁格方程：(-hbar^2 / (2m)) (d^2 psi / dx^2) + 1/2 m omega^2 x^2 psi = E psi，利用待定高斯解 psi_0(x) = C e^{-alpha x^2} 代入驗證，求出基態零點能 E_0 = 1/2 hbar omega。"}
                ],
                "dojo_defense_tasks": [
                    {"id": "D1 28.1", "desc": "學員稱『家用插座是 110V，所以任何瞬間電壓都不會超過 110V』，導師在黑板畫出正弦波，要求學員 30 秒內算出版面峰值 155.6V 並指出擊穿風險。"},
                    {"id": "D2 28.2", "desc": "學員計算量子機率直接對波函數 psi(x) 進行積分，導師截停：『波函數可以是負數甚至虛數！機率密度是模平方！立刻改寫為 |psi|^2 定積分！』"},
                    {"id": "D3 28.3", "desc": "學員宣稱測不準原理是因為『儀器干擾了粒子』，導師在黑板寫出傅立葉變換頻寬積分，要求其在純數學層面證明測不準原理。"}
                ],
                "unseen_sandbox_scenarios": [
                    {"id": "U1 28.1", "desc": "未知破局：設交流電波形為鋸齒波 V(t) = V_0 (t/T) (0 <= t < T)，求其均方根有效值 V_rms。"},
                    {"id": "U2 28.2", "desc": "未知破局：若粒子處於三維各向同性無限深球形勢阱中，寫出基態波函數並驗證球坐標體積積分歸一化。"},
                    {"id": "U3 28.3", "desc": "未知破局：求階躍交變電壓在一整週期內的平均絕對值 V_avg = (1/T) int |V(t)| dt，並計算波形因數 V_rms / V_avg。"}
                ],
                "system_trivialization_arsenal": [
                    {"id": "K1 28.1", "desc": "體制內考題秒殺：高中交流電大考『求電熱絲發熱量』，微積分選手直接調用 V_rms = V_0 / sqrt{2}，Q = (V_rms^2 / R) t 5 秒秒殺全題。"},
                    {"id": "K2 28.2", "desc": "體制內考題秒殺：近代物理光電效應與物質波波長 lambda = h/p，微積分選手結合 E = p^2 / 2m 1 行換算能量與波長。"},
                    {"id": "K3 28.3", "desc": "體制內考題秒殺：測不準原理數量級估算題，微積分學員寫下 Delta x >= hbar / (2 Delta p) 10 秒鎖定答案。"}
                ]
            }
        }
    ]
}

# 寫入 stage6_data.py
with open(os.path.join(SCRATCH_DIR, "stage6_data.py"), "w", encoding="utf-8") as f:
    f.write("# -*- coding: utf-8 -*-\n")
    f.write('"""\nstage6_data.py (有機升級版：包含 Ch 20 - 24 全套 5 大章)\n"""\n\n')
    f.write(f"STAGE_6 = {repr(STAGE_6)}\n")
print("Stage 6 written successfully with 5 lessons (Ch 20-24).")

# 寫入 stage7_data.py
with open(os.path.join(SCRATCH_DIR, "stage7_data.py"), "w", encoding="utf-8") as f:
    f.write("# -*- coding: utf-8 -*-\n")
    f.write('"""\nstage7_data.py (有機升級版：包含 Ch 25 - 28 全套 4 大章)\n"""\n\n')
    f.write(f"STAGE_7 = {repr(STAGE_7)}\n")
print("Stage 7 written successfully with 4 lessons (Ch 25-28).")
