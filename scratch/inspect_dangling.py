import subprocess
import os

workspace_root = r"c:\Users\Bolokaiemi\PycharmProjects\mobileuserinterfaceProject6"

def run_git(args):
    res = subprocess.run(["git"] + args, cwd=workspace_root, capture_output=True, text=True, encoding="utf-8", errors="ignore")
    return res.stdout.strip(), res.stderr.strip()

def main():
    print("=== INSPECTING DANGLING OBJECTS ===")
    
    # 1. Inspect dangling blob f58c79b
    print("\n--- Dangling blob f58c79b (first 200 chars) ---")
    out, _ = run_git(["cat-file", "-p", "f58c79ba0e8fe01927df4c87938ac250c72fa73c"])
    print(repr(out[:200]))
    print(f"Total length: {len(out)} chars")
    
    # 2. Inspect dangling blob 93ccf8e
    print("\n--- Dangling blob 93ccf8e (first 200 chars) ---")
    out2, _ = run_git(["cat-file", "-p", "93ccf8e6acfa8f379f6e0591b381765bd4c7444c"])
    print(repr(out2[:200]))
    print(f"Total length: {len(out2)} chars")
    
    # 3. Inspect dangling tree 4b825dc
    print("\n--- Dangling tree 4b825dc ---")
    out3, _ = run_git(["ls-tree", "-r", "4b825dc642cb6eb9a060e54bf8d69288fbee4904"])
    print(out3)

if __name__ == "__main__":
    main()
