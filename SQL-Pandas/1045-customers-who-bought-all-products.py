import pandas as pd


def find_customers(customer: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    customer.drop_duplicates(inplace=True)
    num_products = product.size
    df = customer['customer_id'].value_counts().reset_index()
    df = df.loc[df['count'] == num_products]
    return df[['customer_id']]


'''
SELECT c.customer_id
FROM (
    # drop duplicate rows
    SELECT *
    FROM customer
    GROUP BY customer_id, product_key
) AS c
GROUP BY c.customer_id
HAVING COUNT(customer_id) = (
    # only keep the rows with purchases size of Product database
    SELECT COUNT(*) AS total_product_cnt
    FROM product
)
'''
