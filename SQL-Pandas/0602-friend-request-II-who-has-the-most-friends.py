import pandas as pd


def most_friends(request_accepted: pd.DataFrame) -> pd.DataFrame:

    df = pd.concat([request_accepted['requester_id'],
                   request_accepted['accepter_id']]).to_frame('id')
    df = df.groupby(by=['id'], as_index=False).agg(
        num=('id', 'count')).sort_values(by=['num'], ascending=False)
    return df.head(1)


'''
SELECT *, COUNT(*) AS num
FROM (
    SELECT requester_id AS id
    FROM RequestAccepted 
    UNION ALL
    SELECT accepter_id AS id
    FROM RequestAccepted 
) AS u
GROUP BY id
ORDER BY num DESC
LIMIT 1
'''
