class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        '''
        length = 5, updates = [[1,3,2],[2,4,3],[0,2,-2]]
        - create the dp of length
        [0,0,0,0,0]
        - insert at start index the increment val
        - insert at end+1 index the opposite increment val to cancel out
            - if end == length: don't do anything, its the end of the array so no operation matters
        - what this does is that at the end we will have a running sum, similar to prefix sum, and insert the val at dp the current running sum

        Ex: if [1,3,2] was our only insert
        - we insert
        [0,2,0,0,-2]
        - fill in the final results
        sum = 0
        [0,2,0,0,-2]
        sum = 2
        [0,2,2,2,-2]
        sum = 0
        [0,2,2,2,0]

        Ex: using all the updates
        [-2,2,3,2,-2]
        => [-2,0,3,5,3]

        n is length
        m is the len of updates arr
        Time: O(n + m)
        Space: O(n)
        '''
        dp = [0] * length
        for start, end, inc in updates:
            dp[start] += inc
            if end < length-1:
                dp[end + 1] -= inc

        res = []
        running_sum = 0
        for num in dp:
            running_sum += num
            res.append(running_sum)

        return res
