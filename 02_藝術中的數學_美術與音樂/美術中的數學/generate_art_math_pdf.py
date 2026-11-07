import fitz
import os
import re
import subprocess
import shutil
import base64

# Step 1: Base64 Logo Encoding
logo_png_path = r'C:\Users\user\Documents\woieyufan-brand-assets\woieyufan-logo-transparent-300dpi.png'
with open(logo_png_path, "rb") as f:
    logo_base64 = base64.b64encode(f.read()).decode("utf-8")
logo_data_uri = f"data:image/png;base64,{logo_base64}"

output_html = r'C:\Users\user\Documents\小學全域_美術中的數學企劃白皮書.html'
output_pdf = r'C:\Users\user\Documents\小學全域_美術中的數學企劃白皮書.pdf'

print("Step 1: Logo prepared.")
