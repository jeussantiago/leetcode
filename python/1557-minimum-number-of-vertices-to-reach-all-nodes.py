class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        '''
        n = 6 ; edges = [[2,1],[2,0],[0,5],[3,4],[4,0]]
        leaf = [2,3]
        visited = [0,5,1,2,3,4]

        e is the number of edges in the graph (arrows direction)
        n is the vertices/nodes in the graph
        Time: O(e + n)
                ; (e) creating the graph
                ; (e + n) traverse the graph
                ; (e + e + n) => (e + n)
        Space: O(e + n) 
                ; graph dict
        '''
        neighbors = collections.defaultdict(list)
        for start_node, end_node in edges:
            neighbors[start_node].append(end_node)

        def dfs(node):
            if node in visited:
                if node in leaves:
                    leaves.remove(node)

                return

            visited.add(node)
            for neigh in neighbors[node]:
                dfs(neigh)

        leaves = set()
        visited = set()
        for node in range(n):
            if node not in visited:
                leaves.add(node)
                dfs(node)

        return list(leaves)


class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        '''
        OR, you can just remove all appearances of the nodes going to since they are not the leaf nodes

        e is the number of edges
        Time: O(e) ; have to check the edges arr
        Space: O(n) ; number of nodes to start the range set
        '''
        leaves = set(range(n))
        for _, end_node in edges:
            if end_node in leaves:
                leaves.remove(end_node)

        return list(leaves)
