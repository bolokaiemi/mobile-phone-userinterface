import json
import os

log_path = r"C:\Users\Bolokaiemi\.gemini\antigravity\brain\75c9cf9e-5e59-4f86-aa17-6925ff18f580\.system_generated\logs\transcript.jsonl"

def main():
    if not os.path.exists(log_path):
        print(f"Log path does not exist: {log_path}")
        return
        
    print("Parsing all file modifications in current conversation...")
    with open(log_path, "r", encoding="utf-8") as f:
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
                        args = call.get("args", {})
                        print(f"\nStep {step_idx}: {name} on {args.get('TargetFile')}")
                        desc = args.get("Description")
                        if desc:
                            print(f"  Description: {desc}")
            except Exception as e:
                print(f"Error parsing line: {e}")

if __name__ == "__main__":
    main()
