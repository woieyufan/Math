# -*- coding: utf-8 -*-
"""
update_assemble_script.py:
重寫 assemble_two_bluepapers.py，完全支援 28 個有機章節體系。
"""

import os
import sys

SCRATCH_DIR = r"C:\Users\user\.gemini\antigravity\brain\17c5c8ea-1f34-4270-a5e4-410bdd5037d4\scratch"

content = '''# -*- coding: utf-8 -*-
"""
assemble_two_bluepapers.py: 將藍皮書正式拆分為兩本完全獨立的工程母本：
1. 《中學超前自學·微積分先修專著出版工程指引（藍皮書·書籍篇）》
   - 28 章（Chapters 1–28，7 大篇有機生長）
   - 196 條核心骨架公式鏈
   - 448 道書籍專屬題目（例題 84 + 邊欄思辨 84 + 基礎 112 + 跨科 112 + 深水 56）
   - 章末道場攻防邀請卡
   - 完整裝幀、排版網格、字體字級、四重邊欄話語體系、20 項合規清單

2. 《中學超前自學·微積分黑板研討道場實戰工程指引（藍皮書·課堂篇）》
   - 28 專題（Topics 1–28，56 小時研討）
   - 196 條核心板書公式鏈
   - 252 道道場專屬實彈題目（黑板攻防 84 + 未知破局 84 + 體制秒殺 84）
   - 黑板四分區動線、120 分鐘節奏控制、蘇格拉底攻防話術、五維雷達評量表
"""

import os
import sys

from stage1_data import STAGE_1
from stage2_data import STAGE_2
from stage3_data import STAGE_3
from stage4_data import STAGE_4
from stage5_data import STAGE_5
from stage6_data import STAGE_6
from stage7_data import STAGE_7

ALL_STAGES = [STAGE_1, STAGE_2, STAGE_3, STAGE_4, STAGE_5, STAGE_6, STAGE_7]

# -------------------------------------------------------------
# 1. 構建《書籍篇》 (The Book Blueprint)
# -------------------------------------------------------------
def build_book_bluepaper():
    lines = []
    lines.append("# 中學超前自學·微積分先修專著出版工程指引（藍皮書·書籍篇）")
    lines.append("\\n**THE PRECOLLEGE CALCULUS MONOGRAPH: BOOK AUTHORING & PUBLISHING BLUEPRINT**\\n")
    lines.append("> **體系機構**：`woieyufan EDUCATION` 智庫出版母本  ")
    lines.append("> **文件版本**：`v2.0 有機進化出版工程定稿（徹底打破 24 堂課人為限制）`  ")
    lines.append("> **定位讀者**：專著撰寫團隊、文字編輯、排版裝幀設計師、超前自學資優生（國二升國三、國三升高一先修）  ")
    lines.append("> **工程定量標準**：**7 大篇 ｜ 28 個有機完整章節 ｜ 196 條核心演繹公式 ｜ 448 道書籍專屬階梯題庫**\\n")
    lines.append("---\\n")
    
    # 目錄
    lines.append("## 全書章節目錄（Table of Contents）\\n")
    lines.append("- [第一篇：專著出版總論與規格體例](#第一篇專著出版總論與規格體例)")
    lines.append("  - 1.1 書名定位與兩階段轉化閉環中的「基石地位」")
    lines.append("  - 1.2 卷冊劃分規劃：雙卷典藏版 vs 單卷旗艦版")
    lines.append("  - 1.3 裝幀工藝與材料標準（硬殼精裝、櫻花道林紙、鎖線平攤）")
    lines.append("  - 1.4 版心網格系統與字體家族（黃金比例大邊欄、思源宋體、AMS Euler）")
    lines.append("  - 1.5 四重邊欄手札話語體系（思想史、深水區、體制解法批判、道場攻防前哨）")
    lines.append("  - 1.6 單章「七步推進標準」與 16 道題排版動線")
    lines.append("  - 1.7 全書 28 章版面字數與邊欄空間預算表（Page & Word Budgeting Grid）")
    lines.append("- [第二篇至第八篇：全書 7 大篇 28 章詳細撰寫母本](#第二篇part-i極限定義無窮小階數與微分算子基礎chapters-13)")
    lines.append("- [第九篇：圖書出版審查清單與解答手冊規範](#第九篇圖書出版審查清單與解答手冊規範)")
    lines.append("  - 9.1 單章出版前 20 項第一性原理合規檢查表")
    lines.append("  - 9.2 書末解答手冊（Solution Manual）編寫規範")
    lines.append("- [第十篇：全書 112 幅核心幾何向量圖繪製規範清冊](#第十篇全書-112-幅核心幾何向量圖繪製規範清冊visual-asset-catalog)")
    lines.append("- [第十一篇：書末附錄·448 道專著題目官方標準答案與關鍵封閉解](#第十一篇書末附錄448-道專著題目官方標準答案與關鍵封閉解master-answer-keys)\\n")
    lines.append("---\\n")
    
    # 第一篇
    lines.append("## 第一篇：專著出版總論與規格體例\\n")
    lines.append("### 1.1 書名定位與兩階段轉化閉環中的「基石地位」")
    lines.append("本書定名為**《中學超前自學微積分：以近代高等數學為唯一骨架之數理通論》**。")
    lines.append("在 `woieyufan EDUCATION` 兩階段閉環中，本書扮演著**「案頭智力沉澱與公理震撼」**的絕對基石角色。讀者在進入黑板研討道場之前，必須藉由研讀本書建立起不可動搖的代數肌肉記憶、無跳步公理意識與相空間直覺。全書徹底摒棄任何課堂數量、章節數量的死板限制，以高中數理化體制內必考痛點公式為核心，自然有機生長至 28 個完整章節，講透為止！\\n")
    
    lines.append("### 1.2 卷冊劃分規劃")
    lines.append("- **上冊【微分學純數脊椎骨、幾何與積分初登場】（Part I – Part IV，Chapters 1–14，約 320 頁）**：涵蓋極限定義、多項式降階、切線重根、連鎖律、隱微分、狀態空間微商、弧度無量綱化、旋轉基底、費馬極值、黎曼和、FTC、第一面積矩、做功線積分，以及高爾頓板二項分佈長條圖坍縮引導出的機率密度函數初登場。")
    lines.append("- **下冊【物理場域實戰、多變數幾何、微分方程與近代物理閉環】（Part V – Part VII，Chapters 15–28，約 380 頁）**：涵蓋三位一體儲能 1/2 狀態積分、流體光壓動量流率、剛體轉動慣量微元、畢奧-薩伐爾導線線圈磁場積分、絕熱過程 PV^gamma=C、對數發明、泰勒級數與斯特靈階乘、多變數全微分誤差傳播、二重極座標幾何、高斯常態分佈終局閉環與馬克士威氣體速率、一階二階常微分方程、RC/RL 暫態、簡諧運動淘汰參考圓、交流電 RMS 與近代量子測不準原理大一統。\\n")
    
    lines.append("### 1.3 裝幀工藝與材料標準")
    lines.append("- **開本尺寸**：標準 16 開（B5 / $182\\,\\mathrm{mm} \\times 257\\,\\mathrm{mm}$）。")
    lines.append("- **封面裝幀**：厚磅硬殼精裝（Hardcover），深藍布紋包覆，封面壓印燙銀 `woieyufan EDUCATION` 向下微標誌徽章。")
    lines.append("- **內頁用紙**：$80\\,\\mathrm{g}$ 日本進口櫻花米白道林紙（色溫柔和護眼、吸墨性強、鉛筆與鋼筆書寫不透墨）。")
    lines.append("- **裝訂工藝**：純手工穿線鎖線膠裝，確保全書可 **$180^\\circ$ 完全平攤於案頭**，讀者雙手脫離書籍書寫筆記時不回彈。\\n")
    
    lines.append("### 1.4 版心網格系統與字體家族（Grid & Typography）")
    lines.append("- **大邊欄網格系統（Marginalia Grid）**：")
    lines.append("  - 內側訂口：$22\\,\\mathrm{mm}$（杜絕裝訂吃字）。")
    lines.append("  - 正文版心：佔頁寬 $65\\%$，行長控制在 38 個漢字左右，達到最優閱讀掃描頻率。")
    lines.append("  - 外側邊欄：佔頁寬 $25\\%$（寬達 $45\\,\\mathrm{mm}$），專供四重邊欄手札與讀者 Apple Pencil / 鉛筆筆記。")
    lines.append("  - 欄間距：$8\\,\\mathrm{mm}$。")
    lines.append("- **字體階層**：")
    lines.append("  - 中文正文：思源宋體（Source Han Serif）10.5pt，行高 1.62。")
    lines.append("  - 西文字體：Palatino / Computer Modern 10pt。")
    lines.append("  - 數學公式：AMS Euler 字體，微商算子 $\\mathrm{d}$ 一律採用直體以區別於距離變數 $d$。")
    lines.append("  - 邊欄手札：思源黑體 8.5pt，灰度 70%，行高 1.4。\\n")
    
    lines.append("### 1.5 四重邊欄手札話語體系")
    lines.append("外側邊欄配置四種固定手札模塊：")
    lines.append("1. **`[思想史溯源 Historical Context]`**：揭示公理演繹背後數學家的生死思辨。")
    lines.append("2. **`[直覺深水區警示 Deepwater Warning]`**：標註定義域陷阱、不可微奇點與量綱失守隱患。")
    lines.append("3. **`[體制內解法批判 System Illusion Debunked]`**：以微積分第一性原理直球對照體制內聯考繁複口訣。")
    lines.append("4. **`[道場攻防前哨 The Dojo Foreshadowing]`**：拋出開放式詰問，為讀者走入實體黑板道場埋下思維伏筆。\\n")
    
    lines.append("### 1.6 單章「七步推進標準」與 16 道題排版動線")
    lines.append("每章依序推進：認知衝突 $\\to$ 公理定義 $\\to$ 7 條核心公式無跳步推導 $\\to$ 幾何動態可視化 $\\to$ 跨科自然科學秒殺 $\\to$ 四重邊欄手札 $\\to$ **16 道階梯題庫**（3 例題 + 3 邊欄思辨 + 4 基礎默寫 + 4 跨科實戰 + 2 深水挑戰） $\\to$ **章末道場攻防邀請卡**。\\n")
    lines.append("---\\n")
    
    # 正文 28 章
    part_names = [
        "Part I：極限定義、無窮小階數與微分算子基礎（Chapters 1–3）",
        "Part II：多變量依賴、隱函數切線與相空間運動學（Chapters 4–6）",
        "Part III：無量綱弧度制、動態旋轉向量與費馬時間極值（Chapters 7–9）",
        "Part IV：黎曼和、微積分基本定理與機率密度的初登場（Chapters 10–14）",
        "Part V：物理場域實戰、三位一體儲能、轉動慣量、電流磁場與絕熱熱力學（Chapters 15–19）",
        "Part VI：超越函數發明、多變數幾何、二重極座標與統計終局大一統（Chapters 20–24）",
        "Part VII：常微分方程、RC/RL 暫態、簡諧運動淘汰參考圓與近代量子閉環（Chapters 25–28）"
    ]
    part_roman = ["第二篇", "第三篇", "第四篇", "第五篇", "第六篇", "第七篇", "第八篇"]
    
    for s_idx, st in enumerate(ALL_STAGES):
        lines.append(f"## {part_roman[s_idx]}：{part_names[s_idx]}\\n")
        lines.append(f"> **本篇主幹主題**：{st['theme']}\\n")
        
        for lesson in st["lessons"]:
            cid = lesson["id"]
            title = lesson["title"]
            lines.append(f"### Chapter {cid}：{title}\\n")
            lines.append(f"> **📖 專著編寫指南（Authoring Blueprint）**：{lesson['book_blueprint']}\\n")
            
            # 7 條公式鏈
            lines.append("#### 本章 7 條核心骨架公式鏈演繹清單")
            for f in lesson["formulas"]:
                fid = f["id"]
                fname = f["name"]
                flatex = f["latex"]
                lines.append(f"- **`{fid}`【{fname}】**：$${flatex}$$")
                
            # 16 道專著題目
            p = lesson["problems"]
            lines.append(f"\\n#### Chapter {cid} 專屬 16 道階梯題庫清冊")
            
            lines.append("##### 1. 公理建構示範例題（Worked Examples, 3 題）")
            for ex in p["worked_examples"]:
                lines.append(f"- **`{ex['id']}`**：{ex['desc']}")
                
            lines.append("\\n##### 2. 邊欄 Socratic 思辨詰問（Margin Inquiries, 3 題）")
            for th in p["margin_inquiries"]:
                lines.append(f"- **`{th['id']}`**：{th['desc']}")
                
            lines.append("\\n##### 3. Level 1: 基礎公理默寫與純數變換（Foundational Drills, 4 題）")
            for p1 in p["foundational_drills"]:
                lines.append(f"- **`{p1['id']}`**：{p1['desc']}")
                
            lines.append("\\n##### 4. Level 2: 自然科學跨學科實戰（Interdisciplinary Applications, 4 題）")
            for p2 in p["interdisciplinary_applications"]:
                lines.append(f"- **`{p2['id']}`**：{p2['desc']}")
                
            lines.append("\\n##### 5. Level 3: 邊界奇異點與深水區挑戰（Deepwater Challenges, 2 題）")
            for p3 in p["deepwater_challenges"]:
                lines.append(f"- **`{p3['id']}`**：{p3['desc']}")
                
            # 道場邀請卡
            lines.append(f"\\n#### 🥋 Chapter {cid} 章末黑板道場攻防邀請卡（The Dojo Invitation Card）")
            lines.append("```")
            lines.append(f"┌────────────────────────────────────────────────────────────────────────┐")
            lines.append(f"│ 🥋 woieyufan EDUCATION · 黑板研討道場攻防邀請卡 · Chapter {cid:02d}           │")
            lines.append(f"├────────────────────────────────────────────────────────────────────────┤")
            lines.append(f"│ 研討專題：{title[:48]} │")
            lines.append(f"│ 入場前提：已完成 Chapter {cid:02d} 16 道習題草稿，徹底理解 7 條核心公式鏈。       │")
            lines.append(f"│ 道場規則：封印一切教材、筆記與計算機！純粹依靠黑板、粉筆與思維肉搏！   │")
            lines.append(f"│ 攻防焦點：導師將在黑板四區隨機抽查，量綱突襲、反例刺穿、未知情境破局！ │")
            lines.append(f"└────────────────────────────────────────────────────────────────────────┘")
            lines.append("```\\n---\\n")
            
    # 第九篇
    lines.append("## 第九篇：圖書出版審查清單與解答手冊規範\\n")
    lines.append("### 9.1 單章出版前 20 項第一性原理合規檢查表")
    checklist = [
        "1. 核心公式是否達到 7 條骨架標準，且編號為 Eq X.1 ～ Eq X.7？",
        "2. 所有物理量綱在微商與定積分運算中是否全程保持齊次性？",
        "3. 微商符號 d 是否嚴格採用 LaTeX 直體 \\\\mathrm{d}？",
        "4. 極限定義是否徹底杜絕『0/0』模糊語言，嚴格用微元展開說明？",
        "5. 鏈鎖律推導是否嚴格說明中間變數可微性，無死板約分假象？",
        "6. 隱函數求導是否在幾何軌跡與相空間層面進行切線驗證？",
        "7. 運動學公式是否全部消去時間，以相空間 a = v(dv/dx) 統一？",
        "8. 弧度制定義是否在第一步徹底完成無量綱化？",
        "9. 三角求導是否在單位圓動態旋轉向量幾何下給出直觀投影？",
        "10. 費馬原理推導是否完整給出光程時間一階導數為零？",
        "11. 黎曼和是否包含分割、取樣、求和、取極限四部曲？",
        "12. FTC 推導是否徹底展示微分算子與定積分算子的互逆抵消？",
        "13. 變力做功是否建立在勢能曲面負梯度的嚴格線積分上？",
        "14. 機率密度初登場是否以二項分佈長條圖坍縮立論，破除單點為零心魔？",
        "15. 三位一體儲能 (動能、電容、電感) 是否在相空間三角形積分下大一統？",
        "16. 電流磁效應是否由畢奧-薩伐爾定律嚴格導出長直導線與圓線圈中心磁場？",
        "17. 絕熱過程 PV^gamma = C 是否由第一定律分離變數法嚴格推導？",
        "18. 高斯積分是否由二重極座標完整證明 sqrt(pi)，清償 Stage 4 係數債務？",
        "19. 簡諧運動是否徹底淘汰參考圓投影，純粹由二階 ODE 特徵解代數閉環？",
        "20. 每章 16 道習題是否嚴格覆蓋 5 大階梯，配備獨立章末邀請卡？"
    ]
    for c in checklist:
        lines.append(f"- [ ] **合規項 {c}**")
        
    lines.append("\\n### 9.2 書末解答手冊（Solution Manual）編寫規範")
    lines.append("- **示範例題**：必須包含完整的『公理出發點』、『無跳步代數推導鏈條』、『量綱檢驗』與『物理幾何意象』四項要素。")
    lines.append("- **邊欄思辨題**：給出 200 字以內直擊本質的哲學與物理判詞，杜絕模稜兩可。")
    lines.append("- **基礎運算與跨科題**：給出標準封閉數值解或代數解析式，關鍵步驟標註微積分變換技巧。")
    lines.append("- **深水挑戰題**：提供完整證明路徑、反例構造或漸近展開的高階修正項。\\n")
    lines.append("---\\n")
    
    return "\\n".join(lines)


# -------------------------------------------------------------
# 2. 構建《課堂篇》 (The Dojo Manual)
# -------------------------------------------------------------
def build_dojo_bluepaper():
    lines = []
    lines.append("# 中學超前自學·微積分黑板研討道場實戰工程指引（藍皮書·課堂篇）")
    lines.append("\\n**THE BLACKBOARD RESEARCH DOJO: OPERATIONAL TEACHING & DIALECTIC MANUAL**\\n")
    lines.append("> **體系機構**：`woieyufan EDUCATION` 智庫教研母本  ")
    lines.append("> **文件版本**：`v2.0 有機進化道場教研定稿（徹底打破 24 堂課人為限制）`  ")
    lines.append("> **定位讀者**：道場主講導師、黑板研討助理教練、客座答辯評審  ")
    lines.append("> **工程定量標準**：**56 小時 ｜ 28 個有機研討專題 ｜ 196 條黑板板書公式 ｜ 252 道實彈攻防題庫**\\n")
    lines.append("---\\n")
    
    # 目錄
    lines.append("## 全書章節目錄（Table of Contents）\\n")
    lines.append("- [第一篇：黑板研討道場憲章與執教 SOP](#第一篇黑板研討道場憲章與執教-sop)")
    lines.append("  - 1.1 道場教育宣言：為什麼「封印 PPT、回歸黑板實彈推導」是不可妥協的底線")
    lines.append("  - 1.2 實體黑板「四分區工程動線」標準佈局（Chalkboard Layout Specification）")
    lines.append("  - 1.3 單堂 120 分鐘精確節奏控制表（Precision Rhythm Protocol）")
    lines.append("  - 1.4 蘇格拉底式「冷酷攻防詰問」操作劇本（Socratic Interrogation Scenarios）")
    lines.append("  - 1.5 學員上台推演與盲點阻斷機制（Chalk Relay & Peer Defense）")
    lines.append("- [第二篇至第八篇：28 個研討專題教案與 252 道實彈題庫](#第二篇stage-i公理出發無窮小與單項式微積分topics-13)")
    lines.append("- [第九篇：道場評量規準與教練考核體系](#第九篇道場評量規準與教練考核體系)")
    lines.append("  - 9.1 學員黑板答辯五維雷達評量表與評分標準（Radar Rubrics）")
    lines.append("  - 9.2 助教研討教練培訓與執教合規檢核表")
    lines.append("- [第十篇：道場附錄·252 道實彈攻防題導師底牌答案與 3 行秒殺動線庫](#第十篇道場附錄252-道實彈攻防題導師底牌答案與-3-行秒殺動線庫dojo-interrogation-keys)\\n")
    lines.append("---\\n")
    
    # 第一篇
    lines.append("## 第一篇：黑板研討道場憲章與執教 SOP\\n")
    lines.append("### 1.1 道場教育宣言：為什麼「封印 PPT、回歸黑板實彈推導」是不可妥協的底線")
    lines.append("投影片（PPT/Keynote）是思維的火葬場。投影念稿營造了一種「我都聽懂了」的致命虛假流暢感，讓學生的思維停留在被動接收的淺層水平。")
    lines.append("在 `woieyufan EDUCATION` 黑板研討道場中，**教室內嚴禁開啟投影機**！唯一的武器是四米長的墨黑磁性黑板、無塵石膏粉筆與板擦。導師與學員必須在黑板上一筆一劃寫出每一個極限、每一個展開項與每一個微元向量。唯有手部肌肉與黑板摩擦產生的代數痕跡，才能將微積分的第一性原理深深烙印在神經元迴路中。全道場打破死板 24 節課框架，拓展為 28 個有機專題，56 小時火力全開！\\n")
    
    lines.append("### 1.2 實體黑板「四分區工程動線」標準佈局")
    lines.append("黑板由左至右嚴格劃分為四大機能區，全堂嚴格執行分區書寫：")
    lines.append("```")
    lines.append("┌─────────────────┬───────────────────────────────┬─────────────────┬─────────────────┐")
    lines.append("│ 一、公理與錨定區 │       二、代數推演主動線區      │ 三、物理幾何投影區│ 四、學員答辯攻防區│")
    lines.append("│                 │                               │                 │                 │")
    lines.append("│ • 數學核心定義   │ • 主定理微商/定積分連鎖展開   │ • 物理情境圖解   │ • 學員推導演練  │")
    lines.append("│ • 邊界條件/已知  │ • 零跳步代數等號鏈條          │ • 相空間軌跡圖   │ • 典型漏洞記錄  │")
    lines.append("│ • 坐標系基底定義 │ • 換元矩陣與消項證明          │ • 向量微元幾何   │ • 體制解法對比  │")
    lines.append("│ (整堂不擦除！)  │ (由左至右、由上而下，寫滿更換)│ (動態圖解標註)  │ (即時論辯攻防)  │")
    lines.append("└─────────────────┴───────────────────────────────┴─────────────────┴─────────────────┘")
    lines.append("```\\n")
    
    lines.append("### 1.3 單堂 120 分鐘精確節奏控制表（Precision Rhythm Protocol）")
    lines.append("- **00–15 min【書籍預讀質疑與公理審查】**：隨機抽查學員對書籍篇相應章節的研讀筆記，針對邊欄思辨題展開破冰攻防。")
    lines.append("- **15–50 min【核心數學工具黑板實彈構建】**：導師在二區與三區完成 7 條核心公式鏈的無跳步演繹，嚴格落實四大鐵律。")
    lines.append("- **50–85 min【自然科學跨科實彈推演與學員上台】**：指定學員走上四區黑板，在無筆記輔助下推導物理模型，導師冷酷詰問。")
    lines.append("- **85–110 min【未知情境破局與體制題降維秒殺】**：現場拋出未知競賽/大學物理情境，全員黑板實彈對攻；隨後展示 3 行秒殺體制題。")
    lines.append("- **110–120 min【思維反芻與下週道場任務發布】**：盤點黑板漏洞，發布下週專題預讀任務與思考題。\\n")
    
    lines.append("### 1.4 蘇格拉底式「冷酷攻防詰問」操作劇本")
    lines.append("導師在課堂上不是慈祥的講授者，而是「思維的冷酷審查官」：")
    lines.append("1. **「追問隱藏前提」**：『你在第 3 行換元時，為什麼沒有檢查被積函數在該區間是否處處可積？』")
    lines.append("2. **「量綱突襲」**：突然指著黑板中間一項：『這項的物理量綱是什麼？在黑板上把 M、L、T 寫出來！』")
    lines.append("3. **「極限反例刺穿」**：『令質量 $m \\\\to 0$ 或速度 $v \\\\to c$，你的公式在幾何上退化成什麼？物理意義崩潰在哪裡？』")
    lines.append("4. **「黑板接力機制（Chalk Relay）」**：學員推導到關鍵節點時，導師突然喊停，將粉筆交給台下另一位學員接續推演，台下學員隨時擔任陪審團抓漏。\\n")
    lines.append("---\\n")
    
    # 正文 28 專題
    stage_names = [
        "Stage I：公理出發、無窮小與單項式微積分（Topics 1–3）",
        "Stage II：複合映射、隱函數與相空間（Topics 4–6）",
        "Stage III：無量綱弧度制與三角分析（Topics 7–9）",
        "Stage IV：黎曼和、基本定理與機率密度的初登場（Topics 10–14）",
        "Stage V：物理場域實戰、三位一體儲能、轉動慣量、電流磁場與絕熱熱力學（Topics 15–19）",
        "Stage VI：超越函數發明、多變數幾何、二重極座標與統計終局大一統（Topics 20–24）",
        "Stage VII：常微分方程、RC/RL 暫態、簡諧運動淘汰參考圓與近代量子閉環（Topics 25–28）"
    ]
    stage_roman = ["第二篇", "第三篇", "第四篇", "第五篇", "第六篇", "第七篇", "第八篇"]
    
    for s_idx, st in enumerate(ALL_STAGES):
        lines.append(f"## {stage_roman[s_idx]}：{stage_names[s_idx]}\\n")
        lines.append(f"> **本階研討目標**：{st['theme']}\\n")
        
        for lesson in st["lessons"]:
            tid = lesson["id"]
            title = lesson["title"]
            lines.append(f"### Topic {tid}：{title}\\n")
            lines.append(f"> **🥋 道場研討核心（Dojo Core Mission）**：{lesson['dojo_core']}\\n")
            
            # 板書核心公式代碼
            lines.append("#### 黑板板書必演 7 條核心公式鏈")
            for f in lesson["formulas"]:
                fid = f["id"].replace("Eq", "Brd")
                fname = f["name"]
                flatex = f["latex"]
                lines.append(f"- **`{fid}`【{fname}】**：$${flatex}$$")
                
            # 道場 9 道實彈題
            p = lesson["problems"]
            lines.append(f"\\n#### Topic {tid} 專屬 9 道道場攻防實彈題庫")
            
            lines.append("##### 1. 黑板現場抽籤攻防題（Chalkboard Defense Tasks, 3 題）")
            for d1 in p["dojo_defense_tasks"]:
                lines.append(f"- **`{d1['id']}`**：{d1['desc']}")
                
            lines.append("\\n##### 2. 未知自然科學情境破局題（Unseen Sandbox Scenarios, 3 題）")
            for d2 in p["unseen_sandbox_scenarios"]:
                lines.append(f"- **`{d2['id']}`**：{d2['desc']}")
                
            lines.append("\\n##### 3. 體制內聯考大題降維秒殺題（System Trivialization Arsenal, 3 題）")
            for d3 in p["system_trivialization_arsenal"]:
                lines.append(f"- **`{d3['id']}`**：{d3['desc']}")
            lines.append("\\n---\\n")
            
    # 第九篇
    lines.append("## 第九篇：道場評量規準與教練考核體系\\n")
    lines.append("### 9.1 學員黑板答辯五維雷達評量表與評分標準（Radar Rubrics）")
    lines.append("道場每次課後針對每位學員進行五維雷達評分（每維度 1～5 分，滿分 25 分）：")
    lines.append("| 評量維度 | 1 分 (危險) | 3 分 (合格) | 5 分 (卓越 / 導師級) |")
    lines.append("| :--- | :--- | :--- | :--- |")
    lines.append("| **1. 公理第一性 (Axiomatic Grounding)** | 依賴記憶口訣，無法說明前提 | 能說出定義，但有跳步 | 嚴格由定義出發，零跳步，邊界條件自洽 |")
    lines.append("| **2. 板書工程結構 (Chalkboard Architecture)** | 字跡混亂，無分區，跳號推演 | 能按四分區書寫，佈局尚可 | 板書如印刷排版，等號對齊，幾何投影精確 |")
    lines.append("| **3. 跨科自然秒殺 (Cross-Domain Mastery)** | 僅能解純數題，遇物理題卡死 | 能列出物理方程但計算拖沓 | 一眼看穿物理模型幾何本質，3 行降維秒殺 |")
    lines.append("| **4. 逆向質疑答辯 (Socratic Defense)** | 導師質疑時慌亂認錯或沉默 | 能回答部分問題，代數修正慢 | 沉著指出導師陷阱，反例刺穿，邏輯反殺 |")
    lines.append("| **5. 體制降維統御 (System Transcendence)** | 仍依賴體制內技巧，解題耗時 | 能用微積分求解但缺乏自信 | 徹底碾壓體制內口訣，一眼識破出題破綻 |\\n")
    
    lines.append("### 9.2 助教研討教練培訓與執教合規檢核表")
    coach_checklist = [
        "1. 執教前是否已在黑板上無小抄獨立推演全堂 7 條公式鏈？",
        "2. 是否嚴格遵守『四分區板書動線』，未佔用或混淆公理區？",
        "3. 是否在課堂前 15 分鐘完成書籍篇邊欄手札的突擊抽查？",
        "4. 是否徹底封印 PPT 與任何電子投屏設備？",
        "5. 學員推導出錯時，是否採用反問與極限反例引導而非直接給答案？",
        "6. 每一條物理推導是否要求學員現場標註 M、L、T 量綱？",
        "7. 是否確保每位學員每兩週至少上台答辯一次（Chalk Relay）？",
        "8. 體制秒殺環節是否徹底講透微積分與初等解法的幾何對偶？",
        "9. 課後是否在 24 小時內完成全員五維雷達評量打分與反饋？",
        "10. 是否嚴守『不讓任何一位資優生帶著半點疑惑離開道場』的教研底線？"
    ]
    for c in coach_checklist:
        lines.append(f"- [ ] **教練檢核項 {c}**")
    lines.append("\\n---\\n")
    
    return "\\n".join(lines)


if __name__ == "__main__":
    book_content = build_book_bluepaper()
    dojo_content = build_dojo_bluepaper()
    
    book_path = r"C:\\Users\\user\\.gemini\\antigravity\\brain\\17c5c8ea-1f34-4270-a5e4-410bdd5037d4\\calculus_precollege_bluepaper_book.md"
    dojo_path = r"C:\\Users\\user\\.gemini\\antigravity\\brain\\17c5c8ea-1f34-4270-a5e4-410bdd5037d4\\calculus_precollege_bluepaper_dojo.md"
    
    with open(book_path, "w", encoding="utf-8") as f:
        f.write(book_content)
        
    with open(dojo_path, "w", encoding="utf-8") as f:
        f.write(dojo_content)
        
    print(f"Book assembled: {len(book_content)} chars")
    print(f"Dojo assembled: {len(dojo_content)} chars")
'''

with open(os.path.join(SCRATCH_DIR, "assemble_two_bluepapers.py"), "w", encoding="utf-8") as f:
    f.write(content)

print("assemble_two_bluepapers.py rewritten successfully for 28 chapters.")
