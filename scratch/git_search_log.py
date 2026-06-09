import subprocess

def main():
    print("Running git log -S 'student portal'...")
    res = subprocess.run(['git', 'log', '-S', 'student portal', '--oneline', '--', 'templates/index.html'], capture_output=True, text=True, encoding='utf-8')
    print("Commits modifying 'student portal' in templates/index.html:")
    print(res.stdout)
    
    res2 = subprocess.run(['git', 'log', '-S', 'student portal', '--oneline', '--', 'index.html'], capture_output=True, text=True, encoding='utf-8')
    print("Commits modifying 'student portal' in index.html:")
    print(res2.stdout)

if __name__ == '__main__':
    main()
