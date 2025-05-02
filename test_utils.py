import unittest
from utils import lorenz_step, hsv_to_rgb
from matrix import matrix_multiplication


# Тестування функції hsv_to_rgb
class TestColorConversion(unittest.TestCase):
    def test_hsv_to_rgb_red(self):
        self.assertEqual(hsv_to_rgb(0, 1, 1), (255, 0, 0))

    def test_hsv_to_rgb_green(self):
        self.assertEqual(hsv_to_rgb(1 / 3, 1, 1), (0, 255, 0))


# Тестування функції matrix_multiplication
class TestMatrixMultiplication(unittest.TestCase):
    def test_multiply_with_identity(self):
        a = [[1, 0], [0, 1]]
        b = [[5, 6], [7, 8]]
        result = matrix_multiplication(a, b)
        self.assertEqual(result, b)

    def test_incompatible_dimensions(self):
        a = [[1, 2], [5, 6]]
        b = [[3, 4]]
        with self.assertRaises(ValueError):
            matrix_multiplication(a, b)


# Тестування функції lorenz_step
class TestLorenzStep(unittest.TestCase):
    def test_output_type_and_length(self):
        x, y, z = 0.01, 0.0, 0.0
        result = lorenz_step(x, y, z, 10, 28, 8 / 3, 0.01)
        self.assertIsInstance(result, tuple)
        self.assertEqual(len(result), 3)
        self.assertTrue(all(isinstance(v, float) for v in result))

    def test_known_output_range(self):
        x, y, z = 1.0, 1.0, 1.0
        x1, y1, z1 = lorenz_step(x, y, z, 10, 28, 8 / 3, 0.01)
        self.assertAlmostEqual(x1, 1.0, delta=0.05)
        self.assertAlmostEqual(y1, 1.26, delta=0.1)
        self.assertAlmostEqual(z1, 0.91, delta=0.1)


if __name__ == "__main__":
    unittest.main()
