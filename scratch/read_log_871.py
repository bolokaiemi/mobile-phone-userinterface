import os

log_871 = r"C:\Users\Bolokaiemi\.gemini\antigravity\brain\75c9cf9e-5e59-4f86-aa17-6925ff18f580\.system_generated\tasks\task-871.log"

def main():
    if os.path.exists(log_871):
        print("=== LOG FOR task-871 ===")
        with open(log_871, "r", encoding="utf-8", errors="ignore") as f:
            print(f.read())
    else:
        print(f"Log file {log_871} does not exist.")

if __name__ == "__main__":
    main()
