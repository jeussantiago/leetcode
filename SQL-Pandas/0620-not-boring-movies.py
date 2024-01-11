import pandas as pd


def not_boring_movies(cinema: pd.DataFrame) -> pd.DataFrame:
    df = cinema.loc[(cinema['id'] % 2 == 1) & (
        cinema['description'] != 'boring')]
    df.sort_values(by=['rating'], ascending=False, inplace=True)
    return df


'''
SELECT *
FROM cinema
WHERE MOD(id, 2) = 1 AND description != 'boring'
ORDER BY rating DESC
'''
