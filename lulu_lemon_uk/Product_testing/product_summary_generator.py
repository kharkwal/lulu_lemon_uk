import pandas as pd
import datetime
def product_summary():
    df = pd.read_csv('../Output/product_details.csv')

    total_available_product = df['avilablity'].values.sum()
    total_out_of_stock_producta = (~df['avilablity']).values.sum()
    total_product_without_discount = df['discounted_price'].isna().sum()
    total_product_with_discount = len(df) - total_product_without_discount

    df_products = pd.DataFrame({'Total Products': [len(df)],
                                'Total Available Products': [total_available_product],
                                'Total Out of Stock Products': [total_out_of_stock_producta],
                                'Total Products Without Discount': [total_product_without_discount],
                                'Total Products With Discount': [len(df) - total_product_without_discount]})
    file_name = str(datetime.datetime.today().date())
    df_products.to_excel('../Output/Product_summary_'+file_name+'.xlsx')

