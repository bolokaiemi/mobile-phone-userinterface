import json
import os

log_path = r"C:\Users\Bolokaiemi\.gemini\antigravity\brain\3c885c20-476d-4b94-94f5-1c9bbbc7f841\.system_generated\logs\transcript.jsonl"

def print_step(step_num):
    if not os.path.exists(log_path):
        print("Log path does not exist")
        return
    with open(log_path, 'r', encoding='utf-8') as f:
        for line in f:
            try:
                d = json.loads(line)
                if d.get('step_index') == step_num:
                    print(f"\n================ STEP {step_num} ================")
                    print("Source:", d.get('source'))
                    print("Type:", d.get('type'))
                    print("Created at:", d.get('created_at'))
                    
                    # Tool call args
                    for call in d.get('tool_calls', []):
                        print("Tool name:", call.get('name'))
                        args = call.get('args', {})
                        for k, v in args.items():
                            print(f"Arg '{k}':")
                            # If it's a string, print first 200 and last 200 chars and length
                            if isinstance(v, str):
                                print(f"  Length: {len(v)}")
                                print(f"  Start: {repr(v[:300])}")
                                print(f"  End: {repr(v[-300:])}")
                            else:
                                print(f"  Value: {repr(v)}")
            except Exception as e:
                pass

def main():
    print_step(1112)
    print_step(1118)

if __name__ == '__main__':
    main()
