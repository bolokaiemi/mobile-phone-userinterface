import json
import os

prev_log_path = r"C:\Users\Bolokaiemi\.gemini\antigravity\brain\3c885c20-476d-4b94-94f5-1c9bbbc7f841\.system_generated\logs\transcript.jsonl"

def main():
    if not os.path.exists(prev_log_path):
        print(f"Previous log path does not exist: {prev_log_path}")
        return
        
    print("Parsing USER inputs and timestamps from PREVIOUS log...")
    with open(prev_log_path, "r", encoding="utf-8") as f:
        for line in f:
            try:
                data = json.loads(line)
                step_idx = data.get("step_index")
                source = data.get("source")
                step_type = data.get("type")
                content = data.get("content")
                
                # Check for USER inputs or SYSTEM timestamps
                # We can also check tools executed.
                # Let's check for any mention of timestamp or time in content.
                if step_type == "USER_INPUT" or source == "USER_EXPLICIT":
                    print(f"\nStep {step_idx}: {source} - {step_type}")
                    if content:
                        print(f"  Content: {content.strip()}")
            except Exception as e:
                print(f"Error parsing line: {e}")

if __name__ == "__main__":
    main()
