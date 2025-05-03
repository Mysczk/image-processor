import unittest
from PIL import Image, ImageChops
from src.filters import grayscale, sepia, invert

class TestFilters(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.test_image = Image.new("RGB", (50, 50), color="blue")

    def test_apply_grayscale(self):
        result = grayscale.apply_grayscale(self.test_image)
        self.assertEqual(result.mode, "L")

    def test_apply_sepia(self):
        result = sepia.apply_sepia(self.test_image.copy())
        self.assertEqual(result.mode, "RGB")

    def test_apply_invert(self):
        inverted = invert.apply_invert(self.test_image)
        difference = ImageChops.difference(inverted, self.test_image)
        self.assertFalse(difference.getbbox() is None)

if __name__ == "__main__":
    unittest.main()
