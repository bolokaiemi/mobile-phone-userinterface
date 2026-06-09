import json
import os

log_path = r"C:\Users\Bolokaiemi\.gemini\antigravity\brain\75c9cf9e-5e59-4f86-aa17-6925ff18f580\.system_generated\logs\transcript.jsonl"

def main():
    if not os.path.exists(log_path):
        print("Log not found")
        return
        
    with open(log_path, "r", encoding="utf-8") as f:
        for line in f:
            try:
                data = json.loads(line)
                step_idx = data.get("step_index")
                if step_idx == 440 or (step_idx in [438, 439, 440, 441, 442] and data.get("type") == "RUN_COMMAND"):
                    print(f"=== Found Step {step_idx} ===")
                    print(data.get("content"))
            except Exception as e:
                pass

if __name__ == "__main__":
    main()
