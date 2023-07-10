class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        '''
        - num can be 0 but if its not 0, then there can't be a leading 0
        (0 good - 011 is bad)
        - value of num is between 0 and 255
        - find all possible valid ip addresses from the s

        - if the len(num) > 1 and num[0] == 0: then bad

        backtracking(index, []):
        index - where we left off in the string
        [] - shows the current ip address creating

        - if len([]) > 4, return False because theres no reason to continue since the string cant create a valid ip address
        - test the last element in the array
            - if not []:
                - check if valid number
                - create function
                    - if len(s) == 1: return True
                    (since length is 1, it doesnt matter what number is the string is)
                    - we can't ignore len 2 and 3
                    - if s[0] == 0: return False
                    - else
                        - turn s into int, if num between 10 - 255
                            return True
                        return false

        Time: O(3^n) decision tree has 3 options at each branch, the height of the tree would be worst case the length of the string
        - but, a valid ip address only has at most 12 characters, so any string over the 12 characters is invalid
        - possibly worst case is O(3^12)
        Space: O()

        '''
        # checks if a strng is a valid string for the ip address
        def isValidString(strng):
            if not strng:
                return False
            # print('isValidString:', strng)
            if len(strng) == 1:
                return True
            elif strng[0] == "0":
                return False
            else:
                num = int(strng)
                return 10 <= num <= 255

        def backtrack(ind, address):
            # test strng
            if address and not isValidString(address[-1]):
                return

            if len(address) == 4 and ind == len(s):
                res.append(".".join(address))
                return

            backtrack(ind+1, address + [s[ind: ind+1]])
            backtrack(ind+2, address + [s[ind: ind+2]])
            backtrack(ind+3, address + [s[ind: ind+3]])

        if len(s) > 12:
            return []

        res = []
        backtrack(0, [])

        return res
