import os
import re
import shutil

base_dir = r"d:\Drone_Advancement_Concept\Website"
assets_dir = os.path.join(base_dir, "assets")

# Files to delete
to_delete = [
    "aerial_detection_scan.jpg",
    "drone_dock_launch.jpg",
    "video_feed_transmission.jpg",
    "wearable_signal_pulse.jpg",
    "Logo.jpg",
    "Logo_Horizontal.jpg",
    "Logo_cropped.jpg",
    "jirawla_logo_wide.png"
]

for f in to_delete:
    p = os.path.join(base_dir, f)
    if os.path.exists(p):
        os.remove(p)
        print(f"Deleted {f}")

# Create assets folder
if not os.path.exists(assets_dir):
    os.makedirs(assets_dir)
    print("Created assets folder")

# Images to move
images_to_move = [
    "Logo_Horizontal_Perfect.png",
    "step_aerial_intervention.jpg",
    "step_coordinated_rescue.jpg",
    "step_drone_deployment.jpg",
    "step_sos_activation.jpg",
    "surveying_capture_drone.jpg",
    "surveying_contour_terrain.jpg",
    "surveying_deliver_field.jpg",
    "surveying_hero_quarry.jpg",
    "surveying_volumetric_base.jpg"
]

for img in images_to_move:
    src = os.path.join(base_dir, img)
    dst = os.path.join(assets_dir, img)
    if os.path.exists(src):
        shutil.move(src, dst)
        print(f"Moved {img} to assets/")

# Update HTML files
html_files = ["index.html", "surveillance-security.html", "surveying-mapping.html"]

for hf in html_files:
    hf_path = os.path.join(base_dir, hf)
    if not os.path.exists(hf_path):
        continue
    
    with open(hf_path, "r", encoding="utf-8") as f:
        content = f.read()
        
    original_content = content
    
    # Replace references to moved images
    for img in images_to_move:
        # We need to replace `src="img"` with `src="assets/img"`
        # Also handle url('img')
        
        # Regex to match exactly the filename in quotes or url()
        # Be careful not to replace it if it's already in assets/
        
        content = re.sub(rf'(src=["\']){img}(["\'])', rf'\1assets/{img}\2', content)
        content = re.sub(rf'(href=["\']){img}(["\'])', rf'\1assets/{img}\2', content)
        content = re.sub(rf'(url\([\'"]?){img}([\'"]?\))', rf'\1assets/{img}\2', content)

    if content != original_content:
        with open(hf_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Updated references in {hf}")
    else:
        print(f"No changes needed in {hf}")

# Verify internal links
print("\nVerifying internal links...")
for hf in html_files:
    hf_path = os.path.join(base_dir, hf)
    if not os.path.exists(hf_path):
        continue
        
    with open(hf_path, "r", encoding="utf-8") as f:
        content = f.read()
        
    links = re.findall(r'href=["\']([^"\']+)["\']', content)
    for link in links:
        # Ignore external links, hashes, etc.
        if link.startswith(("http://", "https://", "mailto:", "tel:", "#", "data:")):
            continue
        
        link_clean = link.split('#')[0].split('?')[0]
        if not link_clean:
            continue
            
        target_path = os.path.join(base_dir, link_clean)
        # Check if the file exists
        if not os.path.exists(target_path):
            print(f"BROKEN LINK in {hf}: {link}")
        
print("Cleanup and verification complete.")
