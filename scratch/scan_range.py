import zlib
import os

history_path = r"C:\Users\Bolokaiemi\AppData\Local\JetBrains\PyCharm2025.2\LocalHistory\changes.storageData"

def main():
    if not os.path.exists(history_path):
        print("History file not found.")
        return
        
    with open(history_path, "rb") as f:
        data = f.read()
    print("Loaded history size:", len(data))
    
    # Scan byte-by-byte from 2215000 to 2216500
    found = False
    for i in range(2214500, min(len(data), 2216500)):
        try:
            dec = zlib.decompressobj(-15)
            decompressed = dec.decompress(data[i:i+50000])
            if len(decompressed) > 1000:
                text = decompressed.decode('utf-8', errors='ignore')
                if "<!DOCTYPE html>" in text:
                    print(f"FOUND at offset {i} (len={len(decompressed)}):")
                    print("  Snippet:", repr(text[:150]))
                    found = True
                    # Let's save it
                    with open("scratch/test_scan_range.html", "w", encoding="utf-8") as out:
                        out.write(text)
                    print("  Saved to scratch/test_scan_range.html")
                    break
        except Exception:
            pass
            
    if not found:
        print("No valid raw deflate block found in the range.")

if __name__ == '__main__':
    main()
