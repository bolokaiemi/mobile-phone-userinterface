import zlib
import os

history_path = r"C:\Users\Bolokaiemi\AppData\Local\JetBrains\PyCharm2025.2\LocalHistory\changes.storageData"
output_dir = r"c:\Users\Bolokaiemi\PycharmProjects\mobileuserinterfaceProject6\scratch\recovered_new"
os.makedirs(output_dir, exist_ok=True)

def main():
    if not os.path.exists(history_path):
        print("History file not found.")
        return
        
    with open(history_path, "rb") as f:
        data = f.read()
    print(f"Loaded {len(data)} bytes. Scanning with raw deflate...")
    
    found_html = 0
    found_js = 0
    found_py = 0
    found_css = 0
    
    i = 0
    total_len = len(data)
    while i < total_len - 100:
        try:
            # Try raw deflate (wbits = -15)
            dec = zlib.decompressobj(-15)
            decompressed = dec.decompress(data[i:i+100000])
            
            if len(decompressed) > 1000:
                try:
                    text = decompressed.decode('utf-8')
                    if "<!DOCTYPE html>" in text and "Student Learning Portal" in text:
                        found_html += 1
                        out_path = os.path.join(output_dir, f"raw_index_{found_html}.html")
                        with open(out_path, "w", encoding="utf-8") as out_f:
                            out_f.write(text)
                        
                    elif "studentAuthWrapper" in text or "renderBookingsUI" in text:
                        found_js += 1
                        out_path = os.path.join(output_dir, f"raw_app_{found_js}.js")
                        with open(out_path, "w", encoding="utf-8") as out_f:
                            out_f.write(text)
                        
                    elif "def book_lesson" in text:
                        found_py += 1
                        out_path = os.path.join(output_dir, f"raw_app_{found_py}.py")
                        with open(out_path, "w", encoding="utf-8") as out_f:
                            out_f.write(text)
                        
                    elif ".hero-section" in text or "custom-scrollbar" in text:
                        found_css += 1
                        out_path = os.path.join(output_dir, f"raw_styles_{found_css}.css")
                        with open(out_path, "w", encoding="utf-8") as out_f:
                            out_f.write(text)
                        
                    used = len(data[i:i+100000]) - len(dec.unused_data)
                    i += max(1, used)
                    continue
                except UnicodeDecodeError:
                    pass
        except Exception:
            pass
        i += 1
        
    print(f"Scan complete. Found: HTML={found_html}, JS={found_js}, PY={found_py}, CSS={found_css}")
    print("Files in recovered_new folder:", os.listdir(output_dir))

if __name__ == '__main__':
    main()
