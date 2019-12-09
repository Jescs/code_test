import unittest
from test_file.employee import Employee


class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.employee = Employee('lily', 'enda', 1000)

    def test_give_default_raise(self):
        self.employee.give_raise()
        self.salary = self.employee.salary
        self.assertEqual(self.salary, 6000)

    def test_give_custom_raise(self):
        self.employee.give_raise(500)
        self.salary = self.employee.salary
        self.assertEqual(self.salary, 1500)


if __name__ == '__main__':
    unittest.main()
