class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        heap

        - get a count of the numbers
        O(n)

        - add each item to the max heap based on the count
        - pop out the k most common numbers in the heap

        Time: O(nlogk)
        Space: O(n + k) counter dict + heap
        '''

        count = collections.Counter(nums)
        print(count)

        # add all the items to heap
        # we do negative(-) val b/c python only has min heaps, but we want max heaps
        h = []
        for key, val in count.items():
            if len(h) < k:
                heappush(h, (val, key))
            else:
                if val > h[0][0]:
                    # take off the smallest and add the current one
                    heappushpop(h, (val, key))

        return [num for _, num in h][::-1]
