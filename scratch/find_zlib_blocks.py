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
    
    # We will look for zlib header 0x78 0x9c (default compression)
    # or other zlib headers (0x78 0x01, 0x78 0xda)
    headers = [b'\x78\x9c', b'\x78\x01', b'\x78\xda']
    
    found_app_py = []
    found_app_js = []
    
    # We will scan byte-by-byte
    print("Scanning for zlib compressed blocks...")
    i = 0
    while i < len(data) - 2:
        # Check if current 2 bytes are a zlib header
        if data[i:i+2] in headers:
            # Try to decompress from this position
            try:
                # Using decompressobj allows us to decompress without knowing the exact length
                dec = zlib.decompressobj()
                decompressed = dec.decompress(data[i:])
                
                # Check if we got something
                if len(decompressed) > 1000:
                    try:
                        text = decompressed.decode('utf-8')
                        
                        # Check keywords
                        if "def book_lesson():" in text or "book_lesson" in text:
                            # It's app.py!
                            found_app_py.append((i, text))
                        if "STUDENT PORTAL AUTH STATUS" in text or "zoomLessonsCard" in text:
                            # It's app.js!
                            found_app_js.append((i, text))
                    except UnicodeDecodeError:
                        pass
                
                # Skip past the processed bytes to speed up
                used_bytes = len(data[i:]) - len(dec.unused_data)
                i += max(1, used_bytes)
                continue
            except Exception:
                pass
        i += 1
        
    print(f"\nScan finished. Found {len(found_app_py)} versions of app.py and {len(found_app_js)} versions of app.js.")
    
    # Save versions
    for idx, (pos, text) in enumerate(found_app_py):
        out_path = os.path.join(output_dir, f"app_py_rec_{idx+1}.py")
        with open(out_path, "w", encoding="utf-8") as out_f:
            out_f.write(text)
        print(f"Saved app.py version {idx+1} (offset={pos}, len={len(text)}) to {out_path}")
        
    for idx, (pos, text) in enumerate(found_app_js):
        out_path = os.path.join(output_dir, f"app_js_rec_{idx+1}.js")
        with open(out_path, "w", encoding="utf-8") as out_f:
            out_f.write(text)
        print(f"Saved app.js version {idx+1} (offset={pos}, len={len(text)}) to {out_path}")

if __name__ == "__main__":
    main()
