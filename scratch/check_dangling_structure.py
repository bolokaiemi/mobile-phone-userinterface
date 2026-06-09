import subprocess
import re

workspace_root = r"c:\Users\Bolokaiemi\PycharmProjects\mobileuserinterfaceProject6"

def run_git(args):
    res = subprocess.run(["git"] + args, cwd=workspace_root, capture_output=True, text=True, encoding="utf-8", errors="ignore")
    return res.stdout

def main():
    html = run_git(["cat-file", "-p", "f58c79ba0e8fe01927df4c87938ac250c72fa73c"])
    css = run_git(["cat-file", "-p", "93ccf8e6acfa8f379f6e0591b381765bd4c7444c"])
    
    print("=== HTML Structure in f58c79b ===")
    # Find card classes and their order
    cards = re.findall(r'<div class="[^"]*card[^"]*"|<section class="[^"]*card[^"]*"', html)
    print(f"Found {len(cards)} cards:")
    for c in cards:
        print(" ", c)
        
    # Let's search for container divs around student-card and emulator-tips
    student_pos = html.find("student-card")
    tips_pos = html.find("emulator-tips-card")
    comments_pos = html.find("reviews-feed-card")
    if comments_pos == -1:
         comments_pos = html.find("comments-card")
         
    print(f"Positions: Comments={comments_pos}, Student={student_pos}, Tips={tips_pos}")
    if comments_pos < student_pos < tips_pos:
        print("Order is correct: Comments -> Student -> Tips (Vertical layout!)")
    else:
        print("Order is different!")
        
    # Check if templates/index.html is the same as f58c79b
    # Let's write them to a temp folder to compare or check
    print("\n=== CSS size in 93ccf8e ===")
    print("Size:", len(css))

if __name__ == "__main__":
    main()
