import unittest
import roman_numerals_lib as roman_nums

class TestRomanToDecimal(unittest.TestCase):

    def test_sanity(self):
        self.assertEqual(roman_nums.convert('I'), 1)

    def test_error_cases(self):
        error_cases = ["IXI","VV","IIII","IM","VXV"]
        for case in error_cases:
            with self.assertRaises(ValueError):
                roman_nums.convert(case)

    def test_specific_cases(self):
        test_cases = [("MDCLXVI",1666), ("XIV",14), ("     i      X     ",9)]
        for roman, decimal in test_cases:
            self.assertEqual(roman_nums.convert(roman), decimal)


class TestDecimalToRoman(unittest.TestCase):

    def test_sanity(self):
        self.assertEqual(roman_nums.numerical(1), 'I')

    def test_error_cases(self):
        error_cases = ["    2  V","-1","0","4000"]
        for case in error_cases:
            with self.assertRaises(ValueError):
                roman_nums.convert(case)

    def test_specific_cases(self):
        test_cases = [(4,"IV"), (999,"CMXCIX"), (1342,"MCCCXLII"),("   2   ","II")]
        for roman, decimal in test_cases:
            self.assertEqual(roman_nums.convert(roman), decimal)


class TestLoopback(unittest.TestCase):
    def test_loopback(self):
        for n in range(1,3999):
            roman = roman_nums.convert(n)
            decimal = roman_nums.convert(roman)
            self.assertEqual(n, decimal)
        

if __name__ == '__main__':
    unittest.main()
