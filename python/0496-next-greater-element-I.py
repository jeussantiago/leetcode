class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        '''
        Stack

        - add numbers to the stack
        - if the current number is bigger than the item in the stack
            - pop off that item
            - store in a lookup the key=popped, val=curr_item
            (this states that the val is the next greater item from the key) 

        - at the end of nums2, go through nums1 to lookup the next greater items

        n1 is the length of nums1
        n2 is the length of nums2
        Time: O(n1 + n2)
            ; (n2) get the next greater element for every item in nums2
            ; (n1) lookup the next greater element for nums1
        Space: O(n2)
        '''
        # get the next greater element for all numbers in nums2
        stack = []
        lookup = {}
        for num in nums2:
            while stack and num > stack[-1]:
                less_num = stack.pop()
                lookup[less_num] = num

            stack.append(num)

        # empty the stack
        while stack:
            lookup[stack.pop()] = -1

        # lookup the next greater element for nums1 using nums2 hashmap lookup
        # can do this b/c guranteed that all nums in nums1 in nums2
        return [lookup[num] for num in nums1]


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        '''
        create an index hashmap of nums2

        - iterate through nums1,
            - look at the index in nums2 through the hashmap

        n1 is the length of nums1
        n2 is the length of nums2
        Time: O(n1 * n2)
            ; (n2) create a hashmap of the indexes of nums2
            ; (n1) iterate through nums1
            ; (1) nums2 index lookup through hashmap
            ; (n2) search rightwards to find the immediate greater elemnt
        Space: O(n2)
            ; (n2) hashmap
        '''

        index = {num: i for i, num in enumerate(nums2)}
        res = []
        for num in nums1:
            # num position in nums2
            num_ind_in_nums2 = index[num] + 1

            while num_ind_in_nums2 < len(nums2) and nums2[num_ind_in_nums2] <= num:
                num_ind_in_nums2 += 1

            next_greater_ele = nums2[num_ind_in_nums2] if num_ind_in_nums2 < len(
                nums2) else -1
            res.append(next_greater_ele)

        return res
