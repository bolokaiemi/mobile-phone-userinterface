import json
import os

log_path = r"C:\Users\Bolokaiemi\.gemini\antigravity\brain\75c9cf9e-5e59-4f86-aa17-6925ff18f580\.system_generated\logs\transcript.jsonl"

def main():
    if not os.path.exists(log_path):
        print("Log not found")
        return
        
    print("Listing git and run_command calls in current session:")
    with open(log_path, "r", encoding="utf-8") as f:
        for line in f:
            try:
                data = json.loads(line)
                step_idx = data.get("step_index")
                tool_calls = data.get("tool_calls", [])
                for call in tool_calls:
                    name = call.get("name")
                    if name == "run_command":
                        cmd = call.get("args", {}).get("CommandLine", "")
                        print(f"Step {step_idx}: run_command -> {cmd}")
            except Exception:
                pass

if __name__ == "__main__":
    main()
