import pandas as pd


def article_views(views: pd.DataFrame) -> pd.DataFrame:
    df = views.loc[views['author_id'] == views['viewer_id']][['author_id']]
    df.drop_duplicates(inplace=True)
    df.rename(columns={'author_id': "id"}, inplace=True)
    df.sort_values(by=['id'], inplace=True, ascending=True)
    return df


'''
SELECT DISTINCT author_id as id
FROM Views
WHERE author_id = viewer_id
ORDER BY author_id ASC
'''
