from copy import deepcopy


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        '''
        - position in visited will correspond to the airport for the path
        - the very first one, since the airports are already sorted, is the greatest lexographical itinerary
            - stop the searching after that first one
            - thats why theres an iteninerary for dfs

        - you could sort the each list in the dict after it has been created
            - or you can sort the tickets list initially so that when you put it in the dict, it is already sorted
            - this will save some time

        Time: O(n * (v + e)) n is all the airports from JFK ; then visit every node and vertex afterwards
        Space: O(v + e)
        '''
        # flights need to be in lexicographical order - sort the flights
        tickets = sorted(tickets, key=lambda airport: airport[1])

        # create adjacency list
        flights = collections.defaultdict(list)
        visited = collections.defaultdict(list)
        for airport_from, airport_to in tickets:
            flights[airport_from].append(airport_to)
            visited[airport_from].append(False)

        # find the first complete itinerary
        def dfs(airport, itinerary):
            if len(itinerary) == len(tickets) + 1:
                return itinerary

            for i, destination in enumerate(flights[airport]):
                if not visited[airport][i]:
                    visited[airport][i] = True
                    possible_itinerary = dfs(
                        destination, itinerary + [destination])
                    if possible_itinerary:
                        return possible_itinerary
                    visited[airport][i] = False

            return None

        return dfs("JFK", ["JFK"])
