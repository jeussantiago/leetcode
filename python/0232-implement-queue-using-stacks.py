class MyQueue:
    '''
    [1,2,3,4]
    [4,3,2,1] <= inverted stack is the queue


    - if the inverted stack is ever empty, we can just fill the inverted stack
    with the contents of the normal stack
    - only time we need to do this, si when we need to return something => pop and peek
    '''

    def __init__(self):
        self.normal_stack = []
        self.inverted_stack = []  # queue

    def push(self, x: int) -> None:
        self.normal_stack.append(x)

    def pop(self) -> int:
        if not self.inverted_stack:
            self.fillInvertedStack()
        return self.inverted_stack.pop()

    def peek(self) -> int:
        if not self.inverted_stack:
            self.fillInvertedStack()
        return self.inverted_stack[-1]

    def empty(self) -> bool:
        return not (self.normal_stack or self.inverted_stack)

    def fillInvertedStack(self) -> None:
        while self.normal_stack:
            self.inverted_stack.append(self.normal_stack.pop())


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
