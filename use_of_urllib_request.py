# -*- coding:utf-8 -*-
'''
The use of urllib.request
'''
from urllib import request as req,parse,error
'''
The use of request.urlopen via GET
'''
def request_urlopen_get():
    response = req.urlopen('https://www.python.org')
    print(type(response))
    print(response.status)
    print(response.msg)
    print(response.version)
    print(response.reason)
    print(response.getheaders())
    print(response.getheader('server'))
    #print(response.read().decode('utf-8'))
'''
The use of requesturlopen via POST
'''
def request__urloprn_post():
    data = bytes(parse.urlencode({'word':'hello'}),encoding = 'utf8')
    response = req.urlopen('http://httpbin.org/post',data = data)
    print(response.read().decode('utf8'))

'''
The use of request.urlopen with timueout option and try except
'''
import socket
def request_urlopen_timeout():
    try:
        res = req.urlopen('http://httpbin.org/get',timeout = 0.1)
    except error.URLError as e:
        # TODO why use socket.timeout?
        if isinstance(e.reason,socket.timeout):
            print('Time out !')
'''
The use of request.request
'''
def request_request():
    request = req.Request('https://python.org')
    response = req.urlopen(request)
    print(response.read().decode('utf-8'))
'''
THe use of request.request with headers
'''
def request_headers():
    url = 'http://httpbin.org/post'
    headers = {
        'User-Agent':'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
        'host':'httpbin.org'
    }
    dict = {
        'name':'germy'
    }
    data = bytes(parse.urlencode(dict), encoding='utf8')
    request = req.Request(url=url, data=data, headers=headers, method='POST')
    response = req.urlopen(request)
    print(response.read().decode('utf-8'))
'''
The use of HTTPBasicAuthHandle
'''
from urllib.request import HTTPPasswordMgrWithDefaultRealm, HTTPBasicAuthHandler, build_opener
from urllib.error import URLError
def request_http_basic_handler():
    username = '918608767@qq.com'
    password = 'jzc206559'
    url = 'https://www.douban.com/'

    p = HTTPPasswordMgrWithDefaultRealm()
    p.add_password(None, url, username, password)
    auth_handler = HTTPBasicAuthHandler(p)
    opener = build_opener(auth_handler)

    try:
        result = opener.open(url)
        html = result.read().decode('utf-8')
        print(html)
    except URLError as e:
        print(e.reason)
'''
The use of request.Proxy

from urllib.error import URLError
from urllib.request import ProxyHandler, build_opener
'''
from urllib.request import ProxyHandler
def request_proxy_handler():
    proxy_handler = ProxyHandler({
        'http':'127.0.0.1:9743',
        'https':'127.0.0.1:9743'
    })
    opener = build_opener(proxy_handler)
    try:
        response = opener.open('https://www.baidu.com')
        print(response.read().decode('utf-8'))
    except URLError as e:
        print(e.reason)
'''
The use of cookies
'''
import http.cookiejar
def request_cookie():
    filename = 'cookies.txt'
    cookie = http.cookiejar.MozillaCookieJar(filename)
    handler = req.HTTPCookieProcessor(cookie)

    opener = build_opener(handler)
    response = opener.open('http://www.baidu.com')
    cookie.save(ignore_discard=True,ignore_expires=True)
    # for item in cookie:
    #     print(item.name +"="+item.value)    

if __name__ == '__main__':
    request_cookie()
