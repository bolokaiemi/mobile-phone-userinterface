import os

scratch_dir = r"c:\Users\Bolokaiemi\PycharmProjects\mobileuserinterfaceProject6\scratch"

def main():
    print("Listing line ranges for index.html view files in scratch:")
    files = [f for f in os.listdir(scratch_dir) if f.startswith("view_index_html_step_") and f.endswith(".txt")]
    files.sort(key=lambda x: int(x.split("_")[-1].split(".")[0]))
    for f in files:
        path = os.path.join(scratch_dir, f)
        with open(path, "r", encoding="utf-8") as file:
            first_lines = [file.readline().strip() for _ in range(10)]
        # Find the line showing "Showing lines X to Y"
        range_line = ""
        for line in first_lines:
            if "Showing lines" in line:
                range_line = line
                break
        print(f"  {f}: {range_line}")

if __name__ == "__main__":
    main()
