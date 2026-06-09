import os

def main():
    recovered_dir = r"c:\Users\Bolokaiemi\PycharmProjects\mobileuserinterfaceProject6\scratch\recovered_new"
    if not os.path.exists(recovered_dir):
        print("Directory does not exist")
        return
        
    print("Files in recovered_new:")
    files = [f for f in os.listdir(recovered_dir) if f.startswith("raw_index_")]
    print(f"Total HTML files: {len(files)}")
    for f in files:
        p = os.path.join(recovered_dir, f)
        with open(p, "r", encoding="utf-8", errors="ignore") as file:
            content = file.read()
        print(f"  {f}: len={len(content)}")
        print(f"    'hero-section' in content: {'hero-section' in content}")
        print(f"    'playground' in content: {'playground' in content}")
        print(f"    'Student Learning Portal' in content: {'Student Learning Portal' in content}")
        print(f"    'feedback-quick-share' in content: {'feedback-quick-share' in content}")
        print(f"    'Quick Share' in content: {'Quick Share' in content}")
        print(f"    'truncated' in content: {'truncated' in content.lower()}")

if __name__ == '__main__':
    main()
