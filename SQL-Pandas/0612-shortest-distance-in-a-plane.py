import pandas as pd


def shortest_distance(point2_d: pd.DataFrame) -> pd.DataFrame:
    df = point2_d.merge(point2_d, how='cross', suffixes=('_a', '_b'))
    df['dist'] = np.sqrt(np.square(df['x_a'] - df['x_b']) +
                         np.square(df['y_a'] - df['y_b'])).round(2)
    df = df.loc[df['dist'] != 0]  # remove the pairings that are the same point
    min_dist = df['dist'].min()  # get the min distance
    # create new dataframe with shortest
    return pd.DataFrame({'shortest': [min_dist]})


'''
SELECT (MIN(ROUND(SQRT(POWER(a.x - b.x, 2) + POWER(a.y - b.y, 2)), 2))) AS shortest
FROM point2d a
CROSS JOIN point2d b
ON !(a.x = b.x AND a.y = b.y)
'''
