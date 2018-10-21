import requests
from pyquery import PyQuery as pq
from requests.exceptions import RequestException

def write_to_text():
    url = 'https://www.zhihu.com/explore'
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36'
    }
    try:   
        res = requests.get(url,headers=headers)
        if res.status_code == 200:
            doc = pq(res.text)
            items = doc('.explore-feed.feed-item').items()
            file = open('explore.txt','a',encoding='utf-8')
            for item in items:
                question = item.find('h2').text()
                vote = item.find('a.zm-item-vote-count').text()
                author = item.find('a.author-link').text()
                info = item.find('span.info').text()
                content = pq(item.find('.content').html()).text()
                link = item.find('a.answer-date-link.meta-item').attr['href']

                file.write('\n'.join([question,vote,author,info,content,link]))
                file.write('\n'+ '='*50 + '\n')
            file.close()        
        return None
    except RequestException as e:
        print(e)
        return None

if __name__ == '__main__':
    write_to_text()
