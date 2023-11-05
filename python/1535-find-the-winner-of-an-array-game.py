class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        '''
        - difers from simulation in that we don't use extra space for the queue

        - any number can win if they reach k
            - however, if you find the max number, then that number will automatically win

        - get the max number in the array
        - while going through the arr, simulate

        - end the game if you find the max number or if you find a number with k wins

        Time: O(n)
        Space: O(1)
        '''
        maxNum = max(arr)
        consecutive_wins = 0
        curr_winning_num = arr[0]

        for i in range(1, len(arr)):
            opponent = arr[i]

            if curr_winning_num > opponent:
                consecutive_wins += 1
            else:
                curr_winning_num = opponent
                consecutive_wins = 1

            if curr_winning_num == maxNum or consecutive_wins == k:
                return curr_winning_num


class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        '''
        Simulation - w/ queue

        arr = [1,2,3,4,5,6,7,8], k = 10
        - every first position number will be pushed onto the end
        - the cycle will finally stop when it reaches the last number(biggest number)
            - then it will complete the k consecutive wins

        arr = [3,2,1], k = 10
        - in this case, 3 would win, but it would cycle many times
        - probably best to reduce k to the length of the array

        Time: O(n)
        Space: O(n)
            ; (n) queue
        '''
        k = min(k, len(arr))
        q = collections.deque(arr)
        consecutive_wins = 0

        while True:
            if q[0] > q[1]:
                winner = q.popleft()
                loser = q.popleft()
                q.appendleft(winner)
                q.append(loser)
                consecutive_wins += 1
            else:
                loser = q.popleft()
                q.append(loser)
                consecutive_wins = 1

            if consecutive_wins == k:
                return q[0]
