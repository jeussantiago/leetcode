class Solution:
    def countAndSay(self, n: int) -> str:
        '''
        - count + previous number
        - go through the string n times
            - each pass, if the number hasn't changed, increase a counter
            - once number has changed, append the 'count' and the 'number' to the end of the string
            - reset counter
        Time: exponential since the string increase by about 2x in length each iteration
        '''

        def countSay(say):
            output = ''
            for num, grp in itertools.groupby(say):
                output += str(len(list(grp))) + num
            return output

        res = '1'
        for _ in range(n-1):
            res = countSay(res)
        return res


class Solution:
    def countAndSay(self, n: int) -> str:

        def countSay(say):
            output = ''
            count = 1
            i = 1
            while i <= len(say):
                if i >= len(say) or say[i-1] != say[i]:
                    output = output + str(count) + say[i-1]
                    count = 0
                count += 1
                i += 1
            return output

        res = '1'
        for _ in range(n-1):
            res = countSay(res)

        return res






