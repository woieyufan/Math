import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

path = r'C:\Users\user\.gemini\antigravity\brain\17c5c8ea-1f34-4270-a5e4-410bdd5037d4\calculus_precollege_curriculum_bluepaper.md'
with open(path, 'r', encoding='utf-8') as f:
    text = f.read()

lessons = re.findall(r'### 第 \d+ 堂：', text)
formulas = re.findall(r'`Eq \d+\.\d+`', text)
worked = re.findall(r'`Ex \d+\.\d+`', text)
margin = re.findall(r'`Th \d+\.\d+`', text)
p1 = re.findall(r'`P1 \d+\.\d+`', text)
p2 = re.findall(r'`P2 \d+\.\d+`', text)
p3 = re.findall(r'`P3 \d+\.\d+`', text)
d1 = re.findall(r'`D1 \d+\.\d+`', text)
d2 = re.findall(r'`D2 \d+\.\d+`', text)
d3 = re.findall(r'`D3 \d+\.\d+`', text)

print(f"Total Lessons: {len(lessons)} (Expect 24)")
print(f"Total Formulas: {len(formulas)} (Expect 168)")
print(f"Worked Examples (Ex): {len(worked)} (Expect 72)")
print(f"Margin Inquiries (Th): {len(margin)} (Expect 72)")
print(f"Foundational Drills (P1): {len(p1)} (Expect 96)")
print(f"Interdisciplinary (P2): {len(p2)} (Expect 96)")
print(f"Deepwater Challenges (P3): {len(p3)} (Expect 48)")
print(f"Dojo Defense (D1): {len(d1)} (Expect 72)")
print(f"Unseen Sandbox (D2): {len(d2)} (Expect 72)")
print(f"System Trivialization (D3): {len(d3)} (Expect 72)")

total_book = len(worked) + len(margin) + len(p1) + len(p2) + len(p3)
total_dojo = len(d1) + len(d2) + len(d3)
total_p = total_book + total_dojo

print(f"\n--- SUMMARY ---")
print(f"Total Book Problems: {total_book} (Expect 384)")
print(f"Total Dojo Problems: {total_dojo} (Expect 216)")
print(f"GRAND TOTAL PROBLEMS: {total_p} (Expect 600)")
