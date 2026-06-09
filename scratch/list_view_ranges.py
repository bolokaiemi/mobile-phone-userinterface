import os

def main():
    scratch_dir = r"c:\Users\Bolokaiemi\PycharmProjects\mobileuserinterfaceProject6\scratch"
    files = sorted([f for f in os.listdir(scratch_dir) if f.startswith("view_app_js_") and f.endswith(".txt")])
    for file in files:
        p = os.path.join(scratch_dir, file)
        with open(p, "r", encoding="utf-8", errors="ignore") as f:
            header = [f.readline().strip() for _ in range(10)]
        
        # Look for the showing lines header
        for h in header:
            if "showing lines" in h.lower():
                print(f"{file}: {h}")
                break

if __name__ == '__main__':
    main()
