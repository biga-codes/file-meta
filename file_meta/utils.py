# file-meta/file_meta/utils.py
from file_meta.metadata import get_image_metadata

def filter_files_by_resolution(files, min_width=0, min_height=0):
    return [file for file in files if get_image_metadata(file)["width"] >= min_width and get_image_metadata(file)["height"] >= min_height]


# file-meta/file_meta/utils.py
import json

def export_metadata_to_json(files, output_file="metadata.json"):
    metadata_list = [get_image_metadata(file) for file in files]
    with open(output_file, "w") as f:
        json.dump(metadata_list, f, indent=4)


