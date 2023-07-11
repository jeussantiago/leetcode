class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        minVal = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(minVal)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
'''
- the only way you can remove an element, is it if you pop it from the top
- this means that the stack is already ordered
- when you add an item to the stack, keep a record of what is lower => the value adding or the value already present
    - whatever is lower, add that number to the end of the minVal stack

stack:      -2  0 -3
minStack:   -2 -2 -3

- if you pop from the stack, you also pop from the minStack
- the new lowest value is whatever is at the top of the minStack
- this way you keep track of the minimum value at all times

- time complexity for all functions are O(1)
- space: O(n)

'''
