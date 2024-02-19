import pandas as pd


def unpopular_books(books: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    # orders from the last year - we get the number of copies sold
    order = orders.loc[orders['dispatch_date'] + pd.Timedelta(
        days=365) > '2019-06-23'].groupby('book_id')['quantity'].sum().reset_index()
    # get the books publish before the last month
    book = books[books['available_from'] < '2019-05-23']
    # we only want to keep the valid books, so merge only on that
    df = book.merge(order, how='left', on='book_id').fillna(0)
    df = df.loc[df['quantity'] < 10]
    return df[['book_id', 'name']]


'''
WITH ValidBooks AS (
    SELECT *
    FROM Books
    WHERE available_from < '2019-05-23'
), LastYearOrders AS (
    SELECT *
    FROM Orders
    WHERE dispatch_date BETWEEN '2018-06-23' AND '2019-06-23'
)

SELECT r.book_id, r.name
FROM (
    # the list of valid books and their sales for the last year,
    # excluding the books published last month
    SELECT A.book_id, A.name, IFNULL(copiesSold, 0) as copiesSold
    FROM ValidBooks A
    LEFT JOIN (
        # these are the orders of the books that 
        # are from 1 year ago and the books that
        # have been published for atleast one month
        SELECT book_id, SUM(quantity) AS copiesSold
        FROM LastYearOrders
        WHERE book_id IN (
            SELECT book_id
            FROM ValidBooks
        )
        GROUP BY book_id
    ) B
    ON A.book_id = B.book_id
) r
WHERE r.copiesSold < 10 


'''
