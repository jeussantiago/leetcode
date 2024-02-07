'''
SELECT project_id
FROM project
GROUP BY project_id
HAVING COUNT(employee_id) = (
    SELECT COUNT(employee_id) AS employee_count
    FROM project
    GROUP BY project_id
    ORDER BY employee_count DESC
    LIMIT 1
)
'''
