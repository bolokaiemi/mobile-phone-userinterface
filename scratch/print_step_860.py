import json

log_path = r"C:\Users\Bolokaiemi\.gemini\antigravity\brain\3c885c20-476d-4b94-94f5-1c9bbbc7f841\.system_generated\logs\transcript.jsonl"

with open(log_path, "r", encoding="utf-8") as f:
    for line in f:
        try:
            data = json.loads(line)
            if data.get("step_index") == 860:
                print("=== Step 860 raw tool call ===")
                call = data.get("tool_calls", [])[0]
                args = call.get("args", {})
                print("TargetFile:", args.get("TargetFile"))
                print("Description:", args.get("Description"))
                # Print the raw ReplacementChunks string to see what is there
                chunks = args.get("ReplacementChunks")
                print("Chunks type:", type(chunks))
                if isinstance(chunks, str):
                    print("Chunks length:", len(chunks))
                    # Print first 500 and last 500 chars
                    print("Start of chunks:", chunks[:500])
                    print("End of chunks:", chunks[-500:])
                else:
                    print("Chunks:", repr(chunks))
        except Exception as e:
            print("Error parsing line:", e)
