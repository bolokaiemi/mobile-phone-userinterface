import json
import os
import re

log_path = r"C:\Users\Bolokaiemi\.gemini\antigravity\brain\3c885c20-476d-4b94-94f5-1c9bbbc7f841\.system_generated\logs\transcript.jsonl"
workspace_root = r"c:\Users\Bolokaiemi\PycharmProjects\mobileuserinterfaceProject6"

def parse_logs():
    tool_calls = []
    with open(log_path, "r", encoding="utf-8") as f:
        for line in f:
            try:
                data = json.loads(line)
                if data.get("source") == "MODEL" and data.get("type") == "PLANNER_RESPONSE":
                    calls = data.get("tool_calls", [])
                    for call in calls:
                        name = call.get("name")
                        if name in ["replace_file_content", "write_to_file", "multi_replace_file_content"]:
                            tool_calls.append((data.get("step_index"), name, call.get("args")))
            except Exception as e:
                pass
    return tool_calls

def main():
    calls = parse_logs()
    print(f"Found {len(calls)} file modification tool calls.")
    
    # Sort calls by step_index to ensure chronological order
    calls.sort(key=lambda x: x[0])
    
    for idx, (step, name, args) in enumerate(calls):
        target_file = args.get("TargetFile")
        if not target_file:
            continue
        
        # Standardize path
        target_file = target_file.strip('"').replace('\\\\', '\\')
        
        # If the target file starts with absolute path containing workspace, use it.
        # Otherwise, if it has a drive letter but is not in workspace, ignore it.
        if ":" in target_file:
            if not target_file.lower().startswith(workspace_root.lower()):
                continue
        else:
            # Relative path
            target_file = os.path.join(workspace_root, target_file)
            
        print(f"\nStep {step} - {name} on {target_file}:")
        
        try:
            if name == "write_to_file":
                overwrite = args.get("Overwrite")
                code_content = args.get("CodeContent")
                print(f"  Action: Write/Overwrite={overwrite}")
                os.makedirs(os.path.dirname(target_file), exist_ok=True)
                with open(target_file, "w", encoding="utf-8") as f:
                    f.write(code_content)
                print(f"  [SUCCESS] Written file.")
                    
            elif name == "replace_file_content":
                start_line = int(args.get("StartLine"))
                end_line = int(args.get("EndLine"))
                target_content = args.get("TargetContent").strip('"').replace('\\"', '"').replace('\\n', '\n').replace('\\r', '\r').replace('\\t', '\t')
                replacement_content = args.get("ReplacementContent").strip('"').replace('\\"', '"').replace('\\n', '\n').replace('\\r', '\r').replace('\\t', '\t')
                
                print(f"  Replace line {start_line}-{end_line}")
                
                if not os.path.exists(target_file):
                    print(f"  [ERROR] File does not exist: {target_file}")
                    continue
                    
                with open(target_file, "r", encoding="utf-8") as f:
                    content = f.read()
                    
                if target_content in content:
                    content = content.replace(target_content, replacement_content, 1)
                    with open(target_file, "w", encoding="utf-8") as f:
                        f.write(content)
                    print(f"  [SUCCESS] Replaced exactly.")
                else:
                    # Try normalization of line endings
                    target_content_lf = target_content.replace('\r\n', '\n')
                    content_lf = content.replace('\r\n', '\n')
                    if target_content_lf in content_lf:
                        content_lf = content_lf.replace(target_content_lf, replacement_content.replace('\r\n', '\n'), 1)
                        with open(target_file, "w", encoding="utf-8") as f:
                            f.write(content_lf)
                        print(f"  [SUCCESS] Replaced after LF normalization.")
                    else:
                        print(f"  [ERROR] Target content not found!")
                        
            elif name == "multi_replace_file_content":
                chunks = args.get("ReplacementChunks", [])
                if isinstance(chunks, str):
                    try:
                        chunks = json.loads(chunks, strict=False)
                    except Exception as e:
                        print(f"  Failed to parse ReplacementChunks as JSON string: {e}")
                        continue
                
                print(f"  Multi-replace with {len(chunks)} chunks")
                if not os.path.exists(target_file):
                    print(f"  [ERROR] File does not exist: {target_file}")
                    continue
                    
                with open(target_file, "r", encoding="utf-8") as f:
                    content = f.read()
                    
                for chunk in chunks:
                    if isinstance(chunk, str):
                        try:
                            chunk = json.loads(chunk, strict=False)
                        except Exception as e:
                            print(f"    Failed to parse chunk string as JSON: {e}")
                            continue
                            
                    target_content = chunk.get("TargetContent").strip('"').replace('\\"', '"').replace('\\n', '\n').replace('\\r', '\r').replace('\\t', '\t')
                    replacement_content = chunk.get("ReplacementContent").strip('"').replace('\\"', '"').replace('\\n', '\n').replace('\\r', '\r').replace('\\t', '\t')
                    
                    if target_content in content:
                        content = content.replace(target_content, replacement_content, 1)
                    else:
                        target_content_lf = target_content.replace('\r\n', '\n')
                        content_lf = content.replace('\r\n', '\n')
                        if target_content_lf in content_lf:
                            content_lf = content_lf.replace(target_content_lf, replacement_content.replace('\r\n', '\n'), 1)
                            content = content_lf
                        else:
                            print(f"    [ERROR] Chunk target content not found!")
                
                with open(target_file, "w", encoding="utf-8") as f:
                    f.write(content)
                print(f"  [SUCCESS] Multi-replaced chunks.")
        except Exception as e:
            print(f"  [CRITICAL ERROR] Failed to apply action: {e}")

if __name__ == "__main__":
    main()
