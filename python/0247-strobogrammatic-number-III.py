class Solution:
    def strobogrammaticInRange(self, low: str, high: str) -> int:
        '''
        n = 3
        [101, 111, 181, 609, 619, 689, 808, 818, 888, 906, 916, 986]
        n = 2
        ["11","69","88","96"]
        n = 1
        ["0","1","8"]
        n = 0
        [""]

        Time: O(4 * 5^(n/2+1)) where n is the length of high
            : O(5^(n/2+1))
        Space: O(5^(n/2+1)) this for tree ; call stack is (n/2)

        '''
        n = len(high)
        low, high = int(low), int(high)
        output = 1 if low == 0 else 0
        strobo_pairs = [('0', '0'), ('1', '1'), ('6', '9'),
                        ('8', '8'), ('9', '6')]

        def helper(nums, low, high, n):
            nonlocal output
            new_nums = []
            for num in nums:
                if num:
                    if len(num) > n:
                        return
                    elif num[0] != '0' and int(num) >= low and int(num) <= high:
                        output += 1
                for pair in strobo_pairs:
                    new_nums.append(pair[0] + num + pair[1])

            helper(new_nums, low, high, n)

        nums = ["", "0", "1", "8"]
        helper(nums, low, high, n)
        return output
