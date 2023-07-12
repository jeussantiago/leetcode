class AllOne:
    '''
    - do what the question ask
    - store the max and min key when asked
        - if there is some sort of increment of decrement, then we need to re-determine what the max and min values are
    '''

    def __init__(self):
        '''
        Time: O(1)
        '''
        self.cache = {}
        self.maxString = None
        self.minString = None

    def inc(self, key: str) -> None:
        '''
        Time: O(1)
        '''
        self.maxString, self.minString = None, None

        self.cache[key] = self.cache.get(key, 0) + 1
        # print(self.cache)

    def dec(self, key: str) -> None:
        '''
        Time: O(1)
        '''
        self.maxString, self.minString = None, None

        if self.cache[key] == 1:
            del self.cache[key]
        else:
            self.cache[key] -= 1

        # print(self.cache)

    def getMaxKey(self) -> str:
        '''
        Time: O(n)
        '''
        if not self.cache:
            return ""

        if not self.maxString:
            self.maxString, _ = max(self.cache.items(), key=lambda x: x[1])

        return self.maxString

    def getMinKey(self) -> str:
        '''
        Time: O(n)
        '''
        if not self.cache:
            return ""

        if not self.minString:
            self.minString, _ = min(self.cache.items(), key=lambda x: x[1])

        return self.minString


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()
