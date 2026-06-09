import subprocess

def run_git(args):
    res = subprocess.run(['git'] + args, capture_output=True, text=True, encoding='utf-8', errors='ignore')
    return res.stdout

def main():
    print("Searching Git commits containing 'student portal' or 'student-portal':")
    commits = []
    log_out = run_git(['log', '--oneline', '-n', '50'])
    for line in log_out.splitlines():
        if not line: continue
        sha = line.split()[0]
        # check if this commit's index.html contains student portal
        show_out = run_git(['show', f'{sha}:index.html'])
        if "student portal" in show_out.lower() or "student-portal" in show_out.lower():
            print(f"  Found in commit {line} (index.html has it)")
        else:
            # check templates/index.html
            show_out_tmpl = run_git(['show', f'{sha}:templates/index.html'])
            if "student portal" in show_out_tmpl.lower() or "student-portal" in show_out_tmpl.lower():
                print(f"  Found in commit {line} (templates/index.html has it)")

if __name__ == '__main__':
    main()
