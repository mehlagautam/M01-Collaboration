import unittest
from fractions import Fraction

from my_sum import sum


class TestSum(unittest.TestCase):
    def test_list_int(self):
        """
        Test that it can sum a list of integers
        """
        data = [1, 2, 3]
        result = sum(data)
        self.assertEqual(result, 6)

    def test_list_fraction(self):
        """
        Test that it can sum a list of fractions
        """
        data = [Fraction(1, 4), Fraction(1, 4), Fraction(2, 5)]
        result = sum(data)
        self.assertEqual(result, 1)

if __name__ == '__main__':
    unittest.main()


#The output gives the details about which line is the problem, a trackback of the failing line.
#name of the test method, which is test_list Fraction and
#The details of the assertion with the expected result (1) and the actual result (Fraction(9, 10))