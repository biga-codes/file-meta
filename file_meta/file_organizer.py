# file-meta/file_meta/file_organizer.py
import os
import shutil
from file_meta.metadata import get_image_metadata

def organize_files_by_resolution(files, target_dir="organized_files"):
    for file in files:
        metadata = get_image_metadata(file)
        resolution = f"{metadata['width']}x{metadata['height']}"
        resolution_folder = os.path.join(target_dir, resolution)
        os.makedirs(resolution_folder, exist_ok=True)
        shutil.move(file, os.path.join(resolution_folder, os.path.basename(file)))
