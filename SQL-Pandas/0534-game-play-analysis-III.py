import pandas as pd


def gameplay_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    activity.sort_values('event_date', inplace=True)
    activity['games_played_so_far'] = activity.groupby(
        'player_id')['games_played'].cumsum()
    return activity[['player_id', 'event_date', 'games_played_so_far']]


'''
SELECT
  A.player_id,
  A.event_date,
  SUM(A.games_played) OVER (
    PARTITION BY
      A.player_id
    ORDER BY
      A.event_date
  ) AS games_played_so_far
FROM
  Activity A;
'''
