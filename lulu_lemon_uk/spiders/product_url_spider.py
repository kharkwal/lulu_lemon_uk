import scrapy
import requests
from scrapy import Request
from bs4 import BeautifulSoup
import re
import pandas as pd
from ..items import UrlItems
from ..parsers import html_parser
class LuluSpiderSpider(scrapy.Spider):
    name = 'product_url_spider'
    lst_urls = []
    lst_products = ['bottoms', 'sports', 'tops']
    category = ['mens', 'womens']
    for cat in category:
        for prod in lst_products:
            sample_url = 'https://www.lululemon.co.uk/en-gb/c/' + cat + '/' + prod
            req = requests.get(sample_url)
            soup = BeautifulSoup(req.content, 'lxml')
            data = soup.find('div', attrs={'class': 'result-count'})
            data = data.text
            temp = re.findall(r'\d+', data)
            res = list(map(int, temp))
            total_items = res[0]
            sample_url = sample_url+'?sz='+str(total_items)
            lst_urls.append(sample_url)
    lst_accessories = ['bags', 'equipment', 'headwear', 'scarves-and-gloves', 'socks']
    for access in lst_accessories:
        sample_url = 'https://www.lululemon.co.uk/en-gb/c/accessories/'+access
        req = requests.get(sample_url)
        soup = BeautifulSoup(req.content, 'lxml')
        data = soup.find('div', attrs={'class': 'result-count'})
        data = data.text
        temp = re.findall(r'\d+', data)
        res = list(map(int, temp))
        total_items = res[0]
        sample_url = sample_url + '?sz=' + str(total_items)
        lst_urls.append(sample_url)
    #
    start_urls = lst_urls

    def parse(self, response):

        items = UrlItems()
        lst_urls = html_parser.hrefExtractor(response.text)
        lst_filtered_urls = []
        url_keyword_str = 'dwvar_|color=|/p/|www.lululemon.co.uk'
        for url in lst_urls:
            check = html_parser.url_keyword_filtering(url, url_keyword_str)
            if check == True:
                lst_filtered_urls.append(url)

        lst_filtered_urls = set(lst_filtered_urls)
        product_link = list(lst_filtered_urls)
        for url in product_link:
            items['product_link'] = url
            yield items
        # df = pd.DataFrame({'product_link': product_link})
        # df.to_csv('product_urls.csv')
        # yield items

