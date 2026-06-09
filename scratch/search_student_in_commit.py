import subprocess

def main():
    out = subprocess.run(['git', 'show', '58a4e83:templates/index.html'], capture_output=True, text=True, encoding='utf-8')
    content = out.stdout
    print("Lines in 58a4e83:templates/index.html with 'student':")
    found = False
    for line in content.splitlines():
        if "student" in line.lower():
            print("  ", line.strip())
            found = True
    if not found:
        print("   No lines containing 'student' found.")

if __name__ == '__main__':
    main()
