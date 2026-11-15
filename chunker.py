import pathlib
import re
def chunker_markdown_text(mdtext: str, source_name: str, chunk_size= 300) -> list[str]:
    chunks= []
    raw_chunks = re.split(r'(?m)^(?=#)',mdtext)
    for raw_chunk in raw_chunks:
        if not raw_chunk.strip() or raw_chunk.startswith('**A'):
            continue
        raw_chunk = raw_chunk.splitlines()
        cleaned_title = []
        for line in raw_chunk:
            if line.strip():
                cleaned_title.append(line.strip(' #*'))

        title = cleaned_title[0] if cleaned_title else "No title found"
        print("TItle is", title)
        print(raw_chunk)

chunker_markdown_text(pathlib.Path("Fy26_Q3.md").read_text(), "FY26_Q3_Consolidated_Financial_Statements.pdf")