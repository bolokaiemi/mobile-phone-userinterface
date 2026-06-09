import subprocess
import os

workspace_root = r"c:\Users\Bolokaiemi\PycharmProjects\mobileuserinterfaceProject6"

def run_git(args):
    res = subprocess.run(["git"] + args, cwd=workspace_root, capture_output=True, text=True, encoding="utf-8", errors="ignore")
    return res.stdout.strip(), res.stderr.strip()

def main():
    print("=== GIT CHECK ===")
    
    # Check stash
    out, err = run_git(["stash", "list"])
    print(f"Stash list:\n{out}\n{err}")
    
    # Check all branches
    out, err = run_git(["branch", "-a"])
    print(f"Branches:\n{out}")
    
    # Check type of the object
    out, err = run_git(["cat-file", "-t", "f58c79ba0e8fe01927df4c87938ac250c72fa73c"])
    print(f"Object type: {out}\n{err}")
    
    # Let's inspect reflog more deeply
    out, err = run_git(["reflog", "show", "--all", "-n", "50"])
    print(f"Reflog:\n{out[:2000]}")
    
if __name__ == "__main__":
    main()
