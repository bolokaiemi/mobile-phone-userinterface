import os

def main():
    scratch_dir = r"c:\Users\Bolokaiemi\PycharmProjects\mobileuserinterfaceProject6\scratch"
    files = sorted([f for f in os.listdir(scratch_dir) if f.startswith("view_app_js_") and f.endswith(".txt")])
    for file in files:
        p = os.path.join(scratch_dir, file)
        with open(p, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()
        if "renderSelectedCourse" in content:
            print(f"\n================ FULL FILE: {file} ================")
            print(content)
            print("==================================================")

if __name__ == '__main__':
    main()
