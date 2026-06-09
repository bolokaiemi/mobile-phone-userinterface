import os

def main():
    scratch_dir = r"c:\Users\Bolokaiemi\PycharmProjects\mobileuserinterfaceProject6\scratch"
    if not os.path.exists(scratch_dir):
        print("Scratch dir does not exist")
        return
        
    print("Searching scratch files for 'dashboard-course-select':")
    found = False
    for root, dirs, files in os.walk(scratch_dir):
        for file in files:
            if file.endswith((".py", ".js", ".txt", ".md", ".json")):
                p = os.path.join(root, file)
                try:
                    with open(p, "r", encoding="utf-8", errors="ignore") as f:
                        content = f.read()
                    if "dashboard-course-select" in content:
                        print(f"  Found in: {p} ({os.path.getsize(p) / 1024:.2f} KB)")
                        found = True
                except Exception:
                    pass
    if not found:
        print("  No occurrences found.")

if __name__ == '__main__':
    main()
