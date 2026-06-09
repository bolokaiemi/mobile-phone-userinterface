import os

def main():
    root_idx = r"c:\Users\Bolokaiemi\PycharmProjects\mobileuserinterfaceProject6\index.html"
    tmpl_idx = r"c:\Users\Bolokaiemi\PycharmProjects\mobileuserinterfaceProject6\templates\index.html"
    
    if not os.path.exists(root_idx) or not os.path.exists(tmpl_idx):
        print("One of the files does not exist")
        return
        
    with open(root_idx, "r", encoding="utf-8") as f:
        root_content = f.read()
    with open(tmpl_idx, "r", encoding="utf-8") as f:
        tmpl_content = f.read()
        
    print(f"index.html length: {len(root_content)}")
    print(f"templates/index.html length: {len(tmpl_content)}")
    print(f"Files are identical: {root_content == tmpl_content}")

if __name__ == '__main__':
    main()
