# encoding  = utf-8

import requests
import unittest


class Requests_login(unittest.TestCase):

    def setUp(self):
        print('Begin test!')
        self.url = "http://192.168.238.88:7300/api/u/login"

    def tearDown(self):
        print('End test!')

    def test_login_wrong(self):
        self.data = {"name": "admin", "password": "aaaaaaa"}
        self.r = requests.post(self.url, self.data)
        s = self.r.json()
        self.assertEqual(s['message'], '用户名或密码错误',msg='login error')

    def test_login_pass(self):
        self.data = {"name": "admin", "password": "1234567"}
        self.r = requests.post(self.url, self.data)
        s = self.r.json()
        self.assertEqual(s['message'], 'success',msg='login error')


if __name__ == '__main__':
    unittest.main()