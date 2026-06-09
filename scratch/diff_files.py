import difflib
import os

def main():
    root_idx = r"c:\Users\Bolokaiemi\PycharmProjects\mobileuserinterfaceProject6\index.html"
    tmpl_idx = r"c:\Users\Bolokaiemi\PycharmProjects\mobileuserinterfaceProject6\templates\index.html"
    
    with open(root_idx, "r", encoding="utf-8") as f:
        root_lines = f.readlines()
    with open(tmpl_idx, "r", encoding="utf-8") as f:
        tmpl_lines = f.readlines()
        
    diff = list(difflib.unified_diff(tmpl_lines, root_lines, fromfile='templates/index.html', tofile='index.html', n=3))
    print(f"Diff output size: {len(diff)} lines")
    if diff:
        print("Diff snippet:")
        for line in diff[:100]:
            print(line.rstrip())
    else:
        print("Files are identical!")

if __name__ == '__main__':
    main()
