# Roman numerals had no way to represent 0, and the largest value
# they could represent was 3,999.
MIN_ROMAN = 1
MAX_ROMAN = 3999


# Function for Converting Roman Numerals into numbers
dictionary = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
def rom_num_func(value):
    value = value.upper().strip().replace(" ", "")
    if len(value) == 1: 
        return dictionary.get(value)
    sum = 0
    i = 0
    while i < len(value):
        if i == (len(value) - 1):
            sum = sum + dictionary.get(value[i])
            i = i + 1
        elif dictionary.get(value[i]) < dictionary.get(value[i+1]):
            sum = sum + dictionary.get(value[i+1]) - dictionary.get(value[i])
            i = i + 2
        else:
            sum = sum + dictionary.get(value[i])
            i = i + 1
    return sum


# Function for Converting Numbers into Roman Numerals 
dict_num = {1:"I", 5:"V", 10:"X", 50:"L", 100:"C", 500:"D", 1000:"M"}
def numerical(value):
    num_str = str(value).strip().replace(" ", "")
    rev_num = num_str[::-1]
    multiplier = 1
    roman_numeral = ""
    for i in rev_num: 
        i = int(i)
        div_five = i//5
        if (i == 4) | (i==9):
            roman_numeral = dict_num.get(multiplier) + dict_num.get((i+1) * multiplier) + roman_numeral
        elif div_five == 0:
            roman_numeral = (i * dict_num.get(multiplier)) + roman_numeral
        else:
            leftover = i - 5
            roman_numeral = dict_num.get(5 * multiplier) + (leftover * dict_num.get(multiplier)) + roman_numeral
        multiplier = multiplier * 10
    return roman_numeral

# Validate and convert supplied value
# thows exception if supplied value is invalid
# returns converted decimal or roman numeral
def convert(value):
    # start with generic validation
    value = str(value)
    value = value.upper().strip().replace(" ", "")
    if not value:
        raise ValueError("Trying to convert a NULL value.")
    # handle decimal-to-roman case, first validate, then convert
    if value.isnumeric():
        value = int(value)
        if value < MIN_ROMAN or value > MAX_ROMAN:
            raise ValueError("Roman numerals can only represet numbers in the range [{},{}].".format(MIN_ROMAN, MAX_ROMAN))
        return numerical(value)
    if not value.isalpha():
        raise ValueError("This method can only convert a purely decimal or purely roman numeral to its counterpart.")
    # handle roman-to-decimal case, first validate, then convert
    for i in range(1, len(value)):
        if value[i] in dictionary.keys():
            if len(value) - i >= 3:
                if (value[i-1] == value[i]) & (value[i] == value[i+1]) & (value[i+1] == value[i+2]):
                    raise ValueError("Invalid roman numeral: 4 or more letter repeats are not allowed.")
            if (dictionary.get(value[i-1]) * 10) < (dictionary.get(value[i])):
                raise ValueError("Invalid roman numeral: '{}{}' invalid prefix decrement / values not decreasing.".format(value[i-1], value[i]))
            if (value[i-1] == value[i]) & ((value[i] == "V" )| (value[i] == "L") | (value[i] == "D")):
                raise ValueError("Invalid roman numeral: Repeating non-repeatable character {}.".format(value[i]))
            if ((dictionary.get(value[i-1])) < dictionary.get(value[i])) & ((value[i-1] == "V") | (value[i-1] == "L") | (value[i-1] == "D")):
                raise ValueError("Invalid roman numeral: Cannot prefix-decrement with {} character.".format(value[i-1]))
            if i == len(value) - 1:
                continue
            if (dictionary.get(value[i-1]) == dictionary.get(value[i+1])) & (dictionary.get(value[i-1]) != dictionary.get(value[i])) & ((value[i-1] != "X") & (value[i-1] != "C") & (value[i-1] != "M")):
                raise ValueError("Invalid roman numeral {}: Cannot prefix-decrement and suffix-increment, {} character is doing so.".format(value, value[i-1]))
        else:
            raise ValueError("Roman numerals are only comprised of {} characters.".format(dictionary.keys()))
    return rom_num_func(value)
