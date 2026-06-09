import os

def main():
    path = "index.html"
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            lines = f.readlines()
        print("index.html lines 685 to 765:")
        for idx in range(684, min(len(lines), 765)):
            print(f"{idx+1}: {lines[idx].rstrip()}")

if __name__ == '__main__':
    main()
