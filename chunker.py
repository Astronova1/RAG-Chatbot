import pathlib
import re
def chunker_markdown_text(mdtext: str, source_name: str, chunk_size= 300) -> list[str]:
    chunks= []
    raw_chunks = re.split(r'(?m)^(?=#)',mdtext)
    print("Number of raw chunks:", len(raw_chunks))
    for raw_chunk in raw_chunks:
        if not raw_chunk.strip() or raw_chunk.startswith('**A'):
            continue
        lines = raw_chunk.splitlines()
        cleaned_lines = []
        for line in lines[1:]:
            if line.strip() and not line.startswith('**Apple Inc.**'):
                cleaned_lines.append(line.strip())
        title = lines[0].strip(' *#') if cleaned_lines else "No title found"
        result = '\n'.join(cleaned_lines)
        contextual_metadata = f"Source: {source_name}\nTitle: {title}\n"
        result = contextual_metadata + result
        print(result)
        chunks.append(result)
    return chunks

chunker_markdown_text(pathlib.Path("Fy26_Q3.md").read_text(), "FY26_Q3_Consolidated_Financial_Statements.pdf")