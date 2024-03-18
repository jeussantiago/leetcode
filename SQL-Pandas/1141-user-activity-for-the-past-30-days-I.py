import pandas as pd


def user_activity(activity: pd.DataFrame) -> pd.DataFrame:
    df = activity.loc[(activity['activity_date'] > "2019-06-27")
                      & (activity['activity_date'] <= "2019-07-27")]
    df = df.groupby(by=['activity_date'])['user_id'].nunique().reset_index()
    df.rename(columns={'activity_date': 'day',
              'user_id': 'active_users'}, inplace=True)
    return df


'''
SELECT activity_date AS "day", COUNT(DISTINCT user_id) AS "active_users"
FROM activity
WHERE activity_date 
    BETWEEN "2019-06-28" AND "2019-07-27"
GROUP BY activity_date
'''
