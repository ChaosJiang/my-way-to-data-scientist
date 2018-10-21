# -*- coding:utf-8 -*-
'''
The use of urllib.error
''' 
from urllib import request, error
def urllib_http_and_url_error():
    try:
        response = request.urlopen('http://cuiqingcai.com/index.htm')
    except error.HTTPError as e:
        print(e.reason, e.code, e.headers, sep='/')
    except error.URLError as e:
        print(e.reason)
    else:
        print('Request Successfully!')
        print(response.read())
'''
The handle of timeout error
'''
import socket
def socket_timeout_error():
    try:
        response = request.urlopen('https://www.baidu.com', timeout=0.01)
    except error.URLError as e:
        print(type(e.reason))
        if isinstance(e.reason, socket.timeout):
            print('TIME OUT!')

if __name__ == '__main__':
    socket_timeout_error()