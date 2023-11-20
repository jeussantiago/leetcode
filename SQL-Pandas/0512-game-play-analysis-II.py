import pandas as pd


def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    idx = activity.groupby([activity['player_id']])['event_date'].idxmin()
    df = activity.loc[idx]
    return df[['player_id', 'device_id']]


'''
SELECT a1.player_id, a1.device_id
FROM activity a1
WHERE (a1.player_id, a1.event_date) IN (
    SELECT a2.player_id, min(a2.event_date)
    FROM activity a2
    GROUP BY a2.player_id
)
'''
