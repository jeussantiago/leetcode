class Solution:
    def decodeString(self, s: str) -> str:
        '''
        Stack:

        cdcdcd
        Time: O(n)
        Space: O(n)
        '''
        stack = []
        i = 0
        sub, num = "", 0
        for c in s:
            if c.isdigit():
                num = (num * 10) + int(c)

            elif c == '[':
                stack.append(num)
                stack.append(sub)
                sub, num = "", 0

            elif c == ']':
                last_sub = stack.pop()
                last_num = stack.pop()
                sub = last_sub + (last_num * sub)

            else:
                sub += c

        return sub


class Solution:
    def decodeString(self, s: str) -> str:
        '''
        - if there is a number, it is guranteed that a bracket will be after the number
            - 10[a]
        Time: O(n)
        Space: O(n)
        '''
        N = len(s)
        self.i = 0

        def decode():
            output = ""
            sub = ""
            while self.i < N:
                if s[self.i].isdigit():
                    num = 0
                    while s[self.i].isdigit():
                        num = (num * 10) + int(s[self.i])
                        self.i += 1
                    # guranteed to be on the open bracket
                    self.i += 1
                    output += (sub + (num * decode()))
                    sub = ""
                elif s[self.i] == ']':
                    self.i += 1
                    break
                else:
                    sub += s[self.i]
                    self.i += 1

            output += sub
            return output

        return decode()
