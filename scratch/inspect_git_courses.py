import subprocess
import sys

sys.stdout.reconfigure(encoding='utf-8')

workspace_root = r"c:\Users\Bolokaiemi\PycharmProjects\mobileuserinterfaceProject6"

def run_git(args):
    res = subprocess.run(["git"] + args, cwd=workspace_root, capture_output=True, text=True, encoding="utf-8", errors="ignore")
    return res.stdout

def main():
    content = run_git(["show", "HEAD:app.js"])
    lines = content.splitlines()
    print("Total lines in HEAD app.js:", len(lines))
    
    # Search for renderCoursesUI
    for idx, l in enumerate(lines):
        if "function renderCoursesUI(" in l:
            print(f"Found renderCoursesUI at line {idx+1}:")
            for i in range(idx, min(len(lines), idx + 80)):
                print(f"{i+1}: {lines[i]}")
            break

if __name__ == "__main__":
    main()
