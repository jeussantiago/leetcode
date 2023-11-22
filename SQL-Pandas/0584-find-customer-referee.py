import pandas as pd


def find_customer_referee(customer: pd.DataFrame) -> pd.DataFrame:
    df = customer.loc[(customer['referee_id'] != 2) |
                      (customer['referee_id'].isnull())]
    return df[['name']]


'''
SELECT name
FROM customer
WHERE referee_id != 2 OR referee_id IS NULL
'''
