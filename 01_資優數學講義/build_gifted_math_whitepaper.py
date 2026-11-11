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
    print("Executing Master Builder for Gifted Math White Paper...")
    success = build.run_build()
    if success:
        print("\n>>> All build tasks completed successfully! <<<")
    else:
        print("\n>>> Build failed! Please check logs above. <<<")
        sys.exit(1)
