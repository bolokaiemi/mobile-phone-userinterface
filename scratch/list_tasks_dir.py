import os

tasks_dir = r"C:\Users\Bolokaiemi\.gemini\antigravity\brain\75c9cf9e-5e59-4f86-aa17-6925ff18f580\.system_generated\tasks"

def main():
    if os.path.exists(tasks_dir):
        print(f"Files in {tasks_dir}:")
        for f in os.listdir(tasks_dir):
            print(f"  {f}")
    else:
        print("Tasks directory does not exist")

if __name__ == "__main__":
    main()
