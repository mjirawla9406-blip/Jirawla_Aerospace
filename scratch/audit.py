import os
import re

base_dir = r"d:\Drone_Advancement_Concept\Website"
html_files = ["index.html", "surveillance-security.html", "surveying-mapping.html"]

def extract_references(html_path):
    with open(html_path, "r", encoding="utf-8") as f:
        content = f.read()

    refs = set()
    
    # regex for src="...", href="..."
    # we also want data-alt paths as mentioned by the user
    # pattern captures everything inside quotes
    patterns = [
        r'src="([^"]+)"',
        r'href="([^"]+)"',
        r'data-alt="([^"]+)"',
        r"url\(['\"]?([^'\")]+)['\"]?\)"
    ]
    
    for pattern in patterns:
        for match in re.finditer(pattern, content):
            ref = match.group(1)
            # ignore absolute urls and hashes
            if ref.startswith(("http://", "https://", "mailto:", "tel:", "#", "data:")):
                continue
            # ignore empty
            if not ref.strip():
                continue
            refs.add(ref.split('#')[0].split('?')[0]) # remove hash/query from url if any
            
    return refs

all_refs = set()
for hf in html_files:
    hf_path = os.path.join(base_dir, hf)
    if os.path.exists(hf_path):
        refs = extract_references(hf_path)
        all_refs.update(refs)

# Get all files recursively
all_files = {}
for root, dirs, files in os.walk(base_dir):
    if "scratch" in root:
        continue
    for f in files:
        full_path = os.path.join(root, f)
        rel_path = os.path.relpath(full_path, base_dir).replace('\\', '/')
        all_files[rel_path] = os.path.getsize(full_path)

required = []
orphaned = []
uncertain = []

# Analyze required files
for f in all_refs:
    # the ref could just be the name or a path
    # relative to base_dir
    f_clean = f.lstrip('./')
    if f_clean in all_files:
        required.append(f_clean)
    else:
        print(f"Missing required file: {f_clean}")

for f in html_files:
    if f in all_files and f not in required:
        required.append(f)

# Analyze all files
for f, size in all_files.items():
    if f in required:
        continue
    # is it orphaned or uncertain?
    # the user said: ORPHANED - unused Stitch drafts, .DS_Store, Thumbs.db, zip archives, backup copies, node_modules.
    # UNCERTAIN - anything you can't confidently classify.
    
    # let's be strict: if it's not referenced, it's orphaned, unless it's an image we're not sure about
    # Wait, the prompt says "UNCERTAIN - anything you can't confidently classify (e.g. an image that might be referenced by a page not yet built)".
    # Images in the folder that aren't referenced are uncertain, unless they clearly look like duplicates like "Logo (1).jpg" or something.
    
    f_lower = f.lower()
    is_image = f_lower.endswith(('.jpg', '.jpeg', '.png', '.gif', '.svg', '.webp'))
    
    is_junk = f_lower in ('.ds_store', 'thumbs.db')
    is_backup = re.search(r'\(\d+\)|\_old', f_lower)
    
    if is_junk or is_backup or f_lower.endswith('.zip'):
        orphaned.append(f)
    elif is_image:
        uncertain.append(f)
    else:
        uncertain.append(f) # Any other file we are not sure about

print("--- REQUIRED ---")
for r in sorted(required):
    print(f"{r} ({all_files.get(r, 0)} bytes)")

print("\n--- ORPHANED ---")
for o in sorted(orphaned):
    print(f"{o} ({all_files[o]} bytes)")

print("\n--- UNCERTAIN ---")
for u in sorted(uncertain):
    print(f"{u} ({all_files[u]} bytes)")
