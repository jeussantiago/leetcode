class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = collections.OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)
        # update key
        self.cache[key] = value

        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
'''
** can used ordered dictionary
(dictionary to keeps track of order, can move keys to front or back)

Get:
- if the key doesn't exist in the dict, return -1
- if the key exist
    - move the key to the end of the ordered dict
    - return value of key

Put:
- if key not in dictionary
    - add (key, value) to end of ordered dictionary
- if the key already exist
    - move it to the end of the list
    - update the item
- if the length of the ordered dictionary > than capacity
    - remove the first item in dictionary (least recently used)

[1,2,3]
get(1)
- 2 becomes the new leasts recently used
[2,3,1]
put(4)
- add to end of list (most recently used)
[2,3,1,4]

Time: O(1)
Space: O(n)

["LRUCache","put","put","put","put","get","get"]
[[2],[2,1],[1,1],[2,3],[4,1],[1],[2]]
output: [null,null,null,null,null,1,-1]
expected: [null,null,null,null,null,-1,3]

["LRUCache","put","put","get","put","get","put","get","get","get"]
[[2],[1,0],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]
output: [null,null,null,-1,null,2,null,-1,-1,4]
expected: [null,null,null,0,null,-1,null,-1,3,4]

'''
