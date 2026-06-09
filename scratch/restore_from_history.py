import os
import re

history_path = r"C:\Users\Bolokaiemi\AppData\Local\JetBrains\PyCharm2025.2\LocalHistory\changes.storageData"
output_dir = r"c:\Users\Bolokaiemi\PycharmProjects\mobileuserinterfaceProject6\scratch"

def extract_file(search_str, output_filename, max_len=160000):
    print(f"Searching for '{search_str}' in PyCharm Local History...")
    if not os.path.exists(history_path):
        print("[ERROR] Local History file not found.")
        return
        
    with open(history_path, "rb") as f:
        data = f.read()
        
    # Find all occurrences of the search string in the binary file
    search_bytes = search_str.encode('utf-8')
    indices = [m.start() for m in re.finditer(re.escape(search_bytes), data)]
    
    print(f"Found {len(indices)} occurrences.")
    
    # For each index, extract the surrounding text block.
    # PyCharm stores history as raw file contents in chunks. We can look for the beginning and end of Python/JS files.
    # A Python file typically starts with imports or comments.
    # A JS file typically starts with comments or document.ready.
    # Let's extract blocks of size max_len around the index and see if they look like valid files.
    
    best_block = None
    best_score = 0
    
    for idx in reversed(indices):
        # Scan backwards to find the start of the block.
        # We can look for some null bytes or non-printable characters which demarcate blocks,
        # or just look for the typical start of our file.
        start_idx = max(0, idx - 40000)
        end_idx = min(len(data), idx + 120000)
        
        chunk = data[start_idx:end_idx]
        
        # Try to find a valid utf-8 string around the index
        # Let's search from the match index backwards for the start of the file:
        # e.g., for app.py: "from flask import"
        # for app.js: "/*\n   Android 14 EbiUI" or similar
        file_start_str = b"from flask import" if "app.py" in output_filename else b"document.addEventListener"
        
        file_start_pos = chunk.rfind(file_start_str, 0, idx - start_idx)
        if file_start_pos != -1:
            # We found a candidate start!
            # Now let's try to decode from this start forward.
            candidate = chunk[file_start_pos:]
            # Find the end of the text. We scan forward until we hit a null byte or non-printable character.
            # Or we can just decode it as utf-8 (ignoring errors or stopping at the first block boundaries).
            decoded = ""
            for i in range(len(candidate)):
                val = candidate[i]
                if val == 0 or (val < 32 and val not in [9, 10, 13]):
                    # End of text block!
                    break
                decoded += chr(val)
                
            if len(decoded) > best_score:
                best_score = len(decoded)
                best_block = decoded
                print(f"Found candidate of length {len(decoded)} starting with: {repr(decoded[:50])}")
                
    if best_block:
        out_path = os.path.join(output_dir, output_filename)
        with open(out_path, "w", encoding="utf-8") as out:
            out.write(best_block)
        print(f"[SUCCESS] Wrote recovered file to {out_path} (length {len(best_block)} chars).")
    else:
        print("[ERROR] Could not extract clean file block.")

def main():
    # Recover app.py
    extract_file("def book_lesson():", "recovered_app.py")
    
    # Recover app.js
    extract_file("STUDENT PORTAL AUTH STATUS & ROUTING", "recovered_app.js")

if __name__ == "__main__":
    main()
