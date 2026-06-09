import os

def main():
    scratch_dir = r"c:\Users\Bolokaiemi\PycharmProjects\mobileuserinterfaceProject6\scratch"
    files = [f for f in os.listdir(scratch_dir) if f.startswith("view_app_js_") and f.endswith(".txt")]
    print(f"Found {len(files)} files to check.")
    for file in files:
        p = os.path.join(scratch_dir, file)
        with open(p, "r", encoding="utf-8", errors="ignore") as f:
            lines = f.readlines()
        
        # Look for 'dashboard-course-select' or 'dashboardCourseSelect' in this file
        matched = []
        for i, line in enumerate(lines):
            if "dashboard-course-select" in line or "dashboardCourseSelect" in line or "course-select" in line:
                matched.append((i+1, line.strip()))
                
        if matched:
            print(f"\n================ Match in {file} ================")
            for num, text in matched[:15]:
                print(f"  Line {num}: {text}")

if __name__ == '__main__':
    main()
