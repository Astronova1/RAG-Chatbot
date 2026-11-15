import pathlib, pymupdf
doc = pymupdf.open("FY26_Q3_Consolidated_Financial_Statements.pdf")
markdown_text = doc.to_markdown()
pathlib.Path("Fy26_Q3.md").write_text(markdown_text)