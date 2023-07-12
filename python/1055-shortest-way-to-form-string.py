class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        '''
        - create a set of existing characters in source
        - if a char in target doesn't exist in the source set, then return -1

        - iterator on target
        - pointer on source
        - figure out how many times we loop through source
        - might be something like 
            - if at end of source, loop to the beginning of source


        if source char != target char
            if source_idx == len(source) -1
                - reset source to the begining
                source_idx = 0
                - increase the concatenation count
                res += 1
            source_idx += 1


        Time: O(n * m) where n is the len of target where m is the len of the source
        Space: O(1)
        '''
        existing_char = set(source)

        res = 0
        source_idx, target_idx = 0, 0
        while target_idx < len(target):
            if target[target_idx] not in existing_char:
                return -1

            if source[source_idx] == target[target_idx]:
                target_idx += 1

            if source_idx == len(source) - 1 or target_idx == len(target):
                source_idx = 0
                res += 1
            else:
                source_idx += 1

        return res
