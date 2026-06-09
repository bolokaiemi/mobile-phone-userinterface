import json
import os
import shutil

log_path = r"C:\Users\Bolokaiemi\.gemini\antigravity\brain\3c885c20-476d-4b94-94f5-1c9bbbc7f841\.system_generated\logs\transcript.jsonl"
index_html_path = r"c:\Users\Bolokaiemi\PycharmProjects\mobileuserinterfaceProject6\index.html"
templates_index_path = r"c:\Users\Bolokaiemi\PycharmProjects\mobileuserinterfaceProject6\templates\index.html"

def main():
    print("Finding step 1548 in logs...")
    step_1548_args = None
    with open(log_path, "r", encoding="utf-8") as f:
        for line in f:
            try:
                data = json.loads(line)
                if data.get("step_index") == 1548:
                    calls = data.get("tool_calls", [])
                    for call in calls:
                        if call.get("name") == "replace_file_content":
                            step_1548_args = call.get("args")
                            break
            except Exception:
                pass
                
    if not step_1548_args:
        print("[ERROR] Could not find step 1548 replace_file_content in logs.")
        return
        
    print("Found step 1548 args.")
    target_content = step_1548_args.get("TargetContent").strip('"').replace('\\"', '"').replace('\\n', '\n').replace('\\r', '\r').replace('\\t', '\t')
    replacement_content = step_1548_args.get("ReplacementContent").strip('"').replace('\\"', '"').replace('\\n', '\n').replace('\\r', '\r').replace('\\t', '\t')
    
    # Let's read current index.html
    with open(index_html_path, "r", encoding="utf-8") as f:
        content = f.read()
        
    # We want to replace replacement_content with target_content to UNDO the change.
    if replacement_content in content:
        content = content.replace(replacement_content, target_content, 1)
        print("[SUCCESS] Reverted step 1548 changes in index.html.")
    else:
        # Try LF normalization
        replacement_content_lf = replacement_content.replace('\r\n', '\n')
        content_lf = content.replace('\r\n', '\n')
        if replacement_content_lf in content_lf:
            content_lf = content_lf.replace(replacement_content_lf, target_content.replace('\r\n', '\n'), 1)
            content = content_lf
            print("[SUCCESS] Reverted step 1548 changes in index.html after LF normalization.")
        else:
            print("[ERROR] Replacement content (step 1548 result) not found in index.html.")
            # Let's print out a sample of both
            print("Current index.html length:", len(content))
            return
            
    with open(index_html_path, "w", encoding="utf-8") as f:
        f.write(content)
        
    # Now copy to templates/index.html
    shutil.copyfile(index_html_path, templates_index_path)
    print("[SUCCESS] Synced templates/index.html.")

if __name__ == "__main__":
    main()
