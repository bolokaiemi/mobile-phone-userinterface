import os

index_path = r"c:\Users\Bolokaiemi\PycharmProjects\mobileuserinterfaceProject6\index.html"
templates_index_path = r"c:\Users\Bolokaiemi\PycharmProjects\mobileuserinterfaceProject6\templates\index.html"

def check_file(path):
    if not os.path.exists(path):
        print(f"{path} does not exist")
        return
    print(f"\nChecking {path}:")
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Check for student portal
    has_student_portal = "student portal" in content.lower() or "student-portal" in content.lower()
    print("Has 'student portal' text?", has_student_portal)
    
    # Check for student portal div
    print("Has 'student-portal-card' class?", "student-portal-card" in content)
    print("Has 'student-card' class?", "student-card" in content)
    
    # Find all divs containing student portal or cards
    # Let's print some lines containing student portal
    lines = content.splitlines()
    for idx, line in enumerate(lines):
        if "student portal" in line.lower() or "student-portal" in line.lower() or "student-card" in line.lower():
            print(f"  Line {idx+1}: {line.strip()[:100]}")

print("=== CHECKING FILES ===")
check_file(index_path)
check_file(templates_index_path)
