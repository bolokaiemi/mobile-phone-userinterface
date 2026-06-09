import json
import os
import subprocess

log_path = r"C:\Users\Bolokaiemi\.gemini\antigravity\brain\3c885c20-476d-4b94-94f5-1c9bbbc7f841\.system_generated\logs\transcript.jsonl"
workspace_root = r"c:\Users\Bolokaiemi\PycharmProjects\mobileuserinterfaceProject6"

files_to_restore = [
    "index.html",
    "app.js",
    "app.py",
    "static/styles.css",
    "templates/index.html",
    "templates/admin.html",
    "templates/mobilephone.html",
    "README.md"
]

def checkout_files():
    print("Resetting files to HEAD commit (58a4e83)...")
    for f in files_to_restore:
        path = os.path.join(workspace_root, f)
        if os.path.exists(path):
            subprocess.run(["git", "checkout", "--", path], cwd=workspace_root)
    print("Git checkout done.")

def parse_logs():
    print(f"Parsing logs from {log_path} up to step 1500...")
    tool_calls = []
    with open(log_path, "r", encoding="utf-8") as f:
        for line in f:
            try:
                data = json.loads(line)
                step_idx = data.get("step_index")
                if step_idx is None or step_idx > 1500:
                    continue
                if data.get("source") == "MODEL" and data.get("type") == "PLANNER_RESPONSE":
                    calls = data.get("tool_calls", [])
                    for call in calls:
                        name = call.get("name")
                        if name in ["replace_file_content", "write_to_file", "multi_replace_file_content"]:
                            tool_calls.append((step_idx, name, call.get("args")))
            except Exception as e:
                pass
    # Sort chronologically by step index
    tool_calls.sort(key=lambda x: x[0])
    return tool_calls

def main():
    checkout_files()
    calls = parse_logs()
    print(f"Found {len(calls)} file modifications up to Step 1500.")
    
    success_count = 0
    fail_count = 0
    
    for idx, (step, name, args) in enumerate(calls):
        target_file = args.get("TargetFile")
        if not target_file:
            continue
            
        # Clean target path
        target_file = target_file.strip('"').replace('\\\\', '\\')
        if ":" in target_file:
            # Check if it lies in workspace or if it's external (e.g. brain artifacts)
            if not target_file.lower().startswith(workspace_root.lower()):
                # It's an artifact in the brain folder, let's skip it so we don't mess up artifacts
                continue
        else:
            target_file = os.path.join(workspace_root, target_file)
            
        print(f"\nStep {step} - {name} on {os.path.basename(target_file)}:")
        
        try:
            if name == "write_to_file":
                overwrite = args.get("Overwrite")
                code_content = args.get("CodeContent")
                os.makedirs(os.path.dirname(target_file), exist_ok=True)
                with open(target_file, "w", encoding="utf-8") as f:
                    f.write(code_content)
                print(f"  [SUCCESS] Written file.")
                success_count += 1
                
            elif name == "replace_file_content":
                start_line = int(args.get("StartLine"))
                end_line = int(args.get("EndLine"))
                target_content = args.get("TargetContent").strip('"').replace('\\"', '"').replace('\\n', '\n').replace('\\r', '\r').replace('\\t', '\t')
                replacement_content = args.get("ReplacementContent").strip('"').replace('\\"', '"').replace('\\n', '\n').replace('\\r', '\r').replace('\\t', '\t')
                
                with open(target_file, "r", encoding="utf-8") as f:
                    content = f.read()
                    
                if target_content in content:
                    content = content.replace(target_content, replacement_content, 1)
                    with open(target_file, "w", encoding="utf-8") as f:
                        f.write(content)
                    print(f"  [SUCCESS] Replaced exactly.")
                    success_count += 1
                else:
                    # Try LF normalization
                    target_content_lf = target_content.replace('\r\n', '\n')
                    content_lf = content.replace('\r\n', '\n')
                    if target_content_lf in content_lf:
                        content_lf = content_lf.replace(target_content_lf, replacement_content.replace('\r\n', '\n'), 1)
                        with open(target_file, "w", encoding="utf-8") as f:
                            f.write(content_lf)
                        print(f"  [SUCCESS] Replaced after LF normalization.")
                        success_count += 1
                    else:
                        print(f"  [FAIL] Target content not found.")
                        print("    Target start:", repr(target_content[:100]))
                        fail_count += 1
                        
            elif name == "multi_replace_file_content":
                chunks = args.get("ReplacementChunks", [])
                if isinstance(chunks, str):
                    chunks = json.loads(chunks, strict=False)
                    
                with open(target_file, "r", encoding="utf-8") as f:
                    content = f.read()
                    
                chunks_success = True
                for chunk in chunks:
                    if isinstance(chunk, str):
                        chunk = json.loads(chunk, strict=False)
                    tc = chunk.get("TargetContent").strip('"').replace('\\"', '"').replace('\\n', '\n').replace('\\r', '\r').replace('\\t', '\t')
                    rc = chunk.get("ReplacementContent").strip('"').replace('\\"', '"').replace('\\n', '\n').replace('\\r', '\r').replace('\\t', '\t')
                    
                    if tc in content:
                        content = content.replace(tc, rc, 1)
                    else:
                        tc_lf = tc.replace('\r\n', '\n')
                        content_lf = content.replace('\r\n', '\n')
                        if tc_lf in content_lf:
                            content_lf = content_lf.replace(tc_lf, rc.replace('\r\n', '\n'), 1)
                            content = content_lf
                        else:
                            print(f"    [FAIL] Chunk target content not found.")
                            print("      Chunk target:", repr(tc[:100]))
                            chunks_success = False
                            
                with open(target_file, "w", encoding="utf-8") as f:
                    f.write(content)
                    
                if chunks_success:
                    print(f"  [SUCCESS] Multi-replaced chunks.")
                    success_count += 1
                else:
                    print(f"  [PARTIAL FAIL] Some chunks failed.")
                    fail_count += 1
                    
        except Exception as e:
            print(f"  [CRITICAL ERROR] {e}")
            fail_count += 1
            
    print(f"\nReconstruction complete. Success: {success_count}, Fail: {fail_count}")

if __name__ == "__main__":
    main()
