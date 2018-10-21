import re
import json
import time
import requests
from requests.exceptions import RequestException

'''
Get the page contents of the given url
'''
def get_one_page(url):
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36'
    }
    try:
        res = requests.get(url,headers=headers)
        if res.status_code == 200:
            return res.text;
        else:
            return None
    except RequestException:
        return None

def parse_one_page(html):
    pattern = re.compile(
        '<dd>.*?board-index.*?>(\d+)</i>.*?data-src="(.*?)".*?name.*?a'
        + '.*?>(.*?)</a>.*?star.*?>(.*?)</p>.*?releasetime.*?>(.*?)</p>'
        +'.*?integer.*?>(.*?)</i>.*?fraction.*?>(.*?)</i>.*?</dd>',re.S)
    items = re.findall(pattern,html)
    for item in items:
        # yield {
        #     'index':item[0],
        #     'image':item[1],
        #     'title':item[2],
        #     'actors':item[3].strip()[3:],
        #     'releasetime':item[4].strip()[5:],
        #     'score':item[5].strip()+item[6].strip()
        # }
        yield (
            item[0],
            item[1],
            item[2],
            item[3].strip()[3:],
            item[4].strip()[5:],
            item[5].strip()+item[6].strip(),
        )


def write_to_file(content):
    with open('movie_top100.txt','a',encoding='utf-8') as f:
        f.write(json.dumps(content, ensure_ascii=False) + '\n')

def main(offset):
    url = 'http://maoyan.com/board/4?offset='+str(offset)
    html = get_one_page(url)
    for item in parse_one_page(html):
        print(item)
        write_to_file(item)

if __name__ == '__main__':
    for i in range(10):
        main(i*10)
        time.sleep(1)