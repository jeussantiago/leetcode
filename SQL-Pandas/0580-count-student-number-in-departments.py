import pandas as pd


def count_students(student: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    df = department.merge(student, on='dept_id', how='left')
    df = df.groupby('dept_name')['student_id'].count().reset_index()
    df.rename(columns={'student_id': 'student_number'}, inplace=True)
    df.sort_values(by=['student_number', 'dept_name'],
                   ascending=[False, True], inplace=True)
    return df


'''
SELECT dept_name, COUNT(s.dept_id) AS student_number
FROM Department d
LEFT JOIN Student s
    ON d.dept_id = s.dept_id
GROUP BY d.dept_name
ORDER BY student_number DESC, d.dept_name
'''
