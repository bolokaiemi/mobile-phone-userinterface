import os

def main():
    path = r"c:\Users\Bolokaiemi\PycharmProjects\mobileuserinterfaceProject6\scratch\current_backup\app.py"
    if not os.path.exists(path):
        print("Backup app.py not found.")
        return
        
    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        lines = f.readlines()
        
    print("Searching for 'truncated' in backup app.py:")
    found = False
    for idx, line in enumerate(lines):
        if "truncated" in line.lower() or "..." in line:
            if "truncated" in line.lower() or "<" in line or ">" in line:
                print(f"  Line {idx+1}: {line.strip()}")
                found = True
    if not found:
        print("  No truncation markers found in backup app.py.")
        print(f"  Total lines in backup: {len(lines)}")

if __name__ == '__main__':
    main()
