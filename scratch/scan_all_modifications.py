import json
import os

log_path = r"C:\Users\Bolokaiemi\.gemini\antigravity\brain\75c9cf9e-5e59-4f86-aa17-6925ff18f580\.system_generated\logs\transcript.jsonl"

def main():
    if not os.path.exists(log_path):
        print(f"Log path does not exist: {log_path}")
        return
        
    print("Scanning all tool calls > 1436...")
    with open(log_path, "r", encoding="utf-8") as f:
        for line in f:
            try:
                data = json.loads(line)
                step_idx = data.get("step_index")
                if step_idx is not None and step_idx > 1436:
                    tool_calls = data.get("tool_calls", [])
                    for call in tool_calls:
                        name = call.get("name")
                        args = call.get("args", {})
                        print(f"Step {step_idx}: {name} on {args.get('TargetFile') or args.get('CommandLine') or args.get('AbsolutePath') or ''}")
            except Exception as e:
                pass

if __name__ == "__main__":
    main()
