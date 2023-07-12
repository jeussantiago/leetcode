class Solution:
    def minInsertions(self, s: str) -> int:
        '''
        Recursion top down
        (2 pointers)

        - if the l_char == r_char
            - this index should be a palindrome
            - we can iterate next positions for both left and right pointers
            l += 1
            r -= 1

        else:
        (l_char != r_char)
            - we don't necessarily know if we need to add only the l_char, the r_char, or both
            - so we can add one or the other
            - add only the l_char to the right side OR add only the r_char to the left side
            (increasing the steps count +1)

            - we can do both left and right paths, whichever path has the minimum amount of insertions, we'll just take that

        "mbadm"
        m == m: go next pos
        b != d:
            - go to a path where we added 'b' to the right side
            (going to next position on right side ; adding +1 for steps ; keep left index same => 
            r -= 1)

                => l=1 ; r=2
            - go to a path where we added 'd' to the left side
            (going to next position on left side ; adding +1 for steps ; keep right index same => 
            l += 1)
                => l=2 ; r=3


        "leetcode"
        l=0 ; r=7
        l != e: explore both paths + 1
            - adding l to the right side => l=1 ; r=7
                - e == e => l=2 ; r=6
                - e != d +1
                    - adding e to the right => l=3 ; r=6
                        - t != d +1
                            - adding t to the right => l=4 ; r=6
                                - c != d +1
                                    - adding c to the right => l=5 ; r=6
                                        - o != d +1
                                            - adding o to the right => l=6 ; r=6
                                                d == d
                                                - now l > r: return the count 0
                                            - adding d to the left => l=5 ; r=5
                                                d == d
                                                - now l > r: return the count 0
                                    - adding d to the left => l=4 ; r=5
                                        - c != o
                                            - adding c to the right => l=5 ; r=5
                                                o == o
                                                - now l > r: return the count 0
                                            - adding o to the left => l=4 ; r=4
                                                c == c
                                                - now l > r: return the count 0
                            - adding d to the left => l=3 ; r=5
                            ....
                    - adding d to the left => l=2 ; r=5
                    ....               
            - adding e to the left side => l=0 ; r=6
            ....

        we are going to visit the same left and right indexes many times
            - to optimize, we will have a cache that will keep have key=(l,r) value=min_steps

        - the time depends on the number of possible values within the cache
        - the only values we'll have in the cache are the combinations of left and right indexes while left < right
        - for example, if the length of the word was 4, th eonly possible options in the cahce are:
         [(0,0),(0,1),(0,2),(0,3)]
         [(1,1),(1,2),(1,3)]
         [(2,2), (2,3)]
         [(3,3)]
        - this means the most possible amount of combinations is left * right. left and right are both N since they can iterate over the entire 
        string length
        Time: O(n^2)
        Space: O(n^2) ; has the same explanation as time complexity
        '''
        cache = {}

        def dfs(l, r):
            if l > r:
                return 0

            if (l, r) in cache:
                return cache[(l, r)]

            if s[l] == s[r]:
                cache[(l, r)] = dfs(l + 1, r - 1)
            else:
                cache[(l, r)] = 1 + min(dfs(l + 1, r), dfs(l, r - 1))

            return cache[(l, r)]

        return dfs(0, len(s)-1)
