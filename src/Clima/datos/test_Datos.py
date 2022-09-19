import unittest
from Datos import Base_de_datos

class TestDatos(unittest.TestCase):
    def test_base(self):
        with self.assertRaises(FileNotFoundError):
            Base_de_datos()
        datos = Base_de_datos('dataset2.csv')

if __name__ == '__main__':
    unittest.main()