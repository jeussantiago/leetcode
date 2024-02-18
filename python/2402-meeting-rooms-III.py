class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        '''
        minheap

        m is the length of meetings array
        n is the number of rooms available
        Time: O(mlogn)
            ; (m) iterate through meetings array 
            ; (n) add meeting to minHeap
            ; (n) remove meeting from minHeap
            ; (m) find the lowest valued room with the max number times used
            ; (m*(logn + logn) + m) => mlogn + m => mlogn
        Space: O(n)
            ; (n) minheap available rooms
            ; (n) minheap occupied rooms
        '''

        meetings.sort()
        # minHeap (room_number, last_used_time, number_of_times_room_used)
        available_rooms = [(room_num, 0, 0) for room_num in range(n)]
        # minHeap (end_time_of_meeting, room_number, number_of_times_room_used)
        occupied_rooms = []

        for meeting_start, meeting_end in meetings:
            # remove all the currently used rooms that have already finished
            # before the starting time of the current meeting
            # OR if all the rooms are occupied, we need to remove one
            # (this second condition assures theres always a room available)
            while occupied_rooms and (occupied_rooms[0][0] <= meeting_start or len(occupied_rooms) == n):
                end_time_of_meeting, room_number, number_of_times_room_used = heappop(
                    occupied_rooms)
                heappush(available_rooms, (room_number,
                         end_time_of_meeting, number_of_times_room_used))

            room_number, last_used_time, number_of_times_room_used = heappop(
                available_rooms)
            # meeting starts after the when theres a room available
            # if the room last used at T=0 and meeting_start_T=1, then the meeting can only start at T=1
            # if the room last used at T=2 and meeting_start_T=1, then the meeting can only start at T=2
            room_start_time = max(last_used_time, meeting_start)
            meeting_length = meeting_end - meeting_start
            room_end_time = room_start_time + meeting_length

            heappush(occupied_rooms, (room_end_time,
                     room_number, number_of_times_room_used + 1))

        # empty meeting rooms
        while occupied_rooms:
            end_time_of_meeting, room_number, number_of_times_room_used = heappop(
                occupied_rooms)
            heappush(available_rooms, (room_number,
                     end_time_of_meeting, number_of_times_room_used))

        # get the max number of times a room is used
        res, _, max_num_times_room_used = max(
            available_rooms, key=lambda x: x[2])
        # get the lowest valued room with number_of_times_used == max
        for room, _, room_used_cnt in available_rooms:
            if room_used_cnt == max_num_times_room_used:
                res = min(res, room)

        return res
