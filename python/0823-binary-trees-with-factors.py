class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        '''
        [2,4,5,10]

        {
            2: 0
            4: 1
            5: 2
            10: 3
        }

        - have to compare each number with the previous numbers
            - check if the previous number is evenly divisible to the current number (mod) => curr_num % prev_num == 0
            (this will be the left child of the node)
            - need to look for right child for node
                - since we know that the curr_num is evenly divisible by the prev_number/left child, to get the value 
                for right child, we can simply (curr_num / left_child) 
                - this number that we are searching for, if its located in the array, then we can set that as a right child

                - since each node can appear in multiple trees, we can multiply the left count by the right count to increase
                the count for the current number

        [1,1,1,1]
        - 4 divisble by 2 (mod). remainder would be 2 which is found in the array. we can increase the value of the 4 position
        [1,2,1,1]
        - 10 divisble by 2 (mod). remainder would be 5 which is found in the array. we can increase the value of the 10 position
        [1,2,1,2]
        - 10 divisble by 5 (mod). remainder would be 2 which is found in the array. we can increase the value of the 10 position
        [1,2,1,3]
        sum = 7

        Time: O(n^2)
            ; (nlogn) sort
            ; (n^2) iterating through the numbers and any number of times until
            ; (n) sum array at end
        Space: O(n)
            ; (n) python sorting
            ; (n) hashmap
        '''
        MOD = 10 ** 9 + 7
        N = len(arr)
        arr.sort()
        dp = [1] * N
        # need hashmap to search using right child node
        val_ind = {num: i for i, num in enumerate(arr)}
        for i, num in enumerate(arr):
            for left_ind in range(i):
                if num % arr[left_ind] == 0:
                    # found even divisible -> left child
                    right_node_val = num / arr[left_ind]
                    if right_node_val in val_ind:
                        # found right node
                        dp[i] += (dp[left_ind] *
                                  dp[val_ind[right_node_val]]) % MOD

        return sum(dp) % MOD
