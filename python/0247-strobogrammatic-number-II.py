class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        '''
        n = 3
        [101, 111, 181, 609, 619, 689, 808, 818, 888, 906, 916, 986]
        n = 2
        ["11","69","88","96"]

        11
        00
        88
        69
        96

        - add these the beginning and the end of the string
        - go to next recursion with n - 2

        - if == 0
            - add the numbers that don't have a leading 0
        - if n == 1:
            - get the mid
            - insert [0,1,8] into the mid
            - go next recurions with n -1

        Time: O(5 ^ ((n / 2) +1)) 
            - can make 5 decisions (5 possibel branches)
            - height of the tree would be max (n/2 + 1) since we keep subtracking by 2
        Space: O(5 ^ ((n / 2) +1)) 
            - call stack would be at most ((n / 2) +1)
            - going through each node on the tree 5 ^ ((n / 2) +1)
        '''
        strobo_pairs = [('0', '0'), ('1', '1'), ('8', '8'),
                        ('6', '9'), ('9', '6')]

        def helper(n, final_length):
            if n == 0:
                return [""]
            if n == 1:
                return ["0", "1", "8"]

            strobo_nums = helper(n - 2, final_length)
            new_strobo_nums = []

            for num in strobo_nums:
                for pair in strobo_pairs:
                    # if the current n is in the final length, we don't want to create a combination
                    # that starts with a 0 in front
                    if n != final_length or pair[0] != '0':
                        new_strobo_nums.append(pair[0] + num + pair[1])

            return new_strobo_nums

        res = helper(n, n)
        return res
