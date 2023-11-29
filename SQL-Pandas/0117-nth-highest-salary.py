import pandas as pd


def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    df = employee.drop_duplicates(subset=["salary"])
    df = df.sort_values(by=['salary'], ascending=False, ignore_index=True)
    df = df.iloc[N-1:N]
    df = df[['salary']]
    if len(df) == 0:
        return pd.DataFrame({f'getNthHighestSalary({N})': [None]})

    df = df.rename(columns={"salary": f'getNthHighestSalary({N})'})
    return df


'''
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
SET N = N-1;
  RETURN (
      # Write your MySQL query statement below.
        SELECT DISTINCT salary 
        FROM Employee
        ORDER BY salary DESC
        LIMIT 1 OFFSET N
  );
END
'''
