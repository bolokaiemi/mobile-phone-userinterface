import os

def check_file(path):
    if not os.path.exists(path):
        print(f"File {path} does not exist.")
        return
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    print(f"\nChecking {os.path.basename(path)} (len={len(content)}):")
    terms = ['student-portal', 'student_portal', 'student portal', 'student-card', 'hero', 'playground', 'quick share', 'germany', 'herne', 'zoomLessonsCard']
    for term in terms:
        print(f"  Term '{term}' count: {content.lower().count(term.lower())}")

def main():
    check_file("index.html")
    check_file("templates/index.html")
    check_file("app.js")
    check_file("static/styles.css")

if __name__ == '__main__':
    main()
