import pandas as pd


def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    df = employee.groupby('managerId').size().reset_index(name='count')
    df = df[df['count'] >= 5]
    df = df.merge(employee, left_on='managerId', right_on='id', how='inner')
    return df[['name']]


'''
SELECT name
FROM Employee e1
WHERE e1.id IN (
    SELECT e2.managerId
    FROM Employee e2
    GROUP BY e2.managerId
    HAVING COUNT(e2.managerId) >= 5
) 
'''
