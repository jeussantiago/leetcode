import pandas as pd


def gameplay_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    # get first login
    first_login = activity.groupby(
        'player_id')['event_date'].min().reset_index()
    # offset each event date by -1 day
    activity['day_before'] = activity['event_date'] - \
        pd.to_timedelta(1, unit="D")
    # Merge then check if the offsetted day is the same as the first login date
    merged_df = activity.merge(
        first_login, on='player_id', suffixes=('_actual', '_first'))
    consecutive_login_df = merged_df[merged_df['day_before']
                                     == merged_df['event_date_first']]
    # Calculate fraction
    fraction = round(consecutive_login_df['player_id'].nunique(
    ) / activity['player_id'].nunique(), 2)
    df = pd.DataFrame({'fraction': [fraction]})
    return df


'''
# get the min event_date for each user
# using that, we can check the original Activity database
#   if the day before (current=2nd day, day_before=1st_day)
#   is in the min event_date
# then we can count how many players exist in this and 
#   divide by the number of DISTINCT total COUNT of players

SElECT 
    ROUND (
        COUNT(a1.player_id) 
        / (SELECT COUNT(DISTINCT a3.player_id) FROM Activity a3)
    , 2) AS fraction
FROM Activity a1
WHERE (a1.player_id, DATE_SUB(a1.event_date, INTERVAL 1 DAY)) IN (
    SELECT
        a2.player_id,
        MIN(a2.event_date)
    FROM 
        Activity a2
    GROUP BY 
        a2.player_id
)

'''
