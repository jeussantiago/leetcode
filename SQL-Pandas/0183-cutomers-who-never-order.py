import pandas as pd


def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    df = customers.merge(
        orders, left_on="id", right_on="customerId", how="left", suffixes=["_c", "_o"])
    df = df.loc[df['customerId'].isnull(), ['name']]
    df = df.rename(columns={'name': 'Customers'})
    return df


'''
SELECT name AS 'Customers'
FROM Customers AS c
LEFT JOIN Orders AS o
ON c.id = o.customerId
WHERE o.customerId IS NULL
'''
