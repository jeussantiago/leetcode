class Solution:
    def frequencySort(self, s: str) -> str:
        '''
        Bucket Sort
        Time: O(n)
            ; it looks like (n^2) when creating the string, but n is the size of the original string
            ; the contents of the buckets can only go to max the number of characters of the string
            ; so even though we eiterate over every character in each bucket, it is still only looking
            ; at each char once (n)
        Space: O(n)
        '''
        counts = Counter(s)
        max_appearance = max(counts.values())

        # create "buckets" to put the chars into
        buckets = [[] for _ in range(max_appearance + 1)]

        # place each character into the buckets
        for c, cnt in counts.items():
            buckets[cnt].append(c)

        # build the string
        res = ''
        for i in range(max_appearance, -1, -1):
            for c in buckets[i]:
                res += (c * i)

        return res


class Solution:
    def frequencySort(self, s: str) -> str:
        '''
        Time: O(nlogn)
            - Counter.most_common is the same thing as sorting, its just built in so its easier to use
        Space: O(n)
        '''
        count = Counter(s)
        res = ''
        for c, cnt in count.most_common():
            res += (c * cnt)

        return res
