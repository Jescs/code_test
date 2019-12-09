import requests
import unittest


class Requests_login(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('Begin test!')
        cls.url = "http://192.168.238.88:7300/api/u/login"


    @classmethod
    def tearDownClass(cls):
        print('End test!')

    def test_login_wrong(self):
        self.data = {"name": "admin", "password": "aaaaaaa"}
        self.r = requests.post(self.url, self.data)
        s = self.r.json()
        self.assertEqual(s['message'], '用户名或密码错误')

    def test_login_pass(self):
        self.data = {"name": "admin", "password": "111111"}
        self.r = requests.post(self.url, self.data)
        s = self.r.json()
        self.assertEqual(s['message'], 'success')


if __name__ == '__main__':
    unittest.main()
