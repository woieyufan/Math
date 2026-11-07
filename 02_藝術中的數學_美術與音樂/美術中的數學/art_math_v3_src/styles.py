# -*- coding: utf-8 -*-
"""
CSS Styles and HTML Head configuration for Art Math White Paper V4.0
iPad 4:3 / A4 Publication Specifications with KaTeX Math Rendering Support.
Overhauled for superior legibility, comfortable font scales (13.5px-14px body),
generous whitespace, balanced vertical distribution, and zero unwanted headers/footers.
"""

HTML_HEAD = r'''<!DOCTYPE html>
<html lang="zh-Hant">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
<title>小學全域：視覺幾何與藝術工程企劃白皮書</title>

<!-- KaTeX for high-precision Math typesetting -->
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.css">
<script src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/contrib/auto-render.min.js"></script>

<style>
  @page {
    size: A4 portrait;
    margin: 0;
  }

  :root {
    --primary: #1e3a8a;
    --primary-dark: #0f172a;
    --primary-light: #eff6ff;
    --primary-border: #bfdbfe;
    --accent: #0284c7;
    --neon-cyan: #00e5ff;
    --text-dark: #1e293b;
    --text-muted: #64748b;
    --border-color: #cbd5e1;
    --card-bg: #ffffff;
    --bg-light: #f8fafc;
  }

  * {
    box-sizing: border-box;
    -webkit-print-color-adjust: exact !important;
    print-color-adjust: exact !important;
  }

  html, body {
    margin: 0;
    padding: 0;
    font-family: -apple-system, BlinkMacSystemFont, "SF Pro Text", "Segoe UI", Roboto, "PingFang TC", "Noto Sans TC", "Microsoft JhengHei", sans-serif;
    background-color: #0b0f19;
    color: var(--text-dark);
    -webkit-font-smoothing: antialiased;
    line-height: 1.65;
  }

  .page-container {
    max-width: 860px;
    margin: 25px auto;
    background: #ffffff;
    box-shadow: 0 12px 48px rgba(0, 0, 0, 0.45);
    border-radius: 4px;
    overflow: hidden;
  }

  /* Cover Layout */
  .cover-wrapper {
    background: linear-gradient(145deg, #09111e 0%, #0f1f3d 50%, #1e3a8a 100%);
    color: #ffffff;
    padding: 48px 52px;
    width: 100%;
    height: 1123px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    position: relative;
    overflow: hidden;
    page-break-after: always;
    break-after: page;
  }

  .cover-watermark {
    position: absolute;
    right: -80px;
    bottom: -80px;
    width: 480px;
    height: 480px;
    opacity: 0.08;
    pointer-events: none;
  }

  .cover-header-brand {
    display: flex;
    align-items: center;
    gap: 18px;
  }

  .brand-logo-img {
    height: 56px;
    width: auto;
    filter: drop-shadow(0 4px 12px rgba(0, 229, 255, 0.3));
  }

  .brand-text-col {
    display: flex;
    flex-direction: column;
  }

  .brand-title {
    font-size: 20px;
    font-weight: 800;
    letter-spacing: 2px;
    color: #ffffff;
  }

  .brand-sub {
    font-size: 11.5px;
    font-weight: 500;
    letter-spacing: 1px;
    color: var(--neon-cyan);
  }

  .cover-main {
    margin: 20px 0;
  }

  .cover-badge {
    display: inline-block;
    padding: 6px 16px;
    background: rgba(0, 229, 255, 0.15);
    border: 1px solid var(--neon-cyan);
    border-radius: 4px;
    color: var(--neon-cyan);
    font-size: 12px;
    font-weight: 700;
    letter-spacing: 2px;
    margin-bottom: 20px;
  }

  .doc-title {
    font-size: 34px;
    font-weight: 900;
    line-height: 1.3;
    margin: 0 0 16px 0;
    letter-spacing: -0.5px;
    background: linear-gradient(180deg, #ffffff 0%, #cbd5e1 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
  }

  .doc-subtitle {
    font-size: 15.5px;
    font-weight: 400;
    color: #94a3b8;
    max-width: 820px;
    line-height: 1.6;
    margin: 0 0 24px 0;
  }

  .meta-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 14px;
    border-top: 1px solid rgba(255, 255, 255, 0.15);
    padding-top: 20px;
  }

  .meta-item {
    display: flex;
    flex-direction: column;
  }

  .meta-label {
    font-size: 11px;
    text-transform: uppercase;
    letter-spacing: 1px;
    color: #94a3b8;
    margin-bottom: 4px;
  }

  .meta-val {
    font-size: 13px;
    font-weight: 600;
    color: #e2e8f0;
  }

  .cover-footer {
    display: flex;
    justify-content: space-between;
    align-items: flex-end;
    border-top: 1px solid rgba(255, 255, 255, 0.12);
    padding-top: 16px;
    font-size: 11.5px;
    color: #64748b;
  }

  /* Section Pages */
  .section-page {
    padding: 38px 46px;
    width: 100%;
    height: 1123px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    position: relative;
    page-break-after: always;
    break-after: page;
    background: #ffffff;
    overflow: hidden;
  }

  .page-top-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-bottom: 2px solid var(--primary);
    padding-bottom: 8px;
    margin-bottom: 14px;
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 1.5px;
    color: var(--primary);
  }

  .header-left {
    text-transform: uppercase;
  }

  .header-right {
    display: flex;
    align-items: center;
    gap: 8px;
    color: var(--text-muted);
  }

  .header-logo-mini {
    height: 18px;
    width: auto;
  }

  .page-bottom-footer {
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-top: 1px solid #e2e8f0;
    padding-top: 8px;
    margin-top: auto;
    font-size: 10.5px;
    color: #94a3b8;
    font-weight: 500;
    letter-spacing: 0.5px;
  }

  .page-bottom-footer .footer-center {
    font-weight: 700;
    color: #475569;
  }

  .chapter-header-box {
    margin-bottom: 12px;
  }

  .chapter-title {
    font-size: 22px;
    font-weight: 800;
    color: var(--primary);
    margin: 0 0 6px 0;
    display: flex;
    align-items: center;
    gap: 10px;
    line-height: 1.35;
  }

  .section-title {
    font-size: 15.5px;
    font-weight: 800;
    color: var(--primary-dark);
    margin: 14px 0 6px 0;
    border-left: 4px solid var(--accent);
    padding-left: 10px;
    line-height: 1.4;
  }

  .para {
    font-size: 13px;
    color: #334155;
    margin-bottom: 10px;
    text-align: justify;
    line-height: 1.65;
  }

  /* Hero Statement */
  .hero-statement {
    font-size: 14px;
    font-weight: 700;
    color: #1e3a8a;
    background: #eff6ff;
    border-left: 4px solid #0284c7;
    padding: 12px 16px;
    border-radius: 6px;
    margin: 12px 0;
    line-height: 1.62;
  }

  /* Centered Formula Box */
  .formula-box {
    text-align: center;
    background: #f8fafc;
    border: 1px solid #e2e8f0;
    border-radius: 8px;
    padding: 10px 16px;
    margin: 10px 0;
    font-size: 14px;
  }

  /* TOC Grid */
  .toc-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 12px;
    margin: 12px 0;
  }

  .toc-item {
    background: var(--bg-light);
    border: 1px solid var(--border-color);
    border-radius: 8px;
    padding: 12px 14px;
    border-left: 4px solid var(--primary);
  }

  .toc-item-title {
    font-size: 13px;
    font-weight: 700;
    color: var(--primary);
    margin-bottom: 4px;
  }

  .toc-item-sub {
    font-size: 11px;
    color: #64748b;
    line-height: 1.48;
  }

  /* Tables */
  .doc-table {
    width: 100%;
    border-collapse: collapse;
    margin: 10px 0;
    font-size: 12px;
    line-height: 1.5;
  }

  .doc-table th {
    background: var(--primary);
    color: #ffffff;
    font-weight: 700;
    padding: 7px 10px;
    text-align: left;
    border: 1px solid var(--primary);
    font-size: 12px;
  }

  .doc-table td {
    padding: 7px 10px;
    border: 1px solid var(--border-color);
    color: var(--text-dark);
    vertical-align: top;
  }

  .doc-table tr:nth-child(even) td {
    background: var(--bg-light);
  }

  /* Stage Banners */
  .stage-banner {
    background: linear-gradient(90deg, var(--primary) 0%, #1e40af 100%);
    color: #ffffff;
    padding: 8px 14px;
    border-radius: 6px;
    font-size: 13.5px;
    font-weight: 700;
    margin-bottom: 12px;
    display: flex;
    justify-content: space-between;
    align-items: center;
  }

  .stage-badge {
    background: var(--neon-cyan);
    color: var(--primary-dark);
    font-size: 11px;
    font-weight: 800;
    padding: 3px 8px;
    border-radius: 4px;
    letter-spacing: 0.5px;
  }

  /* Lesson Cards - Expanded & Balanced */
  .lesson-card {
    border: 1.5px solid var(--border-color);
    border-radius: 8px;
    padding: 14px 18px;
    margin-bottom: 12px;
    background: #ffffff;
    box-shadow: 0 2px 6px rgba(0, 0, 0, 0.03);
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    flex: 1;
  }

  .lesson-header {
    display: flex;
    align-items: center;
    gap: 10px;
    margin-bottom: 8px;
  }

  .lesson-num {
    background: var(--primary-light);
    color: var(--primary);
    border: 1.5px solid var(--primary-border);
    font-size: 12px;
    font-weight: 800;
    padding: 3px 8px;
    border-radius: 4px;
    white-space: nowrap;
  }

  .lesson-title-text {
    font-size: 15px;
    font-weight: 800;
    color: var(--primary-dark);
    line-height: 1.35;
  }

  /* Before / After Columns */
  .ba-container {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 10px;
    margin-bottom: 8px;
  }

  .ba-col {
    padding: 8px 12px;
    border-radius: 6px;
    font-size: 12.5px;
    line-height: 1.55;
  }

  .ba-before {
    background: #fff1f2;
    border-left: 3px solid #f43f5e;
    color: #9f1239;
  }

  .ba-after {
    background: #f0fdf4;
    border-left: 3px solid #22c55e;
    color: #166534;
  }

  .ba-head {
    font-weight: 800;
    font-size: 11px;
    text-transform: uppercase;
    margin-bottom: 3px;
    display: flex;
    align-items: center;
    gap: 4px;
  }

  /* Lesson Details Sub-grid */
  .lesson-grid {
    display: grid;
    grid-template-columns: 1fr 1.25fr 1fr;
    gap: 8px;
    background: var(--bg-light);
    padding: 8px 12px;
    border-radius: 6px;
    border: 1px solid #e2e8f0;
    margin-top: 4px;
  }

  .sub-box {
    display: flex;
    flex-direction: column;
  }

  .sub-label {
    font-size: 10.5px;
    font-weight: 800;
    color: var(--text-muted);
    text-transform: uppercase;
    letter-spacing: 0.5px;
    margin-bottom: 2px;
  }

  .sub-desc {
    font-size: 12px;
    color: #334155;
    line-height: 1.5;
  }

  /* Callouts & Highlights */
  .callout-box {
    background: #f0fdf4;
    border: 1px solid #bbf7d0;
    border-left: 4px solid #16a34a;
    border-radius: 8px;
    padding: 12px 16px;
    margin: 12px 0;
  }

  .callout-title {
    font-size: 13.5px;
    font-weight: 800;
    color: #15803d;
    margin-bottom: 4px;
  }

  .callout-content {
    font-size: 12.5px;
    color: #166534;
    line-height: 1.6;
  }

  /* Rubric Grid */
  .rubric-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 12px;
    margin: 10px 0;
  }

  .rubric-box {
    border: 1px solid var(--border-color);
    border-radius: 8px;
    padding: 12px 14px;
    background: #ffffff;
  }

  .rubric-head {
    font-size: 13px;
    font-weight: 800;
    color: var(--primary);
    margin-bottom: 6px;
    border-bottom: 1px solid var(--border-color);
    padding-bottom: 4px;
  }

  .rubric-item {
    font-size: 11.5px;
    color: #334155;
    margin-bottom: 4px;
    line-height: 1.48;
  }

  @media print {
    body {
      background: #ffffff;
    }
    .page-container {
      max-width: 100%;
      margin: 0;
      padding: 0;
      box-shadow: none;
      border-radius: 0;
    }
    .cover-wrapper, .section-page {
      width: 100%;
      height: 100vh;
      min-height: 100vh;
      max-height: 100vh;
      padding: 38px 46px;
      page-break-after: always;
      page-break-inside: avoid;
      break-after: page;
      break-inside: avoid;
      overflow: hidden;
    }
    .lesson-card {
      page-break-inside: avoid;
      break-inside: avoid;
    }
  }
</style>
</head>
<body>
<div class="page-container">
'''
