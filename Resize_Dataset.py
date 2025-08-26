import os
from pathlib import Path
from PIL import Image

SUPPORTED_EXTENSIONS = {".png"}

img_path = "Images/Original_Images/"
resized_img_path = "Images/Resized_Images"

def is_image_file(file_path):
    return Path(file_path).suffix.lower() in SUPPORTED_EXTENSIONS

def resize(root_dir, output_dir):
    images_dir = os.path.join(output_dir, "images")
    masks_dir = os.path.join(output_dir, "masks")
    os.makedirs(images_dir, exist_ok=True)
    os.makedirs(masks_dir, exist_ok=True)

    # Folders list
    all_entries = os.listdir(root_dir)

    # Create folder list
    folders = []
    for entry in all_entries:
        full_path = os.path.join(root_dir, entry)
        if os.path.isdir(full_path):
            folders.append(entry)

    for idx, folder_name in enumerate(folders, start=1):
        current_dir = os.path.join(root_dir, folder_name)
        folder_num = f"{idx:03d}"  # np. 001, 002, 003

        for file_name in os.listdir(current_dir):
            if not is_image_file(file_name):
                continue
            if file_name.endswith("label_viz.png"):
                continue

            full_file_path = os.path.join(current_dir, file_name)
            im = Image.open(full_file_path)

            base_name = os.path.splitext(file_name)[0]

            if base_name == "img":
                new_name = f"img_{folder_num}.png"
                save_path = os.path.join(images_dir, new_name)
            elif base_name == "label":
                new_name = f"label_{folder_num}.png"
                save_path = os.path.join(masks_dir, new_name)
            else:
                continue

            imResize = im.resize((512, 512), Image.LANCZOS)
            imResize.save(save_path, "PNG", quality=90)
            print(f"Saved {save_path}")

def main():
    if not os.path.isdir(img_path):
        print(f"Error: '{img_path}' is not a correct directory")
        return
    os.makedirs(resized_img_path, exist_ok=True)
    resize(img_path, resized_img_path)

if __name__ == "__main__":
    main()