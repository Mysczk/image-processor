import unittest
from PIL import Image
import numpy as np
from src.math_utils import convolution, histogram_equalization, edge_detection

class TestMathUtils(unittest.TestCase):

    def setUp(self):
        self.image = Image.fromarray(np.random.randint(0, 256, (10, 10), dtype=np.uint8))

    def test_convolution(self):
        kernel = np.array([[0, -1, 0],
                           [-1, 5, -1],
                           [0, -1, 0]])
        result = convolution.apply_convolution(self.image, kernel)
        self.assertIsInstance(result, Image.Image)

    def test_histogram_equalization(self):
        result = histogram_equalization.equalize_histogram(self.image)
        self.assertIsInstance(result, Image.Image)
        # Additional tests to verify correctness
        # 1. Check that output dimensions match input dimensions
        self.assertEqual(result.size, self.image.size)
        
        # 2. Create test image with low contrast and verify improvement
        low_contrast = np.ones((10, 10), dtype=np.uint8) * 127
        low_contrast[3:7, 3:7] = 130  # Slightly higher values in center
        low_contrast_img = Image.fromarray(low_contrast)
        
        equalized = histogram_equalization.equalize_histogram(low_contrast_img)
        equalized_array = np.array(equalized)
        
        # Verify contrast has been expanded
        original_range = np.max(low_contrast) - np.min(low_contrast)
        equalized_range = np.max(equalized_array) - np.min(equalized_array)
        self.assertGreater(equalized_range, original_range)

    def test_edge_detection(self):
        result = edge_detection.detect_edges(self.image)
        self.assertIsInstance(result, Image.Image)

if __name__ == "__main__":
    unittest.main()
