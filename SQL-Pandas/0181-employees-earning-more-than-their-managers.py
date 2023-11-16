import pandas as pd


def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
    df = employee.merge(employee, left_on="managerId",
                        right_on='id', how='inner', suffixes=["_a", "_b"])
    df = df.loc[df['salary_a'] > df['salary_b'], ["name_a"]]
    df = df.rename(columns={'name_a': 'Employee'})
    return df


'''
SELECT a.name AS 'Employee'
FROM 
    Employee AS a,
    Employee AS b
WHERE
    a.managerId = b.id
        AND a.salary > b.salary
'''
