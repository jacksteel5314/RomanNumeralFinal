'''
Checks validity of number or roman numeral and converts it
'''

# Validate and convert supplied value
# thows exception if supplied value is invalid
# returns converted decimal or roman numeral
# pylint: disable=line-too-long

def convert(value):
    '''
    Validates and converts value 
    '''
    # start with generic validation
    value = str(value)
    value = value.upper().strip().replace(" ", "")
    if not value:
        raise ValueError("Trying to convert a NULL value.")
    # handle decimal-to-roman case, first validate, then convert
    if value.isnumeric():
        value = int(value)
        return _numerical(value)
    if not value.isalpha():
        raise ValueError("This method can only convert a purely decimal or purely roman numeral to its counterpart.")
    # handle roman-to-decimal case, first validate, then convert
    if value[0] not in dictionary.keys():
        raise ValueError(f"Roman numerals are only comprised of {dictionary.keys()} characters.")
    for i in range(1, len(value)):
        if value[i] not in dictionary.keys():
            raise ValueError(f"Roman numerals are only comprised of {dictionary.keys()} characters.")
        if (i+1 < len(value)) & value[i+1] not in dictionary.keys():
            raise ValueError(f"Roman numerals are only comprised of {dictionary.keys()} characters.")
        if len(value) - i >= 3:
            if (value[i-1] == value[i]) & (value[i] == value[i+1]) & (value[i+1] == value[i+2]):
                raise ValueError("Invalid roman numeral: 4 or more letter repeats are not allowed.")
        if (dictionary[value[i-1]] * 10) < (dictionary[value[i]]):
            raise ValueError(f"Invalid roman numeral: '{value[i-1]}{value[i]}' invalid prefix decrement / values not decreasing.")
        if (value[i-1] == value[i]) & ((value[i] == "V" )| (value[i] == "L") | (value[i] == "D")):
            raise ValueError(f"Invalid roman numeral: Repeating non-repeatable character {value[i]}.")
        if ((dictionary[value[i-1]]) < dictionary[value[i]]) & ((value[i-1] == "V") | (value[i-1] == "L") | (value[i-1] == "D")):
            raise ValueError(f"Invalid roman numeral: Cannot prefix-decrement with {value[i-1]} character.")
        if i == len(value) - 1:
            continue
        if (dictionary[value[i-1]] == dictionary[value[i+1]]) & (dictionary[value[i-1]] != dictionary[value[i]]) & ((value[i-1] != "X") & (value[i-1] != "C") & (value[i-1] != "M")):
            raise ValueError(f"Invalid roman numeral {value}: Cannot prefix-decrement and suffix-increment, {value[i-1]} character is doing so.")
    return _rom_num_func(value)


# Function for Converting Roman Numerals into numbers
dictionary = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
def _rom_num_func(value):
    value = value.upper().strip().replace(" ", "")
    if len(value) == 1:
        return dictionary[value]
    sums = 0
    i = 0
    while i < len(value):
        if i == (len(value) - 1):
            sums = sums + dictionary[value[i]]
            i = i + 1
        elif dictionary.get(value[i]) < dictionary.get(value[i+1]):
            sums = sums + dictionary[value[i+1]] - dictionary[value[i]]
            i = i + 2
        else:
            sums = sums + dictionary[value[i]]
            i = i + 1
    return sums


# Function for Converting Numbers into Roman Numerals
def _numerical(value):
    dict_num = {1:"I", 5:"V", 10:"X", 50:"L", 100:"C", 500:"D", 1000:"M"}
    # Roman numerals have no way to represent 0, and the largest value
    # they can represent is 3,999.
    min_roman = 1
    max_roman = 3999

    if value < min_roman or value > max_roman:
        raise ValueError(f"Roman numerals can only represet numbers in the range [{min_roman},{max_roman}].")
    num_str = str(value).strip().replace(" ", "")
    rev_num = num_str[::-1]
    multiplier = 1
    roman_numeral = ""
    for i in rev_num:
        i = int(i)
        div_five = i//5
        if (i == 4) | (i==9):
            roman_numeral = dict_num[multiplier] + dict_num[(i+1) * multiplier] + roman_numeral
        elif div_five == 0:
            roman_numeral = (i * dict_num[multiplier]) + roman_numeral
        else:
            leftover = i - 5
            roman_numeral = dict_num[5 * multiplier] + (leftover * dict_num[multiplier]) + roman_numeral
        multiplier = multiplier * 10
    return roman_numeral
