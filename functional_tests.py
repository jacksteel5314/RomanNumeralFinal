import unittest
import roman_numerals_lib as roman_nums

class TestRomanToDecimal(unittest.TestCase):

    def test_sanity(self):
        self.assertEqual(roman_nums.rom_num_func('I'), 1)

    def test_thorough(self):
        # TODO flesh this out
        self.assertFalse(roman_nums.valid_entry_f("IXI"))

class TestDecimalToRoman(unittest.TestCase):

    def test_sanity(self):
        self.assertEqual(roman_nums.numerical(1), 'I')

    def test_thorough(self):
        # TODO flesh this out
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()

