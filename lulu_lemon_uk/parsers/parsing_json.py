import requests
import time
import json


def parsing(response, obj):

    try:
        print(response.url)
        try:
            json_data = json.loads(response.body)
        except:
            json_data = json.loads(response.content)
        product_name = json_data['product']['productName']

        for i in json_data['product']['variationAttributes'][0]['values']:
            if i['selected'] == True:
                product_color = (i['displayValue'])
        try:
            discounted_price = json_data['product']['price']['min']['sales']['formatted']
            mrp_price = json_data['product']['price']['max']['sales']['formatted']
        except:
            mrp_price = json_data['product']['price']['sales']['formatted']
            discounted_price = None
        for i in json_data['product']['variationAttributes'][1]['values']:
            if i['selectable'] == True:
                avilablity = True
            else:
                avilablity = False

            size = i['displayValue']
            obj['avilablity'].append(avilablity)
            obj['product_size'].append(size)
            obj['product_name'].append(product_name)
            obj['product_color'].append(product_color)
            obj['discounted_price'].append(discounted_price)
            obj['mrp_price'].append(mrp_price)
            obj['timestamp'].append(time.time())
            obj['product_url'].append(response.url)


    except Exception as e:
        print('Exception is here',e)

    return obj




