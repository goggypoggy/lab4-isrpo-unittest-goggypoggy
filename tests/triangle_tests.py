import unittest
import triangle as figure

class TriangleTestCase(unittest.TestCase):
    '''
    Tests for area(a, h)
    '''
    def test_area_plain(self):
        res1 = figure.area(3, 5)
        self.assertAlmostEqual(res1, 7.5)
        
        res2 = figure.area(5, 3)
        self.assertAlmostEqual(res2, 7.5)       

    def test_area_big_values(self):
        res = figure.area(9090284, 444182)
        self.assertAlmostEqual(res, 2018870263844)
    
    def test_area_zero_mul(self):
        res00 = figure.area(0, 0)
        self.assertEqual(res00, 0)

        res0A = figure.area(0, 10)
        self.assertEqual(res0A, 0)

        resA0 = figure.area(10, 0)
        self.assertEqual(resA0, 0)
    
    def test_area_neg_values(self):
        resNA = figure.area(-10, 10)
        self.assertEqual(resNA, None)

        resAN = figure.area(10, -10)
        self.assertEqual(resAN, None)

        resNN = figure.area(-10, -10)
        self.assertEqual(resNN, None)
    
    '''
    Tests for perimeter(a, b, c)
    '''
    def test_perimeter_plain(self):
        res = figure.perimeter(3, 4, 5)
        self.assertEqual(res, 12)
    
    def test_perimeter_impossible_triangle(self):
        res1 = figure.perimeter(1, 10, 15)
        self.assertEqual(res1, None)

        res2 = figure.perimeter(10, 1, 15)
        self.assertEqual(res2, None)

        res3 = figure.perimeter(10, 15, 1)
        self.assertEqual(res3, None)

    def test_perimeter_zero_side_possible(self):
        res1 = figure.perimeter(0, 10, 10)
        self.assertEqual(res1, 20)

        res2 = figure.perimeter(10, 0, 10)
        self.assertEqual(res2, 20)

        res3 = figure.perimeter(10, 10, 0)
        self.assertEqual(res3, 20)
    
    def test_perimeter_zero_side_impossible(self):
        res1 = figure.perimeter(0, 10, 15)
        self.assertEqual(res1, None)

        res2 = figure.perimeter(10, 0, 15)
        self.assertEqual(res2, None)

        res3 = figure.perimeter(10, 15, 0)
        self.assertEqual(res3, None)
    
    def test_perimeter_multiple_zeroes_possible(self):
        res = figure.perimeter(0, 0, 0)
        self.assertEqual(res, 0)
    
    def test_perimeter_multiple_zeroes_impossible(self):
        res1 = figure.perimeter(10, 0, 0)
        self.assertEqual(res1, None)

        res2 = figure.perimeter(0, 10, 0)
        self.assertEqual(res2, None)

        res3 = figure.perimeter(0, 0, 10)
        self.assertEqual(res3, None)
    
    def test_perimeter_neg_sides(self):
        res1 = figure.perimeter(-1, 10, 10)
        self.assertEqual(res1, None)

        res2 = figure.perimeter(10, -1, 10)
        self.assertEqual(res2, None)

        res3 = figure.perimeter(10, 10, -1)
        self.assertEqual(res3, None)

        res4 = figure.perimeter(-3, -4, -5)
        self.assertEqual(res4, None)

        res5 = figure.perimeter(-10, -10, 10)
        self.assertEqual(res5, None)
    
    def test_perimeter_big_values(self):
        res = figure.perimeter(33333333, 44444444, 55555555)
        self.assertEqual(res, 133333332)