import os
import glob

tasks_dir = r"C:\Users\Bolokaiemi\.gemini\antigravity\brain\75c9cf9e-5e59-4f86-aa17-6925ff18f580\.system_generated\tasks"

def main():
    if not os.path.exists(tasks_dir):
        print("Tasks directory does not exist.")
        return
        
    # Find all .log files and sort by modification time
    log_files = glob.glob(os.path.join(tasks_dir, "*.log"))
    if not log_files:
        print("No log files found in tasks directory.")
        return
        
    log_files.sort(key=os.path.getmtime)
    
    # Print the last 3 logs
    for path in log_files[-3:]:
        print(f"\n=================== LOG: {os.path.basename(path)} ===================")
        try:
            with open(path, "r", encoding="utf-8", errors="ignore") as f:
                print(f.read())
        except Exception as e:
            print(f"Error reading log: {e}")

if __name__ == "__main__":
    main()
