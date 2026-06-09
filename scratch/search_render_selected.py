import json
import os

log_path = r"C:\Users\Bolokaiemi\.gemini\antigravity\brain\3c885c20-476d-4b94-94f5-1c9bbbc7f841\.system_generated\logs\transcript.jsonl"

def main():
    if not os.path.exists(log_path):
        print("Log not found")
        return
        
    print("Searching logs for 'renderSelectedCourse':")
    with open(log_path, 'r', encoding='utf-8') as f:
        for line in f:
            try:
                d = json.loads(line)
                step_idx = d.get('step_index')
                
                thinking = d.get('thinking', '')
                content = d.get('content', '')
                
                found = "renderselectedcourse" in thinking.lower() or "renderselectedcourse" in content.lower()
                
                if d.get('source') == 'MODEL' and d.get('type') == 'PLANNER_RESPONSE':
                    for call in d.get('tool_calls', []):
                        args_str = json.dumps(call.get('args', {}))
                        if "renderselectedcourse" in args_str.lower():
                            found = True
                            
                if found:
                    print(f"\nStep {step_idx}: type={d.get('type')} source={d.get('source')}")
                    if d.get('source') == 'MODEL' and d.get('type') == 'PLANNER_RESPONSE':
                        for call in d.get('tool_calls', []):
                            name = call.get('name')
                            args = call.get('args', {})
                            args_str = json.dumps(args)
                            if "renderselectedcourse" in args_str.lower():
                                print(f"  Tool {name} on {args.get('TargetFile')}:")
                                # If it's a replace_file_content or write_to_file, let's find the content
                                if name == 'replace_file_content':
                                    rep = args.get('ReplacementContent', '')
                                    print("    ReplacementContent length:", len(rep))
                                    # Print where renderSelectedCourse starts in rep
                                    idx = rep.find('renderSelectedCourse')
                                    if idx != -1:
                                        print("    Snippet:", repr(rep[idx:idx+1500]))
                                elif name == 'multi_replace_file_content':
                                    chunks = args.get('ReplacementChunks', [])
                                    for idx, chunk in enumerate(chunks):
                                        rc = chunk.get('ReplacementContent', '')
                                        if 'renderSelectedCourse' in rc:
                                            print(f"    Chunk {idx} ReplacementContent Snippet:")
                                            print(repr(rc[:1500]))
            except Exception as e:
                pass

if __name__ == '__main__':
    main()
