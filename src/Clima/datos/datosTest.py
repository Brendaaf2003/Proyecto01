
import unittest
from Clima import Peticion

class TestClima(unittest.TestCase):
    def test_clima(self):
        #comprueba que la peticion de clima sea correcta
        self.assertEqual(Peticion('Mexico', 'Los Angeles'), 1)

if __name__ == '__main__':
    unittest.main()


