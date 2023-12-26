import pandas as pd


def acceptance_rate(friend_request: pd.DataFrame, request_accepted: pd.DataFrame) -> pd.DataFrame:
    friend_request.drop_duplicates(
        subset=['sender_id', 'send_to_id'], inplace=True)
    request_accepted.drop_duplicates(
        subset=['requester_id', 'accepter_id'], inplace=True)

    rate = 0 if len(request_accepted) == 0 else round(
        len(request_accepted) / len(friend_request), 2)
    return pd.DataFrame({'accept_rate': [rate]})


'''
SELECT ROUND(
    IFNULL(
        (SELECT COUNT(*) FROM (SELECT DISTINCT requester_id, accepter_id FROM RequestAccepted) AS A) 
        /
        (SELECT COUNT(*) FROM (SELECT DISTINCT sender_id, send_to_id FROM FriendRequest) AS B),
        0
    ), 2
) AS accept_rate
'''
