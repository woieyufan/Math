# -*- coding: utf-8 -*-
"""
Master Entry Point for
《看見幾何：從寫字、拍照、剪衣服到文藝復興名畫的視覺解密》
Advanced Extracurricular STEM/STEAM Book Edition (14-page prototype)

Executes book_vision_geometry_src/build.py
"""
import os
import sys

src_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'book_vision_geometry_src')
if src_dir not in sys.path:
    sys.path.insert(0, src_dir)

import build

if __name__ == '__main__':
    build.run_build()
