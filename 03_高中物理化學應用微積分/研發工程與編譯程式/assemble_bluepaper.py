# -*- coding: utf-8 -*-
"""
assemble_bluepaper.py: 組裝《中學超前自學微積分先修體系藍皮書（細節工程指引）》完整母檔
產出：
1. calculus_precollege_curriculum_bluepaper.md (Artifact)
2. C:\\Users\\user\\Documents\\中學超前自學_微積分先修體系藍皮書_細節工程指引.txt (純文字傳閱本)
"""

import sys
import os

from stage1_data import STAGE_1
from stage2_data import STAGE_2
from stage3_data import STAGE_3
from stage4_data import STAGE_4
from stage5_data import STAGE_5
from stage6_data import STAGE_6
from stage7_data import STAGE_7

ALL_STAGES = [STAGE_1, STAGE_2, STAGE_3, STAGE_4, STAGE_5, STAGE_6, STAGE_7]

def build_markdown():
    lines = []
    
    # 標題與元數據
    lines.append("# 中學超前自學：以近代高等數學工具為骨架之數理跨科先修體系藍皮書（細節工程指引）")
    lines.append("\n**ACADEMIC ENGINEERING IMPLEMENTATION BLUEPRINT & OPERATIONAL MANUAL**\n")
    lines.append("> **體系機構**：`woieyufan EDUCATION` 智庫工程母本  ")
    lines.append("> **文件版本**：`v1.0 正式工程定稿母本`  ")
    lines.append("> **適用對象**：專著撰寫團隊、排版裝幀設計師、道場主講導師、黑板研討助理教練、超前自學資優生（國二升國三、國三升高一先修）  ")
    lines.append("> **工程定量標準**：**24 堂課全域覆蓋 ｜ 精確 168 條核心骨架公式鏈 ｜ 精確 600 道全域階梯題庫**\n")
    lines.append("---\n")
    
    # 目錄
    lines.append("## 全書架構目錄（Table of Contents）\n")
    lines.append("- [第一篇：藍皮書工程定位與操作公理準則（SOP）](#第一篇藍皮書工程定位與操作公理準則sop)")
    lines.append("  - 1.1 白皮書（Why & What）與藍皮書（How & Spec）之工程對接")
    lines.append("  - 1.2 四大工程鐵律的極限落實（公理演繹、第一性原理、零跳步、量綱守恆）")
    lines.append("  - 1.3 出版級專著（書籍）寫作「七步推進標準」與版面參數")
    lines.append("  - 1.4 黑板研討道場（課堂）「四分區黑板動線」與「蘇格拉底式攻防詰問 SOP」")
    lines.append("  - 1.5 全域工程定額矩陣（168 條核心公式鏈 ＋ 600 道階梯題型矩陣）")
    lines.append("- [第二篇：第一階：公理出發、無窮小與單項式微積分（第 1–3 堂）](#第一階公理出發無窮小與單項式微積分第-13-堂)")
    lines.append("- [第三篇：第二階：複合映射、隱函數與相空間（第 4–6 堂）](#第二階複合映射隱函數與相空間第-46-堂)")
    lines.append("- [第四篇：第三階：無量綱弧度制與三角分析（第 7–9 堂）](#第三階無量綱弧度制與三角分析第-79-堂)")
    lines.append("- [第五篇：第四階：黎曼和、基本定理與第一面積矩（第 10–13 堂）](#第四階黎曼和基本定理與第一面積矩第-1013-堂)")
    lines.append("- [第六篇：第五階：狀態空間定積分與幾何形態學（第 14–15 堂）](#第五階狀態空間定積分與幾何形態學第-1415-堂)")
    lines.append("- [第七篇：第六階：超越函數發明與常微分方程（第 16–19 堂）](#第六階超越函數發明與常微分方程第-1619-堂)")
    lines.append("- [第八篇：第七階：連續型機率密度微積分與近代物理（第 20–24 堂）](#第七階連續型機率密度微積分與近代物理第-2024-堂)")
    lines.append("- [第九篇：工程驗收清單與全體系雙軌執行手冊](#第九篇工程驗收清單與全體系雙軌執行手冊)")
    lines.append("  - 9.1 書籍單章出版前 20 項第一性原理合規檢查表")
    lines.append("  - 9.2 道場黑板攻防五維雷達評量表與評分規準（Radar Rubrics）\n")
    lines.append("---\n")
    
    # 第一篇
    lines.append("## 第一篇：藍皮書工程定位與操作公理準則（SOP）\n")
    lines.append("### 1.1 白皮書（Why & What）與藍皮書（How & Spec）之工程對接")
    lines.append("《白皮書》（White Paper v3.0）確立了本體系的戰略哲學：**「數學工具為骨架主軸，自然科學為驗證載體」**，並建立了**【階段一：出版級案頭專著（書籍）】**與**【階段二：黑板研討道場（課堂）】**的兩階段轉化閉環。")
    lines.append("本《藍皮書》（Blue Paper）則是直接面向著作撰寫人、排版設計師、課堂主講導師與助教群的**工業級施工規範（Engineering Blueprint & SOP）**。藍皮書回答的是：**每一堂課究竟包含哪 7 條核心公式？每一堂課到底配置哪 25 道題目？黑板如何分區？詰問如何展開？**\n")
    
    lines.append("### 1.2 四大工程鐵律的極限落實")
    lines.append("全體系（無論文字書寫或黑板板書）必須 100% 服從四大鐵律：")
    lines.append("1. **公理演繹（Axiomatic Deduction）**：嚴禁拋出任何沒有公理與定義支撐的經驗結論，所有公式必須追溯至最底層公理。")
    lines.append("2. **第一性原理（First Principles）**：拒絕中學體制內的記憶口訣（如圓錐曲線切線代換口訣、交流電除以根號二口訣、動能定力推導口訣），還原其微積分幾何與代數本質。")
    lines.append("3. **零跳步代數連鎖（Zero-Skip Algebra）**：所有等號連鎖（$=$）嚴格限制單步只進行一項代數運算，凡有換元、消項、取極限處必須註明依據。")
    lines.append("4. **量綱守恆封閉（Dimensional Conservation）**：每一推導環節嚴格標註物理量綱，嚴禁量綱不符之項相加減。\n")
    
    lines.append("### 1.3 出版級專著（書籍）寫作「七步推進標準」與版面參數")
    lines.append("書籍篇（階段一）每一章必須嚴格依照以下七步推進：")
    lines.append("- **Step 1：認知衝突與直覺破局**（拆解中學體制死記口訣在極端情況下的盲點）。")
    lines.append("- **Step 2：公理體系與數學物件定義**（精確定義變數、定義域、連續性、對稱性）。")
    lines.append("- **Step 3：無跳步代數推演**（7 條核心公式鏈無縫連接，量綱全流程標註）。")
    lines.append("- **Step 4：幾何直觀與動態可視化**（向量圖、相平面軌跡、微元幾何剖析）。")
    lines.append("- **Step 5：跨學科自然科學降維打擊**（力學、電磁、熱學、光學真實場景秒殺）。")
    lines.append("- **Step 6：邊欄手札與思維陷阱（Marginalia）**（思想史、隱藏假設、警示標籤）。")
    lines.append("- **Step 7：反芻實戰階梯題庫**（精選 16 道分層挑戰題）。\n")
    
    lines.append("### 1.4 黑板研討道場（課堂）「四分區黑板動線」與「蘇格拉底式攻防詰問 SOP」")
    lines.append("課堂篇（階段二）**嚴禁使用 PPT 投影念稿**，必須採用實體黑板實彈推導。黑板嚴格劃分為四區：")
    lines.append("```")
    lines.append("┌───────────────┬───────────────────────────────┬───────────────┬───────────────┐")
    lines.append("│  一、公理與錨定區  │       二、代數推演主動線區      │ 三、物理與幾何投影區│ 四、學生答辯攻防區│")
    lines.append("│               │                               │               │               │")
    lines.append("│ • 核心定義     │ • 7 條核心公式微商/定積分鏈條 │ • 物理情境圖解 │ • 學員推導盲點│")
    lines.append("│ • 邊界條件     │ • 零跳步代數展開式             │ • 相空間軌跡圖 │ • 典型反例記錄│")
    lines.append("│ • 量綱基底     │ • 換元矩陣與消去步驟           │ • 向量場幾何   │ • 體制解法比對│")
    lines.append("│ (整堂不擦除)  │ (由左至右、由上而下，寫滿更換) │ (動態圖示)    │ (即時論辯筆記)│")
    lines.append("└───────────────┴───────────────────────────────┴───────────────┴───────────────┘")
    lines.append("```")
    lines.append("**蘇格拉底攻防話術**：『你在哪一步默認了函數可微？』、『這一項的物理量綱是什麼？』、『令極限趨向無窮大，你的公式崩潰在哪裡？』\n")
    
    lines.append("### 1.5 全域工程定額矩陣（168 條核心公式鏈 ＋ 600 道階梯題型矩陣）")
    lines.append("全書 24 堂課標準定額配比：")
    lines.append("- **核心骨架公式**：每堂課固定 **7 條**，全書 24 堂課累計 **168 條**。")
    lines.append("- **書籍篇題庫**：每堂課固定 **16 題**（例題 3 ＋ 邊欄思辨 3 ＋ 基礎默寫 4 ＋ 跨科實戰 4 ＋ 深水挑戰 2），全書累計 **384 題**。")
    lines.append("- **課堂道場篇題庫**：每堂課固定 **9 題**（黑板攻防 3 ＋ 未知破局 3 ＋ 體制秒殺 3），全書累計 **216 題**。")
    lines.append("- **全體系總題量**：$24 \\times 25 = \\mathbf{600 \\text{ 道高密度試題}}$，題題見骨，零無效重複！\n")
    lines.append("---\n")
    
    # 第二至第八篇：各階梯展開
    stage_roman = ["第二篇", "第三篇", "第四篇", "第五篇", "第六篇", "第七篇", "第八篇"]
    
    for s_idx, st in enumerate(ALL_STAGES):
        lines.append(f"## {stage_roman[s_idx]}：{st['title']}\n")
        lines.append(f"> **本階工程主旨**：{st['theme']}\n")
        
        for lesson in st["lessons"]:
            lines.append(f"### 第 {lesson['id']} 堂：{lesson['title']}\n")
            lines.append(f"- **📖 階段一：書籍章節藍圖（The Book）**：{lesson['book_blueprint']}")
            lines.append(f"- **🥋 階段二：課堂道場實戰（The Dojo）**：{lesson['dojo_core']}\n")
            
            # 公式鏈
            lines.append(f"#### 📐 核心骨架公式鏈清冊（Exact Formula Register - 7 式）\n")
            for f in lesson["formulas"]:
                lines.append(f"- **`{f['id']}`【{f['name']}】**：\n  $$\n  {f['latex']}\n  $$")
            lines.append("")
            
            # 題目矩陣
            lines.append(f"#### 🎯 25 題階梯題庫矩陣（Exact Problem Inventory - 25 題）\n")
            p = lesson["problems"]
            
            lines.append("##### 【階段一：出版級專著（書籍）階梯題庫（共 16 題）】")
            lines.append("1. **核心公理與無跳步示範例題（Worked Examples，共 3 題）**：")
            for ex in p["worked_examples"]:
                lines.append(f"   - **`{ex['id']}`**：{ex['desc']}")
            
            lines.append("2. **邊欄思維陷阱與深水反思題（Socratic Margin Tasks，共 3 題）**：")
            for th in p["margin_inquiries"]:
                lines.append(f"   - **`{th['id']}`**：{th['desc']}")
                
            lines.append("3. **基礎公理演練與閉卷默寫題（Level 1: Foundational Drills，共 4 題）**：")
            for p1 in p["foundational_drills"]:
                lines.append(f"   - **`{p1['id']}`**：{p1['desc']}")
                
            lines.append("4. **跨科物理與幾何深度實戰題（Level 2: Interdisciplinary Applications，共 4 題）**：")
            for p2 in p["interdisciplinary_applications"]:
                lines.append(f"   - **`{p2['id']}`**：{p2['desc']}")
                
            lines.append("5. **極限邊界與反例防禦挑戰題（Level 3: Deepwater Challenges，共 2 題）**：")
            for p3 in p["deepwater_challenges"]:
                lines.append(f"   - **`{p3['id']}`**：{p3['desc']}")
            
            lines.append("\n##### 【階段二：黑板研討道場（課堂）實彈彈藥庫（共 9 題）】")
            lines.append("6. **黑板現場抽籤攻防題庫（Chalkboard Defense Tasks，共 3 題）**：")
            for d1 in p["dojo_defense_tasks"]:
                lines.append(f"   - **`{d1['id']}`**：{d1['desc']}")
                
            lines.append("7. **未知自然科學情境破局題庫（Unseen Sandbox Scenarios，共 3 題）**：")
            for d2 in p["unseen_sandbox_scenarios"]:
                lines.append(f"   - **`{d2['id']}`**：{d2['desc']}")
                
            lines.append("8. **體制內難題降維秒殺彈藥庫（System Trivialization Arsenal，共 3 題）**：")
            for d3 in p["system_trivialization_arsenal"]:
                lines.append(f"   - **`{d3['id']}`**：{d3['desc']}")
                
            lines.append("\n---\n")
            
    # 第九篇
    lines.append("## 第九篇：工程驗收清單與全體系雙軌執行手冊\n")
    lines.append("### 9.1 書籍單章出版前 20 項第一性原理合規檢查表")
    checklist_items = [
        "是否以認知衝突或直覺破局開篇，杜絕定義硬塞？",
        "所有引入的變數是否均具備嚴格的幾何/代數定義域？",
        "公式推導中是否存在任何跨越兩步以上的等號跳步？",
        "所有換元、積分上限變更、極限運算是否均註明定理依據？",
        "每一個物理相關公式是否在每一步保持量綱齊次性？",
        "是否包含至少 1 幅高精度向量圖、幾何相圖或微元示意圖？",
        "是否揭穿了至少 1 項中學體制內的記憶口訣謬誤？",
        "是否包含了自然常數、負號或無窮大奇異點的深水區討論？",
        "示範例題是否給出完整的出版級解析與解題哲學評註？",
        "閉卷自測題是否具備從白紙從零推導目標算子的考察能力？",
        "跨科應用是否涵蓋力學、電磁、光學、熱力學或統計真實模型？",
        "挑戰題是否包含極端邊界檢驗（如光速極限或零質量極限）？",
        "排版是否遵循外側邊欄預留 25% 筆記手札空間的黃金比例？",
        "數學符號微商算子 $\\mathrm{d}$ 是否一律採用直體以區別於變數？",
        "向量與張量符號是否嚴格採用粗斜體或標準箭頭標註？",
        "所有公式編號是否符合全書統一編碼體系（Eq k.1 至 Eq k.7）？",
        "單章總題量是否嚴格達標 16 題且階梯分佈嚴密？",
        "語言風格是否維持極致學術莊重、拒絕輕浮口語？",
        "是否具備引導讀者走向第二階段黑板研討道場的思維鉤子？",
        "是否經過雙盲同行評審並確認無任何邏輯死循環？"
    ]
    for idx, item in enumerate(checklist_items):
        lines.append(f"- [ ] **Check {idx+1:02d}**：{item}")
    lines.append("")
    
    lines.append("### 9.2 道場黑板攻防五維雷達評量表與評分規準（Radar Rubrics）")
    lines.append("課堂答辯（階段二）中，導師對學員上台推演的評估採用五維雷達標尺（每項滿分 5 分，總分 25 分）：")
    lines.append("1. **公理意識（Axiomatic Clarity）**：能否隨時說明每一步代數的數學公理與定理依據（5分：精確說出定理名與條件；1分：含糊其辭稱『以前學過』）。")
    lines.append("2. **板書無跳步（Chalkboard Discipline）**：黑板書寫是否字跡端正、符號標準、無任何隱藏代數跳步（5分：完美落實四大分區；1分：混亂塗抹、跳步嚴重）。")
    lines.append("3. **幾何轉譯能力（Geometric Insight）**：能否在沒有公式輔助下畫出相應的物理微元、相空間軌跡或幾何圖像（5分：圖像直擊本質；1分：只會背代數符號）。")
    lines.append("4. **量綱敏感度（Dimensional Reflex）**：能否在 3 秒內心算驗證任何一項的物理量綱（5分：即時發現係數缺失；1分：對量綱毫無概念）。")
    lines.append("5. **反例抗辯力（Counterexample Defense）**：面對導師提出的極端邊界條件或病態反例，能否冷靜修正公式並說明物理破局點（5分：從容自洽反辯；1分：不知所措崩潰）。\n")
    
    lines.append("### 9.3 結語：兩階段閉環的終極工程交付")
    lines.append("本《藍皮書》所鎖定的 **168 條核心骨架公式鏈** 與 **600 道階梯題庫矩陣**，構成了當代中學超前自學資優教育最不可撼動的工程基石。")
    lines.append("從書籍自學汲取公理力量，到黑板道場實彈淬鍊真知，這套體系將陪伴最具天賦的中學學子，徹底跨越體制內升學口訣的平庸泥淖，昂首邁入近代高等科學的壯麗殿堂！\n")
    lines.append("---\n")
    lines.append("**© woieyufan EDUCATION · 機密智庫工程母本 · 版權所有 · 嚴禁外流**")
    
    return "\n".join(lines)

if __name__ == "__main__":
    md_content = build_markdown()
    
    # 寫入 Artifact 目錄
    artifact_path = r"C:\Users\user\.gemini\antigravity\brain\17c5c8ea-1f34-4270-a5e4-410bdd5037d4\calculus_precollege_curriculum_bluepaper.md"
    with open(artifact_path, "w", encoding="utf-8") as f:
        f.write(md_content)
    print(f"Artifact Markdown written: {artifact_path} ({len(md_content)} chars)")
    
    # 寫入純文字傳閱本至 Documents
    txt_path = r"C:\Users\user\Documents\中學超前自學_微積分先修體系藍皮書_細節工程指引.txt"
    with open(txt_path, "w", encoding="utf-8") as f:
        f.write(md_content)
    print(f"Text distribution written: {txt_path} ({len(md_content)} chars)")
