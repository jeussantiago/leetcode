class Solution:
    def findPermutation(self, s: str) -> List[int]:
        '''
        Greedy Stack

        - if we see a D, add curr number to stack
        - if we see an I, pop all numbers from stack and add to results

        IDDI
        - see "I", add next num then pop the entire stack
        [1] ; res=[] ;
        [] ; res=[1] ; 
        - see 2 "D", add the next two numbers to stack
        [2,3] ; res=[1]
        - see "I", add next num then pop the entire stack
        [2,3,4] ; res=[1]
        [] ; res=[1,4,3,2]

        - at the end, we still need to add the last number
        - so add the next number and pop the entire stack
        [5] ; res=[1,4,3,2]
        [] ; res=[1,4,3,2,5]

        Time: O(n)
            ; (2n) go back on itself at most twice since items from stack are being added and popped
        Space: O(n)
        '''

        res = []
        stack = []
        for i, char in enumerate(s):
            stack.append(i+1)

            if char == "I":
                while stack:
                    res.append(stack.pop())

        # add last number and empty the stack
        stack.append(len(s) + 1)
        while stack:
            res.append(stack.pop())

        return res
