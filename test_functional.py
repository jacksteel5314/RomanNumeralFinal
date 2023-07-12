import unittest
import roman_numerals_lib as roman_nums

class TestRomanToDecimal(unittest.TestCase):

    def test_sanity(self):
        self.assertEqual(roman_nums.rom_num_func('I'), 1)

    def test_thorough(self):
        test_one = "MDCLXVI"
        self.assertTrue(roman_nums.valid_entry_f(test_one))
        self.assertEqual(roman_nums.rom_num_func(test_one), 1666)
        test_two = "IXI"
        self.assertFalse(roman_nums.valid_entry_f(test_two))
        test_three = "VV"
        self.assertFalse(roman_nums.valid_entry_f(test_three))
        test_four = "XIV"
        self.assertTrue(roman_nums.valid_entry_f(test_four))
        self.assertEqual(roman_nums.rom_num_func(test_four), 14)
        test_five = "IIII"
        self.assertFalse(roman_nums.valid_entry_f(test_five))
        test_six = "     i      X     " 
        self.assertTrue(roman_nums.valid_entry_f(test_six))
        self.assertEqual(roman_nums.rom_num_func(test_six), 9)
        test_seven = "IM"
        self.assertFalse(roman_nums.valid_entry_f(test_seven))

class TestDecimalToRoman(unittest.TestCase):

    def test_sanity(self):
        self.assertEqual(roman_nums.numerical(1), 'I')

    def test_thorough(self):
        test_one = 4
        self.assertTrue(roman_nums.valid_entry_f(test_one))
        self.assertEqual(roman_nums.numerical(test_one), "IV")
        test_two = 999
        self.assertTrue(roman_nums.valid_entry_f(test_two))
        self.assertEqual(roman_nums.numerical(test_two), "CMXCIX")
        test_three = 1342
        self.assertTrue(roman_nums.valid_entry_f(test_three))
        self.assertEqual(roman_nums.numerical(test_three), "MCCCXLII")
        test_four = "   2   "
        self.assertTrue(roman_nums.valid_entry_f(test_four))
        self.assertEqual(roman_nums.numerical(test_four), "II")
        test_five= "    2  V"
        self.assertFalse(roman_nums.valid_entry_f(test_five))
        

if __name__ == '__main__':
    unittest.main()

