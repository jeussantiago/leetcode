class Solution:
    def minJumps(self, arr: List[int]) -> int:
        '''
        [100,-23,-23,404,100,23,23,23,3,404]

        {
            100: [0, 4] X
            -23: [1, 2] X
            404: [3, 9]
            23: [5, 6]
            3: [8]
        }

        queue = [0]
        visited = [0]
        - pop 0
        - can go forward 1, back 1, or jump
        - add mapping for 100 to queue and visited
        - delete it from hashmap to avoid double calculating
        q = [1, 4]
        visited = [0, 1, 4]
        - pop 1
        - can go forward, backwards, or jump
        - dont add stuff thats already visited
        - delete mapping
        q = [4, 2]
        visited = [0, 1, 4, 2]
        - 100 already deleted so dont need to do anything
        q = [2,5,3]
        v = [0,1,4,2,5,3] 
        - pop 2, already visited all otyher possibel indexes ; nothign changes
        q = [3, 6, 7]
        v = [0,1,4,2,5,3,6,7]

        Time: O(n)
        Space: O(n)
        '''

        N = len(arr)
        q = collections.deque([0])
        visited = set([0])
        locations = collections.defaultdict(list)

        for i, num in enumerate(arr):
            locations[num].append(i)

        minJumps = 0
        while q:
            for _ in range(len(q)):
                idx = q.popleft()

                if idx == N-1:
                    return minJumps

                visited.add(idx)

                forw = idx + 1
                prev = idx - 1
                same_val = locations[arr[idx]]

                # jump forward
                if forw not in visited:
                    q.append(forw)
                    visited.add(forw)
                # jump backwards
                if prev not in visited and prev >= 0:
                    q.append(prev)
                    visited.add(prev)

                # teleport
                if same_val:
                    for i in same_val:
                        if i not in visited:
                            q.append(i)
                            visited.add(i)

                    del locations[arr[idx]]

            minJumps += 1

        return minJumps
