import pandas as pd


def find_investments(insurance: pd.DataFrame) -> pd.DataFrame:
    # drop the rows where the rows have the same lat and lon
    # group by the tiv_2015
    # then sum up the tiv_2016
    df = insurance[insurance.duplicated(subset=['tiv_2015'], keep=False) & ~insurance.duplicated(
        subset=['lat', 'lon'], keep=False)]
    return df.agg(tiv_2016=('tiv_2016', 'sum')).round(2)


'''
SELECT ROUND(SUM(i.tiv_2016), 2) AS tiv_2016
FROM Insurance i
JOIN (
    # repeating tiv_2015
    SELECT *
    FROM Insurance
    GROUP BY tiv_2015
    HAVING COUNT(DISTINCT pid) > 1
) AS i0
ON i.tiv_2015 = i0.tiv_2015
JOIN (
    # unique lat, lon
    SELECT CONCAT(lat, lon) AS lat_lon
    FROM Insurance
    GROUP BY CONCAT(lat, lon)
    HAVING COUNT(DISTINCT pid) = 1
) AS i1
ON CONCAT(i.lat, i.lon) = i1.lat_lon
'''
