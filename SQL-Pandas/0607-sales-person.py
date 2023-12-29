import pandas as pd


def sales_person(sales_person: pd.DataFrame, company: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    df = orders.merge(company, on='com_id', how='left')
    red_sales = df.loc[df['name'] == 'RED']['sales_id']
    res = sales_person[~sales_person['sales_id'].isin(red_sales)]
    return res[['name']]


'''
SELECT name
FROM salesperson s
WHERE s.sales_id NOT IN (
    SELECT DISTINCT(o.sales_id)
    FROM orders o
    LEFT JOIN company c
    ON o.com_id = c.com_id
    WHERE c.name = "RED"
)
'''
