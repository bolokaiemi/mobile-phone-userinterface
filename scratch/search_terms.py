import os
import json

def search_scratch():
    scratch_dir = r"c:\Users\Bolokaiemi\PycharmProjects\mobileuserinterfaceProject6\scratch"
    print("Searching scratch files for features-grid / features-section:")
    for root, dirs, files in os.walk(scratch_dir):
        for file in files:
            if file.endswith((".py", ".js", ".txt", ".md", ".json")):
                p = os.path.join(root, file)
                try:
                    with open(p, "r", encoding="utf-8", errors="ignore") as f:
                        content = f.read()
                    if "features-grid" in content or "features-section" in content:
                        print(f"  Found in: {p} ({os.path.getsize(p) / 1024:.2f} KB)")
                except Exception:
                    pass

def search_logs():
    log_path = r"C:\Users\Bolokaiemi\.gemini\antigravity\brain\3c885c20-476d-4b94-94f5-1c9bbbc7f841\.system_generated\logs\transcript.jsonl"
    if not os.path.exists(log_path):
        print("Log path does not exist")
        return
    print("\nSearching logs for index.html replacement content containing features-grid or features-section:")
    with open(log_path, 'r', encoding='utf-8') as f:
        for line in f:
            try:
                d = json.loads(line)
                step_idx = d.get('step_index')
                if d.get('source') == 'MODEL' and d.get('type') == 'PLANNER_RESPONSE':
                    for call in d.get('tool_calls', []):
                        name = call.get('name')
                        if name in ['write_to_file', 'replace_file_content', 'multi_replace_file_content']:
                            args = call.get('args', {})
                            args_str = json.dumps(args)
                            if "features-grid" in args_str or "features-section" in args_str:
                                print(f"  Step {step_idx}: Tool {name} on {args.get('TargetFile')}")
                                # Let's print the relevant chunk
                                if name == 'write_to_file':
                                    content = args.get('CodeContent', '')
                                    print("    Length of CodeContent:", len(content))
                                elif name == 'replace_file_content':
                                    content = args.get('ReplacementContent', '')
                                    print("    ReplacementContent (truncated):", repr(content[:500]))
                                elif name == 'multi_replace_file_content':
                                    chunks = args.get('ReplacementChunks', [])
                                    print(f"    Multi-replace with {len(chunks)} chunks.")
                                    for idx, chunk in enumerate(chunks):
                                        rc = chunk.get('ReplacementContent', '')
                                        if "features-grid" in rc or "features-section" in rc:
                                            print(f"      Chunk {idx} ReplacementContent (truncated):", repr(rc[:500]))
            except Exception as e:
                pass

if __name__ == '__main__':
    search_scratch()
    search_logs()
