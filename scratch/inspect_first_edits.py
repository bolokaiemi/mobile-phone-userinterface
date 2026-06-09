import json
import os

prev_log_path = r"C:\Users\Bolokaiemi\AppData\Local\JetBrains\PyCharm2025.2\LocalHistory\changes.storageData" # Wait, no! The PyCharm history.
# Let's use the actual previous log path:
prev_log_path = r"C:\Users\Bolokaiemi\.gemini\antigravity\brain\3c885c20-476d-4b94-94f5-1c9bbbc7f841\.system_generated\logs\transcript.jsonl"

def main():
    if not os.path.exists(prev_log_path):
        print(f"Previous log path does not exist: {prev_log_path}")
        return
        
    print("Checking first 10 file edits in previous log:")
    count = 0
    with open(prev_log_path, "r", encoding="utf-8") as f:
        for line in f:
            try:
                data = json.loads(line)
                step_idx = data.get("step_index")
                source = data.get("source")
                step_type = data.get("type")
                
                tool_calls = data.get("tool_calls", [])
                for call in tool_calls:
                    name = call.get("name")
                    if name in ["replace_file_content", "write_to_file", "multi_replace_file_content"]:
                        print(f"Step {step_idx}: {name} on {call.get('args', {}).get('TargetFile')}")
                        desc = call.get('args', {}).get('Description')
                        if desc:
                            print(f"  Description: {desc}")
                        count += 1
                        if count >= 15:
                            return
            except Exception as e:
                pass

if __name__ == "__main__":
    main()
