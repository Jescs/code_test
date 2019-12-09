import requests

url = 'http://192.168.238.88:7300/api/u/login'
data = {"name":"admin","password":"1111111"}

r = requests.post(url,data=data)
print(r.json())
