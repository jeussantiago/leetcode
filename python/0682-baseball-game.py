class Solution:
    def calPoints(self, operations: List[str]) -> int:
        '''
        Time: O(n)
        Space: O(n)
            ; space used for stack
        '''
        self.stack = []

        # add score
        def recordNum(num):
            self.stack.append(num)

        # sum of last 2 scores
        def recordAdd():
            num = self.stack[-1] + self.stack[-2]
            self.stack.append(num)

        # invalidate last score
        def recordCut():
            self.stack.pop()

        # doubles previous score
        def recordDouble():
            self.stack.append(self.stack[-1] * 2)

        for op in operations:
            if op.lstrip('-+').isdigit():
                recordNum(int(op))
            elif op == '+':
                recordAdd()
            elif op == 'D':
                recordDouble()
            else:
                recordCut()

        return sum(self.stack)
