from api_test.api_manage.api_case import login
import unittest
from api_test.config.manage_env import env
host = env('dev')
class Test_Login(unittest.TestCase):

    def setUp(self):
        self.url = host + '/api/u/login'

    def tearDown(self):
        pass

    def test_normal_login(self):
        data = {"name":"admin","password":"1111111"}
        s = login(self.url, data)
        mes = s.json()['message']
        self.assertEqual(mes, '登录成功')

    def test_normal_login(self):
        data = {"name":"admin","password":"1111111"}
        s = login(self.url, data)
        mes = s.json()['message']
        self.assertEqual(mes, '登录成功')


if __name__=='__main__':
    unittest.main()