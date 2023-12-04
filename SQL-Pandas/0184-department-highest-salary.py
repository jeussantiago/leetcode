import pandas as pd


def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    df = employee.merge(department, left_on='departmentId',
                        right_on='id', how='left')
    df.rename(columns={"name_x": 'Employee',
              'name_y': 'Department', 'salary': 'Salary'}, inplace=True)
    max_salary = df.groupby('Department')['Salary'].transform('max')
    df = df[df['Salary'] == max_salary]
    return df[['Employee', 'Salary', 'Department']]


'''
SELECT r.name AS 'Department', p.name AS 'Employee', p.salary AS 'Salary'
FROM Employee p
RIGHT JOIN (
    SELECT e.departmentId, max(e.salary) AS max_salary, d.name
    FROM Employee e
    INNER JOIN Department d ON d.id = e.departmentId
    GROUP BY e.departmentId
) AS r ON p.departmentId = r.departmentId AND p.salary = r.max_salary


OR

SELECT
    Department.name AS 'Department',
    Employee.name AS 'Employee',
    Salary
FROM
    Employee
        JOIN
    Department ON Employee.DepartmentId = Department.Id
WHERE
    (Employee.DepartmentId , Salary) IN
    (   SELECT
            DepartmentId, MAX(Salary)
        FROM
            Employee
        GROUP BY DepartmentId
    )
;
'''
