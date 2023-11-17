import pandas as pd


def delete_duplicate_emails(person: pd.DataFrame) -> None:
    min_id = person.groupby('email')['id'].transform('min')
    other_person_ids = person[person['id'] != min_id]
    person.drop(other_person_ids.index, inplace=True)


'''
DELETE p1
FROM Person AS p1, Person AS p2
WHERE p1.email = p2.email 
    AND p1.id > p2.id
'''
