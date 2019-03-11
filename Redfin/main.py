import scrapy.cmdline
import requests
from lxml.html import fromstring

'''
A method to scrape free publicly available proxies used to crawl. Unutilized at the moment due
to unreliability of public proxies sources (retrying dead proxies and abandoning them slows down
crawling speed drastically) 
'''

def get_proxies():
    url = 'https://free-proxy-list.net/'
    response = requests.get(url)
    parser = fromstring(response.text)
    proxies = []
    for i in parser.xpath('//tbody/tr')[:10]:
        if i.xpath('.//td[5][contains(text(),"elite proxy")]'):
            proxy = ":".join([i.xpath('.//td[1]/text()')[0], i.xpath('.//td[2]/text()')[0]])
            proxies.append(proxy)
    with open('proxies.txt', 'w') as f:
        for proxy in proxies:
            f.write(proxy+'\n')

if __name__ == '__main__':
    # generate proxy list
    # get_proxies()
    scrapy.cmdline.execute(argv=['scrapy','crawl','redfin_crawler'])