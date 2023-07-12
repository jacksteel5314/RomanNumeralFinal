# Function for Converting Roman Numerals into umbers
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

# Entry Validity 
def valid_entry_f(value):
    value = str(value)
    value = value.upper().strip().replace(" ", "")
    if value[0].isnumeric():
        for i in value:
            if i.isnumeric():
                continue
            else:
                return False
    elif value[0].isalpha():
        for i in range(len(value)):
            if value[i].isalpha():
                if value[i] in dictionary.keys():
                    if i == 0:
                        continue
                    else:
                        if (dictionary.get(value[i-1]) * 10) < (dictionary.get(value[i])):
                            return False
                        else:
                            if (value[i-1] == value[i]) & ((value[i] == "V" )| (value[i] == "L") | (value[i] == "D")):
                                return False
                            else:
                                if i == len(value) - 1:
                                    continue
                                else:
                                    if dictionary.get(value[i-1]) == dictionary.get(value[i+1]) & (dictionary.get(value[i-1]) != dictionary.get(value[i])):
                                        return False
                else:
                    return False
            else:
                return False
                
    else:
        return False
    return True

