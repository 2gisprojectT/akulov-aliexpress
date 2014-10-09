__author__ = 'Djonny'
from unittest import TestCase
from numbers import Numbers
import unittest

class NumbersTest(TestCase):
    def test_init(self):
        num = Numbers(1,2,3)
        self.assertEqual(1, num.a, 'A have wrong value')
        self.assertEqual(2, num.b, 'B have wrong value')
        self.assertEqual(3, num.c, 'C have wrong value')
    def test_abs_mult(self):
        num = Numbers(-1,2,1)
        self.assertEqual(2, num.abs_mult(), 'func abs_mult work not correct')
        num1 = Numbers(1,-2,-1)
        self.assertEqual(0, num1.abs_mult(), 'func abs_mult work not correct')
if __name__ == '__main__':
    unittest.main()
