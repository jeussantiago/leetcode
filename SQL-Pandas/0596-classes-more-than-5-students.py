import pandas as pd


def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    df = courses.groupby('class')['student'].count().reset_index()
    df = df.loc[df['student'] >= 5]
    return df[['class']]


'''
SELECT class
FROM Courses
GROUP BY class
HAVING COUNT(student) >= 5
'''
