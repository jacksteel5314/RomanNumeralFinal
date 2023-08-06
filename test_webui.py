'''
Testing Webpage
'''
import unittest

from roman_numeral_web_server import app

class AppTestCase(unittest.TestCase):
    '''
    Tests the functioning of the webui
    '''
    def setUp(self):
        '''
        Runs before the test can begin 
        '''
        self.ctx = app.app_context()
        self.ctx.push()
        self.client = app.test_client()

    def tearDown(self):
        '''
        Runs after the test is finished
        '''
        self.ctx.pop()

    def test_home(self):
        '''
        Ensures that when there is nothing after the slash, that the correct page and method pops up
        '''
        response = self.client.get("/")
        self.assertEqual(200, response.status_code)
        self.assertEqual("<p>Hello, World!</p>", response.get_data(as_text=True))

    def test_roman_to_decimal(self):
        '''
        Ensures that a roman numeral is being correctly converted 
        to a decimal with the right message on the webpage
        '''
        response = self.client.get("/convert?original=MMMCMXCIX")
        self.assertEqual(200, response.status_code)
        self.assertTrue("MMMCMXCIX converts to 3999" in response.get_data(as_text=True))

    def test_decimal_to_roman(self):
        '''
        Ensures that a decimal is being correctly converted to a 
        roman numeral with the right message on the webpage
        '''
        response = self.client.get("/convert?original=3999")
        self.assertEqual(200, response.status_code)
        self.assertTrue("3999 converts to MMMCMXCIX" in response.get_data(as_text=True))

    def test_error_cases(self):
        '''
        Testing error cases on the webpage and ensuring the correct message appears
        '''
        response = self.client.get("/convert?original=4000")
        self.assertEqual(200, response.status_code)
        self.assertTrue("4000 cannot be converted, try again" in response.get_data(as_text=True))
        response = self.client.get("/convert?original=VV")
        self.assertEqual(200, response.status_code)
        self.assertTrue("VV cannot be converted, try again" in response.get_data(as_text=True))
        response = self.client.get("/convert?original=ABC")
        self.assertEqual(200, response.status_code)
        self.assertTrue("ABC cannot be converted, try again" in response.get_data(as_text=True))

if __name__ == "__main__":
    unittest.main()
