# https://github.com/ChaliceofInk/lab10-RR-BF.git
# Partner 1: Russell Richter
# Partner 2: Brendan Fries
import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self):
        self.assertEqual(add(3, 2), 5, 'add(3, 2)')

    def test_subtract(self): # 3 assertions
        self.assertEqual(subtract(4, 2), 2, 'subtract(4, 2)')
        self.assertEqual(subtract(10, 5), 5, 'subtract(10, 5)')
        self.assertEqual(subtract(3, 7), -4, 'subtract(10, 5)')
        
    # ##########################

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(2, 4), 8, 'mul(2, 4)')
    def test_divide(self): # 3 assertions
        self.assertEqual(div(4, 2), 2, 'div(4, 2)')
     ##########################

    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
    #     # call division function inside, example:
         with self.assertRaises(ValueError):
            div(5, 0)

    def test_logarithm(self): # 3 assertions
         self.assertAlmostEqual(logarithm(100, 10), 2, 'log(100, 10)')
         self.assertAlmostEqual(logarithm(8, 2), 3, 'log(8, 2)')
         self.assertAlmostEqual(logarithm(1, 10), 0, 'log(1, 10)')

    def test_log_invalid_base(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(10, 1)
    # ##########################
    
    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        # call log function inside, example:
        # with self.assertRaises(<INSERT_ERROR_TYPE>):
        #     logarithm(0, 5)
        with self.assertRaises(ValueError):
            logarithm(0, 5)

    def test_hypotenuse(self): # 3 assertions
        self.assertEqual(hypotenuse(3, 4), 5, 'hypotenuse(3, 4)')
        self.assertEqual(hypotenuse(3, -4), 5, 'hypotenuse(3, -4)')
        self.assertAlmostEqual(float(hypotenuse(2, 2)), float(2.828427125))
    def test_sqrt(self): # 3 assertions
        # Test for invalid argument, example:
        # with self.assertRaises(<INSERT_ERROR_TYPE>):
        #    square_root(NUM)
        # Test basic function
        with self.assertRaises(ValueError):
            square_root(-9)
        self.assertEqual(square_root(4), 2, 'square_root(4)')
        self.assertEqual(square_root(16), 4, 'square_root(16)')
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()
