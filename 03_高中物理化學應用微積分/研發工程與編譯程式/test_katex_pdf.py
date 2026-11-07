# -*- coding: utf-8 -*-
import subprocess
import os

chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
test_html = r"C:\Users\user\.gemini\antigravity\brain\17c5c8ea-1f34-4270-a5e4-410bdd5037d4\scratch\test_katex.html"
test_pdf = r"C:\Users\user\.gemini\antigravity\brain\17c5c8ea-1f34-4270-a5e4-410bdd5037d4\scratch\test_katex.pdf"

with open(test_html, "w", encoding="utf-8") as f:
    f.write("""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.css">
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.js"></script>
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/contrib/auto-render.min.js" onload="renderMathInElement(document.body);"></script>
</head>
<body>
<h1>Formula Test</h1>
<p>Inline: $E = mc^2$ and $\\int_0^1 x^2 dx = \\frac{1}{3}$.</p>
<p>Display: $$\\frac{d}{dt}\\left(\\frac{\\partial L}{\\partial \\dot{q}}\\right) - \\frac{\\partial L}{\\partial q} = 0$$</p>
</body>
</html>""")

cmd = [
    chrome_path,
    "--headless=new",
    "--disable-gpu",
    "--run-all-compositor-stages-before-draw",
    "--virtual-time-budget=5000",
    "--no-pdf-header-footer",
    f"--print-to-pdf={test_pdf}",
    test_html
]

res = subprocess.run(cmd, capture_output=True, text=True)
print("Return code:", res.returncode)
print("PDF size:", os.path.getsize(test_pdf) if os.path.exists(test_pdf) else 0)
