import subprocess

def main():
    out = subprocess.run(['git', 'show', '58a4e83:templates/index.html'], capture_output=True, text=True, encoding='utf-8')
    content = out.stdout
    print("Checking structural sections in 58a4e83:templates/index.html:")
    
    # check for Hero
    hero_lines = [line.strip() for line in content.splitlines() if "hero" in line.lower() or "banner" in line.lower()]
    print(f"Hero/banner lines count: {len(hero_lines)}")
    if hero_lines:
        print("  Sample hero lines:")
        for line in hero_lines[:5]:
            print("    ", line)
            
    # check for Playground
    pg_lines = [line.strip() for line in content.splitlines() if "playground" in line.lower() or "sandbox" in line.lower()]
    print(f"Playground lines count: {len(pg_lines)}")
    if pg_lines:
        print("  Sample playground lines:")
        for line in pg_lines[:5]:
            print("    ", line)
            
    # check for Quick Share
    qs_lines = [line.strip() for line in content.splitlines() if "quick" in line.lower() or "share" in line.lower()]
    print(f"Quick/Share lines count: {len(qs_lines)}")
    if qs_lines:
        print("  Sample quick share lines:")
        for line in qs_lines[:5]:
            print("    ", line)
            
    # check for Germany or Herne
    ger_lines = [line.strip() for line in content.splitlines() if "germany" in line.lower() or "herne" in line.lower()]
    print(f"Germany/Herne lines count: {len(ger_lines)}")
    if ger_lines:
        print("  Sample Germany/Herne lines:")
        for line in ger_lines[:5]:
            print("    ", line)

if __name__ == '__main__':
    main()
