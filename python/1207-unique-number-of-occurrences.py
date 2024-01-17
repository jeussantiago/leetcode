class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        '''
        2 pass

        n is the length of array
        k is the number of unique numbers
        Time: O(n + k)
        Space: O(n + k)
        '''
        cnt = collections.Counter(arr)
        appearred = set()
        for occurance in cnt.values():
            if occurance in appearred:
                return False

            appearred.add(occurance)

        return True
