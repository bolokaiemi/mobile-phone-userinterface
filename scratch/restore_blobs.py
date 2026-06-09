import subprocess
import os

workspace_root = r"c:\Users\Bolokaiemi\PycharmProjects\mobileuserinterfaceProject6"

def run_git_bytes(args):
    res = subprocess.run(["git"] + args, cwd=workspace_root, capture_output=True)
    return res.stdout

def main():
    print("=== RESTORING HTML AND CSS FROM DANGLING BLOBS ===")
    
    # 1. Restore index.html
    html_bytes = run_git_bytes(["cat-file", "-p", "f58c79ba0e8fe01927df4c87938ac250c72fa73c"])
    if len(html_bytes) > 10000:
        index_path = os.path.join(workspace_root, "index.html")
        templates_index_path = os.path.join(workspace_root, "templates", "index.html")
        
        with open(index_path, "wb") as f:
            f.write(html_bytes)
        print(f"[SUCCESS] Restored {index_path} ({len(html_bytes)} bytes)")
        
        with open(templates_index_path, "wb") as f:
            f.write(html_bytes)
        print(f"[SUCCESS] Restored {templates_index_path} ({len(html_bytes)} bytes)")
    else:
        print("[ERROR] html_bytes length is too small:", len(html_bytes))
        
    # 2. Restore static/styles.css
    css_bytes = run_git_bytes(["cat-file", "-p", "93ccf8e6acfa8f379f6e0591b381765bd4c7444c"])
    if len(css_bytes) > 5000:
        css_path = os.path.join(workspace_root, "static", "styles.css")
        with open(css_path, "wb") as f:
            f.write(css_bytes)
        print(f"[SUCCESS] Restored {css_path} ({len(css_bytes)} bytes)")
    else:
        print("[ERROR] css_bytes length is too small:", len(css_bytes))

if __name__ == "__main__":
    main()
