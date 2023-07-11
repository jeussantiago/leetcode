class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Greedy:

        Do not return anything, modify nums in-place instead.
        [3,5,2,1,6,4]
         |   |   | 
        - if i is even
        ( make sure that it is < than the next number)
            - if num[i] > num[i + 1]
                - swap values

        [3,5,2,1,6,4]
           |   |   | 
        - if i is odd
        (make sure that it is >= than the next number) 
            if num[i] < num[i+1]
                -swap values 

        Time: O(n)
        Space: O(1)
        """

        for i in range(len(nums)-1):
            # odd index
            if i % 2:
                if nums[i] < nums[i+1]:
                    nums[i], nums[i+1] = nums[i+1], nums[i]

            # even index
            else:
                if nums[i] > nums[i+1]:
                    nums[i], nums[i+1] = nums[i+1], nums[i]

        print(nums)
