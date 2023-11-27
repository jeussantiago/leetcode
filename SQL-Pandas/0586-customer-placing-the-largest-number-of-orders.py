import pandas as pd


def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    # this solution also solves for the follow up

    # size counts NaN values, count doesn't include them
    df = orders.groupby(['customer_number'], as_index=False).size()
    df = df.loc[df['size'] == df['size'].max()]
    return df.iloc[:, [0]]


'''
# Write your MySQL query statement below

SELECT customer_number, count(*)
FROM orders
GROUP BY customer_number
ORDER BY count(*) DESC
LIMIT 1

# Follow up: What if more than one customer have the largest number of orders, can you find all the customer_number in this case?
SELECT customer_number
FROM orders
GROUP BY customer_number
HAVING count(customer_number) = (
    SELECT max(numOfOrder)
    FROM (
        SELECT customer_number, count(*) as numOfOrder
        FROM orders
        GROUP BY customer_number
    ) as tmp
)
'''
