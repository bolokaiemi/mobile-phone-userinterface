import subprocess

def main():
    print("Checking commit 58a4e83 for templates/index.html...")
    out = subprocess.run(['git', 'show', '58a4e83:templates/index.html'], capture_output=True, text=True, encoding='utf-8')
    content = out.stdout
    print('Length of 58a4e83:templates/index.html:', len(content))
    terms = ['student-portal', 'student_portal', 'student portal', 'Hero', 'feedback', 'Quick Share', 'Herne, Germany']
    for term in terms:
        print(f'Term "{term}" count:', content.lower().count(term.lower()))

if __name__ == '__main__':
    main()
