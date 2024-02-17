class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        '''
        minHeap

        Time: O(nlogn)
        Space: O(n)
        '''
        N = len(heights)
        ladders_used_minHeap = []
        for i in range(N - 1):
            climb_difference = heights[i + 1] - heights[i]

            if climb_difference <= 0:
                # jump down to next building, don't use any materials
                continue

            # we definitely want to be using a ladder any chance we get
            heappush(ladders_used_minHeap, climb_difference)

            if len(ladders_used_minHeap) <= ladders:
                # not all the ladders are used, go next building
                continue

            # at this point, excess amount of ladders used,
            # remove ladder that covers the least amount of height
            # and replace with bricks
            bricks -= heappop(ladders_used_minHeap)

            # if there are not enough bricks, this is the furthest we can go
            if bricks < 0:
                return i

        # by this point, the person is on the last platform
        return N - 1
