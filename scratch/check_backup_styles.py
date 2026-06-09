import os

def main():
    path = r"c:\Users\Bolokaiemi\PycharmProjects\mobileuserinterfaceProject6\scratch\current_backup\static\styles.css"
    if not os.path.exists(path):
        print("Backup styles.css not found.")
        return
        
    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        lines = f.readlines()
        
    print("Searching for 'truncated' in backup styles.css:")
    found = False
    for idx, line in enumerate(lines):
        if "truncated" in line.lower():
            print(f"  Line {idx+1}: {line.strip()}")
            found = True
    if not found:
        print("  No truncation markers found in backup styles.css.")
        print(f"  Total lines in backup: {len(lines)}")

if __name__ == '__main__':
    main()
