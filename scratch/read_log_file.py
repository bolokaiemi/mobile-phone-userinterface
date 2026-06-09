import os

log_793 = r"C:\Users\Bolokaiemi\.gemini\antigravity\brain\75c9cf9e-5e59-4f86-aa17-6925ff18f580\.system_generated\tasks\task-793.log"
log_802 = r"C:\Users\Bolokaiemi\.gemini\antigravity\brain\75c9cf9e-5e59-4f86-aa17-6925ff18f580\.system_generated\tasks\task-802.log"

def print_log(path, name):
    print(f"\n=== LOG FOR {name} ===")
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8", errors="ignore") as f:
            print(f.read())
    else:
        print(f"Log file {path} does not exist.")

def main():
    print_log(log_793, "Flask Server (task-793)")
    print_log(log_802, "Verifier (task-802)")

if __name__ == "__main__":
    main()
