from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import random
import re
'''
get all links in a page
'''
def get_page_all_links():
    html = urlopen("https://en.wikipedia.org/wiki/Kevin_Bacon")
    bsObj = BeautifulSoup(html)

    for link in bsObj.findAll("a"):
        if 'href' in link.attrs and link.attrs['href'].startswith("http"):
            print(link.attrs['href'] + '\n')
'''
get all the wiki links in a page
'''
def get_page_all_wiki_links():
    html = urlopen("https://en.wikipedia.org/wiki/Kevin_Bacon")
    bsObj = BeautifulSoup(html)

    for link in bsObj.find("div",{"id":"bodyContent"}).findAll("a",
        href=re.compile("^(/wiki/)((?!:).)*$")):
        if 'href' in link.attrs:
            print(link.attrs['href'] + '\n')

def getLinks(articleUrl):
    html = urlopen("https://en.wikipedia.org" + articleUrl)
    bsObj = BeautifulSoup(html)
    return bsObj.find("div",{"id":"bodyContent"}).findAll("a",
        href=re.compile("^(/wiki/)((?!:).)*$"))
def main():
    random.seed(datetime.datetime.now())
    links = getLinks('/wiki/kevin_Bacon')
    while len(links) > 0:
        newArticle = links[random.randint(0,len(links)-1)].attrs["href"]
        print(newArticle)
        links = getLinks(newArticle)

if __name__ == '__main__':
    main()