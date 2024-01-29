import pandas as pd


def sales_analysis(sales: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    min_year_df = sales.groupby('product_id')['year'].min()
    df = sales.merge(min_year_df, how='inner', on='product_id')
    df = df.loc[df['year_x'] == df['year_y']]
    df.rename({'year_x': 'first_year'}, axis=1, inplace=True)
    return df[['product_id', 'first_year', 'quantity', 'price']]


'''
SELECT product_id, year AS first_year, quantity, price
FROM sales
WHERE (product_id, year) IN (
    SELECT product_id, MIN(YEAR) AS year
    FROM sales
    GROUP BY product_id
)
'''
