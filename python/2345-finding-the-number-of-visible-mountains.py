class Solution:
    def visibleMountains(self, peaks: List[List[int]]) -> int:
        '''
        - although we care about the peaks, to see a peak, it is the same as being able to see the bottom corners
        - adjust the peaks array to the values of the left and right positions of the bottom corners
        - sort by increasing left corner, decreasing right corner
            (furthest left, furthest right)

        - by doing this,
            - the values that come first will be the biggest overshadowing peaks
            - we can just compare the positions of the right corners
                - if next right position is > than current
                    - increase peak count
                    - update highest right position

                - there are overlapping mountains
                    - keep a counter of the peaks,
                    - if count of the peak is more than 1, then don't consider it

        Time: O(n)
        Space: O(n)
        '''
        corners = [(x - y, x + y) for x, y in peaks]
        peakCount = Counter(corners)
        corners.sort(key=lambda x: (x[0], -x[1]))

        res = 0
        furthest_right = -inf
        for l, r in corners:
            if r <= furthest_right:
                continue

            furthest_right = r
            if peakCount[(l, r)] == 1:
                res += 1

        return res


class Solution:
    def visibleMountains(self, peaks: List[List[int]]) -> int:
        '''
        - sort: increasing x, decreasing y
        - sort: pos_x_left, decreasing y

        [[2,2],[5,4],[6,3],[6,2],[8,3],[8,8]]
        [[2, 2, 0], [5, 4, 1], [6, 3, 3], [6, 2, 4], [8, 3, 5], [8, 8, 0]]

        - keep track of the largest overshadowing triangle
            - whichever triangle reaches the farthest x-pos
            - x + y ex: [5,4]
                - reaches: 5 + 4 = 9
                - this is greater than the previous max which is 4
                - so we keep referencing to the largest
                - next number 6 + 3 = 9, we don't change since its not greater

        [5,4] compare with [6,3]
        - see the difference in the x positions
        6 - 5 = 1
        - since the peaks are sorted, the lowest value this can become is 0

        - we are trying to find where the slope y-pos of the larger triangle is in comparison to the
        same x pos as the further right triangle
        - the x difference has to be the same as the y difference
        - pos-y where is it meets the 2nd triangle:
            [5,4] => y - diff => 4 - 1 = 3

            position in comparison = [6,3] => [2nd_triangle_x, 1st_triangle_pos_y_calculated]

        Time: O(nlogn)
            ; (n) add value to list
            ; (nlogn) sort
            ; (n) counter and get repeating peaks
            ; (n) greedy count number of peaks
        Space: O(n)

        '''
        peaks = [(x, y, x-y) for x, y in peaks]
        peaks = sorted(peaks, key=lambda x: (x[2], -x[1]))
        repeating_peaks = set()
        for key, val in Counter(peaks).items():
            if val > 1:
                repeating_peaks.add(key)

        res = 0
        highest_peak = [-1, 0]
        for peak in peaks:

            if peak[0] + peak[1] > highest_peak[0] + highest_peak[1]:
                # new mountain range with further right than the current highest peak
                highest_peak = [peak[0], peak[1]]

                if peak in repeating_peaks:
                    continue

                res += 1

        return res
