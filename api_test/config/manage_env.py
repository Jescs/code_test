
def env(environment):
    if environment == 'dev':
        host = 'http://192.168.238.88:7300'
        return host
    elif environment == 'test':
        host = 'http://test.com'
        return host
    elif environment == 'reslase':
        host = 'http://hispl.com'
        return host
    elif environment == 'prod':
        host = 'http://his.com'
        return host

