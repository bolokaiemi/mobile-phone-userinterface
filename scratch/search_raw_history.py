import os

history_path = r"C:\Users\Bolokaiemi\AppData\Local\JetBrains\PyCharm2025.2\LocalHistory\changes.storageData"

def main():
    if not os.path.exists(history_path):
        print("History file not found")
        return
        
    with open(history_path, "rb") as f:
        data = f.read()
        
    print(f"Total history file size: {len(data)} bytes")
    
    # Try searching for some basic keywords
    keywords = [b"bolokaiemi", b"Ebi", b"student", b"html", b"port", b"styles", b"app"]
    for kw in keywords:
        pos = data.find(kw)
        print(f"Keyword '{kw.decode()}' found at pos: {pos}")
        if pos != -1:
            # print surrounding bytes
            start = max(0, pos - 20)
            end = min(len(data), pos + 50)
            print("  Surrounding hex:", data[start:end].hex())
            print("  Surrounding ASCII:", repr(data[start:end]))

if __name__ == '__main__':
    main()
