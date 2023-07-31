from flask import Flask
from flask import request
from flask import render_template
import roman_numerals_lib as roman_nums

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/convert")
def convert():
    value = request.args.get('original', '')
    if value:
        try:
            converted_value = roman_nums.convert(value)
        except ValueError as err:
            print('caught exception')
            return render_template('roman_num_web_form.html', error="true", original=value )
        return render_template('roman_num_web_form.html', converted="true", original=value, converted_value=converted_value)
    else:
        return render_template('roman_num_web_form.html', converted="" )

@app.route("/convert/to_roman/<decimal_value>")
def convert_to_roman(decimal_value):
    return roman_nums.convert(decimal_value)

@app.route("/convert/to_decimal/<roman_value>")
def convert_to_decimal(roman_value):
    return roman_nums.convert(roman_value)
