import json
import hashlib


def md5(str):
    m = hashlib.md5()
    str = str.encode("utf-8")
    m.update(str)
    return m.hexdigest()


if __name__ == '__main__':
    print(md5("123"))