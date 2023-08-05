'''
This is a gui to convert roman numerals
'''


import roman_numerals_lib as roman_nums


# Main Method
def main():
    '''
    Main Method
    '''
    print("Welcome to the Roman Numeral Converter")
    while True:
        value = input("Input a Roman Numeral or Number: \n")

        # Checking Validity
        value = value.upper().strip().replace(" ", "")
        try:
            conversion = roman_nums.convert(value)
        except ValueError as err:
            print("Your Entry was Invalid. Try Again")
            print(err)
            continue

        print("Check the Results File")

        # Writing in a New File
        conversion = str(conversion)
        with open ("Results.txt", "w", encoding="utf-8") as result_file:
            result_file.write("You inputted the value: " + value + "\n")
            result_file.write("Your result was: " + conversion)
            result_file.close()
            break


if __name__ == '__main__':
    main()
