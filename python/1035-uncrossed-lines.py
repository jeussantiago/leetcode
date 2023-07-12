class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        '''
        Recursion (Top-down)

        - if nums1[i] == nums2[j]
            - success
            - we can draw a line
        - else nums1[i] != nums2[j]
            - we don't know whether to iterate the pointer on nums1 or nums2
            - we just have to go down both paths
                - save whichever path gets the most lines

        - save the current number of lines in cache
        key=(i,j) ; value=max_num_of_lines

        n1 is length of nums1
        n2 is length of nums2
        Time: O(n1 * n2)
        Space: O(n1 * n2) ; max(n1, n2) the recursion stack 
        '''
        N1, N2 = len(nums1), len(nums2)
        cache = {}

        def dfs(i, j):
            if i >= N1 or j >= N2:
                return 0

            if (i, j) in cache:
                return cache[(i, j)]

            if nums1[i] == nums2[j]:
                cache[(i, j)] = dfs(i + 1, j + 1) + 1
            else:
                cache[(i, j)] = max(dfs(i + 1, j), dfs(i, j + 1))

            return cache[(i, j)]

        return dfs(0, 0)


class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        '''
        DP:
        n1 is length of nums1
        n2 is length of nums2
        Time: O(n1 * n2)
        Space: O(n1 * n2)
        '''

        N1, N2 = len(nums1), len(nums2)
        # +1 for base case
        dp = [[0] * (N2 + 1) for _ in range(N1 + 1)]

        for i in range(1, N1 + 1):
            for j in range(1, N2 + 1):
                if nums1[i-1] == nums2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i-1][j])

        return dp[-1][-1]
