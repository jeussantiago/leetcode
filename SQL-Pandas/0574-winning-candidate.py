import pandas as pd


def winning_candidate(candidate: pd.DataFrame, vote: pd.DataFrame) -> pd.DataFrame:
    df = vote.groupby('candidateId')[
        'id'].count().reset_index(name='vote_count')
    winner_id = df.loc[df['vote_count'].idxmax()]['candidateId']
    return candidate[candidate['id'] == winner_id][['name']]


'''
SELECT name
FROM Candidate c
JOIN (
    SELECT candidateId, COUNT(id) AS voteCount
    FROM Vote
    GROUP BY candidateId
    ORDER BY voteCount DESC
    LIMIT 1
) AS w ON c.id = w.candidateId

'''
