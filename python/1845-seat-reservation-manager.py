class SeatManager:
    '''
    ptr_seat = 2
    minHeap_seats_unreserved = [

    ]

    - if theres anything in the minHeap, pop from the minHeap
    (if theres something in the minHeap, its definitely going to be < than the ptr_seat)


    reserve:
        - reserve something only if theres no lower seat number
        (minHeap being empty)
        - but if minHeap has something, this means that a lower seat is available
            - pop that out of the minHeap and return that result

        Time: O(logn)
            ; pop item out of minHeap
        Space: O(n)

    unreserve:
        - add number to minHeap

        Time: O(logn)
        Space: O(n)
            ; minHeap

    Overall:
    n is the number of seats available
    Time: O(logn)
    Space: O(n)
    '''

    def __init__(self, n: int):
        self.ptr = 1
        self.minHeap = []

    def reserve(self) -> int:
        if self.minHeap:
            return heappop(self.minHeap)
        else:
            self.ptr += 1
            return self.ptr - 1

    def unreserve(self, seatNumber: int) -> None:
        heappush(self.minHeap, seatNumber)


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)
