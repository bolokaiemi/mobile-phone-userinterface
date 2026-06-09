import json
import os

prev_log_path = r"C:\Users\Bolokaiemi\.gemini\antigravity\brain\3c885c20-476d-4b94-94f5-1c9bbbc7f841\.system_generated\logs\transcript.jsonl"

def main():
    if not os.path.exists(prev_log_path):
        print("Log not found")
        return
        
    target_steps = [1395, 1396, 1401, 1402, 1428, 1429, 1430, 1431]
    print("Checking step status and results in previous logs:")
    with open(prev_log_path, "r", encoding="utf-8") as f:
        for line in f:
            try:
                data = json.loads(line)
                step_idx = data.get("step_index")
                if step_idx in target_steps:
                    print(f"Step {step_idx}: Source={data.get('source')}, Type={data.get('type')}")
                    content = data.get('content', '')
                    if content:
                        # Print first 200 chars of content
                        print(f"  Content: {content.strip()[:300]}")
            except Exception as e:
                pass

if __name__ == "__main__":
    main()
