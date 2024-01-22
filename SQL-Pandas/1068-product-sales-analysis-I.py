import pandas as pd


def sales_analysis(sales: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    df = sales.merge(product, left_on='product_id', right_on='product_id')
    return df[['product_name', 'year', 'price']]


'''
SELECT p.product_name, s.year, s.price
FROM sales s
LEFT JOIN product p
    ON s.product_id = p.product_id
'''
