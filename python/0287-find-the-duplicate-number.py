class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        '''
        [3,3,5,4,1,3] // Compare nums[0] to nums[nums[0]] (i.e. nums[0] to nums[3]). 3 != 4. Swap them. Now the first 3 will be swapped into its correct position, and position 0 has 4
        [4,3,5,3,1,3]
        [1,3,5,3,4,3]
        [3,1,5,3,4,3] 

        Time: O(n)
        Space: O(1)
        '''

        while nums[0] != nums[nums[0]]:
            nums[nums[0]], nums[0] = nums[0], nums[nums[0]]
        return nums[0]


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        '''
        Binary Search
        Time: O(nlogn)
        Space: O(1)
        '''
        low = 1
        high = len(nums) - 1

        while low <= high:
            cur = (low + high) // 2
            count = 0

            # Count how many numbers are less than or equal to 'cur'
            count = sum(num <= cur for num in nums)
            if count > cur:
                duplicate = cur
                high = cur - 1
            else:
                low = cur + 1

        return duplicate


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        '''
        Linked List Cycle
        (Floyds ALgorithm - will tell you the beginning of the cycle of a linked list)

        - find the cycle in the linked list
        - slow and fast pointer
        0 - 1 - 2
            |   |
            3 --

        - then find where the cycle begins
        - pointer on where we found the cycle
        - a pointer at the beginning of the linked list
        ||
        v
        0 - 1 - 2
            |   |
            3 --
            ^
            ||
        - just move them one by one until they meet

        https://www.youtube.com/watch?v=wjYnzkAhcNk&t=42s&ab_channel=NeetCode

        Time: O(n)
        Space: O(1)
        '''

        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow
