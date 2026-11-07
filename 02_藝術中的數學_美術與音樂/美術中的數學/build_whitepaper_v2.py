# -*- coding: utf-8 -*-
"""
Master Build Script for 小學全域：美術中的數學工程企劃白皮書 (Version 3.0)
Course Code: ELEM-ART-MATH-MASTER
Runs art_math_v3_src/build.py
"""
import os
import sys

src_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'art_math_v3_src')
if src_dir not in sys.path:
    sys.path.insert(0, src_dir)

import build
