import json
import os

prev_log_path = r"C:\Users\Bolokaiemi\.gemini\antigravity\brain\3c885c20-476d-4b94-94f5-1c9bbbc7f841\.system_generated\logs\transcript.jsonl"

def main():
    if not os.path.exists(prev_log_path):
        print(f"Previous log path does not exist: {prev_log_path}")
        return
        
    print("Listing edits after Step 1503:")
    with open(prev_log_path, "r", encoding="utf-8") as f:
        for line in f:
            try:
                data = json.loads(line)
                step_idx = data.get("step_index")
                if step_idx > 1503:
                    source = data.get("source")
                    step_type = data.get("type")
                    content = data.get("content")
                    
                    if step_type == "USER_INPUT" or source == "USER_EXPLICIT":
                        print(f"\n--- Step {step_idx}: USER ---")
                        print(content.strip())
                    
                    tool_calls = data.get("tool_calls", [])
                    for call in tool_calls:
                        name = call.get("name")
                        if name in ["replace_file_content", "write_to_file", "multi_replace_file_content"]:
                            print(f"Step {step_idx}: {name} on {call.get('args', {}).get('TargetFile')}")
            except Exception as e:
                pass

if __name__ == "__main__":
    main()
