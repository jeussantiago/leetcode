class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        '''
        2 pointers

        - have a pointer representing the position of positive 
        number and a position for negative number
        - these positions are going to be predertimed

        - initialized a results array, size of nums
        - for through each number in nums
        -   if the number is negative, add the number to the 
            results arr at the negative pointer position
                then increase the value of the negative pointer by 2

        -   do same if number is positive

        Time: O(n)
        Space: O(1)
            ; assuming that the results array doesn't factor into
            ; the overall space (b/c thats what leetcode normally does)
        '''
        res = [0] * len(nums)
        pos_ptr, neg_ptr = 0, 1
        for num in nums:
            if num < 0:
                res[neg_ptr] = num
                neg_ptr += 2
            else:
                res[pos_ptr] = num
                pos_ptr += 2

        return res


class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        '''
        keep space for the numbers

        Time: O(n)
        Space: O(n)
        '''
        pos_nums, neg_nums = [], []
        # seperate the nums, to preserve the order at which the
        # nums appear
        for num in nums:
            if num < 0:
                neg_nums.append(num)
            else:
                pos_nums.append(num)

        # combine the positive and negative nums
        # has to start with positive number
        res = []
        for i in range(len(pos_nums)):
            res.append(pos_nums[i])
            res.append(neg_nums[i])

        return res
