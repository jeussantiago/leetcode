class LFUCache:
    '''
    2 hashmaps

    minFrequency - keeps track of the minimum frequency in the frequency hashmap

    hashmap_1
        key=key
        val=[value, frequency]

    hashmap_2
        key=frequency
        val=ordered_dict(...keys)  collections.OrderedDict

    PUT

        if key in hashmap_1 (update value)
            - save the old_value, old_frequency

            - update the frequency value of the key
            hashmap_1[key] = [new_value, frequency + 1 (hashmap_1[key][1] + 1)]

            - update the frequency in hashmap_2
            - remove the old value from the old frequency
            hashmap_2[old_frequency][key].pop()
            - insert the new value in the new frequency
            hashmap_2[new_frequency][key] = True

            - check if you need to update the minFrequency
                - check the old frequency to see if there are any values in the dictionary
                if hashmap_2[old_frequency].length == 0
                    - if the length of the old_frequency is 0, that means that the last item was increased in frequency
                    minFrequency += 1

        elif key not in hashmap_2 (add value to hashmap)

            - check if reached capacity
            if hashmap_1.length == capacity:
                - pop that min frequency item
                least_freq_key = hashmap_2[minFrequency][0].pop() # get first position in dictionary
                - remove key from hashmap_1
                hashmap_1[least_freq_key].pop()

            hashmap_1[key] = [value, 1]
            hashmap_2[1][key] = True

            minFrequency = 1

    GET

        - update frequncy in hashmap_1
        hashmap_1[key][1] += 1

        - remove the key from the previous frequency in hashmap_2
        - if the frequency is empty, update the minFrequency
        - add the new frequency to hashmap_2

    Time: O(1)
    Space: O(n)

    '''

    def __init__(self, capacity: int):
        self.minFrequency = 1
        self.capacity = capacity
        self.hashmap_1 = {}
        self.hashmap_2 = collections.defaultdict(collections.OrderedDict)

    def get(self, key: int) -> int:
        if key not in self.hashmap_1:
            return -1

        value, old_frequency = self.hashmap_1[key]
        self.updateKey(key, value, old_frequency)

        return value

    def put(self, key: int, value: int) -> None:
        if key in self.hashmap_1:
            old_frequency = self.hashmap_1[key][1]
            self.updateKey(key, value, old_frequency)

        else:
            # check if reached capacity
            if len(self.hashmap_1) == self.capacity:
                least_freq_key = self.hashmap_2[self.minFrequency].popitem(last=False)[
                    0]  # first item
                self.hashmap_1.pop(least_freq_key)

            # insert new value
            self.hashmap_1[key] = [value, 1]
            self.hashmap_2[1][key] = True

            self.minFrequency = 1

    def updateKey(self, key, value, old_frequency):
        # update the value and frequency in hashmap_2
        self.hashmap_1[key] = [value, old_frequency + 1]

        # remove the key from the old frequency in hashmap_1
        self.hashmap_2[old_frequency].pop(key)
        # insert the key in the new freuency
        self.hashmap_2[old_frequency + 1][key] = True

        # check to see if need to update minFreqeuncy
        if len(self.hashmap_2[self.minFrequency]) == 0:
            self.minFrequency += 1


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
