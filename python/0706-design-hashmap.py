class MyHashMap:
    '''
    Time: O(1)
    Space: O(n)
        ; space can also be seen as O(1) since you know how big it is
    '''

    def __init__(self):
        self.mapping = [-1] * (10**6 + 1)

    def put(self, key: int, value: int) -> None:
        self.mapping[key] = value

    def get(self, key: int) -> int:
        return self.mapping[key]

    def remove(self, key: int) -> None:
        self.mapping[key] = -1


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
