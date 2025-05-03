import unittest
import os
from PIL import Image
from src.utils.image_loader import load_image
from src.utils.image_saver import save_image

class TestImageUtils(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """
        Creates a test image file and sets up file paths for use in image utility tests.
        
        This class method runs once before all tests in the class, generating a 100x100 blue RGB image and saving it to disk.
        """
        cls.test_image_path = "test_image.jpg"
        cls.test_output_path = "test_output/test_image_saved.jpg"

        image = Image.new("RGB", (100, 100), color="blue")
        image.save(cls.test_image_path)

    @classmethod
    def tearDownClass(cls):
        """
        Cleans up test files and directories created during the test run.
        
        Removes the test image file, output image file, and output directory if they exist after all tests have completed.
        """
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
        """
        Tests that loading a non-existent image file raises a FileNotFoundError.
        """
        with self.assertRaises(FileNotFoundError):
            load_image("non_existing_image.jpg")

    def test_save_image_success(self):
        """
        Tests that saving an image to a specified path creates the output file successfully.
        """
        image = Image.new("RGB", (50, 50), color="red")
        save_image(image, self.test_output_path)
        self.assertTrue(os.path.exists(self.test_output_path))

if __name__ == "__main__":
    unittest.main()
