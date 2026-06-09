import json
import os

log_path = r"C:\Users\Bolokaiemi\.gemini\antigravity\brain\3c885c20-476d-4b94-94f5-1c9bbbc7f841\.system_generated\logs\transcript.jsonl"

def main():
    if not os.path.exists(log_path):
        print("Log not found")
        return
        
    print("Searching logs for 'feature-card':")
    with open(log_path, 'r', encoding='utf-8') as f:
        for line in f:
            try:
                d = json.loads(line)
                step_idx = d.get('step_index')
                
                # Check thinking, content, or tool calls
                thinking = d.get('thinking', '')
                content = d.get('content', '')
                
                found = "feature-card" in thinking.lower() or "feature-card" in content.lower()
                
                if d.get('source') == 'MODEL' and d.get('type') == 'PLANNER_RESPONSE':
                    for call in d.get('tool_calls', []):
                        args_str = json.dumps(call.get('args', {}))
                        if "feature-card" in args_str.lower():
                            found = True
                            
                if found:
                    print(f"\nStep {step_idx}: type={d.get('type')} source={d.get('source')}")
                    # If it's a tool call, let's print the tool call arguments or parts of them
                    if d.get('source') == 'MODEL' and d.get('type') == 'PLANNER_RESPONSE':
                        for call in d.get('tool_calls', []):
                            name = call.get('name')
                            if "feature-card" in json.dumps(call.get('args', {})):
                                print(f"  Tool {name}:")
                                args = call.get('args', {})
                                for k, v in args.items():
                                    v_str = str(v)
                                    if "feature-card" in v_str:
                                        print(f"    Arg {k}: len={len(v_str)}")
                                        # Let's search if there's any part of v_str containing feature-card that is not truncated
                                        idx = v_str.find("feature-card")
                                        while idx != -1:
                                            print(f"      Occurrence at {idx}: {repr(v_str[idx-100:idx+400])}")
                                            idx = v_str.find("feature-card", idx + 1)
            except Exception as e:
                pass

if __name__ == '__main__':
    main()
