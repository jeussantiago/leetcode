class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        '''
        Solution 1:
        - create array of n!
        - get all permutations for an array of n
        - return kth permutation

        Time: O(n!)

        Solution 2:
        n = 4

        1234
        1243
        1324
        1342
        1423
        1432
        --
        2134
        2143
        2314
        2341
        2413
        2431
        --
        3124
        3142
        3214
        3241
        3412
        3421
        --
        4123
        4132
        4213
        4231
        4312
        4321

        - figure out how to know the number of permuations from n length string
        - divide this number by n (Ex: n = 4, total permutations = 24 => 24/4 = 6)
            (each number represents different quadrants, gotta figure out the qudrant k is in)
            - k // 6(# of permutations in a qudrant) (Ex: 17 // 6 = 2 => 17 permutation is in qudrant 3)
            - first number in res = 2
            - remove 2 from list of numbers using index and now leftover numbers are "1,3,4"
            - k needs to be updated
            (to update k - we need to remove the number of permutations before teh current quadrant
            2(# of qudrants before current qudrant) * 6(number of permutations in each qudrant) = 12)
            - k = 17 - 12 = 5
        - repeate process with the new n=3, the new string="134" and the new k=5

        Time: O(n)
        Space: O(1)
        '''
        k -= 1
        res = ""
        nums = [str(n+1) for n in range(n)]

        while nums:
            N = len(nums)
            total_num_permutations = math.factorial(N)
            num_permutations_in_qudrant = total_num_permutations // N
            # the quadrant the kth index is in - if n=4 and k=17 => k is in the 2nd qudrant
            kth_qudrant = k // num_permutations_in_qudrant
            # remove the number from the possible outcomes
            number = nums.pop(kth_qudrant)
            # add that number to the results
            res += number
            # update k - subtract t amount of permutations before the quadrant k is in
            k = k - (kth_qudrant * num_permutations_in_qudrant) #k % num_permutations_in_qudrant

        return res
       























