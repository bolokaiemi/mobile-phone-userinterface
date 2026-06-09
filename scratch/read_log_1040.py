import os

log_path = r"C:\Users\Bolokaiemi\.gemini\antigravity\brain\75c9cf9e-5e59-4f86-aa17-6925ff18f580\.system_generated\tasks\task-1040.log"

def main():
    if os.path.exists(log_path):
        print("Log size:", os.path.getsize(log_path))
        with open(log_path, "r", encoding="utf-8", errors="ignore") as f:
            print(f.read())
    else:
        print("Log file not found.")

if __name__ == '__main__':
    main()
