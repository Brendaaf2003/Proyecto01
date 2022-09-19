import unittest
from Request import *

class testRequest(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('hola'.upper(), 'HOLA')

    def test_isupper(self):
        self.assertTrue('HOLA'.isupper())
        self.assertFalse('Hola'.isupper())

    def test_split(self):
        s = 'Hola mundo'
        self.assertEqual(s.split(), ['Hola', 'mundo'])
    
    def test_clima(self):

        self.assertTrue(clima(19.4326,-99.1332)())
        self.assertFalse(clima(19.3326,-99.1332)())


if __name__ == '__main__':
    unittest.main()