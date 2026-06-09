import re
import os

def inspect_html(path):
    if not os.path.exists(path):
        return
    print(f"\n================ INSPECTING {path} ================")
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
        
    # Let's find sections or cards
    # E.g. find all sections with classes, or main cards
    print("Found sections/key divs in order:")
    
    # Simple regex to find ids or classes of main containers/cards
    # Let's search for divs/sections with class containing 'hero', 'playground', 'card', 'hub'
    lines = content.splitlines()
    for i, line in enumerate(lines):
        if "<section" in line or "<header" in line or "<footer" in line:
            print(f"  Line {i+1}: {line.strip()}")
        elif "class=" in line and ("card" in line or "hero" in line or "playground" in line or "portal" in line or "auth" in line):
            # Check if it starts a tag
            if "<div" in line or "<section" in line:
                print(f"  Line {i+1}: {line.strip()}")

def main():
    inspect_html("index.html")
    inspect_html("templates/index.html")

if __name__ == '__main__':
    main()
