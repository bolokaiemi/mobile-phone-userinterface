import os

output_dir = r"c:\Users\Bolokaiemi\PycharmProjects\mobileuserinterfaceProject6\scratch\recovered"
out_path = os.path.join(output_dir, "test.txt")

try:
    with open(out_path, "w") as f:
        f.write("hello world")
    print("Write successful, file size:", os.path.getsize(out_path))
    print("Files in recovered directory:", os.listdir(output_dir))
except Exception as e:
    print("Error:", e)
