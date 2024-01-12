import pandas as pd


def exchange_seats(seat: pd.DataFrame) -> pd.DataFrame:

    N = len(seat)

    def helper(row):
        print(row['id'])
        curr_id = row['id']
        # if id is odd and not the not last - take next id
        if curr_id % 2 == 1 and curr_id != N:
            return curr_id + 1
        # if id is odd and the last in odd length data - keep current seat
        elif curr_id % 2 == 1 and curr_id == N:
            return curr_id
        # id is even - always take id before
        else:
            return curr_id - 1

    seat['new_pos'] = seat.apply(helper, axis=1)
    seat = seat[['new_pos', 'student']]
    seat.sort_values(by='new_pos', ascending=True, inplace=True)
    seat.rename(columns={"new_pos": "id"}, inplace=True)
    return seat


'''
SELECT 
    (CASE
        # if id is odd and not the not last - take next id
        WHEN MOD(id, 2) != 0 AND counts != id THEN id + 1
        # if id is odd and the last in odd length data - keep current seat
        WHEN MOD(id, 2) != 0 AND counts = id THEN id 
        # id is even - always take id before
        ELSE id - 1
    END) AS id,
    student
FROM seat, (
    SELECT COUNT(*) AS counts
    FROM Seat
) AS seat_counts
ORDER BY id ASC
'''
