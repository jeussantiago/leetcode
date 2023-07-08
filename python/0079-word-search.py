class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        '''
        adjacent cells = horizontal or vertically connencting

        - go through every character

            - at each character, check if we have visited the position above, below, left, and right
            - if have not visited and character is the next character in the word sequence
                - backtrack on that character
            - if none of the neightboring characters are the next character in the sequence  or all have been visited/out of bounds
                - return 


        Time: O(m * n * dfs) size of the board - dfs length is going to be the length of the word
            - but dfs doesn't just happend once, it has 4 times (top, bottom, left, and right) => 4^(len(word))
            : O(m * n * 4^w) where w = len(word) and m*n = board length
        Space: O(m * n)
        '''
        def backtrack(visited, strng):
            if not strng:
                nonlocal result
                result = True
                return
            current_cell = visited[-1]
            #check neighboring cells - last visited is the current cell
            above = (current_cell[0] - 1, current_cell[1])
            below = (current_cell[0] + 1, current_cell[1])
            left =  (current_cell[0], current_cell[1] - 1)
            right = (current_cell[0], current_cell[1] + 1)
            possible_pos = [above, below, left, right]
            #check if the new position is out of bounds and is the next character
            for pos in possible_pos:
                #in board bounds
                if 0 <= pos[0] <= len(board)-1 and 0 <= pos[1] <= len(board[0])-1:
                    #position has not been visited before
                    if pos not in visited:
                        #pos is the next character in sequence
                        if board[pos[0]][pos[1]] == strng[0]:
                            #go to next character
                            backtrack(visited + [pos], strng[1:])



        result = False

        # To prevent TLE (time limite exceeding),reverse the word if frequency of the first letter is more than the last letter's
        count = collections.Counter(word)
        if count[word[0]] > count[word[-1]]:
            word = word[::-1]

        for row in range(len(board)):
            for col in range(len(board[0])):
                c = board[row][col]
                #if the character is the first character in the word
                if c == word[0]:
                    #backtrack on that word
                    backtrack([(row, col)], word[1:])

        return result






