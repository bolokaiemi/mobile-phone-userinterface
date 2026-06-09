import os

def main():
    path = "app.js"
    if not os.path.exists(path):
        print("app.js not found.")
        return
        
    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        lines = f.readlines()
        
    print("Searching for 'truncated' in app.js:")
    found = False
    for idx, line in enumerate(lines):
        if "truncated" in line.lower() or "..." in line:
            # check if it looks like a log truncation marker
            if "truncated" in line.lower() or "<" in line or ">" in line:
                print(f"  Line {idx+1}: {line.strip()}")
                found = True
    if not found:
        print("  No truncation markers found.")

if __name__ == '__main__':
    main()
