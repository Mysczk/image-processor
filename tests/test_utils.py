import unittest
import os
from PIL import Image
from src.utils.image_loader import load_image
from src.utils.image_saver import save_image

class TestImageUtils(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.test_image_path = "test_image.jpg"
        cls.test_output_path = "test_output/test_image_saved.jpg"

        image = Image.new("RGB", (100, 100), color="blue")
        image.save(cls.test_image_path)

    @classmethod
    def tearDownClass(cls):
        if os.path.exists(cls.test_image_path):
            os.remove(cls.test_image_path)
        if os.path.exists(cls.test_output_path):
            os.remove(cls.test_output_path)
        if os.path.exists(os.path.dirname(cls.test_output_path)):
            os.rmdir(os.path.dirname(cls.test_output_path))

    def test_load_image_success(self):
        image = load_image(self.test_image_path)
        self.assertIsInstance(image, Image.Image)

    def test_load_image_file_not_found(self):
        with self.assertRaises(FileNotFoundError):
            load_image("non_existing_image.jpg")

    def test_save_image_success(self):
        image = Image.new("RGB", (50, 50), color="red")
        save_image(image, self.test_output_path)
        self.assertTrue(os.path.exists(self.test_output_path))

if __name__ == "__main__":
    unittest.main()
