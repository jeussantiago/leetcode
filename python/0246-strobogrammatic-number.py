class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        '''
        - 2 pointers on the end
        - matching numbers are ok
        - if one number is 6, the other number is 9
        Time: O(n)
        Space: O(1)
        '''
        stroboNums = set(['0', '1', '8'])
        reversableStroboNums = {
            '6': '9',
            '9': '6'
        }
        l, r = 0, len(num) - 1
        while l <= r:
            if (num[l] == num[r]):
                if num[l] in stroboNums:
                    l += 1
                    r -= 1
                else:
                    return False
            elif num[l] in reversableStroboNums:
                if reversableStroboNums[num[l]] == num[r]:
                    l += 1
                    r -= 1
                else:
                    return False
            else:
                return False

        return True
