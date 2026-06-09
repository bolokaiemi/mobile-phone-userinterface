import json
import os

log_path = r"C:\Users\Bolokaiemi\.gemini\antigravity\brain\3c885c20-476d-4b94-94f5-1c9bbbc7f841\.system_generated\logs\transcript.jsonl"

def main():
    if not os.path.exists(log_path):
        print("Log not found")
        return
        
    with open(log_path, 'r', encoding='utf-8') as f:
        for line in f:
            try:
                d = json.loads(line)
                step_idx = d.get('step_index')
                if step_idx == 1112:
                    for call in d.get('tool_calls', []):
                        if call.get('name') == 'replace_file_content':
                            args = call.get('args', {})
                            rep = args.get('ReplacementContent', '')
                            print("Step 1112 Replacement Content:")
                            print("-----------------------------")
                            print(rep)
                            print("-----------------------------")
                            # Save to a file
                            with open("scratch/step_1112_content.txt", "w", encoding="utf-8") as out:
                                out.write(rep)
                            print("Saved to scratch/step_1112_content.txt")
            except Exception as e:
                pass

if __name__ == '__main__':
    main()
