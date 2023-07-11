class Solution:
    def lengthLongestPath(self, input: str) -> int:
        '''
        where n is the number of branches
        Time: O(n)
        Space: O(n)
        '''
        lst = input.split('\n')
        path = []

        res = 0
        curr_len = 0
        for branch in lst:
            branch = branch.split('\t')
            tabs = len(branch) - 1

            while path and path[-1][0] >= tabs:
                prev_branch = path.pop()
                curr_len -= len(prev_branch[1])

            path.append((tabs, branch[-1]))
            curr_len += len(branch[-1])

            if "." in branch[-1]:
                res = max(res, curr_len + len(path) - 1)

        return res
