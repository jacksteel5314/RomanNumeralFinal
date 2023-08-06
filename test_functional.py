'''
Unit testing for roman numerals library
'''
import unittest
import roman_numerals_lib as roman_nums

class TestRomanToDecimal(unittest.TestCase):
    '''
    Tests converting a roman numeral to a decimal
    '''

    def test_sanity(self):
        '''
        Ensures that I is equal to 1
        '''
        self.assertEqual(roman_nums.convert('I'), 1)

    def test_error_cases(self):
        '''
        Tests common error roman numeral cases corrected in code
        '''
        error_cases = ["IXI","VV","IIII","IM","VXV"]
        for case in error_cases:
            with self.assertRaises(ValueError):
                roman_nums.convert(case)

    def test_specific_cases(self):
        '''
        Tests specific roman numeral cases that may induce error
        '''
        test_cases = [("MDCLXVI",1666), ("XIV",14), ("     i      X     ",9)]
        for roman, decimal in test_cases:
            self.assertEqual(roman_nums.convert(roman), decimal)


class TestDecimalToRoman(unittest.TestCase):
    '''
    Test converting a decimal to a roman numeral 
    '''
    def test_sanity(self):
        '''
        Ensures 1 is equal to I
        '''
        self.assertEqual(roman_nums.convert(1), 'I')

    def test_error_cases(self):
        '''
        Ensures code doesn't try to convert error cases
        '''
        error_cases = ["    2  V","-1","0","4000"]
        for case in error_cases:
            with self.assertRaises(ValueError):
                roman_nums.convert(case)

    def test_specific_cases(self):
        '''
        Ensures specific decimal cases are converted to correct value
        '''
        test_cases = [(4,"IV"), (999,"CMXCIX"), (1342,"MCCCXLII"),("   2   ","II")]
        for roman, decimal in test_cases:
            self.assertEqual(roman_nums.convert(roman), decimal)


class TestLoopback(unittest.TestCase):
    '''
    Has test_loopback method
    '''
    def test_loopback(self):
        '''
        Tests that the code correctly converts a decimal to a roman numeral and back
        '''
        for number in range(1,3999):
            roman = roman_nums.convert(number)
            decimal = roman_nums.convert(roman)
            self.assertEqual(number, decimal)


if __name__ == '__main__':
    unittest.main()
