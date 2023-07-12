class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        '''
        letters = ["x","x","y","y","y","z"], target = "x"

        - if the target is < than the current char, then the current character is part of the solution set
        if target < curr
            r = mid
        if target >= curr
            l = mid + 1

        Time: O(logn)
        Space: O(n)
        '''
        l, r = 0, len(letters)
        while l < r:
            mid = (l + r)//2
            if target < letters[mid]:
                r = mid
            else:
                l = mid + 1

        if l == len(letters):
            return letters[0]
        return letters[l]
