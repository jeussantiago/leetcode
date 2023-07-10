class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        '''
        [1,2,2]

        []
        [], [1]
        [], [1], [2], [1,2]
        [], [1], [2], [1,2], [2], [1,2], [2,2], [1,2,2]
        - but these have duplicates
        - cant have set since they are not hashable
        - list arent hashtable either so cant put in sets
        - but if we turn the list into tuples then it can go into sets
        (1,2) != (2,1)
        - we can sort the list then

        Time: O(nlogn + 2^n + n + n) nlogn for sort; 2^n get all combinations; go through list created
            : O(2^n)
        Space: O()

        '''
        # sort b/c order matters in sets
        nums.sort()
        res = [[]]

        # get all the combinatioins of the nums
        for num in nums:
            res += [r + [num] for r in res]
            # tmp = []
            # for r in res:
            #     tmp.append(r + [num])
            # res.extend(tmp)

        # turn each list in the res into a tuple so that we can put it in a set to remove duplicates
        res_set = set([tuple(r) for r in res])

        # duplicates have been remove, so turn each tuple to a list
        ans = [list(res) for res in res_set]
        return ans
