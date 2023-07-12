class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        '''
        Greedy

        - sort the children from the biggest appetite to smallest
        - sort the cookies by size

        g = [1,4,6], s = [1,2,3]

        - pointer on cookies
        - if we can't satisfy the current kid (kid_appetite >= cookie)
            - go to the next kid
            - dont move cookie pointer
        else (kid will be satisfied with the current cookie)
            - move to next kid
            - move to next cookie
            - increase res += 1 (amount of satisfied kids)

        n is the size of kids
        m is the size of cookies
        Time: O(max(nlogn, mlogm))
            ; sorting
        Space: O(max(n, m))
            ; python sorting
        '''

        kids = sorted(g, reverse=True)
        cookies = sorted(s, reverse=True)
        i = 0

        res = 0
        for apetite in kids:
            if i == len(cookies):
                break

            if cookies[i] >= apetite:
                i += 1
                res += 1

        return res
