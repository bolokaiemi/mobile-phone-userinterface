import zlib
import os

history_path = r"C:\Users\Bolokaiemi\AppData\Local\JetBrains\PyCharm2025.2\LocalHistory\changes.storageData"

def main():
    if not os.path.exists(history_path):
        print("History file not found.")
        return
        
    with open(history_path, "rb") as f:
        data = f.read()
    print(f"Loaded {len(data)} bytes. Scanning all decompressed blocks...")
    
    found_count = 0
    i = 0
    total_len = len(data)
    while i < total_len - 10:
        # Check standard and raw deflate
        for wbits in [15, -15]:
            try:
                dec = zlib.decompressobj(wbits)
                decompressed = dec.decompress(data[i:i+50000])
                if len(decompressed) > 500:
                    text = decompressed.decode('utf-8')
                    found_count += 1
                    print(f"\nMatch {found_count} at offset {i} (wbits={wbits}, len={len(decompressed)}):")
                    print("  Snippet:", repr(text[:120]))
                    
                    # Skip the decompressed bytes
                    used = len(data[i:i+50000]) - len(dec.unused_data)
                    i += max(1, used)
                    break
            except Exception:
                pass
        i += 1
        
    print(f"\nScan complete. Found {found_count} blocks.")

if __name__ == '__main__':
    main()
