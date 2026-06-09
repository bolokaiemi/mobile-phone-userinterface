import json
import os

log_path = r"C:\Users\Bolokaiemi\.gemini\antigravity\brain\3c885c20-476d-4b94-94f5-1c9bbbc7f841\.system_generated\logs\transcript.jsonl"

def main():
    if not os.path.exists(log_path):
        print("Log path does not exist")
        return
        
    print("Modifications in 3c885c20:")
    with open(log_path, 'r', encoding='utf-8') as f:
        for line in f:
            try:
                d = json.loads(line)
                if d.get('source') == 'MODEL' and d.get('type') == 'PLANNER_RESPONSE':
                    for call in d.get('tool_calls', []):
                        name = call.get('name')
                        if name in ['write_to_file', 'replace_file_content', 'multi_replace_file_content']:
                            args = call.get('args', {})
                            tf = args.get('TargetFile', '')
                            # clean target file name
                            tf_clean = tf.strip('"').replace('\\\\', '\\')
                            print(f"Step {d.get('step_index')} ({d.get('created_at')}): {name} on {os.path.basename(tf_clean)}")
            except Exception as e:
                pass

if __name__ == '__main__':
    main()
