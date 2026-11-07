# -*- coding: utf-8 -*-
"""
CSS Styles and Book Layout configuration for
《看見幾何：從寫字、拍照、剪衣服到文藝復興名畫的視覺解密》
Advanced Extracurricular STEM/STEAM Book Edition.
"""

HTML_HEAD = r'''<!DOCTYPE html>
<html lang="zh-Hant">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
<title>看見幾何：從寫字、拍照、剪衣服到文藝復興名畫的視覺解密</title>

<!-- KaTeX for high-precision Math typesetting -->
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.css">
<script src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/contrib/auto-render.min.js"></script>

<style>
  :root {
    --primary: #1e3a8a;
    --primary-dark: #0f172a;
    --primary-light: #eff6ff;
    --primary-border: #bfdbfe;
    --accent: #0284c7;
    --neon-cyan: #00e5ff;
    --text-dark: #1e293b;
    --text-muted: #64748b;
    --border-color: #e2e8f0;
    --card-bg: #ffffff;
    --bg-light: #f8fafc;
    --gold: #d97706;
    --ruby: #e11d48;
    --emerald: #16a34a;
  }

  * { box-sizing: border-box; }

  body {
    margin: 0;
    padding: 0;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "PingFang TC", "Microsoft JhengHei", sans-serif;
    background-color: #0b0f19;
    color: var(--text-dark);
    -webkit-font-smoothing: antialiased;
    line-height: 1.6;
  }

  .page-container {
    max-width: 1024px;
    margin: 30px auto;
    background: #ffffff;
    box-shadow: 0 10px 40px rgba(0, 0, 0, 0.5);
    border-radius: 8px;
    overflow: hidden;
  }

  /* Cover Layout */
  .cover-wrapper {
    background: linear-gradient(145deg, #080a0f 0%, #0d1527 50%, #1e3a8a 100%);
    color: #ffffff;
    padding: 70px 60px;
    min-height: 820px;
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
    gap: 20px;
  }

  .brand-logo-img {
    height: 60px;
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
    font-size: 11px;
    font-weight: 500;
    letter-spacing: 1px;
    color: var(--neon-cyan);
  }

  .cover-main {
    margin: 40px 0;
  }

  .cover-badge {
    display: inline-block;
    padding: 6px 16px;
    background: rgba(0, 229, 255, 0.15);
    border: 1px solid var(--neon-cyan);
    border-radius: 4px;
    color: var(--neon-cyan);
    font-size: 13px;
    font-weight: 700;
    letter-spacing: 2px;
    margin-bottom: 22px;
  }

  .doc-title {
    font-size: 42px;
    font-weight: 900;
    line-height: 1.25;
    margin: 0 0 16px 0;
    letter-spacing: -0.5px;
    background: linear-gradient(180deg, #ffffff 0%, #cbd5e1 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
  }

  .doc-subtitle {
    font-size: 17.5px;
    font-weight: 400;
    color: #94a3b8;
    max-width: 820px;
    line-height: 1.55;
    margin: 0 0 30px 0;
  }

  .meta-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 16px;
    border-top: 1px solid rgba(255, 255, 255, 0.15);
    padding-top: 22px;
  }

  .meta-item {
    display: flex;
    flex-direction: column;
  }

  .meta-label {
    font-size: 11px;
    text-transform: uppercase;
    letter-spacing: 1px;
    color: #64748b;
    margin-bottom: 4px;
  }

  .meta-val {
    font-size: 13.5px;
    font-weight: 600;
    color: #e2e8f0;
  }

  .cover-footer {
    display: flex;
    justify-content: space-between;
    align-items: flex-end;
    border-top: 1px solid rgba(255, 255, 255, 0.1);
    padding-top: 18px;
    font-size: 11.5px;
    color: #64748b;
  }

  /* Section Pages */
  .section-page {
    padding: 38px 46px;
    min-height: 820px;
    position: relative;
    page-break-after: always;
    break-after: page;
    background: #ffffff;
  }

  .page-top-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-bottom: 2px solid var(--primary);
    padding-bottom: 7px;
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
    height: 16px;
    width: auto;
  }

  .chapter-header-box {
    margin-bottom: 12px;
  }

  .chapter-tag {
    font-size: 11px;
    font-weight: 800;
    text-transform: uppercase;
    color: var(--accent);
    letter-spacing: 1.5px;
    margin-bottom: 2px;
  }

  .chapter-title {
    font-size: 21px;
    font-weight: 800;
    color: var(--primary);
    margin: 0 0 5px 0;
    display: flex;
    align-items: center;
    gap: 10px;
  }

  .para {
    font-size: 12px;
    color: #334155;
    margin-bottom: 8px;
    text-align: justify;
    line-height: 1.6;
  }

  /* Detective Box / Mystery Header */
  .mystery-box {
    background: #fff1f2;
    border-left: 4px solid var(--ruby);
    border-radius: 5px;
    padding: 10px 14px;
    margin-bottom: 12px;
  }

  .mystery-title {
    font-size: 12.5px;
    font-weight: 800;
    color: #9f1239;
    margin-bottom: 4px;
    display: flex;
    align-items: center;
    gap: 6px;
  }

  .mystery-desc {
    font-size: 11.5px;
    color: #881337;
    line-height: 1.55;
  }

  /* Hands-on Workshop Box */
  .workshop-box {
    background: #eff6ff;
    border: 1px solid #bfdbfe;
    border-radius: 6px;
    padding: 11px 14px;
    margin-bottom: 12px;
  }

  .workshop-title {
    font-size: 12.5px;
    font-weight: 800;
    color: var(--primary);
    margin-bottom: 6px;
    display: flex;
    align-items: center;
    gap: 6px;
  }

  .workshop-steps {
    font-size: 11.5px;
    color: #1e3a8a;
    line-height: 1.6;
  }

  .workshop-steps ol {
    margin: 4px 0 0 16px;
    padding: 0;
  }

  .workshop-steps li {
    margin-bottom: 4px;
  }

  /* Mathematical Engine Box / Aha Box */
  .engine-box {
    background: #f0fdf4;
    border-left: 4px solid var(--emerald);
    border-radius: 5px;
    padding: 10px 14px;
    margin-bottom: 12px;
  }

  .engine-title {
    font-size: 12.5px;
    font-weight: 800;
    color: #14532d;
    margin-bottom: 4px;
    display: flex;
    align-items: center;
    gap: 6px;
  }

  .engine-desc {
    font-size: 11.5px;
    color: #166534;
    line-height: 1.55;
  }

  /* Master's Secret Sidebar / Bonus Box */
  .secret-box {
    background: #fffbeb;
    border-left: 4px solid var(--gold);
    border-radius: 5px;
    padding: 9px 13px;
    margin-top: 10px;
  }

  .secret-title {
    font-size: 11.5px;
    font-weight: 800;
    color: #92400e;
    margin-bottom: 3px;
    display: flex;
    align-items: center;
    gap: 5px;
  }

  .secret-desc {
    font-size: 11px;
    color: #78350f;
    line-height: 1.5;
  }

  /* Two Column Page Layout */
  .book-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 14px;
    margin-bottom: 10px;
  }

  .card-pane {
    background: var(--bg-light);
    border: 1px solid var(--border-color);
    border-radius: 6px;
    padding: 11px 13px;
  }

  /* Table styling */
  .doc-table {
    width: 100%;
    border-collapse: collapse;
    margin: 8px 0;
    font-size: 10.5px;
  }

  .doc-table th {
    background: var(--primary);
    color: #ffffff;
    font-weight: 700;
    padding: 6px 9px;
    text-align: left;
    border: 1px solid var(--primary);
  }

  .doc-table td {
    padding: 5px 9px;
    border: 1px solid var(--border-color);
    color: var(--text-dark);
    vertical-align: top;
    line-height: 1.45;
  }

  .doc-table tr:nth-child(even) td {
    background: var(--bg-light);
  }

  /* TOC Styles */
  .toc-vol-box {
    margin-bottom: 8px;
    border: 1px solid var(--border-color);
    border-radius: 5px;
    overflow: hidden;
  }

  .toc-vol-head {
    background: var(--primary);
    color: #ffffff;
    font-size: 11px;
    font-weight: 800;
    padding: 4px 10px;
    display: flex;
    justify-content: space-between;
  }

  .toc-chap-row {
    display: flex;
    justify-content: space-between;
    align-items: baseline;
    padding: 3.5px 10px;
    font-size: 10px;
    border-bottom: 1px solid var(--border-color);
    background: #ffffff;
  }

  .toc-chap-row:last-child {
    border-bottom: none;
  }

  .toc-chap-title {
    font-weight: 600;
    color: var(--primary-dark);
    max-width: 68%;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
  }

  .toc-chap-math {
    color: var(--accent);
    font-weight: 700;
    font-size: 9.5px;
    white-space: nowrap;
  }

  @media print {
    body { background: #ffffff; }
    .page-container {
      max-width: 100%;
      margin: 0;
      padding: 0;
      box-shadow: none;
      border-radius: 0;
    }
    .cover-wrapper { min-height: 98vh; }
    .section-page { min-height: 98vh; }
  }
</style>
</head>
<body>
<div class="page-container">
'''
