# file-meta/file_meta/metadata.py
from PIL import Image

def get_image_metadata(file_path):
    with Image.open(file_path) as img:
        return {
            "width": img.width,
            "height": img.height,
            "format": img.format,
            "mode": img.mode
        }


# file-meta/file_meta/metadata.py
from PyPDF2 import PdfFileReader

def get_pdf_metadata(file_path):
    with open(file_path, 'rb') as file:
        pdf = PdfFileReader(file)
        return {
            "author": pdf.getDocumentInfo().author,
            "page_count": pdf.getNumPages()
        }

# file-meta/file_meta/metadata.py
from mutagen.mp3 import MP3

def get_audio_metadata(file_path):
    audio = MP3(file_path)
    return {
        "duration": audio.info.length,  # Duration in seconds
        "bitrate": audio.info.bitrate  # Bitrate in kbps
    }
