import pandas as pd


def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:
    df = actor_director.groupby(
        by=['actor_id', 'director_id']).size().reset_index(name='count')
    df = df.loc[df['count'] >= 3]
    return df[['actor_id', 'director_id']]


'''
SELECT actor_id, director_id
FROM ActorDirector 
GROUP BY actor_id, director_id
HAVING COUNT(*) >= 3
'''
