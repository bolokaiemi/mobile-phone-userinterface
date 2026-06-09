import os

def main():
    path = "index.html"
    if not os.path.exists(path):
        print("index.html not found.")
        return
        
    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        lines = f.readlines()
        
    print("Searching for 'truncated' in current index.html:")
    found = False
    for idx, line in enumerate(lines):
        if "truncated" in line.lower():
            print(f"  Line {idx+1}: {line.strip()}")
            found = True
    if not found:
        print("  No truncation markers found in current index.html.")

if __name__ == '__main__':
    main()
