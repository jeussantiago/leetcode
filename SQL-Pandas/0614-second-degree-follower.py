import pandas as pd


def second_degree_follower(follow: pd.DataFrame) -> pd.DataFrame:
    follower_cnt = follow.groupby('followee').size(
    ).reset_index(name='user_following_count')
    following_cnt = follow.groupby('follower').size(
    ).reset_index(name='user_follows_count')
    df = follower_cnt.merge(following_cnt, how='inner',
                            left_on='followee', right_on='follower')
    df.rename(columns={'user_following_count': 'num'}, inplace=True)
    return df[['follower', 'num']]


'''
SELECT follower, user_follower_cnt AS num
FROM (
    # num user followers
    SELECT followee, COUNT(follower) AS user_follower_cnt
    FROM Follow 
    GROUP BY followee
) AS f1
# join because user needs to appear in both 
JOIN (
    # num user follows
    SELECT follower, COUNT(followee) AS user_follow_cnt
    FROM Follow
    GROUP BY follower
) AS f2
ON f1.followee = f2.follower
ORDER BY f2.follower 
'''
