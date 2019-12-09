import unittest
from test_file.name_function import get_formatted_name


class NamesTestCase(unittest.TestCase):
    def test_first_last_name(self):
        formatted_name = get_formatted_name('jains', 'jopjh')
        self.assertEqual(formatted_name, 'Jains Jopjh')

    def test_middle_name(self):
        formatted_name = get_formatted_name('jains', 'hahah', 'jopjh')
        self.assertEqual(formatted_name, 'Jains Jopjh Hahah')


if __name__ == '__main__':
    unittest.main()