import os

history_path = r"C:\Users\Bolokaiemi\AppData\Local\JetBrains\PyCharm2025.2\LocalHistory\changes.storageData"

def main():
    if os.path.exists(history_path):
        print(f"[SUCCESS] History path exists: {history_path}")
        size = os.path.getsize(history_path)
        print(f"Size: {size / (1024*1024):.2f} MB")
    else:
        print(f"[ERROR] History path does not exist: {history_path}")
        # Let's check other JetBrains history folders
        local_app_data = os.environ.get("LOCALAPPDATA", "")
        print(f"LOCALAPPDATA: {local_app_data}")
        # Search for changes.storageData in LOCALAPPDATA/JetBrains
        jb_path = os.path.join(local_app_data, "JetBrains")
        if os.path.exists(jb_path):
            print("JetBrains directory found:")
            for root, dirs, files in os.walk(jb_path):
                for file in files:
                    if "changes.storage" in file or "history" in file:
                        p = os.path.join(root, file)
                        print(f"  Found file: {p} ({os.path.getsize(p) / (1024*1024):.2f} MB)")
        else:
            print("JetBrains directory not found in LOCALAPPDATA")

if __name__ == "__main__":
    main()
