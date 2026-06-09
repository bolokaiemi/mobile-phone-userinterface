import os

def check_contact(path):
    if not os.path.exists(path):
        return
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    print(f"\n================ CONTACT INFO IN {path} ================")
    # Print lines containing phone, location, contact, or +49
    for line in content.splitlines():
        if any(term in line.lower() for term in ["phone", "location", "contact", "+49", "herne", "germany"]):
            print("  ", line.strip())

if __name__ == '__main__':
    check_contact("index.html")
    check_contact("templates/index.html")
