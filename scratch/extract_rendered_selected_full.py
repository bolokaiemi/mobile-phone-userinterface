import os

def main():
    scratch_dir = r"c:\Users\Bolokaiemi\PycharmProjects\mobileuserinterfaceProject6\scratch"
    files = sorted([f for f in os.listdir(scratch_dir) if f.startswith("view_app_js_") and f.endswith(".txt")])
    
    # We want to find which file covers lines in app.js around 2750-2820
    for file in files:
        p = os.path.join(scratch_dir, file)
        with open(p, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()
        
        # Check if the file is for app.js and covers the range we need
        if "app.js" in content.lower():
            # Extract line range from file content
            # Look for "Showing lines A to B"
            lines = content.splitlines()
            range_info = ""
            for line in lines[:10]:
                if "showing lines" in line.lower():
                    range_info = line.strip()
                    break
            
            # Let's extract showing lines numbers
            # e.g., "Showing lines 2700 to 2760"
            import re
            m = re.search(r"Showing lines (\d+) to (\d+)", range_info)
            if m:
                start_line = int(m.group(1))
                end_line = int(m.group(2))
                if start_line <= 2780 <= end_line or start_line <= 2761 <= end_line:
                    print(f"\n================ {file} ({range_info}) ================")
                    for line in lines[7:]: # skip headers
                        print(line)
                    print("==================================================")

if __name__ == '__main__':
    main()
