# -*- coding: utf-8 -*-
"""
build_perfect_stages.py:
重組並生成 Stage 4 到 Stage 7 的完美無矛盾數據模組：
- Stage 4: Ch 10-14 (積分基礎、FTC、分部換元、對數發明與 e)
- Stage 5: Ch 15-19 (機率初登場、一階 ODE、火箭流體、RC 暫態、二階 ODE 簡諧運動 + 拉格朗日密技)
- Stage 6: Ch 20-23 (絕熱熱力學、三位一體儲能 1/2、畢奧-薩伐爾磁場、剛體轉動慣量)
- Stage 7: Ch 24-28 (泰勒與斯特靈、全微分誤差傳播、二重極座標、高斯常態分佈終局收割、交流電 RMS 與量子波函數)
"""

import os
import sys

SCRATCH_DIR = r"C:\Users\user\.gemini\antigravity\brain\17c5c8ea-1f34-4270-a5e4-410bdd5037d4\scratch"
sys.path.append(SCRATCH_DIR)

from stage1_data import STAGE_1
from stage2_data import STAGE_2
from stage3_data import STAGE_3

# 讀取現有生成的模組庫來獲取各課詳細數據
import stage4_data, stage5_data, stage6_data, stage7_data

# 建立字典庫方便按主題提取
lesson_pool = {}
for s in [stage4_data.STAGE_4, stage5_data.STAGE_5, stage6_data.STAGE_6, stage7_data.STAGE_7]:
    for l in s["lessons"]:
        title = l["title"]
        if "黎曼和" in title: lesson_pool["riemann"] = l
        elif "微積分基本定理" in title: lesson_pool["ftc"] = l
        elif "冪函數反導" in title: lesson_pool["power_int"] = l
        elif "變力做功" in title: lesson_pool["work"] = l
        elif "對數微積分" in title: lesson_pool["log"] = l
        elif "機率密度函數" in title: lesson_pool["prob_pass1"] = l
        elif "一階常微分" in title: lesson_pool["ode1"] = l
        elif "動量流率" in title or "火箭" in title: lesson_pool["rocket"] = l
        elif "RC" in title: lesson_pool["rc"] = l
        elif "二階常係數" in title or "簡諧" in title: lesson_pool["shm"] = l
        elif "熱力學微積分" in title or "絕熱" in title: lesson_pool["thermo"] = l
        elif "三位一體儲能" in title: lesson_pool["energy12"] = l
        elif "畢奧-薩伐爾" in title or "電流磁效應" in title: lesson_pool["magnetic"] = l
        elif "轉動慣量" in title: lesson_pool["inertia"] = l
        elif "泰勒級數" in title: lesson_pool["taylor"] = l
        elif "全微分" in title: lesson_pool["multivar"] = l
        elif "二重積分" in title: lesson_pool["double_int"] = l
        elif "馬克士威氣體速率" in title or "高斯常態" in title: lesson_pool["prob_pass2"] = l
        elif "交流電網" in title or "量子" in title: lesson_pool["quantum"] = l

print("Loaded lesson pool keys:", list(lesson_pool.keys()))

def reassign_lesson(l, new_id, new_title=None, add_blueprint="", add_dojo=""):
    import copy
    nl = copy.deepcopy(l)
    nl["id"] = new_id
    if new_title: nl["title"] = new_title
    if add_blueprint: nl["book_blueprint"] += add_blueprint
    if add_dojo: nl["dojo_core"] += add_dojo
    for i, f in enumerate(nl["formulas"]):
        f["id"] = f"Eq {new_id}.{i+1}"
    for k, plist in nl["problems"].items():
        prefix = "Ex" if k == "worked_examples" else ("Q1" if k == "margin_inquiries" else ("P1" if k == "foundational_drills" else ("P5" if k == "interdisciplinary_applications" else ("P9" if k == "deepwater_challenges" else ("D1" if k == "dojo_defense_tasks" else ("U1" if k == "unseen_sandbox_scenarios" else "K1"))))))
        for j, p in enumerate(plist):
            p["id"] = f"{prefix} {new_id}.{j+1}"
    return nl

# 1. 構造 Stage 4 (Ch 10 - 14)
# L10: 黎曼和
# L11: FTC
# L12: 冪函數反導與第一面積矩
# L13: 變力做功線積分與位能曲面
# L14: 對數微積分發明與自指自然常數 e
l10 = reassign_lesson(lesson_pool["riemann"], 10)
l11 = reassign_lesson(lesson_pool["ftc"], 11)
l12 = reassign_lesson(lesson_pool["power_int"], 12)
l13 = reassign_lesson(lesson_pool["work"], 13)
l14 = reassign_lesson(lesson_pool["log"], 14, 
    new_title="對數微積分發明與自指自然常數 e（填補反導黑洞與連續複利基石）",
    add_blueprint=" 本章在前置位置徹底確立對數與指數微積分，為後續物理場域的火箭推進、RC 暫態電路、放射性衰變與熱力學等溫做功提供零賒帳、零跳步的堅實數學底座。")

STAGE_4 = {
    "title": "第四階：黎曼和、微積分基本定理與對數超越函數發明（第 10–14 堂）",
    "theme": "從無窮微元累積到算子對偶，微積分基本定理合流，填補冪函數反導黑洞，自然常數 e 與對數微積分基石確立",
    "lessons": [l10, l11, l12, l13, l14]
}

# 2. 構造 Stage 5 (Ch 15 - 19)
# L15: 機率密度初探 (二項分佈長條圖坍縮、記帳懸念)
# L16: 一階常微分方程分離變數法
# L17: 變質量火箭推進與連續介質流體光壓 (使用剛學到的 ln)
# L18: RC/RL 暫態電路 (一階線性 ODE)
# L19: 二階常係數齊次 ODE 簡諧運動 + 【道場神級密技特典：拉格朗日量 L = T - V】
l15 = reassign_lesson(lesson_pool["prob_pass1"], 15,
    new_title="從二項分佈長條圖到機率密度函數（高爾頓板、柱寬坍縮與連續微元初登場）",
    add_blueprint=" 本章承接定積分幾何概念，以直方圖極限破除單點機率為零心魔，並在黑板鄭重記下鐘形曲線 sqrt(2pi) 待償帳單，留待多變數微積分章節清償。")
l16 = reassign_lesson(lesson_pool["ode1"], 16,
    new_title="一階常微分方程分離變數法與反應動力學解析（牛頓冷卻與終端速度）")
l17 = reassign_lesson(lesson_pool["rocket"], 17,
    new_title="變質量運動學微分方程與連續介質流體光壓（火箭推進對數解與雷射光壓）")
l18 = reassign_lesson(lesson_pool["rc"], 18,
    new_title="RC、RL 暫態電路一階線性微分方程與指數衰減（50% 能量佯謬微積分閉環）")

# 在 Ch 19 植入拉格朗日密技
l19 = reassign_lesson(lesson_pool["shm"], 19,
    new_title="二階常係數齊次線性 ODE 與簡諧運動（淘汰參考圓，附道場神級密技：拉格朗日量 L = T - V）",
    add_blueprint=" 【道場神級密技特典：拉格朗日量】在深水挑戰與道場未知破局環節，正式解鎖分析力學黑魔法 L = T - V 與尤拉-拉格朗日方程 d/dt(partial L / partial q_dot) - partial L / partial q = 0；免畫任何受力圖、免分解約束力（正向力、繩張力自動消除），3 行自動生成複雜約束系統的二階運動微分方程（小車單擺、雙彈簧振子黑板秒殺），為資優生提供競賽與大考的終極檢驗底牌！",
    add_dojo=" 【道場黑板黑魔法對決】黑板左側展示體制內牛頓力學寫滿兩黑板的受力分解與慣性力補償；黑板右側亮出拉格朗日量 L = T - V，3 步無腦套入尤拉-拉格朗日方程，3 行自動吐出二階運動微分方程，徹底震撼全場資優生！")

# 替換 Ch 19 的 Deepwater Challenge 1 為拉格朗日密技題
l19["problems"]["deepwater_challenges"][0] = {
    "id": f"P9 19.1",
    "desc": "【拉格朗日量神級密技實彈】光滑水平地面上有一質量為 M 的滑塊，其上懸掛一長度為 L、質量為 m 的單擺；純粹利用廣義坐標 (x, theta) 寫出系統動能 T 與位能 V，構造拉格朗日量 L = T - V；不畫任何受力圖，直接套用尤拉-拉格朗日方程式，3 行嚴格推導出小車與單擺的雙自由度耦合二階運動微分方程組！"
}
l19["problems"]["system_trivialization_arsenal"][0] = {
    "id": f"K1 19.1",
    "desc": "體制內競賽壓軸題秒殺：複雜雙約束質點振動問題，體制內受力分析耗時 25 分鐘且極易漏正負號，微積分選手使用拉格朗日量 L = T - V 3 行自動輸出運動微分方程，30 秒鎖定固有頻率！"
}

STAGE_5 = {
    "title": "第五階：機率密度初探、常微分方程與拉格朗日神級密技（第 15–19 堂）",
    "theme": "二項分佈長條圖連續坍縮，一階常微分方程分離變數法，RC 暫態與簡諧振動，拉格朗日量神級密技出鞘",
    "lessons": [l15, l16, l17, l18, l19]
}

# 3. 構造 Stage 6 (Ch 20 - 23)
# L20: 熱力學微積分 (絕熱 PV^gamma = C 與等溫做功)
# L21: 三位一體儲能 1/2
# L22: 電流磁效應微元場積分 (畢奧-薩伐爾)
# L23: 剛體連續質量分佈與轉動慣量
l20 = reassign_lesson(lesson_pool["thermo"], 20,
    new_title="熱力學微積分：絕熱過程 PV^gamma = C 與氣體做功（第一定律微分式分離變數法）")
l21 = reassign_lesson(lesson_pool["energy12"], 21,
    new_title="三位一體儲能本質：動能、電容能與電感能的「1/2」狀態空間積分（相空間三角形對偶）")
l22 = reassign_lesson(lesson_pool["magnetic"], 22,
    new_title="電流磁效應微元場積分：畢奧-薩伐爾定律與長直導線、圓線圈、螺線管磁場")
l23 = reassign_lesson(lesson_pool["inertia"], 23,
    new_title="剛體連續質量分佈與轉動慣量微元積分（細棒、圓盤、球體與平行軸定理）")

STAGE_6 = {
    "title": "第六階：物理場域實戰、儲能、磁場與熱力學降維統御（第 20–23 堂）",
    "theme": "單變數定積分縱深推進，熱力學絕熱過程，三位一體儲能相空間對偶，電流磁效應微元場積分與剛體轉動慣量",
    "lessons": [l20, l21, l22, l23]
}

# 4. 構造 Stage 7 (Ch 24 - 28)
# L24: 泰勒級數與斯特靈階乘近似
# L25: 多變數全微分與測量誤差獨立正交合成
# L26: 二重積分、空間體積與極座標變換 (屠龍寶刀鑄成)
# L27: 二項分佈極限、高斯常態分佈、68-95-99.7 法則與馬克士威氣體速率大一統 (清償 Ch 15 懸念)
# L28: 交流電網週期平均值與近代物理波函數終極閉環
l24 = reassign_lesson(lesson_pool["taylor"], 24,
    new_title="泰勒級數、馬克勞林級數與斯特靈階乘近似（超越函數多項式化）")
l25 = reassign_lesson(lesson_pool["multivar"], 25,
    new_title="多變數全微分與測量誤差獨立正交合成（BIPM 實驗科學標準）")
l26 = reassign_lesson(lesson_pool["double_int"], 26,
    new_title="二重積分、空間體積與極座標變換（多變數降維武器鑄造）")
l27 = reassign_lesson(lesson_pool["prob_pass2"], 27,
    new_title="二項分佈極限、高斯常態分佈、68-95-99.7 法則與馬克士威氣體速率大一統（終局收割）",
    add_blueprint=" 本章拔出第 26 堂鑄成的二重極座標屠龍刀，計算全域高斯積分 I = sqrt(pi)，徹底償清第 15 堂課記在黑板上的待付帳單，手算 68-95-99.7 法則，並平移至三維速度空間導出馬克士威分佈與活化能尾部！")
l28 = reassign_lesson(lesson_pool["quantum"], 28,
    new_title="交流電網週期平均值與近代物理波函數終極閉環（全書大一統榮譽冠頂）",
    add_blueprint=" 【拉格朗日作用量終極揭秘】揭示拉格朗日作用量 S = int L dt 的量綱正好是 J*s，即普朗克常數 hbar 的量綱；宏觀物體的最小作用量原理，本質上是微觀量子波函數路徑積分在經典軌道附近的相長干涉，完成經典力學與量子力學在微積分下的最高對偶閉環！")

STAGE_7 = {
    "title": "第七階：級數逼近、升維多變數、統計終局與量子大一統（第 24–28 堂）",
    "theme": "泰勒多項式逼近，全微分誤差傳播，二重極座標幾何，高斯常態分佈大一統清償，交流電均方根與量子波函數終極閉環",
    "lessons": [l24, l25, l26, l27, l28]
}

# 寫出所有模組文件
with open(os.path.join(SCRATCH_DIR, "stage4_data.py"), "w", encoding="utf-8") as f:
    f.write("# -*- coding: utf-8 -*-\n")
    f.write('"""stage4_data.py (Ch 10-14 終極無矛盾版)"""\n\n')
    f.write(f"STAGE_4 = {repr(STAGE_4)}\n")

with open(os.path.join(SCRATCH_DIR, "stage5_data.py"), "w", encoding="utf-8") as f:
    f.write("# -*- coding: utf-8 -*-\n")
    f.write('"""stage5_data.py (Ch 15-19 終極無矛盾版，附拉格朗日密技)"""\n\n')
    f.write(f"STAGE_5 = {repr(STAGE_5)}\n")

with open(os.path.join(SCRATCH_DIR, "stage6_data.py"), "w", encoding="utf-8") as f:
    f.write("# -*- coding: utf-8 -*-\n")
    f.write('"""stage6_data.py (Ch 20-23 終極無矛盾版)"""\n\n')
    f.write(f"STAGE_6 = {repr(STAGE_6)}\n")

with open(os.path.join(SCRATCH_DIR, "stage7_data.py"), "w", encoding="utf-8") as f:
    f.write("# -*- coding: utf-8 -*-\n")
    f.write('"""stage7_data.py (Ch 24-28 終極無矛盾版)"""\n\n')
    f.write(f"STAGE_7 = {repr(STAGE_7)}\n")

print("All Stage 4-7 data modules successfully rebuilt with perfected order!")
