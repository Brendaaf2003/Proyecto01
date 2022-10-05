#Prueba unitaria de el clima 
import unittest
from Request import *
from Datos import *
from Clima import *
from Main import *

class TestClima(unittest.TestCase):

    def test_request(self):
        '''test para saber si la peticion es correcta'''
        self.assertEqual([x for x in clima(19.4326, -99.1332).keys()], 
        ['temp', 'feels_like', 'temp_min', 'temp_max', 'pressure', 'humidity'])

    def test_(self):
        '''test para saber si las ciudades estan'''
        clima_dest = pedir_peticion('TLC', 'TAM')
        self.assertIsInstance(clima_dest, dict)

    def test_exist_key(self):
        '''test de la existencia de la clave'''
        Request = Request()
        self.assertTrue(Request.exist_key())

if __name__ == '__main__':
    unittest.main()