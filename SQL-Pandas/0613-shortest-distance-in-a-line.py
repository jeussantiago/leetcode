import pandas as pd


def shortest_distance(point: pd.DataFrame) -> pd.DataFrame:
    df = point.merge(point, how='cross', suffixes=('.a', '.b'))
    df['shortest'] = abs(df['x.a'] - df['x.b'])
    df = df.loc[df['shortest'] != 0]
    min_dist = df['shortest'].min()
    return pd.DataFrame({'shortest': [min_dist]})


'''
SELECT MIN(b.x - a.x) AS shortest
FROM point a
CROSS JOIN point b
WHERE a.x < b.x
'''
