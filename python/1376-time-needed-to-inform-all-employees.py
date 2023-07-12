class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        '''
        DFS
        '''
        adj = collections.defaultdict(list)
        for emp, superior in enumerate(manager):
            adj[superior].append(emp)

        def dfs(superior):
            total_time = 0
            for subordinate in adj[superior]:
                total_time = max(total_time, dfs(
                    subordinate) + informTime[superior])

            return total_time

        return dfs(headID)


class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        '''
        BFS
        n is the size of manager arr
        Time: O(n)
        Space: O(n)
        '''
        adj = collections.defaultdict(list)
        for emp, superior in enumerate(manager):
            adj[superior].append(emp)

        total_time = 0
        q = collections.deque([(headID, 0)])
        while q:
            superior, inform_time = q.popleft()
            total_time = max(total_time, inform_time)
            for subordinate in adj[superior]:
                q.append((subordinate, inform_time + informTime[superior]))

        return total_time
