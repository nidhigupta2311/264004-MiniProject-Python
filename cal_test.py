import unittest
import main

class Calculator_Test(unittest.TestCase):
    def test_Summation(self):
        val = main. find_Summation(10, 20)
        self.assertEqual(val,30)

    def test_Difference(self):
        val = main.find_Difference(200, 390)
        self.assertEqual(val,-190)
        val = main.find_Difference(56, 44)
        self.assertEqual(val,12)


    def test_FloatDivision(self):
        val = main.find_Float_Div(34, 5)
        self.assertEqual(val,6.80)
        self.assertRaises(ZeroDivisionError,
                          main.find_Float_Div, 10, 0)

    def test_IntegerDivision(self):
        val = main.find_Integer_Div(34, 5)
        self.assertEqual(val,6)
        val = main.find_Integer_Div(80, 4)
        self.assertEqual(val,20)
        self.assertRaises(ZeroDivisionError,
                          main.find_Integer_Div, 10, 0)

    def test_Moduluos(self):
        val = main.find_Modulous(80, 5)
        self.assertEqual(val,0)
        val = main.find_Modulous(5, 3)
        self.assertEqual(val, 2)
        self.assertRaises(ZeroDivisionError,
                          main.find_Modulous, 10, 0)
    def test_Product(self):
        val = main.find_Product(4, 6)
        self.assertEqual(val,24)
        val = main.find_Product(96, 63)
        self.assertEqual(val, 6048)
    def test_Power(self):
        val = main.Find_Power(5, 6)
        self.assertEqual(val,15625)
        val = main.Find_Power(16, 1/2)
        self.assertEqual(val, 4)

if __name__ == '__main__':
    unittest.main()
    
