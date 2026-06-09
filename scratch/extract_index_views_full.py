import json
import os

log_path = r"C:\Users\Bolokaiemi\.gemini\antigravity\brain\3c885c20-476d-4b94-94f5-1c9bbbc7f841\.system_generated\logs\transcript.jsonl"

def main():
    if not os.path.exists(log_path):
        print("Log not found")
        return
        
    print("Searching for index.html view_file outputs in previous logs:")
    with open(log_path, "r", encoding="utf-8") as f:
        for line in f:
            try:
                data = json.loads(line)
                step_idx = data.get("step_index")
                step_type = data.get("type")
                content = data.get("content", "")
                
                if step_type == "VIEW_FILE" and "index.html" in content:
                    print(f"Step {step_idx}: Found index.html view! Content length: {len(content)}")
                    out_path = f"scratch/view_index_html_step_{step_idx}.txt"
                    with open(out_path, "w", encoding="utf-8") as out:
                        out.write(content)
                    print(f"  Saved to {out_path}")
            except Exception as e:
                pass

if __name__ == "__main__":
    main()
