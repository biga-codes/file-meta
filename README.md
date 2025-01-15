
---

# file-meta (in progress)

`file-meta` is a Python library designed for extracting and organizing metadata from various file types, such as images, PDFs, and audio files. This tool allows users to easily retrieve and organize file metadata by year, helping streamline the management of large collections of files.

## Features

- Extract metadata from common file types, including images (PNG, JPEG), PDFs, and audio files (MP3).
- Organize files by year based on metadata such as creation date or modification date.
- Supports extracting file-specific metadata such as dimensions (for images), page count (for PDFs), and duration/bitrate (for audio files).

## Installation

### Prerequisites

- Python 3.7+
- pip (Python package installer)

### Install via pip

To install `file-meta` globally using pip, run the following command:

```bash
pip install file-meta
```

### Install from Source

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/file-meta.git
   ```

2. Navigate into the project directory:

   ```bash
   cd file-meta
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Optionally, install `file-meta` globally:

   ```bash
   python setup.py install
   ```

## Usage

### Organizing Metadata by Year

The main feature of `file-meta` is organizing files by year based on their metadata. You can extract metadata for a file and organize it into directories based on its year of creation or modification. Here’s an example of how to organize your files:

### Programmatic Usage

You can use `file-meta` in your Python scripts to extract and organize metadata by year. Below is an example script that organizes files by their creation year:

```python
import os
from file_meta.metadata import get_image_metadata, get_pdf_metadata, get_audio_metadata

def organize_files_by_year(file_paths):
    file_metadata = {}

    for file_path in file_paths:
        file_extension = file_path.split('.')[-1].lower()

        if file_extension in ['jpg', 'jpeg', 'png']:
            metadata = get_image_metadata(file_path)
        elif file_extension == 'pdf':
            metadata = get_pdf_metadata(file_path)
        elif file_extension == 'mp3':
            metadata = get_audio_metadata(file_path)
        else:
            continue  # Skip unsupported file types

        # Extract creation year from metadata (or other suitable field)
        creation_year = metadata.get("year")  # Modify this as per actual metadata field
        if creation_year:
            if creation_year not in file_metadata:
                file_metadata[creation_year] = []
            file_metadata[creation_year].append(file_path)

    # Organize files into directories by year
    for year, files in file_metadata.items():
        year_dir = f"organized_files/{year}"
        os.makedirs(year_dir, exist_ok=True)
        for file in files:
            os.rename(file, os.path.join(year_dir, os.path.basename(file)))

    print("Files have been organized by year.")

# Example usage:
organize_files_by_year(["example-image.jpg", "document.pdf", "music.mp3"])
```

In this example, files are organized into directories named after their creation year, based on the extracted metadata. Modify the metadata extraction logic to pull the `year` information correctly based on each file type.

### Supported File Types and Metadata

- **Images (e.g., JPG, PNG):** Extracts image dimensions (width, height), format, and mode.
- **PDF Files:** Extracts the author and page count, with the potential to add more metadata (such as creation date).
- **Audio (MP3):** Extracts the duration and bitrate of the audio file.

### Example Code for Metadata Extraction:

Here’s how you can extract metadata for different file types:

#### Image Metadata:

```python
from file_meta.metadata import get_image_metadata

image_metadata = get_image_metadata("example-image.jpg")
print(image_metadata)
```

#### PDF Metadata:

```python
from file_meta.metadata import get_pdf_metadata

pdf_metadata = get_pdf_metadata("example-document.pdf")
print(pdf_metadata)
```

#### Audio Metadata:

```python
from file_meta.metadata import get_audio_metadata

audio_metadata = get_audio_metadata("example-audio.mp3")
print(audio_metadata)
```

## Contributing

We welcome contributions! To contribute to the project:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and test them.
4. Submit a pull request describing your changes.

Please ensure that all code adheres to the existing coding style and that any new features are properly documented.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

