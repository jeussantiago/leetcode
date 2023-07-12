class Solution:
    def average(self, salary: List[int]) -> float:
        '''
        - calling min and max respectively would be O(2n), I wanted to do in just O(n) even though it doesnt matter
        T: O(n)
        S: O(1)
        '''
        # mn, mx = float('inf'), float('-inf')
        # total = 0
        # for num in salary:
        #     total += num
        #     mn = min(mn, num)
        #     mx = max(mx, num)

        # return (total - (mn + mx)) / (len(salary) - 2)

        mn, mx = min(salary), max(salary)
        return (sum(salary) - (mn + mx)) / (len(salary) - 2)
