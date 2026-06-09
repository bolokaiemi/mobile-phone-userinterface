import json
import os

prev_log_path = r"C:\Users\Bolokaiemi\.gemini\antigravity\brain\3c885c20-476d-4b94-94f5-1c9bbbc7f841\.system_generated\logs\transcript.jsonl"

def main():
    if not os.path.exists(prev_log_path):
        print("Log not found")
        return
        
    print("Listing step descriptions from 1200 to 1500 in previous log:")
    with open(prev_log_path, "r", encoding="utf-8") as f:
        for line in f:
            try:
                data = json.loads(line)
                step_idx = data.get("step_index")
                if 1200 <= step_idx <= 1500:
                    tool_calls = data.get("tool_calls", [])
                    for call in tool_calls:
                        name = call.get("name")
                        if name in ["replace_file_content", "write_to_file", "multi_replace_file_content"]:
                            args = call.get("args", {})
                            tf = args.get("TargetFile", "")
                            desc = args.get("Description", "")
                            if "index.html" in tf or "styles.css" in tf:
                                print(f"Step {step_idx}: {name} on {os.path.basename(tf)}")
                                print(f"  Description: {desc}")
            except Exception:
                pass

if __name__ == "__main__":
    main()
