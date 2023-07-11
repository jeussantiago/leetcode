class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        '''
        ["ab","ba"]
        expected: [["ba"],["ab"]]

        - use the shifting pattern to be able to tell what strings are in the same group
        (1,1 means that the first character shifted 1 letter to be second character and second shifted 1
        to become third chracter => "abc")

        ["abc","bcd","acef"]
        {
            (1,1): [abc, bcd]
            (2,2,1): [acef]
        }

        Time: O(n * m * 26) where n is the len of the arr and m is the length of the strings
            : O(n * m)
        Space: O(n) hashmap
        '''

        # returns the amount of shift to get from c1 to c2
        def getShift(c1, c2):
            c1, c2 = ord(c1), ord(c2)
            if c1 < c2:
                return c2 - c1
            elif c1 > c2:
                return 26 - (c1 - c2)
            else:
                return 26

        # returns the shifted group pattern in a list

        def getGroup(s):
            if len(s) == 1:
                return tuple([0])
            group = []
            for i in range(len(s)-1):
                group.append(getShift(s[i], s[i+1]))
            return tuple(group)

        groups = collections.defaultdict(list)
        for s in strings:
            group = getGroup(s)
            groups[group].append(s)

        return list(groups.values())
