import os
import re

history_path = r"C:\Users\Bolokaiemi\AppData\Local\JetBrains\PyCharm2025.2\LocalHistory\changes.storageData"
output_dir = r"c:\Users\Bolokaiemi\PycharmProjects\mobileuserinterfaceProject6\scratch\recovered"

os.makedirs(output_dir, exist_ok=True)

def clean_and_decode(candidate):
    # Decode until we hit a null byte or a sequence of non-printable bytes
    decoded = []
    for val in candidate:
        if val == 0:
            break
        # Allow printable characters and standard whitespace (tab, LF, CR)
        if 32 <= val < 127 or val in [9, 10, 13]:
            decoded.append(chr(val))
        else:
            # Non-printable character, stop decoding
            break
    return "".join(decoded)

def extract_file_versions(search_str, file_start_str, file_prefix):
    print(f"\nSearching for '{search_str}' (start marker: {repr(file_start_str)})...")
    if not os.path.exists(history_path):
        print("History file not found.")
        return
        
    with open(history_path, "rb") as f:
        data = f.read()
        
    search_bytes = search_str.encode('utf-8')
    indices = [m.start() for m in re.finditer(re.escape(search_bytes), data)]
    print(f"Found {len(indices)} occurrences.")
    
    version_idx = 1
    seen_contents = set()
    
    for idx in reversed(indices):
        # PyCharm stores chunks of files. Scan backwards to find the file start.
        # We start looking up to 60000 bytes back.
        chunk_start = max(0, idx - 80000)
        chunk_end = min(len(data), idx + 200000)
        chunk = data[chunk_start:chunk_end]
        
        # Search backwards from the match position inside the chunk
        file_start_pos = chunk.rfind(file_start_str.encode('utf-8'), 0, idx - chunk_start)
        if file_start_pos != -1:
            candidate = chunk[file_start_pos:]
            decoded = clean_and_decode(candidate)
            
            if len(decoded) > 1000:
                # Remove duplicate versions
                normalized = decoded.strip()
                if normalized not in seen_contents:
                    seen_contents.add(normalized)
                    out_name = f"{file_prefix}_v{version_idx}.txt"
                    out_path = os.path.join(output_dir, out_name)
                    with open(out_path, "w", encoding="utf-8") as out_f:
                        out_f.write(decoded)
                    print(f"  Saved version {version_idx} (len={len(decoded)}) to {out_name}")
                    version_idx += 1

def main():
    # 1. index.html
    # Start of index.html: "<!DOCTYPE html>"
    # Search string: "+491793264196" (added at 6:47 AM)
    extract_file_versions("Herne, Germany", "<!DOCTYPE html>", "index_html")
    
    # 2. templates/index.html
    # Same as index.html but maybe different path. In JetBrains history, it stores raw content.
    # The search string "+491793264196" should find index.html versions, both static and template.
    
    # 3. app.js
    # Start: "/*" or "document.addEventListener"
    # Search: "userBookingsList" or "loadMilestones"
    extract_file_versions("userBookingsList", "document.addEventListener", "app_js")
    
    # 4. app.py
    # Start: "import " or "from flask"
    # Search: "def book_lesson():"
    extract_file_versions("def book_lesson():", "from flask import", "app_py")
    
    # 5. static/styles.css
    # Start: "/*" or ":root"
    # Search: ".zoom-lessons-card"
    extract_file_versions(".zoom-lessons-card", ":root", "styles_css")

if __name__ == "__main__":
    main()
