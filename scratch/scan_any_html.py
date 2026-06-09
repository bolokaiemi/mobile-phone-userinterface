import zlib
import os

history_path = r"C:\Users\Bolokaiemi\AppData\Local\JetBrains\PyCharm2025.2\LocalHistory\changes.storageData"

def main():
    if not os.path.exists(history_path):
        print("History file not found.")
        return
        
    with open(history_path, "rb") as f:
        data = f.read()
    print(f"Loaded {len(data)} bytes. Scanning for any HTML blocks...")
    
    found_count = 0
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
                    if "<!DOCTYPE html>" in text:
                        found_count += 1
                        print(f"Match {found_count} at offset {i} (len={len(decompressed)}):")
                        # Print terms presence
                        has_student = "student" in text.lower()
                        has_learning = "learning" in text.lower()
                        has_portal = "portal" in text.lower()
                        print(f"  Snippet: {repr(text[:150])}")
                        print(f"  Keywords present: student={has_student}, learning={has_learning}, portal={has_portal}")
                        
                        # Save the first match to see it
                        out_path = f"scratch/recovered_html_{found_count}.html"
                        with open(out_path, "w", encoding="utf-8") as out_f:
                            out_f.write(text)
                        print(f"  Saved to {out_path}")
                        
                        used = len(data[i:i+100000]) - len(dec.unused_data)
                        i += max(1, used)
                        continue
                except UnicodeDecodeError:
                    pass
        except Exception:
            pass
        i += 1
        
    print(f"\nScan complete. Found {found_count} HTML blocks.")

if __name__ == '__main__':
    main()
