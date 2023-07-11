class Vector2D:

    def __init__(self, vec: List[List[int]]):
        # Time: O(n * m)
        # Space: O(n)
        self.vector = []
        self.pointer = -1
        for ele in vec:
            self.vector.extend(ele)

    def next(self) -> int:
        # Time: O(1)
        # i guess don't pop ; idk
        self.pointer += 1
        return self.vector[self.pointer]

    def hasNext(self) -> bool:
        return self.pointer + 1 < len(self.vector)


# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(vec)
# param_1 = obj.next()
# param_2 = obj.hasNext()
