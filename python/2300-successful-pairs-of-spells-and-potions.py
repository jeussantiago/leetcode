class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        '''

        Time: O(mlogn + n * mlogn) where m in len of potions and n is len of spells
            : O((m + n)logm) # factor out the logn
        Space: O(n) results list


        '''
        potions.sort()

        def getSuccessfulPair(spell):
            l, r = 0, len(potions)
            while l < r:
                mid = (l + r) // 2
                if spell * potions[mid] >= success:
                    r = mid
                else:
                    l = mid + 1

            return len(potions) - r

        res = []
        for spell in spells:
            res.append(getSuccessfulPair(spell))

        return res
