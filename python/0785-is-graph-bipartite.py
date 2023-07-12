class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        ''' 
        - seperate teh graph into 2 groups where 1 group is not connected with any other node in its own group
        - if group A had [1,3,5],
            - node 1 can't have an edge with node 5

        e is the number of eddges
        n is the number of vertices/nodes
        Time: O(e + n)
        Space: O(n) ; nodes array
        '''
        nodes = [0] * len(graph)

        def dfs(node):
            for neigh in graph[node]:
                # if the value in the neighbor is opposite to the value in the current node, then its good
                # 1 ; -1
                if nodes[neigh] == nodes[node]:
                    # visited node - same group
                    return False

                elif nodes[neigh] == 0:
                    # unvisited node - turn it to the opposite group
                    nodes[neigh] = nodes[node] * -1
                    if not dfs(neigh):
                        return False

                # don't do anything for visited nodes of opposite group
            return True

        for node in range(len(graph)):
            if nodes[node] == 0:
                nodes[node] = 1
                if not dfs(node):
                    return False
        return True
