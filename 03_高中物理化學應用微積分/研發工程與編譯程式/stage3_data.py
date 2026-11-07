# -*- coding: utf-8 -*-
"""
stage3_data.py: 第三階：無量綱弧度制與三角分析（第 7–9 堂）
包含：
- 第 7 堂：弧度無量綱化與幾何夾擠定理
- 第 8 堂：極坐標基底微分幾何與向心加速度
- 第 9 堂：變分極值雛形：費馬時間極值原理
每堂課配賦：7 條核心公式鏈 + 25 道階梯題庫（書籍 16 + 道場 9）
"""

STAGE_3 = {
    "title": "第三階：無量綱弧度制與三角分析（第 7–9 堂）",
    "theme": "旋轉對稱性破局，從無量綱弧度公理到向心加速度向量微商與光學變分極值",
    "lessons": [
        {
            "id": 7,
            "title": "弧度無量綱化與幾何夾擠定理（三角極限第一基石）",
            "book_blueprint": "揭示為什麼『角度制 360° 是人為產物，而弧度制 rad 是宇宙公理』；以單位圓扇形面積夾擠嚴格證明 $\\lim_{x\\to 0}\\frac{\\sin x}{x} = 1$；推導正弦餘弦微商對偶循環。",
            "dojo_core": "黑板直擊：在黑板上畫出單位圓、內接三角形與外切直角三角形，現場推導面積夾擠不等式；導師當場刺穿如果用『角度（度數）』求導會多出一個骯髒係數 $\\frac{\\pi}{180}$ 的本質災難。",
            "formulas": [
                {"id": "Eq 7.1", "name": "弧度無量綱公理定義式", "latex": "\\theta = \\frac{s}{r} = \\frac{[\\mathrm{L}]}{[\\mathrm{L}]} = 1 \\quad (\\text{純幾何比率，無量綱})"},
                {"id": "Eq 7.2", "name": "單位圓扇形面積夾擠不等式", "latex": "\\frac{1}{2}\\sin\\theta < \\frac{1}{2}\\theta < \\frac{1}{2}\\tan\\theta \\quad \\left(0 < \\theta < \\frac{\\pi}{2}\\right)"},
                {"id": "Eq 7.3", "name": "三角極限定理第一基石式", "latex": "\\lim_{\\theta \\to 0} \\frac{\\sin\\theta}{\\theta} = 1"},
                {"id": "Eq 7.4", "name": "餘弦二階小量極限定理式", "latex": "\\lim_{\\theta \\to 0} \\frac{1 - \\cos\\theta}{\\theta^2} = \\lim_{\\theta \\to 0} \\frac{2\\sin^2(\\theta/2)}{\\theta^2} = \\frac{1}{2}"},
                {"id": "Eq 7.5", "name": "正弦函數微分算子定義導出式", "latex": "\\frac{\\mathrm{d}}{\\mathrm{d}x}\\sin x = \\lim_{\\Delta x \\to 0} \\frac{\\sin(x+\\Delta x) - \\sin x}{\\Delta x} = \\cos x"},
                {"id": "Eq 7.6", "name": "餘弦函數微分算子定義導出式", "latex": "\\frac{\\mathrm{d}}{\\mathrm{d}x}\\cos x = -\\sin x"},
                {"id": "Eq 7.7", "name": "角度制微商污染係數檢驗式", "latex": "\\frac{\\mathrm{d}}{\\mathrm{d}x^\\circ}\\sin(x^\\circ) = \\frac{\\pi}{180}\\cos(x^\\circ) \\quad (\\text{體制角度制引入人工係數破壞優雅性})"}
            ],
            "problems": {
                "worked_examples": [
                    {"id": "Ex 7.1", "desc": "在單位圓中作圓心角為 $\\theta$ 的扇形，作內接直角三角形與外切直角三角形，寫出三者面積關係，嚴格夾擠證明 $\\cos\\theta < \\frac{\\sin\\theta}{\\theta} < 1$，並取雙側極限證明 $\\lim_{\\theta\\to 0}\\frac{\\sin\\theta}{\\theta}=1$。"},
                    {"id": "Ex 7.2", "desc": "利用和差化積公式 $\\sin(x+\\Delta x) - \\sin x = 2\\cos\\left(x + \\frac{\\Delta x}{2}\\right)\\sin\\left(\\frac{\\Delta x}{2}\\right)$，無跳步推導 $(\\sin x)' = \\cos x$，展示第一基石極限在其中的關鍵替換。"},
                    {"id": "Ex 7.3", "desc": "利用商法則與正餘弦導數，推導正切函數 $\\tan x$ 與正割函數 $\\sec x$ 的導函數，並求 $f(x) = \\tan x$ 在 $x = \\pi/4$ 處的切線方程。"}
                ],
                "margin_inquiries": [
                    {"id": "Th 7.1", "desc": "【深水思辨】如果歷史上巴比倫人規定圓周分為 100 度或 400 度，微積分會發生改變嗎？為什麼只有將圓周定義為 $2\\pi$ 弧度時，$(\\sin x)'$ 才能純淨地等於 $\\cos x$？"},
                    {"id": "Th 7.2", "desc": "【體制內盲點】很多學生在求極限 $\\lim_{x\\to 0}\\frac{\\sin x}{x}$ 時，脫口而出『用羅必達法則，分子求導是 $\\cos x$，分母求導是 1，所以等於 1』。這犯了怎樣荒謬的循環論證（Circular Reasoning）錯誤？"},
                    {"id": "Th 7.3", "desc": "【幾何圖像直觀】為什麼當 $\\theta$ 極小時，長度為 $\\theta$ 的圓弧可以近乎等同於直角邊 $\\sin\\theta$？二者的誤差為什麼是 $\\theta$ 的三階小量 $O(\\theta^3)$？"}
                ],
                "foundational_drills": [
                    {"id": "P1 7.1", "desc": "閉卷畫出單位圓夾擠幾何圖，默寫面積不等式與取極限過程。"},
                    {"id": "P1 7.2", "desc": "無跳步求極限：$\\lim_{x \\to 0} \\frac{\\tan 3x}{\\sin 5x}$。"},
                    {"id": "P1 7.3", "desc": "利用倍角公式與極限基石，計算 $\\lim_{x \\to 0} \\frac{1 - \\cos 4x}{x^2}$。"},
                    {"id": "P1 7.4", "desc": "求導函數：$f(x) = x^2 \\sin x + 2x \\cos x - 2\\sin x$，展示化簡後的優雅結果。"}
                ],
                "interdisciplinary_applications": [
                    {"id": "P2 7.1", "desc": "【簡諧單擺小角度近似】單擺回復力方程 $m L \\frac{\\mathrm{d}^2\\theta}{\\mathrm{d}t^2} = -mg \\sin\\theta$。在小角度 $\\theta \\ll 1$ 下，利用 $\\sin\\theta \\approx \\theta$ 建立線性二階常微分方程並求週期。"},
                    {"id": "P2 7.2", "desc": "【波動光學單縫繞射】第一暗紋條件 $\\frac{\\sin\\alpha}{\\alpha} = 0$，中央明紋角寬度涉及小角正弦微商逼近，分析光強分佈 $I(\\theta) = I_0 \\left(\\frac{\\sin\\beta}{\\beta}\\right)^2$ 的極限行為。"},
                    {"id": "P2 7.3", "desc": "【天文視差測距】恆星週年視差角 $\\theta \\approx 10^{-6}\\,\\mathrm{rad}$，以弧度定義 $d = \\frac{1\\,\\mathrm{AU}}{\\theta}$ 推導秒差距（Parsec）的幾何與量綱定義。"},
                    {"id": "P2 7.4", "desc": "【交流發電機轉子】線圈在均勻磁場中旋轉，磁通量 $\\Phi(t) = B S \\cos(\\omega t)$，利用法拉第電磁感應定律 $\\mathcal{E} = -\\frac{\\mathrm{d}\\Phi}{\\mathrm{d}t}$ 導出正弦電動勢。"}
                ],
                "deepwater_challenges": [
                    {"id": "P3 7.1", "desc": "【泰勒級數正弦無窮展開】利用連續高階求導循環 $(\\sin x)^{(4)} = \\sin x$，證明正弦函數可在原點展開為無窮交錯冪級數 $\\sum_{n=0}^\\infty \\frac{(-1)^n}{(2n+1)!} x^{2n+1}$，並證明其收斂半徑為 $\\infty$。"},
                    {"id": "P3 7.2", "desc": "【歐拉公式純數胚芽】設 $f(x) = \\cos x + \\mathrm{i}\\sin x$，證明 $f'(x) = \\mathrm{i} f(x)$，解剖三角函數與複指數函數微分同構的公理本質。"}
                ],
                "dojo_defense_tasks": [
                    {"id": "D1 7.1", "desc": "學員甲在黑板求 $\\lim_{x\\to 0}\\frac{\\sin(x^\\circ)}{x}$，直接寫出等於 1。導師走上台，用紅色粉筆寫下 $\\frac{\\pi}{180}$，詰問：『度數符號 $^\\circ$ 的物理量綱是什麼？如果直接算，你的答案整整差了 57 倍！』"},
                    {"id": "D1 7.2", "desc": "學員乙被要求在黑板上證明 $(\\cos x)' = -\\sin x$，不准用和差化積，必須從誘導公式 $\\cos x = \\sin(\\pi/2 - x)$ 配合複合連鎖律推導，導師審查負號的幾何起源。"},
                    {"id": "D1 7.3", "desc": "學員丙上黑板推導 $\\frac{\\mathrm{d}}{\\mathrm{d}x}\\sec x = \\sec x \\tan x$，導師質詢：『在 $x = \\pi/2$ 奇異點兩側，導數符號如何突變？幾何圖像如何反映這種正負無窮大的漸近線行為？』"}
                ],
                "unseen_sandbox_scenarios": [
                    {"id": "D2 7.1", "desc": "給定一個球面三角形，三內角和不等於 $\\pi$，球面多邊形面積與角虧滿足哈拉德定理，現場構造極小角極限下退化為歐氏三角形的微商條件。"},
                    {"id": "D2 7.2", "desc": "地震波橫波穿透地殼，波形滿足正弦剪切位移，現場建立剪切應變 $\\epsilon = \\frac{\\partial u}{\\partial x}$ 與應變能密度的微分積分式。"},
                    {"id": "D2 7.3", "desc": "量子自旋態在布洛赫球面上的進動，旋轉角 $\\theta(t)$ 滿足非線性力矩，現場構造自旋投影微商。"}
                ],
                "system_trivialization_arsenal": [
                    {"id": "D3 7.1", "desc": "高中聯考極限難題：求 $\\lim_{x\\to 0} \\frac{x - \\sin x}{x^3}$。傳統高中解法完全無法處理（超綱），利用三階泰勒一秒寫出答案 $\\frac{1}{6}$。"},
                    {"id": "D3 7.2", "desc": "高二數甲模擬題：求函數 $f(x) = \\frac{\\sin x}{2 + \\cos x}$ 的最大值。傳統方法換元判別式或輔助角繁瑣，直接求導令分子等於零，解餘弦方程一步到位。"},
                    {"id": "D3 7.3", "desc": "物理競賽題：小球在擺動過程中張力最大處的向心加速度，用正餘弦微分極值一分鐘內得出結論。"}
                ]
            }
        },
        {
            "id": 8,
            "title": "極坐標基底微分幾何與向心加速度（二維旋轉算子）",
            "book_blueprint": "打破笛卡兒固定基底坐標系的認知侷限；引入動態旋轉局部基底 $(\\hat{\\mathbf{r}}, \\hat{\\boldsymbol{\\theta}})$；用微積分證明基底向量本身的微商 $\\frac{\\mathrm{d}\\hat{\\mathbf{r}}}{\\mathrm{d}t} = \\dot{\\theta}\\hat{\\boldsymbol{\\theta}}$；第一性原理推導向心加速度與科里奧利力。",
            "dojo_core": "黑板直擊：在黑板上分步畫出動態基底旋轉幾何三角形，讓學員親手推導出速度與加速度在極坐標下的完整四項展開式（向心項、科氏項、角加速項、徑向加速項），讓體制內死背公式的學生啞口無言。",
            "formulas": [
                {"id": "Eq 8.1", "name": "極坐標動態基底定義式", "latex": "\\hat{\\mathbf{r}} = \\cos\\theta\\,\\hat{\\mathbf{i}} + \\sin\\theta\\,\\hat{\\mathbf{j}}, \\quad \\hat{\\boldsymbol{\\theta}} = -\\sin\\theta\\,\\hat{\\mathbf{i}} + \\cos\\theta\\,\\hat{\\mathbf{j}}"},
                {"id": "Eq 8.2", "name": "基底向量旋轉微商基本式", "latex": "\\frac{\\mathrm{d}\\hat{\\mathbf{r}}}{\\mathrm{d}t} = \\dot{\\theta}\\hat{\\boldsymbol{\\theta}}, \\quad \\frac{\\mathrm{d}\\hat{\\boldsymbol{\\theta}}}{\\mathrm{d}t} = -\\dot{\\theta}\\hat{\\mathbf{r}}"},
                {"id": "Eq 8.3", "name": "極坐標質點速度向量展開式", "latex": "\\mathbf{v} = \\frac{\\mathrm{d}}{\\mathrm{d}t}(r\\hat{\\mathbf{r}}) = \\dot{r}\\hat{\\mathbf{r}} + r\\dot{\\theta}\\hat{\\boldsymbol{\\theta}}"},
                {"id": "Eq 8.4", "name": "極坐標加速度全項微商定理式", "latex": "\\mathbf{a} = \\frac{\\mathrm{d}\\mathbf{v}}{\\mathrm{d}t} = (\\ddot{r} - r\\dot{\\theta}^2)\\hat{\\mathbf{r}} + (r\\ddot{\\theta} + 2\\dot{r}\\dot{\\theta})\\hat{\\boldsymbol{\\theta}}"},
                {"id": "Eq 8.5", "name": "等速圓周向心加速度封閉解", "latex": "r = R, \\dot{r}=0, \\dot{\\theta}=\\omega \\implies \\mathbf{a} = -R\\omega^2\\hat{\\mathbf{r}} = -\\frac{v^2}{R}\\hat{\\mathbf{r}}"},
                {"id": "Eq 8.6", "name": "科里奧利加速度微分項", "latex": "\\mathbf{a}_{\\text{coriolis}} = 2\\dot{r}\\dot{\\theta}\\hat{\\boldsymbol{\\theta}} = 2\\boldsymbol{\\omega} \\times \\mathbf{v}_{\\text{rel}}"},
                {"id": "Eq 8.7", "name": "克卜勒面積速度常數微商守恆式", "latex": "\\frac{\\mathrm{d}A}{\\mathrm{d}t} = \\frac{1}{2}r^2\\dot{\\theta} = \\frac{L}{2m} = \\text{const} \\iff a_\\theta = 0"}
            ],
            "problems": {
                "worked_examples": [
                    {"id": "Ex 8.1", "desc": "利用動態基底定義，對 $\\hat{\\mathbf{r}} = \\cos\\theta\\hat{\\mathbf{i}} + \\sin\\theta\\hat{\\mathbf{j}}$ 兩側對時間求導，嚴格利用連鎖律提出 $\\dot{\\theta}$，證明 $\\frac{\\mathrm{d}\\hat{\\mathbf{r}}}{\\mathrm{d}t} = \\dot{\\theta}\\hat{\\boldsymbol{\\theta}}$。"},
                    {"id": "Ex 8.2", "desc": "對速度向量 $\\mathbf{v} = \\dot{r}\\hat{\\mathbf{r}} + r\\dot{\\theta}\\hat{\\boldsymbol{\\theta}}$ 進行乘積求導，無跳步展示四項微分過程，最終整理為徑向加速度 $(\\ddot{r} - r\\dot{\\theta}^2)$ 與角向加速度 $(r\\ddot{\\theta} + 2\\dot{r}\\dot{\\theta})$。"},
                    {"id": "Ex 8.3", "desc": "一隻螞蟻在以恆定角速度 $\\omega$ 旋轉的電唱機唱片上，沿徑向以恆定相對速度 $u$ 向外爬行（$r(t) = ut$）。利用極坐標加速度公式，計算螞蟻在半徑 $R$ 處所受的真實加速度與方向。"}
                ],
                "margin_inquiries": [
                    {"id": "Th 8.1", "desc": "【深水思辨】在笛卡兒坐標系中，基底向量 $\\hat{\\mathbf{i}}, \\hat{\\mathbf{j}}$ 的導數恆為零；但在極坐標中，為什麼基底的導數不為零？這種『基底本身隨點而變』的數學幾何，正是愛因斯坦廣義相對論黎曼幾何的初級模型！"},
                    {"id": "Th 8.2", "desc": "【體制內盲點】中學物理課本推導向心加速度 $a = v^2/r$ 時，往往畫一個速度向量三角形用相似比強行解釋。為什麼這種幾何推導無法推廣到非勻速、半徑變化的真實曲線運動？"},
                    {"id": "Th 8.3", "desc": "【科氏力之謎】加速度公式中的 $2\\dot{r}\\dot{\\theta}$ 為什麼係數正好是 2？拆解它的雙重幾何來源：一半來自徑向速度方向的旋轉，另一半來自旋轉半徑增大導致切向速度的增長！"}
                ],
                "foundational_drills": [
                    {"id": "P1 8.1", "desc": "閉卷寫出極坐標基底微分關係式，並無跳步推導向心加速度 $a_r = -r\\dot{\\theta}^2$。"},
                    {"id": "P1 8.2", "desc": "質點運動方程為 $r(t) = 2t^2, \\theta(t) = 3t$，求 $t=1$ 時刻質點的徑向速度、切向速度與總速率。"},
                    {"id": "P1 8.3", "desc": "求阿基米德螺線 $r = a\\theta$ 在旋轉角速度 $\\dot{\\theta} = \\omega = \\text{const}$ 下的加速度大小。"},
                    {"id": "P1 8.4", "desc": "已知一質點在平面內運動，受到純徑向有心力作用，證明其角向加速度 $r\\ddot{\\theta} + 2\\dot{r}\\dot{\\theta} = \\frac{1}{r}\\frac{\\mathrm{d}}{\\mathrm{d}t}(r^2\\dot{\\theta}) = 0$。"}
                ],
                "interdisciplinary_applications": [
                    {"id": "P2 8.1", "desc": "【地球自轉科里奧利力】北半球由北向南發射的砲彈，因地球自轉角速度 $\\Omega$，利用極坐標微分項計算砲彈向右偏轉的橫向加速度。"},
                    {"id": "P2 8.2", "desc": "【克卜勒第二定律】證明在任何有心力場（萬有引力、庫侖力）作用下，質點對力心的角動量 $\\mathbf{L} = \\mathbf{r} \\times m\\mathbf{v}$ 對時間的微商恆為零，面積速度守恆。"},
                    {"id": "P2 8.3", "desc": "【迴旋加速器】帶電粒子在均勻垂直磁場中旋轉，洛倫茲力充當向心力 $q v B = m \\frac{v^2}{R}$，求迴旋頻率 $\\omega = \\frac{qB}{m}$ 對粒子能量微商（相對論前無關性）。"},
                    {"id": "P2 8.4", "desc": "【氣象學颱風旋渦】低氣壓中心氣流受氣壓梯度力與科氏力平衡，構造地轉風方程的極坐標微商關係。"}
                ],
                "deepwater_challenges": [
                    {"id": "P3 8.1", "desc": "【自然坐標系曲率推導】設平面曲線弧長為 $s$，切向量為 $\\hat{\\mathbf{T}} = \\frac{\\mathrm{d}\\mathbf{r}}{\\mathrm{d}s}$，法向量為 $\\hat{\\mathbf{N}}$。推導弗雷奈-塞雷（Frenet-Serret）公式 $\\frac{\\mathrm{d}\\hat{\\mathbf{T}}}{\\mathrm{d}s} = \\kappa\\hat{\\mathbf{N}}$，證明一般曲線運動加速度 $\\mathbf{a} = \\frac{\\mathrm{d}v}{\\mathrm{d}t}\\hat{\\mathbf{T}} + \\frac{v^2}{\\rho}\\hat{\\mathbf{N}}$。"},
                    {"id": "P3 8.2", "desc": "【雙星系統相對運動】兩顆質量為 $m_1, m_2$ 的恆星繞質心旋轉，在相對極坐標系中構造折合質量 $\\mu = \\frac{m_1 m_2}{m_1+m_2}$ 的動力學微商方程。"}
                ],
                "dojo_defense_tasks": [
                    {"id": "D1 8.1", "desc": "學員甲在黑板推導極坐標速度 $\\mathbf{v}$，直接把 $r$ 對 $t$ 求導寫成 $\\dot{r}$，忘了基底向量也在變。導師當面要求學員畫出時間差 $\\Delta t$ 後基底向量的幾何偏轉角 $\\Delta\\theta$，逼問 $\\Delta\\hat{\\mathbf{r}}$ 的極限方向！"},
                    {"id": "D1 8.2", "desc": "學員乙被要求在黑板解釋為什麼向心加速度帶負號 $-r\\dot{\\theta}^2$。導師質詢：『負號的公理幾何意義是什麼？它指向哪裡？如果角速度逆時針旋轉與順時針旋轉，向心加速度的正負號會改變嗎？』"},
                    {"id": "D1 8.3", "desc": "學員丙上黑板展示科氏力實驗：在旋轉圓盤上滾動的小球軌跡。導師詰問：在慣性系看來小球走的是直線，但在旋轉盤上看到的是曲線，這多出來的加速度是真實的力還是坐標系微商的代數產物？"}
                ],
                "unseen_sandbox_scenarios": [
                    {"id": "D2 8.1", "desc": "恆星塌縮為中子星時半徑劇烈收縮 $R(t) = R_0(1 - t/\\tau)$，角動量守恆，現場推導中子星表面赤道質點向心加速度隨時間的爆發性微分增長。"},
                    {"id": "D2 8.2", "desc": "高速旋轉離心機分離同位素分子，在極坐標旋轉參考系中構造有效勢能梯度與漂移速度微商。"},
                    {"id": "D2 8.3", "desc": "脈衝星向外發射相對論帶電粒子束，粒子在磁偶極場中的螺線運動極坐標微分方程構造。"}
                ],
                "system_trivialization_arsenal": [
                    {"id": "D3 8.1", "desc": "高中物理競賽壓軸題：質點在圓錐面內作水平勻速圓周運動，求支持力與角速度。傳統受力分解繁複，以極坐標加速度分量方程一步列出平衡方程。"},
                    {"id": "D3 8.2", "desc": "高三聯考力學難題：小球在光滑半球頂端由靜止滑落，求脫離球面的臨界角。傳統能量守恆加向心力聯立需多步代入，直接以法向加速度 $a_n = g\\cos\\theta$ 在脫離點法向力為零 3 行秒殺得出 $\\cos\\theta = 2/3$。"},
                    {"id": "D3 8.3", "desc": "物理模擬題：圓盤上半徑位置有一小孔，光滑桿穿孔旋轉，滑塊在桿上自由滑動，求滑塊在離心力與科氏力下的運動軌跡，直接調用極坐標加速度方程秒出微分方程。"}
                ]
            }
        },
        {
            "id": 9,
            "title": "變分極值雛形：費馬時間極值原理（幾何光學第一性原理）",
            "book_blueprint": "從『導數為零是極值的必要條件』跨越到『大自然依照極值原理運作』的哲學飛躍；以費馬原理『光沿著耗時最短的路徑傳播』為唯一起點，無跳步推導幾何光學折射斯涅爾定律；奠定拉格朗日最小作用量原理雛形。",
            "dojo_core": "黑板直擊：在黑板上建立介質分界面坐標，設定光傳播時間函數 $T(x)$，讓學生在黑板上對位置坐標求導並令 $\\frac{\\mathrm{d}T}{\\mathrm{d}x} = 0$，直擊無幾何輔助線而自動誕生 $\\frac{\\sin\\theta_1}{v_1} = \\frac{\\sin\\theta_2}{v_2}$ 的代數奇蹟。",
            "formulas": [
                {"id": "Eq 9.1", "name": "費馬最小光程時間泛函式", "latex": "T = \\int \\frac{\\mathrm{d}s}{v} = \\frac{1}{c}\\int n\\,\\mathrm{d}s \\quad (\\text{時間極值公理})"},
                {"id": "Eq 9.2", "name": "兩介質折射總傳播時間函數", "latex": "T(x) = \\frac{\\sqrt{h_1^2 + x^2}}{v_1} + \\frac{\\sqrt{h_2^2 + (L - x)^2}}{v_2}"},
                {"id": "Eq 9.3", "name": "時間對分界點坐標一階微商式", "latex": "\\frac{\\mathrm{d}T}{\\mathrm{d}x} = \\frac{x}{v_1\\sqrt{h_1^2 + x^2}} - \\frac{L - x}{v_2\\sqrt{h_2^2 + (L - x)^2}}"},
                {"id": "Eq 9.4", "name": "幾何三角幾何正弦對應式", "latex": "\\sin\\theta_1 = \\frac{x}{\\sqrt{h_1^2 + x^2}}, \\quad \\sin\\theta_2 = \\frac{L - x}{\\sqrt{h_2^2 + (L - x)^2}}"},
                {"id": "Eq 9.5", "name": "極值駐點斯涅爾定律導出式", "latex": "\\frac{\\mathrm{d}T}{\\mathrm{d}x} = 0 \\iff \\frac{\\sin\\theta_1}{v_1} = \\frac{\\sin\\theta_2}{v_2} \\iff n_1 \\sin\\theta_1 = n_2 \\sin\\theta_2"},
                {"id": "Eq 9.6", "name": "時間二階微商嚴格正定極小檢驗", "latex": "\\frac{\\mathrm{d}^2T}{\\mathrm{d}x^2} = \\frac{h_1^2}{v_1 (h_1^2 + x^2)^{3/2}} + \\frac{h_2^2}{v_2 (h_2^2 + (L-x)^2)^{3/2}} > 0 \\quad (\\text{必為時間極小值})"},
                {"id": "Eq 9.7", "name": "非均勻介質光線微分方程", "latex": "\\frac{\\mathrm{d}}{\\mathrm{d}s}\\left(n \\frac{\\mathrm{d}\\mathbf{r}}{\\mathrm{d}s}\\right) = \\nabla n \\quad (\\text{連續介質光學極限})"}
            ],
            "problems": {
                "worked_examples": [
                    {"id": "Ex 9.1", "desc": "給定兩點 $A(0, h_1)$ 與 $B(L, -h_2)$，介質分界面為 $x$ 軸。寫出光線由 $A$ 經 $(x, 0)$ 到 $B$ 的總時間 $T(x)$，無跳步計算 $\\frac{\\mathrm{d}T}{\\mathrm{d}x}$，令其為零嚴格導出折射定律 $n_1\\sin\\theta_1 = n_2\\sin\\theta_2$。"},
                    {"id": "Ex 9.2", "desc": "計算時間函數的二階導數 $\\frac{\\mathrm{d}^2T}{\\mathrm{d}x^2}$，證明其各項均大於零，從而嚴格證明該駐點是局域極小值（耗時最短）而非極大值。"},
                    {"id": "Ex 9.3", "desc": "利用費馬原理分析平面鏡反射：光在同種均勻介質中傳播，證明入射角等於反射角，並說明此時時間為極小的幾何直線對稱解。"}
                ],
                "margin_inquiries": [
                    {"id": "Th 9.1", "desc": "【深水思辨】光沒有大腦，它在起點出發時怎麼知道終點在哪裡？它怎麼知道該選擇哪一條路徑耗時最短？這種『目的論』色彩的極值原理，在量子電動力學（費曼路徑積分）中是如何被量子相干疊加還原為純物理波的？"},
                    {"id": "Th 9.2", "desc": "【體制內盲點】中學物理將反射定律與折射定律當成兩個獨立實驗經驗定律死背。微積分告訴我們：自然界只遵循一條公理——時間泛函極值，這展示了怎樣的降維打擊？"},
                    {"id": "Th 9.3", "desc": "【極大還是極小？】費馬原理的嚴格表述是『時間取駐值（Stationary Time）』，它一定是極小值嗎？在凹面鏡反射中，是否存在時間取極大值或鞍點的真實光線？"}
                ],
                "foundational_drills": [
                    {"id": "P1 9.1", "desc": "閉卷寫出兩介質傳播時間函數 $T(x)$，並展示利用鏈式法則求導得出斯涅爾定律的全過程。"},
                    {"id": "P1 9.2", "desc": "設光在第一介質速度為 $c$，第二介質速度為 $c/2$，$h_1 = 3, h_2 = 4, L = 5$，求分界面入射點 $x$ 滿足的四次代數方程形式。"},
                    {"id": "P1 9.3", "desc": "救生員在岸上奔跑速度為 $v_1 = 6\\,\\mathrm{m/s}$，在水中游泳速度為 $v_2 = 2\\,\\mathrm{m/s}$，溺水者位於斜前方海中，利用費馬折射微積分求最快營救路線的折角條件。"},
                    {"id": "P1 9.4", "desc": "證明在均勻介質中，兩點間光程最短的路徑必為直線。"}
                ],
                "interdisciplinary_applications": [
                    {"id": "P2 9.1", "desc": "【海市蜃樓大氣折射】地表空氣溫度高、密度小，折射率隨高度增加 $n(y) = n_0\\sqrt{1 + k y}$。利用連續分層斯涅爾定律 $n(y)\\cos\\theta(y) = \\text{const}$，推導光線彎曲軌跡的微分方程並求拋物線解。"},
                    {"id": "P2 9.2", "desc": "【漸變折射率光纖】光纖芯軸折射率呈拋物線分佈 $n(r) = n_0[1 - \\frac{1}{2}\\Delta(r/a)^2]$，利用費馬原理證明光線在光纖內傳播軌跡為正弦曲線，不同入射角光線耗時嚴格等時（自聚焦透鏡）。"},
                    {"id": "P2 9.3", "desc": "【地震波走時反演】地球地幔中地震波速隨深度增加，震源激發的波線在地球內部向下彎曲並返回地面，構造走時曲線 $T(X)$ 的變分微商關係。"},
                    {"id": "P2 9.4", "desc": "【最速降線經典問題雛形】質點在重力場中從 $A$ 點無摩擦滑到 $B$ 點，根據能量守恆 $v = \\sqrt{2gy}$，將最速降線問題轉譯為等效折射率 $n(y) = 1/\\sqrt{y}$ 的光學路徑，求擺線微分方程。"}
                ],
                "deepwater_challenges": [
                    {"id": "P3 9.1", "desc": "【歐拉-拉格朗日方程初探】設路徑泛函 $J[y] = \\int_{x_1}^{x_2} F(x, y, y')\\,\\mathrm{d}x$。設最優路徑為 $y(x)$，引入微擾 $\\eta(x)$，證明極值條件必導致微分方程 $\\frac{\\partial F}{\\partial y} - \\frac{\\mathrm{d}}{\\mathrm{d}x}\\left(\\frac{\\partial F}{\\partial y'}\\right) = 0$。"},
                    {"id": "P3 9.2", "desc": "【光學引力透鏡效應】在廣義相對論弱場近似下，巨大質量星體周圍時空彎曲，等效折射率為 $n(r) = 1 + \\frac{2GM}{c^2 r}$。利用費馬原理計算光線掠過恆星邊緣時的偏折角 $\\Delta\\theta = \\frac{4GM}{c^2 b}$。"}
                ],
                "dojo_defense_tasks": [
                    {"id": "D1 9.1", "desc": "學員甲在黑板求 $\\frac{\\mathrm{d}T}{\\mathrm{d}x} = 0$，得到代數方程後試圖通分交叉相乘求解四次方程。導師立即喝止：『不要陷入中學死算的代數泥淖！抬起頭看圖，這個比值不正是幾何直角三角形的正弦值嗎？立刻換元寫出 $\\sin\\theta$！』"},
                    {"id": "D1 9.2", "desc": "學員乙被要求在黑板分析光的全反射臨界角。導師質詢：『在全反射發生時，折射角 $\\theta_2 = 90^\\circ$。在費馬時間函數中，分界點 $x$ 跑到哪裡去了？時間極值點是否已經越過了幾何邊界？』"},
                    {"id": "D1 9.3", "desc": "學員丙上黑板論證橢圓鏡面的光學性質：從一個焦點出發的光線經橢圓反射必匯聚於另一焦點。導師詰問：『這條光線的傳播時間是極大、極小還是所有路徑時間完全嚴格相等？為什麼？』"}
                ],
                "unseen_sandbox_scenarios": [
                    {"id": "D2 9.1", "desc": "在各向異性雙折射晶體中，折射率是傳播方向的函數 $n(\\theta)$，現場利用費馬變分原理構造光線波法線與射線方向分離的微分關係。"},
                    {"id": "D2 9.2", "desc": "聲納信號在深海深海聲道（SOFAR channel）中傳播，海水中聲速在某一深度達到極小，現場構造聲波在該聲道內往返振盪傳播的極限微商。"},
                    {"id": "D2 9.3", "desc": "二維表面上存在高度起伏 $z = h(x, y)$，螞蟻在曲面上爬行遵循測地線（耗時最短），現場構造測地線微分方程。"}
                ],
                "system_trivialization_arsenal": [
                    {"id": "D3 9.1", "desc": "高中物理競賽題：證明光線穿過平行玻璃磚後出射光線與入射光線平行且產生側移。傳統幾何多次追蹤折射角，利用費馬原理分界面切向動量守恆直接 1 行判定出射角相等。"},
                    {"id": "D3 9.2", "desc": "高二幾何光學難題：半徑為 $R$ 的玻璃球折射率為 $n = \\sqrt{3}$，平行光入射後在球後表面焦點位置。利用費馬原理光程差為零，比傳統三角計算快 3 倍求出焦點坐標。"},
                    {"id": "D3 9.3", "desc": "數學競賽極值題：平面上求一點 $P$ 到直線兩側兩定點折線權重距離之和最小。轉譯為費馬光學折射模型，直接用斯涅爾定律正弦比秒出幾何角。"}
                ]
            }
        }
    ]
}

if __name__ == "__main__":
    print(f"Loaded {STAGE_3['title']} with {len(STAGE_3['lessons'])} lessons.")
    total_f = sum(len(l['formulas']) for l in STAGE_3['lessons'])
    total_p = sum(
        len(l['problems']['worked_examples']) +
        len(l['problems']['margin_inquiries']) +
        len(l['problems']['foundational_drills']) +
        len(l['problems']['interdisciplinary_applications']) +
        len(l['problems']['deepwater_challenges']) +
        len(l['problems']['dojo_defense_tasks']) +
        len(l['problems']['unseen_sandbox_scenarios']) +
        len(l['problems']['system_trivialization_arsenal'])
        for l in STAGE_3['lessons']
    )
    print(f"Total formulas: {total_f} (Expect 21), Total problems: {total_p} (Expect 75)")
