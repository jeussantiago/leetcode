class Solution:
    def sortArray(self, nums: List[int]) -> int:
        '''
        [4,2,0,3,1] => [0,1,2,3,4]
        [1,0,2,4,3] => [1,2,3,4,0]

        situation of getting 0 to front:

            - keep swapping 0 with the position the rightful number should be placed in
            [4,2,0,3,1] => [4,0,2,3,1] => [4,1,2,3,0] => [0,1,2,3,4]

            - might have a situation where 0 is in the final spot but the array isnt sorted
            [2,4,0,3,1] => [0,4,2,3,1]
                - swap with the num that is in the wrong place
                - while loop: (num == ind)
                    ind += 1

                - if the ind is at the end
                    - array is sorted
                    - return count

        situation of getting 0 to back:
            - similar idea
            - evrything needs to offsetted by 1
            [1,0,2,4,3] => [1,2,0,4,3] => [1,2,3,4,0]
            [2,3,1,4,0]


        Time: O(n)
            ; visit every number once
            ; do operation twice for putting 0 in front and back
        Space: O(n)
            ; dictionary of indicies
            ; copy of nums
        '''
        return min(self.helper(nums[:], 0), self.helper(nums[:], len(nums)-1))

    def helper(self, nums, finalZeroInd):

        def swapZeroPlace(swap_num):
            swap_ind, zero_ind = ind_dict[swap_num], ind_dict[0]
            # update the array
            nums[zero_ind], nums[swap_ind] = nums[swap_ind], nums[zero_ind]
            # update the dictionary
            ind_dict[0], ind_dict[swap_num] = swap_ind, zero_ind

        res = 0
        ind_dict = {num: i for i, num in enumerate(nums)}
        # if 0 in front, we don't want to offset the numbers
        offset = 0 if finalZeroInd == 0 else 1
        # starting index for searching
        i = 1 if finalZeroInd == 0 else 0

        while True:
            if ind_dict[0] != finalZeroInd:
                swapZeroPlace(ind_dict[0] + offset)
                res += 1
            else:
                # 0 is already in its final position - swap with the first item not in order
                while i < len(nums) and nums[i] == i + offset:
                    i += 1

                # i at end of array means sorted array
                if i == len(nums) - offset:
                    return res

                swapZeroPlace(nums[i])
                res += 1

        return res
