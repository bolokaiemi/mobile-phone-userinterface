import json
import os

log_path = r"C:\Users\Bolokaiemi\.gemini\antigravity\brain\3c885c20-476d-4b94-94f5-1c9bbbc7f841\.system_generated\logs\transcript.jsonl"
target_file = r"c:\Users\Bolokaiemi\PycharmProjects\mobileuserinterfaceProject6\app.py"

def main():
    # First revert app.py to clean HEAD state
    os.system("git checkout app.py")
    
    calls = []
    with open(log_path, "r", encoding="utf-8") as f:
        for line in f:
            try:
                data = json.loads(line)
                if data.get("source") == "MODEL" and data.get("type") == "PLANNER_RESPONSE":
                    for call in data.get("tool_calls", []):
                        if call.get("name") in ["replace_file_content", "write_to_file", "multi_replace_file_content"]:
                            tf = call.get("args", {}).get("TargetFile", "").strip('"').replace('\\\\', '\\')
                            if "app.py" in tf:
                                calls.append((data.get("step_index"), call.get("name"), call.get("args")))
            except Exception:
                pass
                
    calls.sort(key=lambda x: x[0])
    print(f"Found {len(calls)} calls on app.py.")
    
    for step, name, args in calls:
        print(f"\nStep {step} - {name}:")
        if name == "replace_file_content":
            target_content = args.get("TargetContent").strip('"').replace('\\"', '"').replace('\\n', '\n').replace('\\r', '\r').replace('\\t', '\t')
            replacement_content = args.get("ReplacementContent").strip('"').replace('\\"', '"').replace('\\n', '\n').replace('\\r', '\r').replace('\\t', '\t')
            
            with open(target_file, "r", encoding="utf-8") as f:
                content = f.read()
                
            if target_content in content:
                content = content.replace(target_content, replacement_content, 1)
                with open(target_file, "w", encoding="utf-8") as f:
                    f.write(content)
                print("  [SUCCESS] Replaced.")
            else:
                target_content_lf = target_content.replace('\r\n', '\n')
                content_lf = content.replace('\r\n', '\n')
                if target_content_lf in content_lf:
                    content_lf = content_lf.replace(target_content_lf, replacement_content.replace('\r\n', '\n'), 1)
                    with open(target_file, "w", encoding="utf-8") as f:
                        f.write(content_lf)
                    print("  [SUCCESS] Replaced after LF normalization.")
                else:
                    print("  [ERROR] Target not found!")
                    print("  Target content repr:", repr(target_content[:100]))

if __name__ == "__main__":
    main()
