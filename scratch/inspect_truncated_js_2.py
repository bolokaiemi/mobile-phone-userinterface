import sys

# Set stdout to use utf-8 to avoid encoding crashes on windows
sys.stdout.reconfigure(encoding='utf-8')

with open("app.js", "r", encoding="utf-8") as f:
    lines = f.readlines()

def print_around(line_num):
    print(f"\n=== Lines around line {line_num} ===")
    start = max(0, line_num - 20)
    end = min(len(lines), line_num + 20)
    for i in range(start, end):
        if i < len(lines):
            print(f"{i+1}: {lines[i].rstrip()}")

print_around(2355)
