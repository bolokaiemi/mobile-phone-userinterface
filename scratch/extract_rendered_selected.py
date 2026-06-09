import os

def main():
    scratch_dir = r"c:\Users\Bolokaiemi\PycharmProjects\mobileuserinterfaceProject6\scratch"
    files = sorted([f for f in os.listdir(scratch_dir) if f.startswith("view_app_js_") and f.endswith(".txt")])
    for file in files:
        p = os.path.join(scratch_dir, file)
        with open(p, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()
        if "function renderSelectedCourse" in content:
            print(f"\n================ Found function start in {file} ================")
            lines = content.splitlines()
            start_printing = False
            for line in lines:
                if "function renderSelectedCourse" in line:
                    start_printing = True
                if start_printing:
                    print(line)
            print("==================================================")
        elif "renderSelectedCourse" in content and "const isBooked" in content:
            print(f"\n================ Found middle/end in {file} ================")
            lines = content.splitlines()
            for line in lines[-30:]:
                print(line)

if __name__ == '__main__':
    main()
