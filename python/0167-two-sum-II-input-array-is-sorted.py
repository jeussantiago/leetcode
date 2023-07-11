class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        '''

        numbers = [2,7,8,9,10,13,15], target = 19
        - if total > target:
            right pointer -= 1
        - total < target:
            left pointer += 1

        - if the total == target:
            return (left pointer, right pointer)

        - there is exactly 1 solution so we dont have to worry about after the loop

        Time: O(logn)
        Space: O(1)

        '''

        N = len(numbers)-1
        l, r = 0, N
        while l < r:
            total = numbers[l] + numbers[r]

            if total == target:
                return [l+1, r+1]
            elif total > target:
                r -= 1
            else:
                l += 1

        return [0+1, N+1]
