class SnakeGame:
    '''
    __init__:
        T: O(1)
        S: O(1)

    n being the length of food array
    - the snake can only grow as big as there are food on the board
    move: 
        T: O(1)
        S: O(n)

    '''

    def __init__(self, width: int, height: int, food: List[List[int]]):
        self.snake = collections.deque([(0, 0)])
        self.snake_set = {(0, 0): 1}
        self.width = width
        self.height = height
        # stack
        self.food = food[::-1]
        self.score = 0
        self.movement = {
            'R': (0, 1),
            'L': (0, -1),
            'U': (-1, 0),
            'D': (1, 0)
        }

    def checkValidBoardPos(self, row, col):
        if (
            # not in the board
            row < 0 or row >= self.height or
            col < 0 or col >= self.width or
            # run into own body
            (row, col) in self.snake_set and
            (row, col) != self.snake[0]  # tail
        ):
            return False
        return True

    def move(self, direction: str) -> int:
        head = self.snake[-1]
        new_head = (head[0] + self.movement[direction][0],
                    head[1] + self.movement[direction][1])

        if not self.checkValidBoardPos(new_head[0], new_head[1]):
            return -1

        if self.food and list(new_head) == self.food[-1]:
            # food position, extend the snake
            self.food.pop()
            self.score += 1
        else:
            # not food position, update tail position
            tail = self.snake.popleft()
            del self.snake_set[tail]

        # add head no matter what
        self.snake.append(new_head)
        self.snake_set[new_head] = 1

        return self.score


# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)
