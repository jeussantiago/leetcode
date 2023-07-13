class ListNode:
    def __init__(self, val=None):
        self.val = val
        self.next = None


class MyLinkedList:
    '''
    Time: O(n)
        ; adding to the front is O(1)
        ; everything else would be O(n) since you have
        to go through the entire linked list
    Space: O(n)
    '''

    def __init__(self):
        self.head = ListNode(0)
        self.size = 0

    def get(self, index: int) -> int:
        if index >= self.size:
            return -1

        curr = self.head
        for _ in range(index + 1):
            curr = curr.next

        return curr.val

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return

        self.size += 1
        # go to the node just before index
        curr = self.head
        for _ in range(index):
            curr = curr.next

        temp = ListNode(val)
        temp.next = curr.next
        curr.next = temp

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.size:
            return

        self.size -= 1
        curr = self.head
        for _ in range(index):
            curr = curr.next

        curr.next = curr.next.next


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
