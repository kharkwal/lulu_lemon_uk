import pandas as pd
import requests
from black_rock_here.lulu_lemon_uk.lulu_lemon_uk.parsers import parsing_json
# from ..parsers import parsing_json
import product_summary_generator
def product_testing(test_range):
    test_result = ''
    for i in range(test_range):
        df = pd.read_csv('../Output/product_details.csv')
        random_row = df.sample()
        row_data = random_row.to_dict(orient='records')
        row_data = row_data[0]
        product_url = row_data['product_url']
        product_name = row_data['product_name']
        product_size = row_data['product_size']

        req = requests.get(product_url)
        obj = {'avilablity': [], 'product_name': [], 'product_color': [], 'product_size': [],
               'mrp_price': [], 'discounted_price': [], 'product_url': [], 'timestamp': []}
        obj = parsing_json.parsing(req, obj)

        if obj['product_name'][0] == product_name:
            test_result = test_result + 'Test Case Result ---->PASS  (Product Url--->' + product_url + ')\n'
        else:
            test_result = test_result + 'Test Case Result ---->FAIL  (Product Url--->' + product_url + ')\n'

    f = open("../Output/TestCases.txt", "a")
    f.write(test_result)
    f.close()
    product_summary_generator.product_summary()
input_cases = int(input('Enter total number of test cases to execute'))
product_testing(input_cases)