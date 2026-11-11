# 全域設定與專案開發規範 (Global Project Rules)

## 核心規則：禁止主動生成 PDF (Do Not Proactively Generate PDF)
1. **全域原則**：在任何情境下，**不得主動生成、編譯或列印 PDF 文件**。
2. **預設輸出格式**：白皮書、手冊、專案文件或圖表等所有交付物，預設僅生成 **HTML**、**Markdown** 或原始程式碼。
3. **PDF 生成之嚴格例外**：只有在使用者發出**明確的指令**要求產出 PDF（例如直接提出「請生成 PDF」、「編譯為 PDF」或指定 `--pdf` 參數）時，才允許執行 PDF 編譯流程（如 Headless Chrome 列印或 PyMuPDF 處理）。
4. **編譯腳本規範**：所有構建與排版腳本預設均僅輸出 HTML，只有在明確傳入 `--pdf` 等顯式旗標時方可調用 PDF 生成模組。
