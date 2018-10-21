import requests
import re
def fetch_zhihu_re():
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36'
    }
    r = requests.get('https://www.zhihu.com/explore',headers=headers)
    pattern = re.compile('explore-feed.*?question_link.*?>(.*?)</a>', re.S)
    tittles = re.findall(pattern, r.text)
    print(tittles)
'''
Get the icon of github
'''
def get_github_icon():
    r = requests.get('https://github.com/favicon.ico')
    # print(r.text)
    # print(r.content)
    with open('favicon.ico','wb') as f:
        f.write(r.content)
'''
Request post
'''
def requests_post():
    data = {
        'name':'germery',
        'age':22
    }
    re = requests.post('http://httpbin.org/post',data=data)
    print(re.text)
    print(re.cookies)
'''
resuests uoload file
'''
def upload_file():
    files = {'file':open('favicon.ico','rb')}
    res = requests.post('http://httpbin.org/post',files=files)

'''
Login from　cookies
'''
def login_from_cookie():
    cookies = 'q_c1=31653b264a074fc9a57816d1ea93ed8b|1474273938000|1474273938000; d_c0="AGDAs254kAqPTr6NW1U3XTLFzKhMPQ6H_nc=|1474273938"; __utmv=51854390.100-1|2=registration_date=20130902=1^3=entry_date=20130902=1;a_t="2.0AACAfbwdAAAXAAAAso0QWAAAgH28HQAAAGDAs254kAoXAAAAYQJVTQ4FCVgA360us8BAklzLYNEHUd6kmHtRQX5a6hiZxKCynnycerLQ3gIkoJLOCQ==";z_c0=Mi4wQUFDQWZid2RBQUFBWU1DemJuaVFDaGNBQUFCaEFsVk5EZ1VKV0FEZnJTNnp3RUNTWE10ZzBRZFIzcVNZZTFGQmZn|1474887858|64b4d4234a21de774c42c837fe0b672fdb5763b0'
    jar = requests.cookies.RequestsCookieJar()
    headers = {
        'Host': 'www.zhihu.com',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36'
    }
    for cookie in cookies.split(';'):
        key, value = cookie.split('=', 1)
        jar.set(key, value)
    r = requests.get('http://www.zhihu.com', cookies=jar, headers=headers)
    print(r.text)
'''
The use of requests session
'''
def requests_session():
    s = requests.session()
    s.get('http://httpbin.org/cookies/set/number/123456789')
    r = s.get('http://httpbin.org/cookies')
    print(r.text)
'''
The use of requests SSL verify
'''
import logging
def requests_ssl_verify():
    logging.captureWarnings(True)
    response = requests.get('https://www.12306.cn',verify=False)
    print(response.status_code)
if __name__ == '__main__':
    requests_ssl_verify()