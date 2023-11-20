import pandas as pd


def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    df = activity.groupby([activity['player_id']])[
        'event_date'].agg(['min']).reset_index()
    return df.rename(columns={'min': 'first_login'})


'''
SELECT player_id, MIN(event_date) as first_login
FROM Activity
GROUP BY player_id
'''
