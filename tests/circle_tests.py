import unittest
import circle as figure

class CircleTestCase(unittest.TestCase):
    '''
    Tests for area(r)
    '''
    def test_area_plain(self):
        res = figure.area(5)
        self.assertAlmostEqual(res, 78.53981633974483, 3)
    
    def test_area_big_radius(self):
        res = figure.area(3002912)
        self.assertAlmostEqual(res, 28329250429053.113, 1)
    
    def test_area_zero_mul(self):
        res = figure.area(0)
        self.assertEqual(res, 0)
    
    def test_area_neg_radius(self):
        res = figure.area(-10)
        self.assertEqual(res, None)
    
    '''
    Tests for perimeter(r)
    '''
    def test_perimeter_plain(self):
        res = figure.perimeter(5)
        self.assertAlmostEqual(res, 31.41592653589793, 3)
    
    def test_perimeter_big_radius(self):
        res = figure.perimeter(3002912)
        self.assertAlmostEqual(res, 18867852.557153266, 2)
    
    def test_perimeter_zero_mul(self):
        res = figure.perimeter(0)
        self.assertEqual(res, 0)
    
    def test_perimeter_neg_radius(self):
        res = figure.perimeter(-10)
        self.assertEqual(res, None)