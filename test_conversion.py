import unittest
from conversion import convertX, convertY

class TestConversion(unittest.TestCase):

    def testConvertX(self):
        test_cases = [
            (0.5496, 2.04943),
            (0.5556, 2.07181),
            (0.5616, 2.09418),
        ]
        for case in test_cases:
            input, expected = case
            actual = convertX(input)
            self.assertEqual(actual, expected)
    
    def testConvertY(self):
        maxValue = 1080000.0
        test_cases = [
            (212.85096, 1.97E-04),
            (206.326,   1.91E-04),
            (194.82697, 1.80E-04),
            (1174.2904, 1.09E-03),
            (2290.4461, 0.00212)
        ]
        for case in test_cases:
            input, expected = case
            actual = convertY(input, maxValue)
            print(f"expected: {expected} actual: {actual}")
            self.assertAlmostEqual(actual, expected)    

if __name__ == "main":
    unittest.main()