import pandas as pd


def sales_analysis(product: pd.DataFrame, sales: pd.DataFrame) -> pd.DataFrame:
    sales_agg = sales.groupby('seller_id')['price'].sum().reset_index()

    max_sales_price = max(sales_agg['price'])
    df = sales_agg.loc[sales_agg['price'] == max_sales_price]
    return df[['seller_id']]


'''
WITH total_sales_table AS (
    SELECT seller_id, SUM(price) AS total_sales
    FROM sales
    GROUP BY seller_id
)
SELECT seller_id
FROM total_sales_table a
WHERE total_sales = (
    SELECT MAX(total_sales)
    FROM total_sales_table
)
'''
