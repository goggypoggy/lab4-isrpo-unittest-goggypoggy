import unittest
import rectangle as figure

class RectangleTestCase(unittest.TestCase):
    '''
    Test for area(a, b)
    '''
    def test_area_plain(self):
        res1 = figure.area(3, 5)
        self.assertEqual(res1, 15)
        
        res2 = figure.area(5, 3)
        self.assertEqual(res2, 15)       

    def test_area_big_values(self):
        res = figure.area(546681, 9799582)
        self.assertEqual(res, 5357245287342)
    
    def test_area_zero_mul(self):
        res00 = figure.area(0, 0)
        self.assertEqual(res00, 0)

        res0A = figure.area(0, 10)
        self.assertEqual(res0A, 0)

        resA0 = figure.area(10, 0)
        self.assertEqual(resA0, 0)
    
    def test_area_neg_sides(self):
        resNA = figure.area(-10, 10)
        self.assertEqual(resNA, None)

        resAN = figure.area(10, -10)
        self.assertEqual(resAN, None)

        resNN = figure.area(-10, -10)
        self.assertEqual(resNN, None)

    '''
    Test for perimeter(a, b)
    '''
    def test_perimeter_plain(self):
        res1 = figure.perimeter(3, 5)
        self.assertEqual(res1, 16)
        
        res2 = figure.perimeter(5, 3)
        self.assertEqual(res2, 16)       

    def test_perimeter_big_values(self):
        res = figure.perimeter(546681, 9799582)
        self.assertEqual(res, 20692526)
    
    def test_perimeter_zero_mul(self):
        res00 = figure.perimeter(0, 0)
        self.assertEqual(res00, 0)

        res0A = figure.perimeter(0, 10)
        self.assertEqual(res0A, 20)

        resA0 = figure.perimeter(10, 0)
        self.assertEqual(resA0, 20)
    
    def test_perimeter_neg_sides(self):
        resNA = figure.perimeter(-10, 10)
        self.assertEqual(resNA, None)

        resAN = figure.perimeter(10, -10)
        self.assertEqual(resAN, None)

        resNN = figure.perimeter(-10, -10)
        self.assertEqual(resNN, None)