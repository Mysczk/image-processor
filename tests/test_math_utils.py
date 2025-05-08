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

    def test_edge_detection(self):
        result = edge_detection.detect_edges(self.image)
        self.assertIsInstance(result, Image.Image)

if __name__ == "__main__":
    unittest.main()
