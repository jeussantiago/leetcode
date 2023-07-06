class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        '''
        - might be duplicates in candidates
        - sort candidates first
            - b/c the lower numbers are not going to be used once we try all combinations of them

        Constrainsts:
        - each number can only be used once
        - there is atleast one number in candidates
        - value of candidates numbers atleast 1
        - target atleast 1

        Time: O(2^n + nlogn = 2^n) decision tree with 2 combinations to include number or not include number; tree size is number of value sin candidates (n) : sorting will take nlogn
        '''
        res = []
        def helper(i, candidate):
            if sum(candidate) == target:
                res.append(candidate.copy())
                return
            if sum(candidate) > target or i >= len(candidates):
                return
            
            for j in range(i, len(candidates)):
                #skip duplicates
                if j > i and candidates[j] == candidates[j-1]:
                    continue
                candidate.append(candidates[j])
                helper(j+1, candidate)
                candidate.pop()

        candidates.sort()
        helper(0, [])
        return res