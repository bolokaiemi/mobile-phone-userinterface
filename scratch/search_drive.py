import os

def main():
    home_dir = r"C:\Users\Bolokaiemi"
    print("Searching user directory for recovered files:")
    found = False
    # Only scan up to 3 levels deep to be fast
    for root, dirs, files in os.walk(home_dir):
        # Skip appdata local history to avoid matching the source file
        if "AppData" in root:
            continue
        # Skip node_modules or .venv
        if "node_modules" in root or ".venv" in root or ".git" in root:
            continue
            
        # check depth
        depth = root.replace(home_dir, "").count(os.sep)
        if depth > 4:
            continue
            
        for f in files:
            if f.startswith("raw_index_") or f.startswith("raw_app_") or f.startswith("raw_styles_"):
                p = os.path.join(root, f)
                print(f"  Found: {p} ({os.path.getsize(p) / 1024:.2f} KB)")
                found = True
                
    if not found:
        print("  No recovered files found.")

if __name__ == '__main__':
    main()
