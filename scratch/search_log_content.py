import json
import os

log_path = r"C:\Users\Bolokaiemi\.gemini\antigravity\brain\3c885c20-476d-4b94-94f5-1c9bbbc7f841\.system_generated\logs\transcript.jsonl"

def main():
    if not os.path.exists(log_path):
        print("Log path does not exist")
        return
        
    print("Searching log for Hero, banner, playground:")
    with open(log_path, 'r', encoding='utf-8') as f:
        for line in f:
            try:
                d = json.loads(line)
                step_idx = d.get('step_index')
                
                # Check thinking or content or tool calls
                thinking = d.get('thinking', '')
                content = d.get('content', '')
                
                found = False
                for term in ['hero', 'playground', 'sandbox']:
                    if term in thinking.lower() or term in content.lower():
                        found = True
                        
                # Check tool call arguments
                if d.get('source') == 'MODEL' and d.get('type') == 'PLANNER_RESPONSE':
                    for call in d.get('tool_calls', []):
                        args_str = json.dumps(call.get('args', {}))
                        for term in ['hero', 'playground', 'sandbox']:
                            if term in args_str.lower():
                                found = True
                                
                if found:
                    print(f"Step {step_idx} ({d.get('created_at')}): type={d.get('type')} source={d.get('source')}")
                    if thinking:
                        print("  Thinking snippet:", repr(thinking[:100]))
                    # If it's a file modification, let's see which file
                    if d.get('source') == 'MODEL' and d.get('type') == 'PLANNER_RESPONSE':
                        for call in d.get('tool_calls', []):
                            name = call.get('name')
                            if name in ['write_to_file', 'replace_file_content', 'multi_replace_file_content']:
                                args = call.get('args', {})
                                tf = args.get('TargetFile', '')
                                print(f"  Tool: {name} on {tf}")
            except Exception as e:
                pass

if __name__ == '__main__':
    main()
