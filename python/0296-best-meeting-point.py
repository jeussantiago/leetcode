class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        '''
        x_homes = [0,0,2] # cols
        y_homes = [0,4,2] # rows

        best meeting point = (y_median, x_median) = (2,0)

        - use manhattan formula to caluclate the distance between the
        houses and the best meeting point

        Time: O(m * n)
        Space: O(m * n)

        - can reduce space complexity if I don't store the x_homes and y_homes
        but instead only store the medians of the two

        '''
        ROWS, COLS = len(grid), len(grid[0])
        x_homes, y_homes = [], []
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    y_homes.append(i)
                    x_homes.append(j)

        x_median = statistics.median(x_homes)
        y_median = statistics.median(y_homes)
        # (y_median, x_median) is the mid point => best meeting point => shortest distance from everyone

        # calculate the distance between the starting house and the midpoint
        totalDist = 0
        for i, j in zip(y_homes, x_homes):
            if grid[i][j] == 1:
                # get the distance from the midpoint from each house
                totalDist += abs(i - y_median) + abs(j - x_median)

        return int(totalDist)

        '''
        BFS (Queue) - time limit exceeding
        => algorithm that searches in a circle around target

        - get positions of friends houses

        - each friend needs a hashmap for path traveled where key=position val=number of steps it takes to get there
            - serach vertical and horizont ;; don't search diagonal since it is manhattan distance
        - when all of the friends have a common position, thats when we stop

        - the distances might different for each house, so we need to calculate the 

        - each house has its own queue

        Time: O(n * m + 4^logn)
        Space: O()
        '''
        ROWS, COLS = len(grid), len(grid[0])
        next_path = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def validPos(row, col, starting_house):
            if (
                0 <= row < ROWS and
                0 <= col < COLS and
                (row, col) not in visited_path[starting_house]
            ):
                return True
            else:
                return False

        def checkMeetingPoint():
            for pos in visited_path[0]:
                union = True
                for starting_house in range(1, len(visited_path)):
                    if pos not in visited_path[starting_house]:
                        union = False
                        break

                if union:
                    return pos
            return None

        def calculateDistFromMeetingPoint(meeting_point):
            return sum(house_path[meeting_point] for house_path in visited_path)

        houses = []
        friend_count = 0
        for i, row in enumerate(grid):
            for j, num in enumerate(row):
                if num == 1:
                    houses.append((i, j, friend_count))
                    friend_count += 1

        visited_path = [{(house[0], house[1]): 0} for house in houses]
        q = collections.deque(houses)

        meeting_point = None
        steps = 1
        while q:
            for _ in range(len(q)):
                pos = q.pop()
                for row, col in next_path:
                    next_row = pos[0] + row
                    next_col = pos[1] + col
                    starting_house = pos[2]
                    if validPos(next_row, next_col, starting_house):
                        q.appendleft((next_row, next_col, starting_house))
                        visited_path[starting_house][(
                            next_row, next_col)] = steps
            steps += 1

            # check for common meeting point
            meeting_point = checkMeetingPoint()
            if meeting_point:
                break

        return calculateDistFromMeetingPoint(meeting_point)
