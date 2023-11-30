import pandas as pd


def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    scores['rank'] = scores['score'].rank(method='dense', ascending=False)
    scores = scores[['score', 'rank']].sort_values(
        by=['score'], ascending=False)
    return scores


'''
# combine the database with itself
#   create every combination possible for the score and every number >= to it
#   3.85    3.85
#   3.85    4
#   3.85    4
# then we can group by the original score and id
#   and count the number of table 2's scores (we need to count the 
#   number of distinct since thats how many numbers are above it in rank)


SELECT
    s1.score,
    COUNT(DISTINCT s2.score) AS 'rank'
FROM
    Scores s1
INNER JOIN Scores s2 ON s1.score <= s2.score
GROUP BY 
    s1.id,
    s1.score
ORDER BY
    s1.score DESC

--------------------------
OR using DENSE RANK

SELECT
  S.score,
  DENSE_RANK() OVER (
    ORDER BY
      S.score DESC
  ) AS 'rank'
FROM
  Scores S;


'''
