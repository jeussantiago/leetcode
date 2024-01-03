import pandas as pd


def triangle_judgement(triangle: pd.DataFrame) -> pd.DataFrame:

    def isTriangle(row):
        if (
            row['x'] + row['y'] > row['z']
            and row['z'] + row['y'] > row['x']
            and row['x'] + row['z'] > row['y']
        ):
            return "Yes"

        return "No"

    triangle['triangle'] = triangle.apply(isTriangle, axis=1)
    return triangle


'''
# create a triangle if x + y > z
SELECT *, 
    CASE
        WHEN x + y > z AND x + z > y AND y + z > x
            THEN "Yes"
        ELSE "No"
    END AS triangle
FROM Triangle
'''
