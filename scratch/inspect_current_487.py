import json
import os

log_path = r"C:\Users\Bolokaiemi\.gemini\antigravity\brain\75c9cf9e-5e59-4f86-aa17-6925ff18f580\.system_generated\logs\transcript.jsonl"

def main():
    if not os.path.exists(log_path):
        print("Log not found")
        return
        
    with open(log_path, "r", encoding="utf-8") as f:
        for line in f:
            try:
                data = json.loads(line)
                step_idx = data.get("step_index")
                if step_idx in [487, 493]:
                    print(f"\n=== Step {step_idx} ===")
                    for call in data.get("tool_calls", []):
                        print("Tool name:", call.get("name"))
                        args = call.get("args", {})
                        print("StartLine:", args.get("StartLine"))
                        print("EndLine:", args.get("EndLine"))
                        print("TargetContent (first 100):", repr(args.get("TargetContent", "")[:100]))
                        print("ReplacementContent (first 100):", repr(args.get("ReplacementContent", "")[:100]))
                        print("ReplacementContent (last 200):", repr(args.get("ReplacementContent", "")[-200:]))
            except Exception as e:
                pass

if __name__ == "__main__":
    main()
