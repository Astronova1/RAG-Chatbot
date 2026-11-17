import pathlib
import re
import tiktoken
def chunker_markdown_text(mdtext: str, source_name: str, chunk_size= 300) -> list[str]:
    chunks= []
    raw_chunks = re.split(r'(?m)^(?=#)',mdtext)  # Split on lines that start with a '#'
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
        length = count_token(result, "o200k_base")  # Count tokens for the chunk
        if length > chunk_size:
           print(f"Chunk exceeds {chunk_size} tokens, length: {length}. Consider splitting further.")
        print(length)
        print(result)
        chunks.append(result)
    return chunks

def count_token(text: str, model_name: str) -> int:
    encoding = tiktoken.get_encoding(model_name)
    num_tokens = len(encoding.encode(text))
    return num_tokens



chunker_markdown_text(pathlib.Path("Fy26_Q3.md").read_text(), "FY26_Q3_Consolidated_Financial_Statements.pdf")