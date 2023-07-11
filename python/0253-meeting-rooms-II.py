class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        '''
        - if something overlaps => need another conference room

        [[7,10],[2,4],[8,9],[3,4]]
        [[2,4],[3,6],[4,6],[6,8],[7,9],[7,10]]

        - seperate the start and ending times
        - when we see an ending time, we know that some meeting has ended
        (we don't know which meeting but we know a meeting has ended)
            - if a meeting has ended, we don't need to use another room

        if the start_time >= end_time:
            #current meeting can use the room, the end_time meeting used

            # go to next ending meeting
            end_time += 1

        elif start_time < end_time:
            # the room is occupied, go to another room
            room += 1

        Time: O(nlog(n)) sorting of the arrays
        Space: O(n)
        '''
        rooms = 0
        start_times = sorted(interval[0] for interval in intervals)
        end_times = sorted(interval[1] for interval in intervals)

        # we need to go through all the meetings but they don't need to all end
        end_idx = 0
        for start_time in start_times:
            end_time = end_times[end_idx]

            if start_time >= end_time:
                end_idx += 1
            else:
                # rooms occupied, go to new room
                rooms += 1

        return rooms
