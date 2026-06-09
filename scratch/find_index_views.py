import os

scratch_dir = r"c:\Users\Bolokaiemi\PycharmProjects\mobileuserinterfaceProject6\scratch"

def main():
    print("Searching for index.html or styles.css views in scratch folder:")
    for f in os.listdir(scratch_dir):
        if f.startswith("view_app_"):
            path = os.path.join(scratch_dir, f)
            with open(path, "r", encoding="utf-8", errors="ignore") as file:
                content = file.read()
            if "<!DOCTYPE html>" in content:
                print(f"  Found index.html in: {f} ({os.path.getsize(path)/1024:.2f} KB)")
            if ":root" in content or "body {" in content:
                print(f"  Found styles.css in: {f} ({os.path.getsize(path)/1024:.2f} KB)")

if __name__ == "__main__":
    main()
