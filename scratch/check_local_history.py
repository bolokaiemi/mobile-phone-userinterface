import os

def main():
    paths = [
        r"C:\Users\Bolokaiemi\AppData\Local\JetBrains\PyCharm2025.2\LocalHistory\changes.storageData",
        r"C:\Users\Bolokaiemi\AppData\Local\JetBrains\PyCharm2025.1\LocalHistory\changes.storageData",
        r"C:\Users\Bolokaiemi\AppData\Local\JetBrains\PyCharm2026.1\LocalHistory\changes.storageData",
        r"C:\Users\Bolokaiemi\AppData\Local\JetBrains\PyCharm2024.3\LocalHistory\changes.storageData"
    ]
    for p in paths:
        if os.path.exists(p):
            print(f"FOUND: {p} ({os.path.getsize(p) / 1024 / 1024:.2f} MB)")
        else:
            print(f"NOT FOUND: {p}")
            
    # Also list directory in AppData\Local\JetBrains
    jb_dir = r"C:\Users\Bolokaiemi\AppData\Local\JetBrains"
    if os.path.exists(jb_dir):
        print("\nListing JetBrains folder:")
        try:
            for item in os.listdir(jb_dir):
                print("  ", item)
                p2 = os.path.join(jb_dir, item, "LocalHistory", "changes.storageData")
                if os.path.exists(p2):
                    print(f"    Found local history inside: {p2} ({os.path.getsize(p2) / 1024 / 1024:.2f} MB)")
        except Exception as e:
            print("  Error listing:", e)

if __name__ == '__main__':
    main()
