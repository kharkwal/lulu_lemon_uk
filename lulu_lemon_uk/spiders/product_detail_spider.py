import scrapy
import requests
from scrapy import Request
from bs4 import BeautifulSoup
import re
import json
import time
import logging
from scrapy.utils.log import configure_logging
import pandas as pd
from ..parsers import parsing_json
from ..items import LululemonProductDetailsItem
df = pd.read_csv('Output/product_urls.csv')
lst_p_urls = set(df['product_link'].values)
class LuluProductSpider(scrapy.Spider):
    name = 'product_detail'
    configure_logging(install_root_handler=False)
    logging.basicConfig(
        filename='log.txt',
        format='%(levelname)s: %(message)s',
        level=logging.INFO
    )
    try:

        lst_json_urls = []
        for url in lst_p_urls:
            pro_id = url.split('/')[6].split('.')[0]
            color_id = url.split('/')[6].split('color=')[1]
            url_sapmle_json = 'https://www.lululemon.co.uk/on/demandware.store/Sites-UK-Site/en_GB/Product-Variation?dwvar_' + pro_id + '_color=' + color_id + '&pid=' + pro_id + '&quantity=1'
            lst_json_urls.append(url_sapmle_json)

        start_urls = lst_json_urls

    except Exception as e:
        print(e)
    def parse(self, response):
        items = LululemonProductDetailsItem()
        obj = {'avilablity': [], 'product_name': [], 'product_color': [], 'product_size': [],
               'mrp_price': [], 'discounted_price': [], 'product_url': [], 'timestamp': []}

        obj = parsing_json.parsing(response, obj)
        print('len of obj-->',
              len(obj['avilablity']))
        for i in range(len(obj['avilablity'])):

            items['avilablity'] = obj['avilablity'][i]
            items['product_name'] = obj['product_name'][i]
            items['product_color'] = obj['product_color'][i]
            items['product_size'] = obj['product_size'][i]
            items['mrp_price'] = obj['mrp_price'][i]
            items['discounted_price'] = obj['discounted_price'][i]
            items['product_url'] = obj['product_url'][i]
            items['timestamp'] = obj['timestamp'][i]
            yield items


