# -*- coding: utf-8 -*-
"""
Master Entry Point for
《中學數理資優思維與奧林匹克競賽教研白皮書》 Version 4.0 (16 pages)
Executes 資優數學白皮書編譯系統/build.py
"""
import os
import sys

src_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '資優數學白皮書編譯系統')
if src_dir not in sys.path:
    sys.path.insert(0, src_dir)

import build

if __name__ == '__main__':
    generate_pdf = "--pdf" in sys.argv
    mode_text = "HTML + PDF" if generate_pdf else "HTML Only (Default: 不主動生成 PDF)"
    print(f"Executing Master Builder for Gifted Math White Paper [{mode_text}]...")
    success = build.run_build(generate_pdf=generate_pdf)
    if success:
        print("\n>>> All build tasks completed successfully! <<<")
    else:
        print("\n>>> Build failed! Please check logs above. <<<")
        sys.exit(1)
