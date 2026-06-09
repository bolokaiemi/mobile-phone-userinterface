import json

log_path = r"C:\Users\Bolokaiemi\.gemini\antigravity\brain\3c885c20-476d-4b94-94f5-1c9bbbc7f841\.system_generated\logs\transcript.jsonl"
index_html_path = r"c:\Users\Bolokaiemi\PycharmProjects\mobileuserinterfaceProject6\index.html"

with open(log_path, "r", encoding="utf-8") as f:
    for line in f:
        try:
            data = json.loads(line)
            if data.get("step_index") == 1548:
                call = data["tool_calls"][0]
                args = call["args"]
                replacement_content = args["ReplacementContent"].strip('"').replace('\\"', '"').replace('\\n', '\n').replace('\\r', '\r').replace('\\t', '\t')
                break
        except Exception:
            pass

with open(index_html_path, "r", encoding="utf-8") as f:
    content = f.read()

print("Replacement Content starts with:")
print(repr(replacement_content[:150]))
print("Is it in content?", replacement_content[:150] in content)

# Find where it diverges
prefix = ""
for char in replacement_content:
    if prefix + char in content:
        prefix += char
    else:
        print(f"Diverges at position {len(prefix)}:")
        print(f"Expected char in log: {repr(char)}")
        print(f"Actual next chars in file: {repr(content[content.find(prefix) + len(prefix) : content.find(prefix) + len(prefix) + 20])}")
        break
