import os

history_dir = r"C:\Users\Bolokaiemi\AppData\Local\JetBrains\PyCharm2025.2\LocalHistory"

def main():
    if os.path.exists(history_dir):
        print(f"Listing files in {history_dir}:")
        for f in os.listdir(history_dir):
            path = os.path.join(history_dir, f)
            print(f"  {f} - {os.path.getsize(path) / 1024:.2f} KB")
    else:
        print("Directory does not exist")
        # Check parent directory
        parent = os.path.dirname(history_dir)
        if os.path.exists(parent):
            print(f"Listing {parent}:")
            for d in os.listdir(parent):
                print(f"  {d}")

if __name__ == "__main__":
    main()
