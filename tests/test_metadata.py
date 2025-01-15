# file-meta/tests/test_metadata.py
import unittest
import os
from file_meta.metadata import get_image_metadata, get_video_metadata, get_pdf_metadata, get_audio_metadata
from file_meta.file_organizer import organize_files_by_year

class TestFileMeta(unittest.TestCase):

    def test_get_image_metadata(self):
        # Ensure that the test image exists
        test_image_path = "helloo.jpg"
        metadata = get_image_metadata(test_image_path)
        self.assertEqual(metadata["format"], "JPEG")
        self.assertGreater(metadata["width"], 0)
        self.assertGreater(metadata["height"], 0)


if __name__ == "__main__":
    unittest.main()