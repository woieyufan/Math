import sys

path1 = r'C:\Users\user\Documents\中學微積分先修專著_第01章_詳細解答.md'
path2 = r'C:\Users\user\.gemini\antigravity\brain\17c5c8ea-1f34-4270-a5e4-410bdd5037d4\calculus_volume1_ch01_solutions.md'

with open(path1, 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('依據導數的第一性原理公理定義', '依據導數的極限定義式')
content = content.replace('第一性原理', '基礎定義')

target = '在幾何上，此結果表明在任意點 $x$，拋物線切線的傾斜斜率恆等於該點橫坐標的兩倍。'

addition = '''

第六步，切線方程式數值檢驗與切點幾何論證。
在點 $(1, 1)$ 處，切線斜率為 $f'(1) = 2$。
由點斜式寫出該點的切線方程式：
$$y - 1 = 2(x - 1) \\implies y = 2x - 1$$
我們在切點兩側進行數值驗證，檢驗曲線與直線的位置關係：
1. 當 $x = 1$ 時：曲線高度 $y = 1^2 = 1$，直線高度 $y = 2(1) - 1 = 1$。兩者重合於點 $(1, 1)$。
2. 當 $x = 0.9$（切點左側）時：曲線高度 $y = 0.9^2 = 0.81$，直線高度 $y = 2(0.9) - 1 = 0.80$。曲線高於直線（$0.81 > 0.80$）。
3. 當 $x = 1.1$（切點右側）時：曲線高度 $y = 1.1^2 = 1.21$，直線高度 $y = 2(1.1) - 1 = 1.20$。曲線高於直線（$1.21 > 1.20$）。
在點 $(1, 1)$ 的左右兩側，拋物線均嚴格高於直線。這證明該直線在局部緊貼著拋物線底部支撐著它，且在該鄰域內與曲線僅有唯一公共點 $(1, 1)$，符合嚴格的幾何切線定義。'''

if target in content:
    content = content.replace(target, target + addition)
    print("Found target and replaced.")
else:
    print("Target not found directly, checking substring...")
    # let's find the sentence
    for line in content.splitlines():
        if '拋物線切線的傾斜斜率' in line:
            print("Found line:", repr(line))

with open(path1, 'w', encoding='utf-8', newline='\n') as f:
    f.write(content)

with open(path2, 'w', encoding='utf-8', newline='\n') as f:
    f.write(content)

print("Finished updating.")
