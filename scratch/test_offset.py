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
    
    offsets = [2215286, 1273934, 24834, 2183428]
    for offset in offsets:
        if offset < len(data):
            print(f"\nTrying offset {offset}:")
            try:
                dec = zlib.decompressobj(-15)
                decompressed = dec.decompress(data[offset:offset+100000])
                print("  Decompressed length:", len(decompressed))
                text = decompressed.decode('utf-8', errors='ignore')
                print("  Snippet:", repr(text[:200]))
            except Exception as e:
                print("  Error:", e)
        else:
            print(f"\nOffset {offset} is out of bounds (file size {len(data)})")

if __name__ == '__main__':
    main()
