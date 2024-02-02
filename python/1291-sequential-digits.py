class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        '''
        Sliding Window

        - there are a finite amount of combinations where the next number increases
        [1,2,3,4,5,6,7,8,9]

        - even if the high is 10**9, it doesn't matter since the biggest number
        we can create is 123,456,789
        - so start the window with the length of the low, end the window with lenght of high
        - we need to try all the length combinations between those two
        Ex: low=100 high: 13000
            - we need to try window combinations of length 3 to length 5

                - then we need to move the window starting from 1, all the way up
                to the end of 9(accounting for window length)

                    - if the number is between low and high then we add the number to the result
                    - this will also ensure the numbers are sorted

        Time: O(1)
        Space: O(1)
        '''

        numbers = '123456789'
        res = []
        for window_size in range(len(str(low)), len(str(high)) + 1):
            # print(window_size)
            # 10 is the size of 123456789
            for start in range(10 - window_size):
                num = int(numbers[start: start + window_size])
                if low <= num <= high:
                    res.append(num)

        return res
