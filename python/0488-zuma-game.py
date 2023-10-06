class Solution:
    def findMinStep(self, board: str, hand: str) -> int:
        '''
        BFS - min number of steps

        - go through all the iterations of placing all balls in your hands in all the possibel positions in the board

        - skip repeating balls in your hand
            - solution: sort your hand and skip a ball if the current ball is the same as previous ball => skip

        - skip continuously repeating same balls on board since putting the same ball in a different position doesnt make a difference
            - solution: check if the current ball is the same as previous ball => skip

        - simulate adding a ball from your hand to the board
            - case 1: the current board ball is the same as the hand ball
                (board[i] == hand[j])
            - case 2: the current board ball is the same as the previous board ball
                - board="GGBBGGBB" => no removals - but just in case
                - board="GGGBBBGGGBBB" => remove everything; for this, you dont need to check if youre at the end of "GGG" sequence, since it
                will be added to the BFS queue if the board that it creates isnt visited. you can start checking at the first position
                (i < len(board)-1 and board[i] == board[i+1])

            - these cases look for a situation where theres atleast 2 balls of the same color

        - remove the balls w/ the hand ball attached
            - use a while loop to go left and right to find the furtheset index
            - check if the length is >= 3
            - if True: return the new board (without the left and right indexes)

        - get a new hand without the index of the hand added to the board

        - check if board is empty: return steps

        - if new_board and new hand not is visited
            - add new board and new hand to queue
            - add new board and new hand to visited

        - if not yet returned anything and out of items in queue: return -1 to indicate cant accomplish

        n is the length of the board
        m is the length of the hand
        Time: O(n^n)
            ; (mlogm) sort hand
            ; for every position in the board, you have to check every possible item in the hand. We sort our hand
            ; so that we don't use the same balls again when inserting so that can be reduced to (5) => (1)
            ; we need to decided to add the ball or not for every position. Worst case, the board can be "RYBGWRYBGW"
            ; and hand is "RYBGW", where everything repeats once so you check every position. Currently its exponential (n^something)
            ; the height of the tree should be the number of combinations of the board and the hand (5 *n)
            ; ((5*n) ^ (5*n)) => (n^n)
        Space: O(n)
            ; (5 * n) visited set
        '''
        def getNewBoard(temp_board, left):
            right = left + 1
            while 0 < right < len(temp_board) and temp_board[right] == temp_board[right - 1]:
                right += 1

            while left > 0 and temp_board[left] == temp_board[left-1]:
                left -= 1

            if right - left >= 3:
                # when we delete a sequence, a new combination might come togethere and we need to check for that
                # Ex: WWBBBBWW => WWWW
                return getNewBoard(temp_board[:left] + temp_board[right:], left - 1)
            else:
                return temp_board

        hand = "".join(sorted(hand))
        q = collections.deque([(board, hand, 0)])
        visited = set([(board, hand)])
        while q:
            curr_board, curr_hand, steps = q.pop()
            for i in range(len(curr_board)):
                # skip same board ball
                if i > 0 and curr_board[i] == curr_board[i-1]:
                    continue

                for j in range(len(curr_hand)):
                    # skip same hand ball
                    if j > 0 and curr_hand[j] == curr_hand[j-1]:
                        continue

                    if (
                        curr_board[i] == curr_hand[j] or
                        (i < len(curr_board) -
                         1 and curr_board[i] == curr_board[i+1])
                    ):
                        # I put it on the right, rather than the left because of testcases like this
                        # board="RRWWRRBBRR" hand="WB" => board="RBRWWRRBBRR" hand="B"
                        # now just insert the "W" in place and the entire board clears
                        new_board = getNewBoard(
                            curr_board[:i+1] + curr_hand[j] + curr_board[i+1:], i)
                        new_hand = curr_hand[:j] + curr_hand[j+1:]

                        if not new_board:
                            return steps + 1

                        if (new_board, new_hand) not in visited:
                            q.appendleft((new_board, new_hand, steps + 1))
                            visited.add((new_board, new_hand))

        return -1
