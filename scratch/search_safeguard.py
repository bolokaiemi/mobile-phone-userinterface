import json
import os

log_path = r"C:\Users\Bolokaiemi\.gemini\antigravity\brain\3c885c20-476d-4b94-94f5-1c9bbbc7f841\.system_generated\logs\transcript.jsonl"

def main():
    if not os.path.exists(log_path):
        print("Log not found")
        return
        
    print("Searching logs for 'Safeguard your platform':")
    with open(log_path, 'r', encoding='utf-8') as f:
        for line in f:
            try:
                d = json.loads(line)
                step_idx = d.get('step_index')
                
                thinking = d.get('thinking', '')
                content = d.get('content', '')
                
                found = "safeguard your platform" in thinking.lower() or "safeguard your platform" in content.lower()
                
                if d.get('source') == 'MODEL' and d.get('type') == 'PLANNER_RESPONSE':
                    for call in d.get('tool_calls', []):
                        args_str = json.dumps(call.get('args', {}))
                        if "safeguard your platform" in args_str.lower():
                            found = True
                            
                if found:
                    print(f"\nStep {step_idx}: type={d.get('type')} source={d.get('source')}")
                    # If it's a tool call, let's print the tool call arguments
                    if d.get('source') == 'MODEL' and d.get('type') == 'PLANNER_RESPONSE':
                        for call in d.get('tool_calls', []):
                            name = call.get('name')
                            args = call.get('args', {})
                            args_str = json.dumps(args)
                            if "safeguard your platform" in args_str.lower():
                                print(f"  Tool {name} on {args.get('TargetFile')}:")
                                # Print occurrence snippet
                                idx = args_str.lower().find("safeguard your platform")
                                print(f"    Snippet: {repr(args_str[idx-200:idx+600])}")
            except Exception as e:
                pass

if __name__ == '__main__':
    main()
