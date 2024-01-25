import pandas as pd


def sales_analysis(sales: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    df = sales.groupby('product_id')['quantity'].sum().reset_index()
    return df.rename(columns={'quantity': 'total_quantity'})


'''
SELECT product_id, SUM(quantity) AS total_quantity 
FROM sales
GROUP BY product_id
'''
