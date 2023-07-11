class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        '''
        version1 = "1.0", version2 = "1.0.0.0"

        - split between "."
        - go through each split
        - some versions are longer than others like above
            - if they are shorter than the other version, just fill it with 0s
        - so when you go through each split, you can just compare the number values
        - if int in v1 > v2: return 1
        - elif int in v1 < v2: return -1

        - out of loop, at the end: return 0

        Time: O(n)
        Space: O(n)
        '''
        v1 = version1.split(".")
        v2 = version2.split(".")
        N, M = len(v1), len(v2)

        for i in range(max(N, M)):
            n1 = 0 if i >= N else int(v1[i])
            n2 = 0 if i >= M else int(v2[i])

            if n1 > n2:
                return 1
            elif n1 < n2:
                return -1

        return 0
