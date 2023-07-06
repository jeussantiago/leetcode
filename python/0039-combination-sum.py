class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        '''
        - iterate through array
            - check how many times the num goes into the target
                - if theres no remainder - create an array of the number
                - if theres remainder 
                    - calculate how much you still need then repeat the process for the other numbers (backtracking)
        - helper (parameters: the current list that we're creating, new target (sum of list - target))
            - if the current number is over the new target => return False (backtract)
            - call helper([newList + appended current number, new_target])
            - newList.pop()
        - since the array is sorted in increasing order, we can assume that if we find all combinations of the lower numbers, then those numbers should not appear in future/higher number combinations
            - keep track of the index
        
        Constraints:
        - all elements of list are distinct
        - can use all elements however many times you want
        - there will be atleast 1 number in List
        - values of num in List will be between 2-40
        - target between 1-40

        Time: O(2^n) make 2 decisions at every branch of our decision tree (2^ height_of_tree) ; height of tree (n) can be atmost the number in the target
        '''
        res = []
        def helper(i, candidate):
            if sum(candidate) == target and candidate not in res:
                #we append a copy because we are going to be modifying it in other tracks
                res.append(candidate.copy())
                return
            if sum(candidate) > target or i >= len(candidates):
                return
            #try combination of repeating number
            candidate.append(candidates[i])
            helper(i, candidate)
            #try a combination without the previous number but then the next numbers
            candidate.pop()
            helper(i+1, candidate)

        helper(0, [])
        return res


