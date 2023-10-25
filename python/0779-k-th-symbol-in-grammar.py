class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        '''
        n=5 k=8

        0
        01
        0110
        01101001
        0110100110010110
               ^

        - subtract 1 from k => k-1 = 7
        (0 index position)
        - we don't know how the final row will look like,
            - but we do know the position of the number we are looking for at each row

            n=5 k=7
            n=4 k=3
            n=3 k=1
            n=2 k=0

            - we start from n=2 and work our way up
            - if the value is even, then we take the left subtree
            - if the value is odd, then we take the right subtree

            n=2 k=0, we take the left of the first row

            - might keep the rows on a stack

        n is the number of rows
        Time: O(n)
            ; going through the tree
        Space: O(n)
            ; stack
        '''
        pos_stack = []
        k -= 1
        while n >= 2:
            pos_stack.append(k)
            k //= 2
            n -= 1

        prev_num = 0
        while pos_stack:
            pos = pos_stack.pop()
            next_sub = "01" if prev_num == 0 else "10"

            if pos % 2:
                prev_num = int(next_sub[1])
            else:
                prev_num = int(next_sub[0])

        return prev_num
