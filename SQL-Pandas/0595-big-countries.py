import pandas as pd


def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    df = world.loc[(world['area'] >= 3000000) |
                   (world['population'] >= 25000000)]
    return df[['name', 'population', 'area']]


'''
SELECT w.name, w.population, w.area
FROM world w
WHERE w.area >= 3000000 OR w.population >= 25000000
'''
