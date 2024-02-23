class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        '''
        min heap
        - grab the next flight with the lowest cost, 
        - then find the neighbors of that
        - if the total stops exceed, then don't continue with that route

        e is the number of flights
        n is the number of cities
        Time: O((n + e) * k)
        Space: O(n)
            ; (n) adj list
        '''

        adj = collections.defaultdict(list)
        for start_city, end_city, cost in flights:
            adj[start_city].append((end_city, cost))

        # (curr_city, price to get to this city from src, number of stops available)
        minHeap = [(0, src, k + 1)]
        # the minimum number of visits to each city
        visited = collections.defaultdict(int)

        while minHeap:

            curr_cost, curr_city, num_stops_remaining = heapq.heappop(minHeap)

            if curr_city == dst:
                # since we get the city from the min heap, the first time
                # we arrive at the city is the lowest cost to get to that city
                return curr_cost

            if num_stops_remaining == 0:
                continue

            # We want to keep the number of visits at a node to its minimum
            # if a city has been visited with more stops than previous city visits,
            # then we can skip this city since its not an improvement
            if num_stops_remaining < visited[curr_city]:
                continue
            # update the city to the new minimum numeber of visits
            visited[curr_city] = num_stops_remaining

            # add neighboring cities
            for end in adj[curr_city]:
                end_city, flight_cost = end
                heappush(minHeap, (curr_cost + flight_cost,
                         end_city, num_stops_remaining - 1))

        return -1
