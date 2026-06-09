import difflib
import os

def main():
    root_idx = r"c:\Users\Bolokaiemi\PycharmProjects\mobileuserinterfaceProject6\index.html"
    tmpl_idx = r"c:\Users\Bolokaiemi\PycharmProjects\mobileuserinterfaceProject6\templates\index.html"
    
    with open(root_idx, "r", encoding="utf-8") as f:
        root_lines = f.readlines()
    with open(tmpl_idx, "r", encoding="utf-8") as f:
        tmpl_lines = f.readlines()
        
    print(f"Comparing index.html ({len(root_lines)} lines) and templates/index.html ({len(tmpl_lines)} lines)...")
    
    # Let's find lines that are in templates/index.html but not in index.html (like url_for or Jinja tags)
    jinja_lines = []
    for i, line in enumerate(tmpl_lines):
        if "{{" in line or "{%" in line or "url_for" in line:
            jinja_lines.append((i+1, line.strip()))
            
    print(f"\nJinja/Flask template lines found in templates/index.html ({len(jinja_lines)} lines):")
    for num, text in jinja_lines:
        print(f"  Line {num}: {text}")

if __name__ == '__main__':
    main()
