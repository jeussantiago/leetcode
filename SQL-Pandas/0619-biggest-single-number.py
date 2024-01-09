import pandas as pd


def biggest_single_number(my_numbers: pd.DataFrame) -> pd.DataFrame:
    df = my_numbers.groupby(['num'])['num'].count().reset_index(name='counts')
    df = df.loc[df['counts'] == 1]
    max_singular = df['num'].max()
    return pd.DataFrame({'num': [max_singular]})


'''
SELECT MAX(num) AS num
FROM (
    SELECT *
    FROM MyNumbers 
    GROUP BY num
    HAVING COUNT(num) = 1
) s
'''
