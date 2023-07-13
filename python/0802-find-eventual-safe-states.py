class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        '''
        {
            0: F
            1: F
            2: T
            3: F
            4: T
        }
        [2,4,5,6]

        {
            0: F
            1: F
            2: F
            3: F
        }
        [4]

        Time: O(n)
            ; visit every position once
        Space: O(n)
            ; visited dict
        '''
        visited = {}

        def dfs(i):
            if i in visited:
                return visited[i]

            if len(graph[i]) == 0:
                # terminal node
                return True

            visited[i] = False
            # all neighbors need to lead to a terminal node for
            # this current node to also be a safe node and thus be true
            allSafePaths = True
            for neigh in graph[i]:
                allSafePaths = (allSafePaths and dfs(neigh))

            visited[i] = allSafePaths
            return visited[i]

        res = []
        for i in range(len(graph)):
            if dfs(i):
                res.append(i)
        return res


class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        '''
        - slight difference in that, if you see that a path is not a safe path anymore, you stop search
        - this doesnt make any time or space updates as it still visits every node once
        '''
        visited = {}

        def dfs(i):
            if i in visited:
                return visited[i]

            if len(graph[i]) == 0:
                return True

            visited[i] = False
            allSafePaths = True
            for neigh in graph[i]:
                if not dfs(neigh):
                    return False

            visited[i] = True
            return visited[i]

        res = []
        for i in range(len(graph)):
            if dfs(i):
                res.append(i)
        print(visited)
        return res
