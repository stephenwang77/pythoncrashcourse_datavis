import unittest
from get_code import get_country_codes

class TestCodes(unittest.TestCase):
    def test_get_code(self):
        code = get_country_codes('Yemen')
        self.assertEqual(code, 'ye')

unittest.main()
