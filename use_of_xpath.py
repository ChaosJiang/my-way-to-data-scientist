from lxml import etree
def main():
    html = etree.parse('./test.html',etree.HTMLParser())
    #result = html.xpath('//ul/a')
    #result = html.xpath('//a[@href="link4.html"]/../@class')
    #result = html.xpath('//a[@href="link4.html"]/parent::*/@class')
    #result = html.xpath('//li[@class="item-1"]/a/text()')
    result = html.xpath('//li/a/@href')
    print(result)
if __name__ == '__main__':
    main()