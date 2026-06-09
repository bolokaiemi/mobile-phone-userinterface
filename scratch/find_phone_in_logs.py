import json
import os

prev_log_path = r"C:\Users\Bolokaiemi\.gemini\antigravity\brain\3c885c20-476d-4b94-94f5-1c9bbbc7f841\.system_generated\logs\transcript.jsonl"

def main():
    if not os.path.exists(prev_log_path):
        print("Log not found")
        return
        
    print("Searching for phone/address updates in previous log:")
    with open(prev_log_path, "r", encoding="utf-8") as f:
        for line in f:
            try:
                data = json.loads(line)
                step_idx = data.get("step_index")
                tool_calls = data.get("tool_calls", [])
                for call in tool_calls:
                    name = call.get("name")
                    if name in ["replace_file_content", "multi_replace_file_content"]:
                        args = call.get("args", {})
                        arg_str = str(args)
                        if "+491793264196" in arg_str or "Germany" in arg_str:
                            print(f"Step {step_idx}: {name} on {args.get('TargetFile')}")
                            # Check if the step succeeded (the next line in logs usually contains system response)
            except Exception:
                pass

if __name__ == "__main__":
    main()
