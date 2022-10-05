#Prueba unitaria de el clima 
import unittest
from Request import *
from Datos import *
from Clima import *

class TestClima(unittest.TestCase):
    def test_request(self):
        self.assertEqual([x for x in clima(19.4326, -99.1332).keys()], 
        ['temp', 'feels_like', 'temp_min', 'temp_max', 'pressure', 'humidity'])

if __name__ == '__main__':
    unittest.main()
