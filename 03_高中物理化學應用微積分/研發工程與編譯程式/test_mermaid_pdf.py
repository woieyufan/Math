# -*- coding: utf-8 -*-
import subprocess
import os

chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
test_html = r"C:\Users\user\.gemini\antigravity\brain\17c5c8ea-1f34-4270-a5e4-410bdd5037d4\scratch\test_mermaid.html"
test_pdf = r"C:\Users\user\.gemini\antigravity\brain\17c5c8ea-1f34-4270-a5e4-410bdd5037d4\scratch\test_mermaid.pdf"

with open(test_html, "w", encoding="utf-8") as f:
    f.write("""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<script src="https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.min.js"></script>
<script>mermaid.initialize({startOnLoad:true});</script>
</head>
<body>
<h1>Mermaid Test</h1>
<div class="mermaid">
flowchart LR
    A[Start] --> B[Next]
    B --> C[Done]
</div>
</body>
</html>""")

cmd = [
    chrome_path,
    "--headless=new",
    "--disable-gpu",
    "--run-all-compositor-stages-before-draw",
    "--virtual-time-budget=6000",
    "--no-pdf-header-footer",
    f"--print-to-pdf={test_pdf}",
    test_html
]

res = subprocess.run(cmd, capture_output=True, text=True)
print("Return code:", res.returncode)
print("PDF size:", os.path.getsize(test_pdf) if os.path.exists(test_pdf) else 0)
