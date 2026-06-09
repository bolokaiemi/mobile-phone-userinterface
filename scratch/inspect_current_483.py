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
                if step_idx == 483:
                    print("=== Found Step 483 ===")
                    for call in data.get("tool_calls", []):
                        args = call.get("args", {})
                        rc = args.get("ReplacementContent", "")
                        print("Length of ReplacementContent:", len(rc))
                        print("Content:")
                        print(rc)
            except Exception as e:
                pass

if __name__ == "__main__":
    main()
