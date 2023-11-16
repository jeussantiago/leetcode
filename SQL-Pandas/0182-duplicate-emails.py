import pandas as pd


def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    df = person.groupby("email").filter(lambda x: len(x) > 1)
    df = df[['email']].drop_duplicates()
    return df


'''
SELECT email 
FROM Person
GROUP By Email
HAVING count(email) > 1
'''
