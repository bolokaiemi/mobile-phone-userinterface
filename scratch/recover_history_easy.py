import zlib
import os

history_path = r"C:\Users\Bolokaiemi\AppData\Local\JetBrains\PyCharm2025.2\LocalHistory\changes.storageData"
output_dir = r"c:\Users\Bolokaiemi\PycharmProjects\mobileuserinterfaceProject6\scratch\recovered_easy"
os.makedirs(output_dir, exist_ok=True)

def main():
    if not os.path.exists(history_path):
        print("History file not found.")
        return
        
    print(f"Reading history file...")
    with open(history_path, "rb") as f:
        data = f.read()
    
    found_html = []
    found_css = []
    
    print("Scanning for compressed blocks...")
    i = 0
    total_len = len(data)
    
    while i < total_len - 10:
        for wbits in [15, -15]:
            try:
                dec = zlib.decompressobj(wbits)
                decompressed = dec.decompress(data[i:i+120000])
                
                if len(decompressed) > 5000:
                    try:
                        text = decompressed.decode('utf-8')
                        
                        # index.html check
                        # It must contain zoom-lessons-card and a typical html tag
                        if "<!DOCTYPE html>" in text and "zoom-lessons-card" in text:
                            found_html.append((i, wbits, text))
                            
                        # styles.css check
                        # It must contain zoom-lessons-card and css style rules
                        if ".zoom-lessons-card" in text and ".hub-footer" in text:
                            # Avoid html files matching this
                            if "<!DOCTYPE html>" not in text and "<html" not in text:
                                found_css.append((i, wbits, text))
                    except UnicodeDecodeError:
                        pass
                    
                    used_bytes = len(data[i:i+120000]) - len(dec.unused_data)
                    i += max(1, used_bytes)
                    break
            except Exception:
                pass
        i += 1
        
    print(f"\nScan finished. Found {len(found_html)} HTML versions and {len(found_css)} CSS versions.")
    
    # Save HTML versions
    for idx, (pos, wbits, text) in enumerate(found_html):
        out_name = f"recovered_index_{idx+1}.html"
        out_path = os.path.join(output_dir, out_name)
        with open(out_path, "w", encoding="utf-8") as out_f:
            out_f.write(text)
        print(f"  Saved HTML version {idx+1} (offset={pos}, len={len(text)}) to {out_name}")
        
    # Save CSS versions
    for idx, (pos, wbits, text) in enumerate(found_css):
        out_name = f"recovered_styles_{idx+1}.css"
        out_path = os.path.join(output_dir, out_name)
        with open(out_path, "w", encoding="utf-8") as out_f:
            out_f.write(text)
        print(f"  Saved CSS version {idx+1} (offset={pos}, len={len(text)}) to {out_name}")

if __name__ == "__main__":
    main()
