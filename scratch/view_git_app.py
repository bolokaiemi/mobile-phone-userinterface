import subprocess

workspace_root = r"c:\Users\Bolokaiemi\PycharmProjects\mobileuserinterfaceProject6"

def run_git(args):
    res = subprocess.run(["git"] + args, cwd=workspace_root, capture_output=True, text=True, encoding="utf-8", errors="ignore")
    return res.stdout

def main():
    content = run_git(["show", "HEAD:app.py"])
    print("=== app.py in HEAD (length = %d) ===" % len(content))
    lines = content.splitlines()
    
    # Print mail configuration
    print("\n--- Mail Config in HEAD ---")
    for l in lines:
        if "mail" in l.lower() or "sender" in l.lower() or "smtp" in l.lower():
            print(l.strip())
            
    # Print a mail sending function example if exists
    print("\n--- Mail Sending occurrences ---")
    for idx, l in enumerate(lines):
        if "mail.send" in l or "Message(" in l:
            print(f"Line {idx+1}: {l.strip()}")
            # print surrounding lines
            for i in range(max(0, idx-5), min(len(lines), idx+10)):
                print(f"  {i+1}: {lines[i]}")

if __name__ == "__main__":
    main()
