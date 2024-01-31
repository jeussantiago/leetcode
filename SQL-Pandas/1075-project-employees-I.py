import pandas as pd


def project_employees_i(project: pd.DataFrame, employee: pd.DataFrame) -> pd.DataFrame:
    df = project.merge(employee, how='left', on='employee_id')
    res = df.groupby('project_id')['experience_years'].mean().round(
        2).reset_index(name='average_years')
    return res


'''
SELECT p.project_id, ROUND(AVG(e.experience_years), 2) AS average_years
FROM project p
LEFT JOIN employee e
    ON p.employee_id = e.employee_id
GROUP BY p.project_id
'''
