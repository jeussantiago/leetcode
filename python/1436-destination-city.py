class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        '''
        Time: O(n)
        Space: O(n)
        '''
        hasDest = set()
        for city, _ in paths:
            hasDest.add(city)

        for _, city in paths:
            if city not in hasDest:
                return city

        return ""
