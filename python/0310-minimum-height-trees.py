class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        '''
        Topological Sort:

        - undirected adjacency list

        - find the leaf nodes
            - leaf nodes are nodes with only 1 connection

        BFS
        - traverse through leaf nodes
            - go to the neighbors of the leaf nodes
                - turn the neighbors into a leaf node by removing the current leaf node from the neighbor
                (this will turn the neighbor into a leaf node after most of its connections have been removed)
                - if the neighbor only has 1 connection, and therefore becomes a leaf node
                    - then we can add to queue, and traverse it's neighbors

        {
            0: [1]
            1: [0,2,3]
            2: [1]
            3: [1]
        }
        - leaf nodes are [0,2,3]
        - go through neighbors of all of them and remove itself from that neighbor
            - remove 0 from 1
            - remove 2 from 1
            (1 only has 1 connection now to 3, so we can finally add it to the queue)
            - remove 3 from 1

        {
            0: [1]
            1: []
            2: [1]
            3: [1]
        }
        queue = [1]

        ** atmost, there will be 2 roots
            - 1 for odd n
            - 2 for even n

        Time: O(e + n) 
        Space: O(e + n)
        '''
        if n <= 2:
            return list(range(n))

        # undirected adjacency list
        adj = collections.defaultdict(set)
        for node1, node2, in edges:
            adj[node1].add(node2)
            adj[node2].add(node1)

        # find the leaf nodes
        leaves = [node for node, neighbors in adj.items()
                  if len(neighbors) == 1]

        # BFS - find roots
        q = leaves
        remaining_nodes = n
        while remaining_nodes > 2:
            leaves = []
            for node in q:
                for neigh in adj[node]:
                    adj[neigh].remove(node)
                    if len(adj[neigh]) == 1:
                        leaves.append(neigh)

            remaining_nodes -= len(q)
            q = leaves

        return q
