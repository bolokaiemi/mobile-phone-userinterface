import zlib
import os

history_path = r"C:\Users\Bolokaiemi\AppData\Local\JetBrains\PyCharm2025.2\LocalHistory\changes.storageData"
output_dir = r"c:\Users\Bolokaiemi\PycharmProjects\mobileuserinterfaceProject6\scratch\recovered"
os.makedirs(output_dir, exist_ok=True)

def main():
    if not os.path.exists(history_path):
        print("History file not found.")
        return
        
    print(f"Reading history file {history_path}...")
    with open(history_path, "rb") as f:
        data = f.read()
    print(f"File read. Total size: {len(data)} bytes.")
    
    headers = [b'\x78\x9c', b'\x78\x01', b'\x78\xda']
    
    found_app_py = []
    found_app_js = []
    found_index_html = []
    found_styles_css = []
    
    print("Scanning for zlib compressed blocks...")
    i = 0
    while i < len(data) - 2:
        if data[i:i+2] in headers:
            try:
                dec = zlib.decompressobj()
                decompressed = dec.decompress(data[i:])
                
                if len(decompressed) > 1000:
                    try:
                        text = decompressed.decode('utf-8')
                        
                        # Identify file type based on contents
                        if "def book_lesson" in text:
                            found_app_py.append((i, text))
                        elif "studentAuthWrapper" in text or "renderBookingsUI" in text:
                            found_app_js.append((i, text))
                        elif "<!DOCTYPE html>" in text and "Student Learning Portal" in text:
                            found_index_html.append((i, text))
                        elif "custom-scrollbar" in text or ".hero-section" in text:
                            found_styles_css.append((i, text))
                    except UnicodeDecodeError:
                        pass
                
                # Skip processed bytes
                used_bytes = len(data[i:]) - len(dec.unused_data)
                i += max(1, used_bytes)
                continue
            except Exception:
                pass
        i += 1
        
    print(f"\nScan finished.")
    print(f"Found {len(found_app_py)} versions of app.py")
    print(f"Found {len(found_app_js)} versions of app.js")
    print(f"Found {len(found_index_html)} versions of index.html")
    print(f"Found {len(found_styles_css)} versions of styles.css")
    
    # Save versions
    for idx, (pos, text) in enumerate(found_app_py):
        out_path = os.path.join(output_dir, f"recovered_app_{idx+1}.py")
        with open(out_path, "w", encoding="utf-8") as out_f:
            out_f.write(text)
        print(f"Saved app.py v{idx+1} (offset={pos}, len={len(text)})")
        
    for idx, (pos, text) in enumerate(found_app_js):
        out_path = os.path.join(output_dir, f"recovered_app_{idx+1}.js")
        with open(out_path, "w", encoding="utf-8") as out_f:
            out_f.write(text)
        print(f"Saved app.js v{idx+1} (offset={pos}, len={len(text)})")
        
    for idx, (pos, text) in enumerate(found_index_html):
        out_path = os.path.join(output_dir, f"recovered_index_{idx+1}.html")
        with open(out_path, "w", encoding="utf-8") as out_f:
            out_f.write(text)
        print(f"Saved index.html v{idx+1} (offset={pos}, len={len(text)})")
        
    for idx, (pos, text) in enumerate(found_styles_css):
        out_path = os.path.join(output_dir, f"recovered_styles_{idx+1}.css")
        with open(out_path, "w", encoding="utf-8") as out_f:
            out_f.write(text)
        print(f"Saved styles.css v{idx+1} (offset={pos}, len={len(text)})")

if __name__ == "__main__":
    main()
