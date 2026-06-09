import subprocess
import os

workspace_root = r"c:\Users\Bolokaiemi\PycharmProjects\mobileuserinterfaceProject6"

def run_git(args):
    res = subprocess.run(["git"] + args, cwd=workspace_root, capture_output=True, text=True, encoding="utf-8", errors="ignore")
    return res.stdout

def main():
    # Read current app.js
    with open(os.path.join(workspace_root, "app.js"), "r", encoding="utf-8") as f:
        curr_js = f.read()
    
    # Read HEAD app.js
    head_js = run_git(["show", "HEAD:app.js"])
    
    # Let's locate the three <truncated> markers in curr_js
    markers = ["<truncated 1562 bytes>", "<truncated 2737 bytes>", "<truncated 2210 bytes>"]
    
    for marker in markers:
        pos = curr_js.find(marker)
        if pos == -1:
            print(f"Marker '{marker}' not found in current app.js")
            continue
            
        print(f"\n=================== FOUND MARKER: {marker} ===================")
        # Print 200 chars before and 200 chars after the marker in current app.js
        start_before = max(0, pos - 300)
        end_after = min(len(curr_js), pos + len(marker) + 300)
        print("--- SURROUNDING IN CURRENT app.js ---")
        print(curr_js[start_before:pos])
        print(">>> MARKER <<<")
        print(curr_js[pos + len(marker):end_after])
        
if __name__ == "__main__":
    main()
