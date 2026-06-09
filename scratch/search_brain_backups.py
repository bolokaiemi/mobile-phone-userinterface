import os

brain_dir = r"C:\Users\Bolokaiemi\.gemini\antigravity\brain"

def main():
    if not os.path.exists(brain_dir):
        print("Brain directory does not exist")
        return
        
    print("Searching for app.py or app.js in brain directory:")
    matches = []
    for root, dirs, files in os.walk(brain_dir):
        for file in files:
            if file in ["app.py", "app.js", "recovered_app.py", "recovered_app.js", "app_py_rec.py", "app_js_rec.js"]:
                p = os.path.join(root, file)
                matches.append(p)
                print(f"  Found: {p} ({os.path.getsize(p) / 1024:.2f} KB)")
                
    if not matches:
        # Let's search for any files containing code snippets
        print("No exact file matches. Searching for files containing 'def book_lesson':")
        for root, dirs, files in os.walk(brain_dir):
            for file in files:
                if file.endswith((".py", ".js", ".txt", ".md", ".json", ".jsonl")):
                    p = os.path.join(root, file)
                    try:
                        # Skip very large files if possible, or read first few MBs
                        if os.path.getsize(p) < 5 * 1024 * 1024:
                            with open(p, "r", encoding="utf-8", errors="ignore") as f:
                                content = f.read()
                            if "def book_lesson" in content:
                                print(f"  Found keyword 'def book_lesson' in: {p} ({os.path.getsize(p) / 1024:.2f} KB)")
                    except Exception:
                        pass

if __name__ == "__main__":
    main()
