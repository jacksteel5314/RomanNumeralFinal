"""
This is a CLI (command line interface) to convert roman numerals
"""


import argparse
import sys
import roman_numerals_lib as roman_nums


# Main Method
def main():
    """
    Main Method
    """
    parser = argparse.ArgumentParser(
        description="Input a roman numeral or decimal and output will be its coversion."
    )
    parser.add_argument(
        "input_value", help="The decimal or roman numeral to be converted"
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="for more verbose output on invalid inputs",
    )
    args = parser.parse_args()

    value = args.input_value

    # Checking Validity
    value = value.upper().strip().replace(" ", "")
    try:
        conversion = roman_nums.convert(value)
    except ValueError as err:
        if args.verbose:
            print(err, file=sys.stderr)
            return
    conversion = str(conversion)
    print(conversion)


if __name__ == "__main__":
    main()
