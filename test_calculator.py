import unittest
from calculator import add, subtract, multiply, divide


class CalculatorTestCase(unittest.TestCase):

    def test_add(self):
        """Тест сложения"""
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(10, 5), 15)
        self.assertEqual(add(-1, 1), 0)

    def test_subtract(self):
        """Тест вычитания"""
        self.assertEqual(subtract(10, 5), 5)
        self.assertEqual(subtract(5, 10), -5)
        self.assertEqual(subtract(0, 0), 0)

    def test_multiply(self):
        """Тест умножения"""
        self.assertEqual(multiply(3, 4), 12)
        self.assertEqual(multiply(5, 0), 0)
        self.assertEqual(multiply(-2, 3), -6)

    def test_divide(self):
        """Тест деления"""
        self.assertEqual(divide(10, 2), 5)
        self.assertEqual(divide(9, 3), 3)
        self.assertAlmostEqual(divide(7, 2), 3.5)

    def test_divide_by_zero(self):
        """Тест деления на ноль"""
        with self.assertRaises(ValueError):
            divide(10, 0)


if __name__ == '__main__':
    unittest.main()