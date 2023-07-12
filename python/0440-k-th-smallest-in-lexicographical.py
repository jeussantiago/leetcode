class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        '''
        Time: O(n)
        Space: O(logn)
        '''
        cur = 1
        k -= 1
        while k > 0:
            steps = self.countSteps(n, cur)
            if steps <= k:
                cur += 1
                k -= steps
            else:
                cur *= 10
                k -= 1

        return cur

    def countSteps(self, n, cur):
        steps = 0
        nxt = cur + 1
        while cur <= n:
            steps += min(n - cur + 1, nxt - cur)
            cur *= 10
            nxt *= 10

        return steps
