import pandas as pd


def employee_bonus(employee: pd.DataFrame, bonus: pd.DataFrame) -> pd.DataFrame:
    df = employee.merge(bonus, how='left', on='empId')
    df = df.loc[(df['bonus'] < 1000) | (df['bonus'].isnull())]
    return df[['name', 'bonus']]


'''
SELECT e.name, b.bonus
FROM Employee as e
LEFT JOIN Bonus as b
ON e.empId = b.empId
WHERE bonus < 1000 or bonus IS NULL
'''
