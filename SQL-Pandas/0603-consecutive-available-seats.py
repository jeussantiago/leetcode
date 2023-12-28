import pandas as pd


def consecutive_available_seats(cinema: pd.DataFrame) -> pd.DataFrame:
    df = cinema.join(cinema, how='cross', lsuffix="_a", rsuffix='_b')
    df['diff'] = abs(df['seat_id_a'] - df['seat_id_b'])
    df = df.loc[(df['diff'] == 1) & (df['free_a'] == 1) & (df['free_b'] == 1)]
    df.rename(columns={'seat_id_a': 'seat_id'}, inplace=True)
    res = df[['seat_id']].drop_duplicates().sort_values(
        by=['seat_id'], ascending=True)
    return res


'''
SELECT DISTINCT(a.seat_id)
FROM cinema a 
JOIN cinema b
    # find the seats that are 1 id next to
    ON ABS(a.seat_id - b.seat_id) = 1 
    # both seats need to be free, has value of 1
    AND a.free = 1 AND b.free = 1
ORDER BY a.seat_id
'''
