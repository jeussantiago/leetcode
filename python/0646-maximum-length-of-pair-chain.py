class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        '''
        [[1,5], [2,5], [3,5]]

        - sort by 2nd element(end of chain)
        - keep track of current end of chain value

        - since its sorted, if the first element(start of pair chain) > current end of chain
            - update current end of chain to be the end of pair chain(2nd element)
            - increase the chain count

        Time: O(nlogn)
            ; (nlogn) sort by 2nd element
            ; (n) greedy search
        Space: O(1)
            ; (n) python sort - not really counted in complexity evaluation
        '''

        pairs.sort(key=lambda x: x[1])
        end_of_chain = float(-inf)
        res = 0
        for start, end in pairs:
            if start > end_of_chain:
                res += 1
                end_of_chain = end

        return res
