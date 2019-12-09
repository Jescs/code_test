import unittest
from test_file.city_functions import fun_city

class TestCity(unittest.TestCase):
    def test_city_country(self):
        str_city = fun_city('santiago', 'chile')
        self.assertEqual(str_city,'Santiago, Chile - population 20')

    def test_city_country_population(self):
        str_city = fun_city('santiago', 'chile', 5000000)
        self.assertEqual(str_city, 'Santiago, Chile - population 5000000')


if __name__ == '__main__':
    unittest.main()
