import unittest
import square as figure

class SquareTestCase(unittest.TestCase):
    '''
    Test for area(a)
    '''
    def test_area_plain(self):
        res = figure.area(5)
        self.assertEqual(res, 25)       

    def test_area_big_value(self):
        res = figure.area(8804386)
        self.assertEqual(res, 77517212836996)
    
    def test_area_zero_mul(self):
        res = figure.area(0)
        self.assertEqual(res, 0)
    
    def test_area_neg_side(self):
        res = figure.area(-10)
        self.assertEqual(res, None)

    '''
    Test for perimeter(a)
    '''
    def test_perimeter_plain(self):
        res = figure.perimeter(5)
        self.assertEqual(res, 20)       

    def test_perimeter_big_value(self):
        res = figure.perimeter(8804386)
        self.assertEqual(res, 35217544)
    
    def test_perimeter_zero_mul(self):
        res = figure.perimeter(0)
        self.assertEqual(res, 0)
    
    def test_perimeter_neg_side(self):
        res = figure.perimeter(-10)
        self.assertEqual(res, None)