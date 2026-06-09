import json
import os

prev_log_path = r"C:\Users\Bolokaiemi\.gemini\antigravity\brain\3c885c20-476d-4b94-94f5-1c9bbbc7f841\.system_generated\logs\transcript.jsonl"

def main():
    if not os.path.exists(prev_log_path):
        print("Log not found")
        return
        
    print("Checking features in previous log up to step 1500:")
    with open(prev_log_path, "r", encoding="utf-8") as f:
        for line in f:
            try:
                data = json.loads(line)
                step_idx = data.get("step_index")
                if step_idx > 1500:
                    break
                for call in data.get("tool_calls", []):
                    name = call.get("name")
                    if name in ["replace_file_content", "write_to_file", "multi_replace_file_content"]:
                        args = call.get("args", {})
                        target = args.get("TargetFile", "")
                        desc = args.get("Description", "")
                        # Search description or content for register, email, book, bookings
                        if any(w in desc.lower() or w in str(args).lower() for w in ["register", "email", "book-lesson", "bookings", "zoom"]):
                            print(f"Step {step_idx} on {os.path.basename(target)}: {desc[:120]}")
            except Exception:
                pass

if __name__ == "__main__":
    main()
