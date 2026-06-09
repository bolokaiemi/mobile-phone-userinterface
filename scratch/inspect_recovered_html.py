import os

def main():
    recovered_dir = r"c:\Users\Bolokaiemi\PycharmProjects\mobileuserinterfaceProject6\scratch\recovered_new"
    if not os.path.exists(recovered_dir):
        print("Directory does not exist")
        return
        
    print("Inspecting recovered HTML files:")
    candidates = []
    for f in os.listdir(recovered_dir):
        if f.startswith("raw_index_") and f.endswith(".html"):
            p = os.path.join(recovered_dir, f)
            with open(p, "r", encoding="utf-8", errors="ignore") as file:
                content = file.read()
            
            # Check keywords
            has_hero = "hero-section" in content
            has_playground = "playground" in content
            has_student = "Student Learning Portal" in content
            has_quick_share = "feedback-quick-share" in content or "Quick Share EbiUI" in content
            has_truncated = "truncated" in content.lower()
            
            if has_hero and has_playground and has_student and has_quick_share:
                print(f"  {f}: Hero={has_hero}, Playground={has_playground}, Student={has_student}, QuickShare={has_quick_share}, Truncated={has_truncated}, size={len(content)}")
                if not has_truncated:
                    candidates.append((f, len(content), p))
                    
    print("\nClean candidates (no truncations):")
    for name, size, path in candidates:
        print(f"  * {name} ({size / 1024:.2f} KB)")
        
if __name__ == '__main__':
    main()
