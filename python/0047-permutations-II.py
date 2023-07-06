class Solution:
    def __init__(self):
        self.res = []

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        '''
        elimenate duplicates by tarnsforming nums into a Count hashmap
        [1,1,2]
        [num, counter]
        [1,   2      ]
        [2,   1      ]
        --------------
        1 - (used one counter for 1)
        1,1 - (used one counter for 1)
        1,1,2 - (used one counter for 2)
        new iteration
        1,2 - (used one counter for 2)
        1,2,1 - (used one counter for 1)
        since we're trying ot find permutaions with a hash map counter, then 
        we can only use up a number if its available

        python trick => path.copy() == path[:] (just faster)
        '''
        # self.backtrack(nums, [], 11)
        # return self.res
        count = collections.Counter(nums)
        self.dfsBacktrack(count, [])
        return self.res

    def dfsBacktrack(self, count, path):
        if sum(count.values()) <= 0:
            self.res.append(path[:])
            return
        
        for num in count.keys():
            if count[num] > 0:
                count[num] -= 1
                path.append(num)
                self.dfsBacktrack(count, path[:])
                path.pop()
                count[num] += 1



    