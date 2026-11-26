# -*- coding: utf-8 -*-
"""
Master Builder for
《文化中的數理：生活與新聞中的文明密碼》 (37 Chapters + Epilogue)
預設僅輸出單檔發行級 HTML（內建側邊導航與 KaTeX），嚴格遵循全域規範：
未明確傳入 --pdf 參數時，絕不主動生成 PDF 文件。
"""

import html
import os
import re
import shutil
import subprocess
import sys


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
INPUT_MD = os.path.join(BASE_DIR, "文化中的數理_生活與新聞中的文明專書.md")
OUTPUT_HTML = os.path.join(BASE_DIR, "文化中的數理_生活與新聞中的文明專書.html")
OUTPUT_PDF = os.path.join(BASE_DIR, "文化中的數理_生活與新聞中的文明專書.pdf")


HTML_HEAD = r"""<!DOCTYPE html>
<html lang="zh-Hant">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>文化中的數理：生活與新聞中的文明密碼</title>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.css">
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.js"></script>
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/contrib/auto-render.min.js"
  onload="renderMathInElement(document.body, {
    delimiters: [
      {left: '\\[', right: '\\]', display: true},
      {left: '$$', right: '$$', display: true},
      {left: '\\(', right: '\\)', display: false},
      {left: '$', right: '$', display: false}
    ],
    throwOnError: false,
    ignoredTags: ['script', 'noscript', 'style', 'textarea', 'pre', 'code']
  });"></script>
<style>
  :root {
    --bg-page: #f6f4ef;
    --bg-paper: #ffffff;
    --bg-sidebar: #14213d;
    --bg-sidebar-hover: #1f325a;
    --ink-main: #1e293b;
    --ink-muted: #475569;
    --ink-sidebar: #e2e8f0;
    --accent-indigo: #1e3a8a;
    --accent-amber: #b45309;
    --accent-amber-bg: #fffbeb;
    --accent-teal: #0f766e;
    --accent-teal-bg: #f0fdfa;
    --accent-slate-bg: #f8fafc;
    --accent-purple: #5b21b6;
    --accent-purple-bg: #f5f3ff;
    --border-soft: #e2e8f0;
    --border-warm: #e5dccb;
  }

  * {
    box-sizing: border-box;
  }

  html {
    scroll-behavior: smooth;
  }

  body {
    margin: 0;
    padding: 0;
    background: var(--bg-page);
    color: var(--ink-main);
    font-family: "Noto Serif TC", "PingFang TC", "Microsoft JhengHei", -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
    line-height: 1.82;
    font-size: 16.5px;
  }

  .layout-shell {
    display: flex;
    min-height: 100vh;
  }

  /* Sidebar Navigation */
  .sidebar {
    width: 310px;
    flex-shrink: 0;
    background: var(--bg-sidebar);
    color: var(--ink-sidebar);
    position: sticky;
    top: 0;
    height: 100vh;
    overflow-y: auto;
    padding: 22px 16px 40px;
    border-right: 1px solid #0f172a;
    z-index: 40;
  }

  .sidebar-brand {
    padding-bottom: 14px;
    margin-bottom: 14px;
    border-bottom: 1px solid rgba(255, 255, 255, 0.14);
  }

  .sidebar-brand .tag {
    font-size: 11px;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    color: #93c5fd;
    font-weight: 700;
  }

  .sidebar-brand h1 {
    font-size: 18px;
    line-height: 1.4;
    margin: 6px 0 4px;
    color: #ffffff;
  }

  .sidebar-brand p {
    margin: 0;
    font-size: 12.5px;
    color: #cbd5e1;
  }

  .toc-vol-label {
    margin: 16px 6px 6px;
    font-size: 12px;
    font-weight: 700;
    color: #fbbf24;
    letter-spacing: 0.04em;
  }

  .toc-link {
    display: block;
    padding: 6px 10px;
    margin: 2px 0;
    border-radius: 6px;
    color: #e2e8f0;
    text-decoration: none;
    font-size: 13.5px;
    line-height: 1.45;
    transition: background 0.15s ease, color 0.15s ease;
  }

  .toc-link:hover,
  .toc-link.active {
    background: var(--bg-sidebar-hover);
    color: #ffffff;
  }

  .toc-link.active {
    border-left: 3px solid #fbbf24;
    padding-left: 7px;
    font-weight: 600;
  }

  .mobile-nav-btn {
    display: none;
    position: fixed;
    bottom: 18px;
    right: 18px;
    z-index: 60;
    background: var(--bg-sidebar);
    color: #ffffff;
    border: 1px solid #93c5fd;
    border-radius: 999px;
    padding: 10px 16px;
    font-size: 14px;
    font-weight: 600;
    cursor: pointer;
    box-shadow: 0 8px 24px rgba(15, 23, 42, 0.35);
  }

  /* Main Reading Column */
  .main-content {
    flex: 1;
    min-width: 0;
    padding: 36px 28px 80px;
  }

  .book-container {
    max-width: 880px;
    margin: 0 auto;
    background: var(--bg-paper);
    border: 1px solid var(--border-warm);
    border-radius: 12px;
    box-shadow: 0 10px 36px rgba(15, 23, 42, 0.06);
    padding: 48px 54px 64px;
  }

  .hero-header {
    border-bottom: 2px solid var(--accent-indigo);
    padding-bottom: 26px;
    margin-bottom: 34px;
  }

  .hero-kicker {
    display: inline-block;
    background: #eff6ff;
    color: var(--accent-indigo);
    border: 1px solid #bfdbfe;
    border-radius: 999px;
    padding: 4px 14px;
    font-size: 12.5px;
    font-weight: 700;
    letter-spacing: 0.05em;
  }

  .hero-header h1 {
    font-size: 32px;
    line-height: 1.32;
    margin: 14px 0 8px;
    color: #0f172a;
  }

  .hero-subtitle {
    font-size: 17px;
    color: var(--ink-muted);
    margin: 0 0 16px;
  }

  .hero-meta {
    background: #f8fafc;
    border-left: 4px solid var(--accent-indigo);
    padding: 14px 18px;
    border-radius: 0 8px 8px 0;
    font-size: 14.5px;
    color: #334155;
  }

  .hero-meta p {
    margin: 4px 0;
  }

  .volume-banner {
    margin: 44px 0 24px;
    padding: 16px 22px;
    border-radius: 10px;
    background: linear-gradient(135deg, #14213d 0%, #1e3a8a 100%);
    color: #ffffff;
  }

  .volume-banner h2 {
    margin: 0;
    font-size: 22px;
    letter-spacing: 0.03em;
  }

  .volume-banner p {
    margin: 6px 0 0;
    font-size: 14px;
    color: #dbeafe;
  }

  .chapter-section {
    padding: 26px 0 34px;
    border-bottom: 1px dashed #cbd5e1;
  }

  .chapter-section:last-of-type {
    border-bottom: none;
  }

  .chapter-title {
    font-size: 24px;
    line-height: 1.4;
    color: #0f172a;
    margin: 0 0 18px;
    padding-left: 14px;
    border-left: 5px solid var(--accent-amber);
  }

  /* Semantic Module Cards */
  .module-card {
    margin: 18px 0;
    padding: 18px 22px;
    border-radius: 10px;
    border: 1px solid var(--border-soft);
    background: #ffffff;
  }

  .module-card.mod-news {
    background: #fffbeb;
    border-color: #fde68a;
  }

  .module-card.mod-story {
    background: #f8fafc;
    border-color: #cbd5e1;
  }

  .module-card.mod-math {
    background: #f0fdfa;
    border-color: #99f6e4;
  }

  .module-card.mod-exercise {
    background: #f8fafc;
    border-color: #bfdbfe;
    border-left: 4px solid var(--accent-indigo);
  }

  .module-card.mod-philosophy {
    background: var(--accent-purple-bg);
    border: 1px solid #ddd6fe;
    border-left: 5px solid var(--accent-purple);
  }

  .module-heading {
    margin: 0 0 12px;
    font-size: 17.5px;
    color: #0f172a;
    border-bottom: 1px solid rgba(15, 23, 42, 0.09);
    padding-bottom: 6px;
  }

  .callout-subhead {
    margin: 18px 0 8px;
    font-size: 16px;
    font-weight: 700;
    color: #0f766e;
    padding-left: 10px;
    border-left: 3px solid #14b8a6;
  }

  p {
    margin: 10px 0;
  }

  ul, ol {
    margin: 8px 0 12px;
    padding-left: 24px;
  }

  li {
    margin: 6px 0;
  }

  blockquote {
    margin: 14px 0;
    padding: 12px 18px;
    border-left: 4px solid var(--accent-amber);
    background: #fffdf7;
    color: #334155;
    border-radius: 0 8px 8px 0;
  }

  blockquote p {
    margin: 4px 0;
  }

  code {
    font-family: "JetBrains Mono", "Fira Code", Consolas, monospace;
    font-size: 0.88em;
    background: #f1f5f9;
    padding: 1px 6px;
    border-radius: 4px;
    color: #0f172a;
  }

  pre.book-ascii {
    font-family: "JetBrains Mono", "Noto Sans Mono CJK TC", Consolas, monospace;
    font-size: 14px;
    line-height: 1.55;
    background: #0f172a;
    color: #e2e8f0;
    padding: 16px 20px;
    border-radius: 8px;
    overflow-x: auto;
    margin: 14px 0;
  }

  .table-wrap {
    overflow-x: auto;
    margin: 14px 0;
  }

  table {
    width: 100%;
    border-collapse: collapse;
    font-size: 14.5px;
    background: #ffffff;
  }

  th, td {
    border: 1px solid #cbd5e1;
    padding: 9px 12px;
    text-align: left;
    vertical-align: top;
  }

  th {
    background: #1e3a8a;
    color: #ffffff;
    font-weight: 600;
  }

  tr:nth-child(even) td {
    background: #f8fafc;
  }

  .katex-display {
    overflow-x: auto;
    overflow-y: hidden;
    padding: 6px 0;
    margin: 10px 0 !important;
  }

  @media (max-width: 980px) {
    .sidebar {
      position: fixed;
      left: -320px;
      transition: left 0.25s ease;
    }
    .sidebar.open {
      left: 0;
    }
    .mobile-nav-btn {
      display: inline-flex;
      align-items: center;
    }
    .main-content {
      padding: 18px 12px 72px;
    }
    .book-container {
      padding: 26px 20px 44px;
    }
  }

  @media print {
    .sidebar, .mobile-nav-btn {
      display: none !important;
    }
    body {
      background: #ffffff;
    }
    .main-content {
      padding: 0;
    }
    .book-container {
      box-shadow: none;
      border: none;
      max-width: 100%;
      padding: 12px;
    }
    .module-card, .volume-banner {
      break-inside: avoid;
    }
  }
</style>
</head>
<body>
<div class="layout-shell">
"""


HTML_FOOTER = r"""
  </div><!-- .book-container -->
  </main>
</div><!-- .layout-shell -->
<button class="mobile-nav-btn" id="mobileNavBtn" type="button">章節目錄</button>
<script>
  document.addEventListener("DOMContentLoaded", function() {
    var sidebar = document.getElementById("sidebarNav");
    var btn = document.getElementById("mobileNavBtn");
    if (btn && sidebar) {
      btn.addEventListener("click", function() {
        sidebar.classList.toggle("open");
      });
    }
    var links = document.querySelectorAll(".toc-link");
    links.forEach(function(link) {
      link.addEventListener("click", function() {
        if (sidebar) sidebar.classList.remove("open");
      });
    });

    var sections = document.querySelectorAll(".chapter-section");
    if ("IntersectionObserver" in window && sections.length > 0) {
      var observer = new IntersectionObserver(function(entries) {
        entries.forEach(function(entry) {
          if (entry.isIntersecting) {
            var id = entry.target.getAttribute("id");
            links.forEach(function(l) {
              l.classList.toggle("active", l.getAttribute("href") === "#" + id);
            });
          }
        });
      }, { rootMargin: "-15% 0px -70% 0px" });
      sections.forEach(function(sec) { observer.observe(sec); });
    }
  });
</script>
</body>
</html>
"""


def protect_math_tokens(text):
    """Replace LaTeX math spans with placeholder tokens before Markdown/HTML escaping."""
    tokens = []

    def _store(match):
        idx = len(tokens)
        tokens.append(match.group(0))
        return f"@@MATHTOKEN_{idx}@@"

    # 1. Display math \[ ... \] (multiline)
    text = re.sub(r"\\\[[\s\S]*?\\\]", _store, text)
    # 2. Display math $$ ... $$ (multiline)
    text = re.sub(r"\$\$[\s\S]*?\$\$", _store, text)
    # 3. Inline math \( ... \)
    text = re.sub(r"\\\([\s\S]*?\\\)", _store, text)
    # 4. Inline math $ ... $ (single-line, non-escaped)
    text = re.sub(r"(?<!\\)\$(?!\$)([^\n$]+?)(?<!\\)\$", _store, text)
    return text, tokens


def restore_math_tokens(rendered_html, tokens):
    """Restore HTML-escaped math expressions cleanly so KaTeX parses raw LaTeX."""
    def _replace(match):
        idx = int(match.group(1))
        return html.escape(tokens[idx], quote=False)

    return re.sub(r"@@MATHTOKEN_(\d+)@@", _replace, rendered_html)


def format_inline(text):
    """Escape HTML and convert inline Markdown while preserving math tokens."""
    # Protect inline code first so ** inside backticks stays literal
    code_spans = []

    def _store_code(m):
        idx = len(code_spans)
        code_spans.append(html.escape(m.group(1), quote=False))
        return f"@@CODESPAN_{idx}@@"

    text = re.sub(r"`([^`]+)`", _store_code, text)
    text = html.escape(text, quote=False)

    # Bold **...**
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
    # Italic *...* (only outside math tokens)
    text = re.sub(r"(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)", r"<em>\1</em>", text)
    # Markdown links [label](url)
    text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', text)

    def _restore_code(m):
        idx = int(m.group(1))
        return f"<code>{code_spans[idx]}</code>"

    text = re.sub(r"@@CODESPAN_(\d+)@@", _restore_code, text)
    return text


def render_table(rows):
    """Render Markdown pipe table rows into HTML table."""
    if not rows:
        return ""
    out = ['<div class="table-wrap"><table>']
    header_done = False
    for idx, row in enumerate(rows):
        cells = [c.strip() for c in row.strip().strip("|").split("|")]
        if idx == 1 and all(re.fullmatch(r":?-+:?", c.replace(" ", "")) for c in cells if c != ""):
            continue
        if not header_done:
            out.append("<thead><tr>" + "".join(f"<th>{format_inline(c)}</th>" for c in cells) + "</tr></thead><tbody>")
            header_done = True
        else:
            out.append("<tr>" + "".join(f"<td>{format_inline(c)}</td>" for c in cells) + "</tr>")
    if header_done:
        out.append("</tbody>")
    out.append("</table></div>")
    return "\n".join(out)


def classify_module(heading_text):
    if "新聞與生活" in heading_text:
        return "mod-news"
    if "文明故事" in heading_text or "器物構造" in heading_text:
        return "mod-story"
    if "核心數理" in heading_text:
        return "mod-math"
    if "動手算術" in heading_text:
        return "mod-exercise"
    if "數理哲學前瞻" in heading_text or "🌌" in heading_text:
        return "mod-philosophy"
    return ""


def markdown_to_html_book(md_text):
    """Parse monograph Markdown into sidebar TOC + structured semantic HTML."""
    # Pre-extract fenced ASCII/text blocks before math tokenization
    ascii_blocks = []

    def _store_fence(match):
        idx = len(ascii_blocks)
        body = match.group(2).rstrip("\n")
        ascii_blocks.append(html.escape(body, quote=False))
        return f"@@ASCIIBLOCK_{idx}@@"

    md_text = re.sub(r"```([a-zA-Z0-9_-]*)\n([\s\S]*?)```", _store_fence, md_text)
    protected_md, math_tokens = protect_math_tokens(md_text)

    lines = protected_md.splitlines()
    body_parts = []
    toc_items = []  # list of tuples: ("vol", label) or ("ch", id, label)

    title = "文化中的數理：生活與新聞中的文明密碼"
    subtitle = ""
    hero_meta_lines = []

    in_hero = True
    in_plain_toc = False
    in_section = False
    in_module_card = False

    table_buf = []
    list_buf = []   # list of dicts: {"text": str, "subitems": [(indent, tag, text)]}
    list_type = None
    ol_start = 1
    quote_buf = []

    def flush_table():
        nonlocal table_buf
        if table_buf:
            body_parts.append(render_table(table_buf))
            table_buf = []

    def render_subitems(subitems):
        if not subitems:
            return ""
        # Group into top sublevel vs deeper sublevel based on first indent
        base_indent = subitems[0][0]
        chunks = []
        cur_tag = None
        cur_items = []  # [{"text": str, "children": [(tag, text)]}]

        def _flush_cur():
            nonlocal cur_tag, cur_items
            if not cur_items:
                return
            lis = []
            for it in cur_items:
                inner = format_inline(it["text"])
                if it["children"]:
                    child_tag = it["children"][0][0]
                    child_lis = "".join(f"<li>{format_inline(ct)}</li>" for _, ct in it["children"])
                    inner += f"<{child_tag}>{child_lis}</{child_tag}>"
                lis.append(f"<li>{inner}</li>")
            chunks.append(f"<{cur_tag}>{''.join(lis)}</{cur_tag}>")
            cur_tag = None
            cur_items = []

        for ind, tag, txt in subitems:
            if ind > base_indent + 1 and cur_items:
                cur_items[-1]["children"].append((tag, txt))
            else:
                if cur_tag and cur_tag != tag:
                    _flush_cur()
                cur_tag = tag
                cur_items.append({"text": txt, "children": []})
        _flush_cur()
        return "".join(chunks)

    def flush_list():
        nonlocal list_buf, list_type, ol_start
        if list_buf:
            tag = list_type or "ul"
            open_tag = f'<ol start="{ol_start}">' if (tag == "ol" and ol_start != 1) else f"<{tag}>"
            lis = []
            for item in list_buf:
                inner = format_inline(item["text"]) + render_subitems(item["subitems"])
                lis.append(f"<li>{inner}</li>")
            body_parts.append(f"{open_tag}{''.join(lis)}</{tag}>")
            list_buf = []
            list_type = None
            ol_start = 1

    def flush_quote():
        nonlocal quote_buf
        if quote_buf:
            q_html = "".join(f"<p>{format_inline(q)}</p>" for q in quote_buf)
            body_parts.append(f"<blockquote>{q_html}</blockquote>")
            quote_buf = []

    def flush_blocks():
        flush_table()
        flush_list()
        flush_quote()

    def close_module_card():
        nonlocal in_module_card
        flush_blocks()
        if in_module_card:
            body_parts.append("</div><!-- .module-card -->")
            in_module_card = False

    def close_section():
        nonlocal in_section
        close_module_card()
        if in_section:
            body_parts.append("</section>")
            in_section = False

    ch_counter = 0

    for raw_line in lines:
        stripped = raw_line.strip()
        indent = len(raw_line) - len(raw_line.lstrip(" "))

        # Hero header metadata before first ## section
        if in_hero:
            if stripped.startswith("# "):
                title = stripped[2:].strip()
                continue
            elif stripped.startswith("**") and stripped.endswith("**") and not subtitle:
                subtitle = stripped.strip("*").strip()
                continue
            elif stripped.startswith(">"):
                hero_meta_lines.append(stripped.lstrip(">").strip())
                continue
            elif stripped == "---" or stripped == "":
                continue
            elif stripped.startswith("## "):
                # Flush Hero header
                meta_html = "".join(f"<p>{format_inline(m)}</p>" for m in hero_meta_lines)
                body_parts.append(
                    f'<header class="hero-header">'
                    f'<span class="hero-kicker">woieyufan EDUCATION · 跨學科文明專書</span>'
                    f'<h1>{format_inline(title)}</h1>'
                    f'<p class="hero-subtitle">{format_inline(subtitle)}</p>'
                    f'<div class="hero-meta">{meta_html}</div>'
                    f'</header>'
                )
                in_hero = False
                # fall through to process this ## heading

        # Skip plain-text TOC in HTML (we build interactive sidebar TOC)
        if in_plain_toc:
            if stripped.startswith("## ") and ("目錄" not in stripped):
                in_plain_toc = False
            else:
                continue

        if stripped.startswith("## ") and ("目錄" in stripped or "全書架構導覽" in stripped):
            flush_blocks()
            in_plain_toc = True
            continue

        # Volume Banner (## 第一卷 ... )
        if re.match(r"^##\s+第[一二三四五六]卷", stripped):
            close_section()
            vol_text = stripped[3:].strip()
            vol_id = f"vol-{len(toc_items) + 1}"
            toc_items.append(("vol", vol_text))
            body_parts.append(
                f'<div class="volume-banner" id="{vol_id}">'
                f'<h2>{format_inline(vol_text)}</h2>'
                f'</div>'
            )
            continue

        # Chapter Heading (## 第 xx 章 ... or ## 結語 ...)
        if stripped.startswith("## "):
            close_section()
            heading_text = stripped[3:].strip()
            if heading_text.startswith("第") and "章" in heading_text:
                ch_counter += 1
                sec_id = f"ch-{ch_counter:02d}"
            elif "結語" in heading_text:
                sec_id = "epilogue"
            else:
                sec_id = f"sec-{len(toc_items) + 1}"
            toc_items.append(("ch", sec_id, heading_text))
            body_parts.append(f'<section class="chapter-section" id="{sec_id}">')
            body_parts.append(f'<h2 class="chapter-title">{format_inline(heading_text)}</h2>')
            in_section = True
            continue

        # IMPORTANT: Check #### BEFORE ### so #### subheadings stay inside module cards
        if stripped.startswith("#### "):
            flush_blocks()
            sub_text = stripped[5:].strip()
            body_parts.append(f'<h4 class="callout-subhead">{format_inline(sub_text)}</h4>')
            continue

        if stripped.startswith("### "):
            close_module_card()
            mod_text = stripped[4:].strip()
            mod_cls = classify_module(mod_text)
            cls_attr = f"module-card {mod_cls}".strip()
            body_parts.append(f'<div class="{cls_attr}">')
            body_parts.append(f'<h3 class="module-heading">{format_inline(mod_text)}</h3>')
            in_module_card = True
            continue

        # ASCII Fenced Blocks
        ascii_match = re.fullmatch(r"@@ASCIIBLOCK_(\d+)@@", stripped)
        if ascii_match:
            flush_blocks()
            idx = int(ascii_match.group(1))
            body_parts.append(f'<pre class="book-ascii">{ascii_blocks[idx]}</pre>')
            continue

        # Horizontal Rule
        if stripped == "---":
            flush_blocks()
            continue

        # Tables
        if stripped.startswith("|") and stripped.endswith("|"):
            flush_list()
            flush_quote()
            table_buf.append(stripped)
            continue
        else:
            flush_table()

        # Blockquotes
        if stripped.startswith(">"):
            flush_list()
            quote_buf.append(stripped.lstrip(">").strip())
            continue
        else:
            flush_quote()

        # List Items (Unordered and Ordered, including nested indented subitems)
        ul_match = re.match(r"^[-*]\s+(.*)$", stripped)
        ol_match = re.match(r"^(\d+)\.\s+(.*)$", stripped)
        if ul_match or ol_match:
            item_tag = "ul" if ul_match else "ol"
            item_text = ul_match.group(1).strip() if ul_match else ol_match.group(2).strip()
            if indent >= 2 and list_buf:
                list_buf[-1]["subitems"].append((indent, item_tag, item_text))
                continue
            if list_type and list_type != item_tag:
                flush_list()
            if item_tag == "ol" and not list_buf:
                ol_start = int(ol_match.group(1))
            list_type = item_tag
            list_buf.append({"text": item_text, "subitems": []})
            continue

        # Empty Line
        if stripped == "":
            flush_blocks()
            continue

        # Regular Paragraph
        flush_blocks()
        body_parts.append(f"<p>{format_inline(stripped)}</p>")

    close_section()

    # Build Sidebar Navigation HTML
    sidebar_parts = [
        '<aside class="sidebar" id="sidebarNav">',
        '  <div class="sidebar-brand">',
        '    <div class="tag">woieyufan EDUCATION</div>',
        '    <h1>文化中的數理</h1>',
        '    <p>生活與新聞中的文明密碼（37 章全本）</p>',
        '  </div>',
        '  <nav aria-label="章節目錄">',
    ]
    for item in toc_items:
        if item[0] == "vol":
            sidebar_parts.append(f'    <div class="toc-vol-label">{format_inline(item[1])}</div>')
        else:
            _, sec_id, label = item
            sidebar_parts.append(f'    <a class="toc-link" href="#{sec_id}">{format_inline(label)}</a>')
    sidebar_parts.append("  </nav>")
    sidebar_parts.append("</aside>")
    sidebar_parts.append('<main class="main-content">')
    sidebar_parts.append('  <div class="book-container">')

    full_html = HTML_HEAD + "\n".join(sidebar_parts) + "\n" + "\n".join(body_parts) + HTML_FOOTER
    full_html = restore_math_tokens(full_html, math_tokens)
    return full_html, ch_counter


def validate_artifacts(md_text, html_text):
    """Run automated structural and mathematical syntax validation."""
    errors = []

    # 1. Check display math balance in Markdown
    open_disp = len(re.findall(r"(?m)^\\\[\s*$", md_text))
    close_disp = len(re.findall(r"(?m)^\\\]\s*$", md_text))
    if open_disp != close_disp:
        errors.append(f"Display math \\[ ({open_disp}) != \\] ({close_disp})")

    # Check inline $ balance per non-code line
    in_code = False
    for lineno, line in enumerate(md_text.splitlines(), 1):
        if line.strip().startswith("```"):
            in_code = not in_code
            continue
        if in_code:
            continue
        unescaped_dollars = re.findall(r"(?<!\\)\$", line)
        if len(unescaped_dollars) % 2 != 0:
            errors.append(f"Unbalanced inline $ at line {lineno}: {line[:80]}")

    # 2. Check chapter headings 01..37
    ch_matches = re.findall(r"^##\s+第\s*(\d+)\s*章", md_text, flags=re.MULTILINE)
    nums = [int(x) for x in ch_matches]
    if nums != list(range(1, 38)):
        errors.append(f"Chapter numbering mismatch: found {nums}")

    # 3. Check all 37 chapters have all 4 standard modules and no tables inside exercise module
    chapter_chunks = re.split(r"(?m)^##\s+第\s*\d+\s*章", md_text)[1:]
    if len(chapter_chunks) == 37:
        # Strip trailing epilogue from ch 37 chunk
        chapter_chunks[-1] = re.split(r"(?m)^##\s+結語", chapter_chunks[-1])[0]
        for idx, chunk in enumerate(chapter_chunks, 1):
            for kw in ["新聞與生活", "文明故事", "核心數理", "動手算術"]:
                if kw not in chunk:
                    errors.append(f"Chapter {idx:02d} missing module keyword: {kw}")
            ex_split = re.split(r"(?m)^###\s+.*動手算術", chunk)
            if len(ex_split) > 1:
                if "|" in ex_split[1] and re.search(r"(?m)^\|.*\|$", ex_split[1]):
                    errors.append(f"Chapter {idx:02d} contains table inside exercise module")

    # 4. HTML checks
    if "@@MATHTOKEN" in html_text or "@@ASCIIBLOCK" in html_text or "@@CODESPAN" in html_text:
        errors.append("Residual internal placeholder token found in compiled HTML")

    sec_open = len(re.findall(r'<section class="chapter-section"', html_text))
    sec_close = len(re.findall(r"</section>", html_text))
    if sec_open != 38 or sec_close != 38:
        errors.append(f"Expected 38 <section> pairs, got open={sec_open}, close={sec_close}")

    subheads = len(re.findall(r'<h4 class="callout-subhead">', html_text))

    # Strip <style>, <script>, <pre> before checking for leaked ** or ##
    stripped_html = re.sub(r"<(style|script|pre)[\s\S]*?</\1>", "", html_text)
    if "**" in stripped_html:
        errors.append("Leaked raw Markdown '**' in HTML body")
    if re.search(r"(?m)^#{1,4}\s", stripped_html):
        errors.append("Leaked raw Markdown '#' heading in HTML body")

    return errors, open_disp, subheads, sec_open


def compile_pdf_if_requested():
    chrome_paths = [
        shutil.which("google-chrome"),
        shutil.which("chromium"),
        shutil.which("chromium-browser"),
        "/usr/bin/google-chrome",
        "/usr/bin/chromium",
        "/usr/bin/chromium-browser",
    ]
    chrome_bin = next((p for p in chrome_paths if p and os.path.exists(p)), None)
    if not chrome_bin:
        print("Error: Chrome / Chromium not found for --pdf compilation.")
        return False
    cmd = [
        chrome_bin,
        "--headless",
        "--disable-gpu",
        "--no-sandbox",
        f"--print-to-pdf={OUTPUT_PDF}",
        f"file://{OUTPUT_HTML}",
    ]
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode != 0:
        print("Chrome PDF compilation error:", res.stderr)
        return False
    print(f"PDF generated at: {OUTPUT_PDF}")
    return True


def main():
    if not os.path.exists(INPUT_MD):
        print(f"Error: Input Markdown not found at {INPUT_MD}")
        sys.exit(1)

    with open(INPUT_MD, "r", encoding="utf-8") as f:
        md_text = f.read()

    html_text, ch_count = markdown_to_html_book(md_text)
    errors, disp_count, subhead_count, sec_count = validate_artifacts(md_text, html_text)

    if errors:
        print("Validation Errors Detected:")
        for e in errors:
            print("  -", e)
        sys.exit(1)

    with open(OUTPUT_HTML, "w", encoding="utf-8") as f:
        f.write(html_text)

    size_bytes = os.path.getsize(OUTPUT_HTML)
    print(f"[OK] Compiled {OUTPUT_HTML} ({size_bytes:,} bytes)")
    print(f"     Chapters: {ch_count} | Sections: {sec_count} | Display Math Pairs: {disp_count} | Subheads (h4): {subhead_count}")

    if "--pdf" in sys.argv:
        ok = compile_pdf_if_requested()
        if not ok:
            sys.exit(1)
    else:
        print("[PDF Skipped] 全域設定：預設不主動生成 PDF。僅輸出 HTML。若明確需要 PDF，請傳入 --pdf 參數。")


if __name__ == "__main__":
    main()
