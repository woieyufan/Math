# -*- coding: utf-8 -*-
"""
CSS Styles and HTML Head configuration for Middle-School Gifted Math White Paper V4.0
Publication Specifications with KaTeX Math Typesetting, Elegant Typography, and Multi-Device Compatibility.
"""

HTML_HEAD = r'''<!DOCTYPE html>
<html lang="zh-Hant">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
<title>中學數理資優思維與奧林匹克競賽教研白皮書</title>

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
    --primary: #1e3a8a;          /* Deep Academic Indigo */
    --primary-dark: #0f172a;     /* Obsidian Dark */
    --primary-light: #eff6ff;    /* Sky tint */
    --primary-border: #bfdbfe;   /* Border blue */
    --accent: #0284c7;           /* Cerulean Accent */
    --emerald: #059669;          /* Cyber Emerald */
    --emerald-light: #ecfdf5;    /* Emerald background */
    --amber: #d97706;            /* Warm Amber */
    --amber-light: #fffbeb;      /* Amber background */
    --rose: #e11d48;             /* Crimson Rose */
    --rose-light: #fff1f2;       /* Rose background */
    --neon-cyan: #00e5ff;        /* Neon cyan brand */
    --text-dark: #1e293b;        /* Slate text */
    --text-muted: #64748b;       /* Muted text */
    --border-color: #cbd5e1;     /* Border slate */
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
    line-height: 1.6;
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
    background: linear-gradient(145deg, #060d1a 0%, #0c1a36 45%, #1e3a8a 100%);
    color: #ffffff;
    padding: 38px 46px;
    width: 100%;
    height: 1120px;
    box-sizing: border-box;
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
    height: 52px;
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
    margin: 12px 0;
  }

  .cover-badge {
    display: inline-block;
    padding: 5px 14px;
    background: rgba(0, 229, 255, 0.15);
    border: 1px solid var(--neon-cyan);
    border-radius: 4px;
    color: var(--neon-cyan);
    font-size: 11.5px;
    font-weight: 700;
    letter-spacing: 2px;
    margin-bottom: 16px;
  }

  .doc-title {
    font-size: 30px;
    font-weight: 900;
    line-height: 1.3;
    margin: 0 0 14px 0;
    letter-spacing: -0.5px;
    background: linear-gradient(180deg, #ffffff 0%, #cbd5e1 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
  }

  .doc-subtitle {
    font-size: 14px;
    font-weight: 400;
    color: #94a3b8;
    max-width: 820px;
    line-height: 1.55;
    margin: 0 0 20px 0;
  }

  .meta-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 12px;
    border-top: 1px solid rgba(255, 255, 255, 0.15);
    padding-top: 16px;
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
    margin-bottom: 12px;
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
    margin-bottom: 10px;
  }

  .chapter-tag {
    display: inline-block;
    font-size: 11px;
    font-weight: 700;
    color: var(--accent);
    text-transform: uppercase;
    letter-spacing: 1px;
    margin-bottom: 4px;
  }

  .chapter-title {
    font-size: 21px;
    font-weight: 800;
    color: var(--primary);
    margin: 0 0 4px 0;
    display: flex;
    align-items: center;
    gap: 10px;
    line-height: 1.35;
  }

  .chapter-desc {
    font-size: 12.5px;
    color: var(--text-muted);
    margin: 0;
  }

  .hero-statement {
    background: linear-gradient(135deg, #f0f7ff 0%, #e0f2fe 100%);
    border-left: 4px solid var(--accent);
    padding: 12px 16px;
    border-radius: 0 6px 6px 0;
    font-size: 13.5px;
    font-weight: 600;
    color: #0369a1;
    margin-bottom: 12px;
    line-height: 1.6;
  }

  .section-title {
    font-size: 15px;
    font-weight: 800;
    color: var(--primary-dark);
    margin: 10px 0 6px 0;
    border-left: 3.5px solid var(--accent);
    padding-left: 8px;
  }

  .para {
    font-size: 13px;
    color: #334155;
    line-height: 1.65;
    margin-bottom: 10px;
  }

  /* Theorem & Concept Cards */
  .concept-card {
    background: #ffffff;
    border: 1px solid #e2e8f0;
    border-radius: 6px;
    padding: 12px 14px;
    margin-bottom: 10px;
    box-shadow: 0 2px 6px rgba(0, 0, 0, 0.03);
  }

  .concept-card-emerald {
    border-top: 3px solid var(--emerald);
    background: var(--emerald-light);
  }

  .concept-card-indigo {
    border-top: 3px solid var(--primary);
    background: var(--primary-light);
  }

  .concept-card-amber {
    border-top: 3px solid var(--amber);
    background: var(--amber-light);
  }

  .concept-card-rose {
    border-top: 3px solid var(--rose);
    background: var(--rose-light);
  }

  .card-title {
    font-size: 14px;
    font-weight: 800;
    color: var(--primary-dark);
    margin-bottom: 6px;
    display: flex;
    align-items: center;
    gap: 8px;
  }

  /* Two Column & Grid Layouts */
  .two-col-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 12px;
    margin-bottom: 10px;
  }

  .three-col-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 10px;
    margin-bottom: 10px;
  }

  .four-col-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 10px;
    margin-bottom: 10px;
  }

  /* Tables */
  .doc-table {
    width: 100%;
    border-collapse: collapse;
    font-size: 12px;
    margin: 8px 0;
  }

  .doc-table th {
    background: #f1f5f9;
    color: #1e293b;
    font-weight: 700;
    text-align: left;
    padding: 8px 10px;
    border: 1px solid #cbd5e1;
  }

  .doc-table td {
    padding: 7px 10px;
    border: 1px solid #e2e8f0;
    color: #334155;
    vertical-align: top;
    line-height: 1.5;
  }

  .doc-table tr:nth-child(even) td {
    background: #f8fafc;
  }

  /* Proof & Problem Box */
  .problem-box {
    background: #ffffff;
    border: 1px solid #cbd5e1;
    border-left: 4px solid var(--primary);
    border-radius: 4px;
    padding: 10px 14px;
    margin: 8px 0;
    font-size: 12.5px;
  }

  .problem-header {
    font-weight: 800;
    color: var(--primary);
    margin-bottom: 4px;
  }

  .proof-box {
    background: #f8fafc;
    border: 1px dashed #94a3b8;
    border-radius: 4px;
    padding: 10px 12px;
    margin: 6px 0;
    font-size: 12px;
    line-height: 1.6;
    color: #1e293b;
  }

  .proof-step {
    margin-bottom: 4px;
  }

  .step-num {
    font-weight: 700;
    color: var(--accent);
  }

  /* Code / Monospace Formula Box */
  .formula-highlight {
    background: #0f172a;
    color: #38bdf8;
    border-radius: 4px;
    padding: 8px 12px;
    margin: 6px 0;
    font-family: "Fira Code", monospace;
    font-size: 12px;
    text-align: center;
  }

  /* Flow / Step List */
  .step-list {
    list-style: none;
    padding-left: 0;
    margin: 6px 0;
  }

  .step-list li {
    position: relative;
    padding-left: 24px;
    margin-bottom: 6px;
    font-size: 12.5px;
    line-height: 1.5;
  }

  .step-list li::before {
    content: "➜";
    position: absolute;
    left: 4px;
    top: 0;
    color: var(--accent);
    font-weight: 800;
  }

  /* Annotation Anchors */
  .annot-target {
    display: inline-block;
    padding: 1px 4px;
    border-bottom: 1.5px dashed var(--accent);
    cursor: pointer;
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
      padding: 34px 44px;
      page-break-after: always;
      page-break-inside: avoid;
      break-after: page;
      break-inside: avoid;
      overflow: hidden;
    }
  }
</style>
</head>
<body>
<div class="page-container">
'''
