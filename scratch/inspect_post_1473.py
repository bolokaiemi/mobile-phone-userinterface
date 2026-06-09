import json
import os

prev_log_path = r"C:\Users\Bolokaiemi\.gemini\antigravity\brain\3c885c20-476d-4b94-94f5-1c9bbbc7f841\.system_generated\logs\transcript.jsonl"

def main():
    if not os.path.exists(prev_log_path):
        print(f"Previous log path does not exist: {prev_log_path}")
        return
        
    print("Parsing file modifications after Step 1473...")
    with open(prev_log_path, "r", encoding="utf-8") as f:
        for line in f:
            try:
                data = json.loads(line)
                step_idx = data.get("step_index")
                if step_idx < 1473:
                    continue
                source = data.get("source")
                step_type = data.get("type")
                
                tool_calls = data.get("tool_calls", [])
                for call in tool_calls:
                    name = call.get("name")
                    if name in ["replace_file_content", "write_to_file", "multi_replace_file_content"]:
                        args = call.get("args", {})
                        print(f"\nStep {step_idx}: {name} on {args.get('TargetFile')}")
                        desc = args.get("Description")
                        if desc:
                            print(f"  Description: {desc}")
            except Exception as e:
                print(f"Error parsing line: {e}")

if __name__ == "__main__":
    main()
