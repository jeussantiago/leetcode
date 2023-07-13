class ListNode():
    def __init__(self, val, nextNode=None):
        self.val = val
        self.next = nextNode


class MyCircularQueue:
    '''
    singly linked list

    []
    [3,2,1]

    '''

    def __init__(self, k: int):
        self.head = None
        self.tail = None
        self.size = 0
        self.cap = k

    def enQueue(self, value: int) -> bool:
        if self.size == self.cap:
            return False
        elif self.size == 0:
            self.head = ListNode(value)
            self.tail = self.head
        else:
            self.tail.next = ListNode(value)
            self.tail = self.tail.next

        self.size += 1
        return True

    def deQueue(self) -> bool:
        if self.size == 0:
            return False
        elif self.size == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next

        self.size -= 1
        return True

    def Front(self) -> int:
        if self.size == 0:
            return -1
        return self.head.val

    def Rear(self) -> int:
        if self.size == 0:
            return -1
        return self.tail.val

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.cap


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
