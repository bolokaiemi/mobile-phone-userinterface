import os

def main():
    lh_dir = r"C:\Users\Bolokaiemi\AppData\Local\JetBrains\PyCharm2025.2\LocalHistory"
    if os.path.exists(lh_dir):
        print(f"Listing files in {lh_dir}:")
        for root, dirs, files in os.walk(lh_dir):
            for file in files:
                p = os.path.join(root, file)
                print(f"  {os.path.relpath(p, lh_dir)} ({os.path.getsize(p) / 1024 / 1024:.2f} MB)")
    else:
        print("LocalHistory directory not found.")

if __name__ == '__main__':
    main()
