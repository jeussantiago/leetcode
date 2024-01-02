import pandas as pd


def tree_node(tree: pd.DataFrame) -> pd.DataFrame:
    # get the root id
    root_id = tree.loc[tree['p_id'].isnull()]['id'].values[0]
    # get the parent ids
    parent_ids = tree['p_id'].drop_duplicates().dropna().values

    # filter function
    def get_type(row):
        if row['id'] == root_id:
            return 'Root'
        elif row['id'] in parent_ids:
            return 'Inner'
        else:
            return 'Leaf'

    tree['type'] = tree.apply(get_type, axis=1)
    tree = tree[['id', 'type']].sort_values(by='id')
    return tree


'''
SELECT id,
    CASE
        # root when not parent
        WHEN tree.id = (
            SELECT t1.id
            FROM tree t1 
            WHERE t1.p_id IS NULL
        )
            THEN 'Root'
        # node is a parent of another node (check if the id appears in 
        # the other column)
        WHEN tree.id IN (
            SELECT t2.p_id
            FROM tree t2
        )
            THEN 'Inner'
        # last case
        ELSE 'Leaf'
    END AS type
FROM tree
ORDER BY id
'''
