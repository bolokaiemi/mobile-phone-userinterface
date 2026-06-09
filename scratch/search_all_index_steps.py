import json
import os

log_path = r"C:\Users\Bolokaiemi\.gemini\antigravity\brain\3c885c20-476d-4b94-94f5-1c9bbbc7f841\.system_generated\logs\transcript.jsonl"

def main():
    if not os.path.exists(log_path):
        print("Log not found")
        return
        
    print("Listing all steps modifying index.html or templates/index.html:")
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
                            target = args.get('TargetFile', '')
                            if 'index.html' in target:
                                desc = args.get('Description', '')
                                has_trunc = "truncated" in str(args).lower()
                                print(f"  Step {step_idx}: Tool={name} Target={os.path.basename(target)} Truncated={has_trunc} Desc={desc[:80]}")
            except Exception as e:
                pass

if __name__ == '__main__':
    main()
