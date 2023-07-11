class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        '''
        - some buildings might be surrounded by other buildings or obstacles,
        - in this case, there is no possible way for that building to reach the other paths and the other builds can't reach the insidepath
        [
            1,1
            0,1
        ]
        or
        [
            0,0,0,0,0,0
            0,1,1,1,1,0
            0,1,1,0,1,0
            0,1,1,1,1,0
            0,0,0,0,0,0
        ]
        (the inside 0 cant reach outside and the corner 1's can't reach inside 
        - NO INTERSECTING EMPTY LAND)

        Time: O((m * n)^2) where m is the row lenght and n is the col length => for each building position, go through the entire grid to 
                            find the distances of the other positions
        Space: O(m * n)
        '''
        ROWS, COLS = len(grid), len(grid[0])
        neighbor = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        # the distance between all the houses and all the positions
        dist = [[0] * COLS for row in range(ROWS)]

        def isValidPos(row, col, empty_land):
            if (
                0 <= row < ROWS and
                0 <= col < COLS and
                grid[row][col] == empty_land
            ):
                return True
            return False

        # decrease the original matrix by -1 if visited
        # increase the dist matrix by how many steps it takes to visit
        def traversePaths(building, empty_land):
            local_dist = float('inf')
            empty_land = -(empty_land)
            q = collections.deque([building])
            steps = 1
            while q:
                for _ in range(len(q)):
                    row, col = q.pop()
                    for n_row, n_col in neighbor:
                        next_row, next_col = n_row + row, n_col + col
                        if isValidPos(next_row, next_col, empty_land):
                            grid[next_row][next_col] -= 1
                            q.appendleft((next_row, next_col))
                            dist[next_row][next_col] += steps
                            local_dist = min(
                                local_dist, dist[next_row][next_col])

                steps += 1
            return local_dist

        min_distance_from_all_buildings = float('inf')
        building_cnt = 0
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1:
                    # some build
                    local_min_dist = traversePaths((row, col), building_cnt)
                    min_distance_from_all_buildings = local_min_dist
                    building_cnt += 1

        if min_distance_from_all_buildings == float('inf'):
            return -1
        return min_distance_from_all_buildings


class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        '''

        '''

        ROWS, COLS = len(grid), len(grid[0])
        # get the building positions
        building_pos = []
        visited_land = []
        building_cnt = 0
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1:
                    building_pos.append((row, col, building_cnt))
                    building_cnt += 1
                    visited_land.append({})

        # find the first position where all the buildings intersect

        def isValidPos(row, col, building):
            if (
                0 <= row < ROWS and
                0 <= col < COLS and
                grid[row][col] <= 0 and
                (row, col) not in visited_land[building]
            ):
                return True
            return False

        def checkMeetingPoint():
            itersecting_lands = []
            for land in visited_land[0].keys():
                isLandItersect = True
                for i in range(1, len(visited_land)):
                    if land not in visited_land[i]:
                        isLandItersect = False
                        break

                if isLandItersect:
                    itersecting_lands.append(land)

            return itersecting_lands

        def calculateManhattanDistBetweenBuildings(itersecting_lands):
            min_toal_manhattan_distance = float('inf')
            for intersecting_pos in itersecting_lands:
                total_manhattan_distance = 0
                for building in visited_land:
                    total_manhattan_distance += building[intersecting_pos]
                print(total_manhattan_distance)
                min_toal_manhattan_distance = min(
                    min_toal_manhattan_distance, total_manhattan_distance)

            return min_toal_manhattan_distance

        neighbor = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        q = collections.deque(building_pos)
        # print(q)
        steps = 1
        while q:
            for _ in range(len(q)):
                row, col, building = q.pop()
                for next_row, next_col in neighbor:
                    if isValidPos(row + next_row, col + next_col, building):
                        q.appendleft(
                            (row + next_row, col + next_col, building))
                        visited_land[building][(
                            row + next_row, col + next_col)] = steps

            itersecting_lands = checkMeetingPoint()
            if itersecting_lands:
                # print(visited_land)
                print('intersect_point:', itersecting_lands)
                # calculate total manhattan distace
                return calculateManhattanDistBetweenBuildings(itersecting_lands)

            steps += 1

        return -1
