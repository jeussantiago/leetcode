import pandas as pd


def rising_temperature(weather: pd.DataFrame) -> pd.DataFrame:
    weather['nextDayDate'] = weather['recordDate'] + timedelta(days=-1)
    df = weather.merge(weather, left_on='recordDate', right_on='nextDayDate')
    df = df.loc[df['temperature_y'] > df['temperature_x'], ['id_y']]
    return df.rename(columns={'id_y': 'Id'})


'''
SELECT w1.id
FROM Weather as w1, Weather as w2
WHERE w1.temperature > w2.temperature
    AND DATEDIFF(w1.recordDate, w2.recordDate) = 1
'''
