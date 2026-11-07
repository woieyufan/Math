# -*- coding: utf-8 -*-
"""
assemble_two_bluepapers.py: 完美拆分為兩本獨立工程母本 (28 堂全域無矛盾版)
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
    lines.append("\n**THE PRECOLLEGE CALCULUS MONOGRAPH: BOOK AUTHORING & PUBLISHING BLUEPRINT**\n")
    lines.append("> **體系機構**：`woieyufan EDUCATION` 智庫出版母本  ")
    lines.append("> **文件版本**：`v3.0 完美無矛盾出版工程定稿`  ")
    lines.append("> **定位讀者**：專著撰寫團隊、文字編輯、排版裝幀設計師、超前自學資優生（國二升國三、國三升高一先修）  ")
    lines.append("> **工程定量標準**：**7 大篇 ｜ 28 個有機完整章節 ｜ 196 條核心演繹公式 ｜ 448 道書籍專屬階梯題庫**\n")
    lines.append("---\n")
    
    # 目錄
    lines.append("## 全書章節目錄（Table of Contents）\n")
    lines.append("- [第一篇：專著出版總論與規格體例](#第一篇專著出版總論與規格體例)")
    lines.append("  - 1.1 書名定位與兩階段轉化閉環中的「基石地位」")
    lines.append("  - 1.2 卷冊劃分規劃：雙卷典藏版（上冊 Ch 1–19 / 下冊 Ch 20–28）")
    lines.append("  - 1.3 裝幀工藝與材料標準（硬殼精裝、櫻花道林紙、鎖線平攤）")
    lines.append("  - 1.4 版心網格系統與字體家族（黃金比例大邊欄、思源宋體、AMS Euler）")
    lines.append("  - 1.5 四重邊欄手札話語體系（思想史、深水區、體制解法批判、道場攻防前哨）")
    lines.append("  - 1.6 單章「七步推進標準」與 16 道題排版動線")
    lines.append("  - 1.7 全書 28 章版面字數與邊欄空間預算表（Page & Word Budgeting Grid）")
    lines.append("- [第二篇至第八篇：全書 7 大篇 28 章詳細撰寫母本](#第二篇part-i極限定義無窮小階數與微分算子基礎chapters-13)")
    lines.append("- [第九篇：圖書出版審查清單與解答手冊規範](#第九篇圖書出版審查清單與解答手冊規範)")
    lines.append("- [第十篇：全書 112 幅核心幾何向量圖繪製規範清冊](#第十篇全書-112-幅核心幾何向量圖繪製規範清冊visual-asset-catalog--specs)")
    lines.append("- [第十一篇：書末附錄·448 道專著題目官方標準答案與關鍵封閉解](#第十一篇書末附錄448-道專著題目官方標準答案與關鍵封閉解master-answer-keys)\n")
    lines.append("---\n")
    
    # 第一篇
    lines.append("## 第一篇：專著出版總論與規格體例\n")
    lines.append("### 1.1 書名定位與兩階段轉化閉環中的「基石地位」")
    lines.append("本書定名為**《中學超前自學微積分：以近代高等數學為唯一骨架之數理通論》**。")
    lines.append("在 `woieyufan EDUCATION` 兩階段閉環中，本書扮演著**「案頭智力沉澱與公理震撼」**的絕對基石角色。讀者在進入黑板研討道場之前，必須藉由研讀本書建立起不可動搖的代數肌肉記憶、無跳步公理意識與相空間直覺。全書徹底摒棄死板 24 格限制，以高中數理化體制內必背痛點公式為核心，自然有機生長至 28 個完整章節，講透為止！\n")
    
    lines.append("### 1.2 卷冊劃分規劃")
    lines.append("- **上冊【純數脊椎骨、單變數積分與常微分方程實戰】（Part I – Part V，Chapters 1–19，約 420 頁）**：涵蓋極限定義、多項式降階、切線重根、連鎖律、隱微分、狀態空間微商、弧度無量綱化、旋轉基底、費馬極值、黎曼和、FTC、第一面積矩、換元分部、對數超越函數發明、機率密度初探、一階 ODE 分離變數法、火箭流體、RC 暫態電路、二階線性 ODE 簡諧運動，以及拉格朗日量神級密技特典。")
    lines.append("- **下冊【物理場域實戰、多變數幾何、統計終局與量子大一統】（Part VI – Part VII，Chapters 20–28，約 380 頁）**：涵蓋熱力學絕熱過程 PV^gamma=C、三位一體儲能 1/2 相空間積分、畢奧-薩伐爾導線線圈磁場積分、剛體轉動慣量微元、泰勒級數與斯特靈階乘、多變數全微分誤差傳播、二重極座標幾何、高斯常態分佈終局閉環與馬克士威氣體速率、交流電 RMS 與近代量子測不準原理大一統。\n")
    
    lines.append("### 1.3 裝幀工藝與材料標準")
    lines.append("- **開本尺寸**：標準 16 開（B5 / 182 mm x 257 mm）。")
    lines.append("- **封面裝幀**：厚磅硬殼精裝（Hardcover），深藍布紋包覆，封面壓印燙銀 `woieyufan EDUCATION` 向下微標誌徽章。")
    lines.append("- **內頁用紙**：80g 日本進口櫻花米白道林紙（色溫柔和護眼、吸墨性強、鉛筆與鋼筆書寫不透墨）。")
    lines.append("- **裝訂工藝**：純手工穿線鎖線膠裝，確保全書可 **180 度完全平攤於案頭**，讀者雙手脫離書籍書寫筆記時不回彈。\n")
    
    lines.append("### 1.4 版心網格系統與字體家族（Grid & Typography）")
    lines.append("- **大邊欄網格系統（Marginalia Grid）**：內側訂口 22 mm，正文版心佔頁寬 65%，外側邊欄佔頁寬 25%（寬達 45 mm，專供四重邊欄手札），欄間距 8 mm。")
    lines.append("- **字體階層**：中文正文思源宋體 10.5pt，西文 Palatino 10pt，數學公式 AMS Euler 字體（微商算子 d 一律採用直體），邊欄手札思源黑體 8.5pt。\n")
    
    lines.append("### 1.5 四重邊欄手札話語體系")
    lines.append("外側邊欄配置四種固定手札模塊：1. [思想史溯源] 2. [直覺深水區警示] 3. [體制內解法批判] 4. [道場攻防前哨]。每條嚴格控制在 80～120 字內。\n")
    
    lines.append("### 1.6 單章「七步推進標準」與 16 道題排版動線")
    lines.append("每章依序推進：認知衝突 -> 公理定義 -> 7 條核心公式無跳步推導 -> 幾何動態可視化 -> 跨科自然科學秒殺 -> 四重邊欄手札 -> 16 道階梯題庫 -> 章末道場攻防邀請卡。\n")
    lines.append("---\n")
    
    # 正文 28 章
    part_names = [
        "Part I：極限定義、無窮小階數與微分算子基礎（Chapters 1–3）",
        "Part II：多變量依賴、隱函數切線與相空間運動學（Chapters 4–6）",
        "Part III：無量綱弧度制、動態旋轉向量與費馬時間極值（Chapters 7–9）",
        "Part IV：黎曼和、微積分基本定理與對數超越函數發明（Chapters 10–14）",
        "Part V：機率密度初探、常微分方程與拉格朗日神級密技（Chapters 15–19）",
        "Part VI：物理場域實戰、儲能、磁場與熱力學降維統御（Chapters 20–23）",
        "Part VII：級數逼近、升維多變數、統計終局與量子大一統（Chapters 24–28）"
    ]
    part_roman = ["第二篇", "第三篇", "第四篇", "第五篇", "第六篇", "第七篇", "第八篇"]
    
    for s_idx, st in enumerate(ALL_STAGES):
        lines.append(f"## {part_roman[s_idx]}：{part_names[s_idx]}\n")
        lines.append(f"> **本篇主幹主題**：{st['theme']}\n")
        
        for lesson in st["lessons"]:
            cid = lesson["id"]
            title = lesson["title"]
            lines.append(f"### Chapter {cid}：{title}\n")
            lines.append(f"> **📖 專著編寫指南（Authoring Blueprint）**：{lesson['book_blueprint']}\n")
            
            # 7 條公式鏈
            lines.append("#### 本章 7 條核心骨架公式鏈演繹清單")
            for f in lesson["formulas"]:
                fid = f["id"]
                fname = f["name"]
                flatex = f["latex"]
                lines.append(f"- **`{fid}`【{fname}】**：$${flatex}$$")
                
            # 16 道專著題目
            p = lesson["problems"]
            lines.append(f"\n#### Chapter {cid} 專屬 16 道階梯題庫清冊")
            
            lines.append("##### 1. 公理建構示範例題（Worked Examples, 3 題）")
            for ex in p["worked_examples"]:
                lines.append(f"- **`{ex['id']}`**：{ex['desc']}")
                
            lines.append("\n##### 2. 邊欄 Socratic 思辨詰問（Margin Inquiries, 3 題）")
            for th in p["margin_inquiries"]:
                lines.append(f"- **`{th['id']}`**：{th['desc']}")
                
            lines.append("\n##### 3. Level 1: 基礎公理默寫與純數變換（Foundational Drills, 4 題）")
            for p1 in p["foundational_drills"]:
                lines.append(f"- **`{p1['id']}`**：{p1['desc']}")
                
            lines.append("\n##### 4. Level 2: 自然科學跨學科實戰（Interdisciplinary Applications, 4 題）")
            for p2 in p["interdisciplinary_applications"]:
                lines.append(f"- **`{p2['id']}`**：{p2['desc']}")
                
            lines.append("\n##### 5. Level 3: 邊界奇異點與深水區挑戰（Deepwater Challenges, 2 題）")
            for p3 in p["deepwater_challenges"]:
                lines.append(f"- **`{p3['id']}`**：{p3['desc']}")
                
            # 道場邀請卡
            lines.append(f"\n#### 🥋 Chapter {cid} 章末黑板道場攻防邀請卡（The Dojo Invitation Card）")
            lines.append("```")
            lines.append(f"┌────────────────────────────────────────────────────────────────────────┐")
            lines.append(f"│ 🥋 woieyufan EDUCATION · 黑板研討道場攻防邀請卡 · Chapter {cid:02d}           │")
            lines.append(f"├────────────────────────────────────────────────────────────────────────┤")
            lines.append(f"│ 研討專題：{title[:48]} │")
            lines.append(f"│ 入場前提：已完成 Chapter {cid:02d} 16 道習題草稿，徹底理解 7 條核心公式鏈。       │")
            lines.append(f"│ 道場規則：封印一切教材、筆記與計算機！純粹依靠黑板、粉筆與思維肉搏！   │")
            lines.append(f"│ 攻防焦點：導師將在黑板四區隨機抽查，量綱突襲、反例刺穿、未知情境破局！ │")
            lines.append(f"└────────────────────────────────────────────────────────────────────────┘")
            lines.append("```\n---\n")
            
    # 第九篇
    lines.append("## 第九篇：圖書出版審查清單與解答手冊規範\n")
    lines.append("### 9.1 單章出版前 20 項第一性原理合規檢查表")
    checklist = [
        "1. 核心公式是否達到 7 條骨架標準，且編號為 Eq X.1 ～ Eq X.7？",
        "2. 所有物理量綱在微商與定積分運算中是否全程保持齊次性？",
        "3. 微商符號 d 是否嚴格採用 LaTeX 直體 \\mathrm{d}？",
        "4. 極限定義是否徹底杜絕『0/0』模糊語言，嚴格用微元展開說明？",
        "5. 鏈鎖律推導是否嚴格說明中間變數可微性，無死板約分假象？",
        "6. 隱函數求導是否在幾何軌跡與相空間層面進行切線驗證？",
        "7. 運動學公式是否全部消去時間，以相空間 a = v(dv/dx) 統一？",
        "8. 弧度制定義是否在第一步徹底完成無量綱化？",
        "9. 三角求導是否在單位圓動態旋轉向量幾何下給出直觀投影？",
        "10. 費馬原理推導是否完整給出光程時間一階導數為零？",
        "11. 黎曼和是否包含分割、取樣、求和、取極限四部曲？",
        "12. FTC 推導是否徹底展示微分算子與定積分算子的互逆抵消？",
        "13. 對數 ln 與 e 是否在 Ch 14 提前確立，徹底杜絕物理公式賒帳？",
        "14. 機率密度初登場是否以二項分佈長條圖坍縮立論，破除單點為零心魔？",
        "15. 一階 ODE 分離變數法是否在單變數框架內打穿牛頓冷卻與 RC 暫態？",
        "16. 二階 ODE 簡諧運動是否淘汰參考圓，並解鎖拉格朗日神級密技？",
        "17. 三位一體儲能 (動能、電容、電感) 是否在相空間三角形積分下大一統？",
        "18. 電流磁效應是否由畢奧-薩伐爾定律嚴格導出長直導線與圓線圈中心磁場？",
        "19. 絕熱過程 PV^gamma = C 是否由第一定律分離變數法嚴格推導？",
        "20. 高斯積分是否由二重極座標完整證明 sqrt(pi)，清償 Stage 5 係數債務？"
    ]
    for c in checklist:
        lines.append(f"- [ ] **合規項 {c}**")
        
    lines.append("\n### 9.2 書末解答手冊（Solution Manual）編寫規範")
    lines.append("- **示範例題**：必須包含完整的『公理出發點』、『無跳步代數推導鏈條』、『量綱檢驗』與『物理幾何意象』四項要素。")
    lines.append("- **邊欄思辨題**：給出 200 字以內直擊本質的哲學與物理判詞，杜絕模稜兩可。")
    lines.append("- **基礎運算與跨科題**：給出標準封閉數值解或代數解析式，關鍵步驟標註微積分變換技巧。")
    lines.append("- **深水挑戰題**：提供完整證明路徑、反例構造或漸近展開的高階修正項。\n")
    lines.append("---\n")
    
    return "\n".join(lines)


# -------------------------------------------------------------
# 2. 構建《課堂篇》 (The Dojo Manual)
# -------------------------------------------------------------
def build_dojo_bluepaper():
    lines = []
    lines.append("# 中學超前自學·微積分黑板研討道場實戰工程指引（藍皮書·課堂篇）")
    lines.append("\n**THE BLACKBOARD RESEARCH DOJO: OPERATIONAL TEACHING & DIALECTIC MANUAL**\n")
    lines.append("> **體系機構**：`woieyufan EDUCATION` 智庫教研母本  ")
    lines.append("> **文件版本**：`v3.0 完美無矛盾道場教研定稿`  ")
    lines.append("> **定位讀者**：道場主講導師、黑板研討助理教練、客座答辯評審  ")
    lines.append("> **工程定量標準**：**56 小時 ｜ 28 個有機研討專題 ｜ 196 條黑板板書公式 ｜ 252 道實彈攻防題庫**\n")
    lines.append("---\n")
    
    # 目錄
    lines.append("## 全書章節目錄（Table of Contents）\n")
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
    lines.append("- [第十篇：道場附錄·252 道實彈攻防題導師底牌答案與 3 行秒殺動線庫](#第十篇道場附錄252-道實彈攻防題導師底牌答案與-3-行秒殺動線庫dojo-interrogation-keys)\n")
    lines.append("---\n")
    
    # 第一篇
    lines.append("## 第一篇：黑板研討道場憲章與執教 SOP\n")
    lines.append("### 1.1 道場教育宣言：為什麼「封印 PPT、回歸黑板實彈推導」是不可妥協的底線")
    lines.append("投影片（PPT/Keynote）是思維的火葬場。在 `woieyufan EDUCATION` 黑板研討道場中，**教室內嚴禁開啟投影機**！唯一的武器是四米長的墨黑磁性黑板、無塵石膏粉筆與板擦。導師與學員必須在黑板上一筆一劃寫出每一個極限、每一個展開項與每一個微元向量。全道場打破死板 24 節課框架，拓展為 28 個有機專題，56 小時火力全開！\n")
    
    lines.append("### 1.2 實體黑板「四分區工程動線」標準佈局")
    lines.append("黑板由左至右嚴格劃分為四大機能區：一、公理與錨定區；二、代數推演主動線區；三、物理幾何投影區；四、學員答辯攻防區。\n")
    
    lines.append("### 1.3 單堂 120 分鐘精確節奏控制表")
    lines.append("- 00–15 min：書籍預讀質疑與公理審查\n- 15–50 min：核心數學工具黑板實彈構建\n- 50–85 min：自然科學跨科實彈推演與學員上台（Chalk Relay）\n- 85–110 min：未知情境破局與體制題降維秒殺（含拉格朗日量黑魔法對決）\n- 110–120 min：思維反芻與下週任務發布\n")
    
    lines.append("### 1.4 蘇格拉底式「冷酷攻防詰問」操作劇本")
    lines.append("導師必備四大殺招：1. 追問隱藏前提 2. 量綱突襲 3. 極限反例刺穿 4. 黑板接力機制（Chalk Relay）。\n")
    lines.append("---\n")
    
    # 正文 28 專題
    stage_names = [
        "Stage I：公理出發、無窮小與單項式微積分（Topics 1–3）",
        "Stage II：複合映射、隱函數與相空間（Topics 4–6）",
        "Stage III：無量綱弧度制與三角分析（Topics 7–9）",
        "Stage IV：黎曼和、微積分基本定理與對數超越函數發明（Topics 10–14）",
        "Stage V：機率密度初探、常微分方程與拉格朗日神級密技（Topics 15–19）",
        "Stage VI：物理場域實戰、儲能、磁場與熱力學降維統御（Topics 20–23）",
        "Stage VII：級數逼近、升維多變數、統計終局與量子大一統（Topics 24–28）"
    ]
    stage_roman = ["第二篇", "第三篇", "第四篇", "第五篇", "第六篇", "第七篇", "第八篇"]
    
    for s_idx, st in enumerate(ALL_STAGES):
        lines.append(f"## {stage_roman[s_idx]}：{stage_names[s_idx]}\n")
        lines.append(f"> **本階研討目標**：{st['theme']}\n")
        
        for lesson in st["lessons"]:
            tid = lesson["id"]
            title = lesson["title"]
            lines.append(f"### Topic {tid}：{title}\n")
            lines.append(f"> **🥋 道場研討核心（Dojo Core Mission）**：{lesson['dojo_core']}\n")
            
            # 板書核心公式代碼
            lines.append("#### 黑板板書必演 7 條核心公式鏈")
            for f in lesson["formulas"]:
                fid = f["id"].replace("Eq", "Brd")
                fname = f["name"]
                flatex = f["latex"]
                lines.append(f"- **`{fid}`【{fname}】**：$${flatex}$$")
                
            # 道場 9 道實彈題
            p = lesson["problems"]
            lines.append(f"\n#### Topic {tid} 專屬 9 道道場攻防實彈題庫")
            
            lines.append("##### 1. 黑板現場抽籤攻防題（Chalkboard Defense Tasks, 3 題）")
            for d1 in p["dojo_defense_tasks"]:
                lines.append(f"- **`{d1['id']}`**：{d1['desc']}")
                
            lines.append("\n##### 2. 未知自然科學情境破局題（Unseen Sandbox Scenarios, 3 題）")
            for d2 in p["unseen_sandbox_scenarios"]:
                lines.append(f"- **`{d2['id']}`**：{d2['desc']}")
                
            lines.append("\n##### 3. 體制內聯考大題降維秒殺題（System Trivialization Arsenal, 3 題）")
            for d3 in p["system_trivialization_arsenal"]:
                lines.append(f"- **`{d3['id']}`**：{d3['desc']}")
            lines.append("\n---\n")
            
    # 第九篇
    lines.append("## 第九篇：道場評量規準與教練考核體系\n")
    lines.append("### 9.1 學員黑板答辯五維雷達評量表與評分標準（Radar Rubrics）")
    lines.append("道場每次課後針對每位學員進行五維雷達評分（每維度 1～5 分，滿分 25 分）：1. 公理第一性 2. 板書工程結構 3. 跨科自然秒殺 4. 逆向質疑答辯 5. 體制降維統御。\n")
    
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
    lines.append("\n---\n")
    
    return "\n".join(lines)
