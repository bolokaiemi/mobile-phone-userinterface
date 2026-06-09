import os

def view_surround(path, line_num):
    if not os.path.exists(path):
        return
    with open(path, "r", encoding="utf-8") as f:
        lines = f.readlines()
    print(f"\n================ SURROUNDING LINE {line_num} IN {path} ================")
    start = max(0, line_num - 10)
    end = min(len(lines), line_num + 10)
    for idx in range(start, end):
        prefix = ">>>" if idx + 1 == line_num else "   "
        print(f"{prefix} {idx+1}: {lines[idx].rstrip()}")

def main():
    view_surround("index.html", 82)
    view_surround("index.html", 695)
    view_surround("index.html", 722)

if __name__ == '__main__':
    main()
