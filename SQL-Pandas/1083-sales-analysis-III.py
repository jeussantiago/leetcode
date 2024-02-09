import pandas as pd


def sales_analysis(product: pd.DataFrame, sales: pd.DataFrame) -> pd.DataFrame:
    sales_product = sales.merge(product, on='product_id')
    s8_df = sales_product.loc[sales_product['product_name'] == 'S8']
    iPhone_df = sales_product.loc[sales_product['product_name'] == 'iPhone']
    df = s8_df.loc[~s8_df['buyer_id'].isin(iPhone_df['buyer_id'])]
    return df[['buyer_id']].drop_duplicates()


'''
# S8 Sales
SELECT DISTINCT buyer_id
FROM sales s
LEFT JOIN product p
ON s.product_id = p.product_id
WHERE p.product_name = "S8"
# S8 sales NOT IN iPhone sales
AND buyer_id NOT IN (
    # iPhone sales
    SELECT DISTINCT buyer_id
    FROM sales s
    LEFT JOIN product p
    ON s.product_id = p.product_id
    WHERE p.product_name = "iPhone"
)
'''
