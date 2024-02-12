import pandas as pd


def sales_analysis(product: pd.DataFrame, sales: pd.DataFrame) -> pd.DataFrame:
    q1_start = pd.to_datetime("2019-01-01")
    q1_end = pd.to_datetime("2019-03-31")
    # groupby essentially drops the duplicates
    df = sales.groupby('product_id').filter(
        lambda x: min(x['sale_date']) >= q1_start and max(
            x['sale_date']) <= q1_end
    )
    df.drop_duplicates(subset='product_id', inplace=True)
    df = df.merge(product, on='product_id')
    return df[['product_id', 'product_name']]


'''
SELECT p.product_id, p.product_name
FROM Sales s
Left JOIN Product p
ON p.product_id = s.product_id
GROUP BY p.product_id
HAVING MIN(s.sale_date) >= "2019-01-01" AND MAX(s.sale_date) <= "2019-03-31"
'''
