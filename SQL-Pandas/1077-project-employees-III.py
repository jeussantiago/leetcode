import pandas as pd


def project_employees(project: pd.DataFrame, employee: pd.DataFrame) -> pd.DataFrame:
    project_employee = project.merge(employee, on='employee_id', how='left')
    experience_max = project_employee.groupby(
        'project_id')['experience_years'].max().reset_index()
    df = project_employee.merge(
        experience_max, on=['project_id', 'experience_years'])
    return df[['project_id', 'employee_id']]


'''
WITH project_employees AS (
    SELECT p.project_id, p.employee_id, e.experience_years
    FROM project p
    LEFT JOIN employee e
        ON p.employee_id = e.employee_id
)
SELECT a.project_id, a.employee_id
FROM project_employees a
LEFT JOIN (
    SELECT project_id, MAX(experience_years) AS max_experience
    FROM project_employees 
    GROUP BY project_id
) b
    ON a.project_id = b.project_id
WHERE a.experience_years = b.max_experience
'''
