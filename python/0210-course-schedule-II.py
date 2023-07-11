class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        '''
        [[0,1], [0,2], [1,3], [1,4], [3,4]]

        0 -> 1 -> 3
        |    |    |   
        |    |    v  
        v    L--> 4  
        2

        Adjancency list:
        crs pre
        0   [1,2]
        1   [3,4]
        2   []
        3   [4]
        4   []

        res: [2,4,3,1,0]

        [[0, 1], [3, 4]]
        0 -> 1
        3 -> 4

        Adjancency list:
        crs pre
        0   [1]
        3   [4]

        res: [0,1,3,4]

        - the idea of this is that you go all the way down to the bottom first so that you can add those without worry

        - create an adjancency list

        - go through all the keys in the adjancency list
        (doesn't matter where you start)
            - if the current course is already in the result/visit set, we can skip it then
                - return True
            - if the current course is in a cycle
            (the courses can't be compelted - no reason to keep going)
                - return False

            - go through all the pre-requisites of the current course

            - if the crs has no pre-requisites or you've gone through all the pre-requisites, then
                - add the crs to the results
                - add the crs to a visit set, this will make searching faster since its in a set

            - at each crs, we'll keep track of the current cycle of course so that none repeat



        Time: O(n)
        Space: O(n)
        '''
        prereq = collections.defaultdict(list)
        for crs, pre in prerequisites:
            prereq[crs].append(pre)

        res, resVisitedCourses = [], set()

        def dfs(crs, courseCycle):
            if crs in courseCycle:
                # uncompeltable sequence of courses
                return False

            if crs in resVisitedCourses:
                # crs already in results, so don't need to add again
                return True

            courseCycle.add(crs)
            for pre in prereq[crs]:
                if not dfs(pre, courseCycle):
                    return False
            courseCycle.remove(crs)

            res.append(crs)
            resVisitedCourses.add(crs)
            return True

        for i in range(numCourses):
            if not dfs(i, set()):
                return []

        return res
