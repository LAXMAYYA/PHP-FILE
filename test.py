import unittest
import requests
class TestATGWebsite(unittest.TestCase):
    def test_website_loading(self):
        response = requests.get('https://atg.world')
        self.assertEqual(response.status_code, 200)
if __name__ == '__main__':
    unittest.main()
