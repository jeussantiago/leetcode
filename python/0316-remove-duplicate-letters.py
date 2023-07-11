class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        '''
        - find the last iterations of the each character
            - this will tell you if it is ok to remove an existing character 
            b/c its not in lexicographical order since its not the last time it will appear
        s = "cbacdcbc"
        last index for char to appear = {
            c: 7
            b: 6
            a: 2
            d: 4
        }

        - add the character if it is lexicographical order
            - this means that if a duplicate character appears, we DONT ADD it

        if char not in results
            - when we decide to add a character, we need to make sure that the other chars in results are in lexicographical order
            - compare the char adding if it comes first in the alphabet before the character at the end of the results
            adding "a" ; results = ["b"]
            - "a" < "b"
            (keep doing this process until the statement is not true anymore or there is an empty list)
                - "b" is not in order
                - ask again if "b" is the last time it appears in the string
                - if it isn't: remove "b"
                - if it is: don't touch b

            adding "c" ; results = ["b"]
            - "c" > "b"
                - just add to the results

        Time: O(2n + n) we go through the chars in the string 1 time. but at most we go back to look over it again a second time + ternarary
            : O(n)
        Space: O(n)
        '''

        char_last_appear_ind = {c: i for i, c in enumerate(s)}

        res_set = set()
        res = []
        for i, char in enumerate(s):
            if char not in res_set:
                # make sure that the last char appears again later in the list
                # make sure that current char in lexicographically comes before the last char in results
                while res and i < char_last_appear_ind[res[-1]] and char < res[-1]:
                    last_c = res.pop()
                    res_set.remove(last_c)

                res.append(char)
                res_set.add(char)
        return "".join(res)
