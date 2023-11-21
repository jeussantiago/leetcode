class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        '''
        - this problem probably involves finding a common ground number
        - we don't know which pairs match up with each other or what they will
        sum to
        - we only have the current number

        - we could take the current number and subtract that from it's reverse
        counterpart

        42 - rev(42) = 42 - 24 = 18
        97 - rev(97) = 97 - 79 = 18

        - this tells us that these numbers are pairs of each other

        - might have a case of all single digits where each number complements
        each other
        [1,2,3,4,5,6,7,8]
        - we can have a hash map to keep track of the appearances of the (num - rev(num))
        {
            0: 8
        }
        - since each number is a combination of every number before it, the total count
        of nice pairs is factorial (!num)

        - but in place, we can just add the current num value

        k is the number of digits in num but that is at most 9 digits since 
            constraints are 0 <= nums[i] <= 109
        Time: O(n)
            ; (n) iterating through nums
            ; (1) reversing nums
        Space: O(n)
            ; hashmap
        '''

        def rev(num):
            total = 0
            while num:
                total = (total * 10) + (num % 10)
                num //= 10
            return total

        # create the hashmap/calculate
        pairs = collections.defaultdict(int)
        res = 0
        MOD = 10 ** 9 + 7
        for num in nums:
            diff = num - rev(num)
            res = (res + pairs[diff]) % MOD
            pairs[diff] += 1

        return res
