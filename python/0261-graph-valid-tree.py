class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        '''
        Valid Tree:
        - doesn't have loops
        - length of the tree is the same length as (n)

        - create a hash list of the nodes

        {
            0: 1,2,3
            1: 0,4
            2: 0
            3: 0
            4: 1
        }

        - have a visited set
        - start the serach at 0, if 0 is seperated from a second tree with the rest of the values
        then it is not a valid tree
        - so the tree has to have 0 as one of it's nodes (doesn't need to be the root)

        - since the each node is undirectional (going both ways), we need to keep in memory
        the previous node so that we can skip that node in the list
        (ex: 0 -> 1 but 0 is in the list for 1. we need to skip this so that we don't treat it as a visited node)

        ---------

        - if the node is in visited
            - return false

        - add this node to visited

        - go  through the node's connected nodes
            - skip the previos node that allowed you to enter this node list

            - recurse through the current node in the list
            - if this recursion is False,
            (next node is visited => loop)
                - return False

        - return True
        (no loops)


        -------

        - check if valid tree
        - if n != len(tree)
               == (visited set)
        - initially the previous node can be -1 since constraints says the min node value is 0

        Time: O(E + V) where E is the number of edges and V is the number of vertices/nodes
        Space: O(E + V)
        '''

        # create adjacency lsit
        adj = {i: [] for i in range(n)}
        for node1, node2 in edges:
            adj[node1].append(node2)
            adj[node2].append(node1)

        visited = set()

        def dfs(node, prev_node):
            if node in visited:
                return False

            visited.add(node)

            for adj_node in adj[node]:
                # skip the previous node
                if adj_node == prev_node:
                    continue

                if not dfs(adj_node, node):
                    return False

            return True

        return dfs(0, -1) and n == len(visited)
