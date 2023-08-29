class Solution:
    def bestClosingTime(self, customers: str) -> int:
        '''
        0 0 0 1 1 - number of No’s to the left
        3 2 1 1 0 - number of Yes’ to the right

        3 2 1 2 1 - total, we just need to find the min value and return the index of that

        We’re counting how many penalties from each side if we closed at time i. We get penalties from the left of i if it’s No. we get penalties from right if it’s Yes. Prefix sum. 

        Converge the two sides

        Time: (n)
        Space: (n)
        '''

        N = len(customers)
        left = [0] * (N + 1)
        right = [0] * (N + 1)

        curr_sum = 0
        for ind, c in enumerate(customers):
            if c == 'N':
                curr_sum += 1
            left[ind+1] = curr_sum

        curr_sum = 0
        for ind in range(N-1, -1, -1):
            if customers[ind] == 'Y':
                curr_sum += 1
            right[ind] = curr_sum

        total = [left[i] + right[i] for i in range(len(left))]

        return total.index(min(total))
