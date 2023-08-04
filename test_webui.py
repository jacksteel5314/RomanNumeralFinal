import unittest

from roman_numeral_web_server import app

class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.ctx = app.app_context()
        self.ctx.push()
        self.client = app.test_client()

    def tearDown(self):
        self.ctx.pop()

    def test_home(self):
        response = self.client.get("/")
        self.assertEqual(200, response.status_code)
        self.assertEqual("<p>Hello, World!</p>", response.get_data(as_text=True))

    def test_roman_to_decimal(self):
        response = self.client.get("/convert?original=MMMCMXCIX")
        self.assertEqual(200, response.status_code)
        self.assertTrue("MMMCMXCIX converts to 3999" in response.get_data(as_text=True))

    def test_decimal_to_roman(self):
        response = self.client.get("/convert?original=3999")
        self.assertEqual(200, response.status_code)
        self.assertTrue("3999 converts to MMMCMXCIX" in response.get_data(as_text=True))

    def test_error_cases(self):
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
