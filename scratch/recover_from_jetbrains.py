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
    
    found_html = []
    found_css = []
    
    # We will scan byte-by-byte. To make it fast, we can search for blocks that decompress.
    # We will try both standard zlib header decomp and raw deflate (wbits = -15)
    print("Scanning for compressed blocks...")
    i = 0
    total_len = len(data)
    
    # We skip to save time if we know typical offsets, but byte-by-byte is thorough.
    # To optimize, we check for potential starting bytes or try every byte.
    # Since the file is only 2.8 MB, scanning byte-by-byte takes only a few seconds in Python if done efficiently.
    while i < total_len - 10:
        # Check standard and raw deflate
        for wbits in [15, -15]:
            try:
                # Limit input data to avoid reading too much
                dec = zlib.decompressobj(wbits)
                decompressed = dec.decompress(data[i:i+150000])
                
                if len(decompressed) > 5000:
                    try:
                        text = decompressed.decode('utf-8')
                        
                        # Check index.html keywords
                        if "<!DOCTYPE html>" in text and "+491793264196" in text:
                            found_html.append((i, wbits, text))
                        # Check styles.css keywords
                        if "custom-scrollbar" in text or ".hero-title" in text:
                            if "designed by: bolokaiemi ebi" in text.lower():
                                found_css.append((i, wbits, text))
                    except UnicodeDecodeError:
                        pass
                    
                    # Skip past the processed bytes
                    used_bytes = len(data[i:i+150000]) - len(dec.unused_data)
                    i += max(1, used_bytes)
                    break
            except Exception:
                pass
        i += 1
        
    print(f"\nScan finished. Found {len(found_html)} versions of index.html and {len(found_css)} versions of styles.css.")
    
    # Save HTML versions
    for idx, (pos, wbits, text) in enumerate(found_html):
        out_path = os.path.join(output_dir, f"recovered_index_html_v{idx+1}.html")
        with open(out_path, "w", encoding="utf-8") as out_f:
            out_f.write(text)
        print(f"Saved index.html version {idx+1} (offset={pos}, wbits={wbits}, len={len(text)}) to {os.path.basename(out_path)}")
        
    # Save CSS versions
    for idx, (pos, wbits, text) in enumerate(found_css):
        out_path = os.path.join(output_dir, f"recovered_styles_v{idx+1}.css")
        with open(out_path, "w", encoding="utf-8") as out_f:
            out_f.write(text)
        print(f"Saved styles.css version {idx+1} (offset={pos}, wbits={wbits}, len={len(text)}) to {os.path.basename(out_path)}")

if __name__ == "__main__":
    main()
