import json

log_path = r"C:\Users\Bolokaiemi\.gemini\antigravity\brain\3c885c20-476d-4b94-94f5-1c9bbbc7f841\.system_generated\logs\transcript.jsonl"

with open(log_path, "r", encoding="utf-8") as f:
    for line in f:
        try:
            data = json.loads(line)
            step = data.get("step_index")
            if step in [900, 1286, 1484]:
                print(f"=== Step {step} ===")
                calls = data.get("tool_calls", [])
                for call in calls:
                    args = call.get("args", {})
                    chunks = args.get("ReplacementChunks")
                    print("Type of chunks:", type(chunks))
                    if isinstance(chunks, str):
                        print("Length of chunks string:", len(chunks))
                        print("Sample chunks:", repr(chunks[:200]))
                    else:
                        print("Chunks value:", repr(chunks))
        except Exception as e:
            pass
