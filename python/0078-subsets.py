class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        '''
        Time: O(n^!n)
        Space: O()
        [1,2,3]
        []
        [1]
        [1,2]
        [1,2,3]
        [1,3]
        [2]

        this method uses a subset of the nums as arguments
        '''
        def backtracking(currentNumsSub, sub):
            res.append(sub.copy())
            if not currentNumsSub: return
            for i in range(len(currentNumsSub)):
                sub.append(currentNumsSub[i])
                backtracking(currentNumsSub[i+1:], sub)
                sub.pop()

        res = []
        backtracking(nums, [])
        return res
    
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        '''
        this method uses the index as the argument - saves space
        - we don't append the number to the sub (current subset creating) b/c we don't want to bring that number over after
        every iteration. this is the reason why we pop after backtracking
            - to solve, we enter as an argument the sub array with the number without doing it outside the backtracking fucntion.
            This allows for non memory usage
        '''
        res = []
        def backtracking(start_i, sub):
            res.append(sub)
            for i in range(start_i, len(nums)):
                backtracking(i+1, sub+[nums[i]])

        backtracking(0, [])
        return res

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        '''
        [1,2,3]
        res = []
        num = 1
        res = [[], [1]]
        num = 2
        res = [[], [1], [2], [1,2]]
        num = 3
        res = [[], [1], [2], [1,2], [3], [1,3], [2,3], [1,2,3]]

        for each number in nums:
            append that number to the end of the result's current values
            (you are nto modifying, you are creatinga new array)

        Time: O()
        Space: O()
        '''

        res = [[]]
        for num in nums:
            res += [sub + [num] for sub in res]
        return res


























