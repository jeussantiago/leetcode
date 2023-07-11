class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
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

        - go through adjancecy list
            - get to the very bottom of the pre requisite (notified by empty list)
            - if we hit an empty list, return
            - once returned, remove the prerequisite from the list

        cycle in loop, unable to complete
        [[0,1], [1,2], [2,0]]

        0   [1]
        1   [2]
        2   [0]

        - we can have a visit set
        (
            - visit 0, sees that it has 1 has a pre
                - add 0 to visit set
                - pass set into dfs for 1
            - visit 1, pre is 2
                - add 1 to visit set
                - pass set into dfs for 2
            - visit 2
                - sees 0 as a pre
                - 0 is in the visit set
                    - return False
        )


        Time: O(n + p) where n (nodes) is the number of paths allowed taken and p is the number of pre-requisites
        - its not more than that b/c we remove the courses we know that have a pre requisite that can be compelted
        - so we visit each node once
        Space: O(p)
        '''
        # numCourses = 5
        # prerequisites = [[1,4],[2,4],[3,1],[3,2]]
        # expect: true

        preMap = collections.defaultdict(list)
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        visitCourse = set()

        def dfs(crs):
            if crs in visitCourse:
                return False
            if preMap[crs] == []:
                return True

            visitCourse.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            visitCourse.remove(crs)
            # we know we can take all the pre-requisites without returning False
            # in case a different course visits this same course in the future, set it to
            # an empty list signifiying that you don't need to check again
            preMap[crs] = []
            return True

        # we go through every course because the graph might not be connenct
        # 1 -> 2    3 -> 4
        for crs, pre in prerequisites:
            if not dfs(crs):
                return False
        return True
