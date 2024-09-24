import unittest
from multiply import multiply_3_numbers

class TestMultiply(unittest.TestCase):
    def test_1(self):
        """Test numbers are multiplied"""
        num1 = 2
        num2 = 3
        num3 = 1
        result = multiply_3_numbers(num1, num2, num3)
        self.assertEqual(result, 6, "Wrong answer")
    
    def test_2(self):
        """Test should take in floats as arguments"""
        result = multiply_3_numbers(2.5, 1.5, 2.0)
        self.assertEqual(result, 7.5)

if __name__ == "main":
    unittest.main()