# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
# class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """

class Solution:
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None

        - work in a clockwise manner, keep hugging the right side
        - if there is an open space, move the robot to that space
        - if the space is visited or the space is a wall, turn the robot right

        - when the robot moves, we want to keep the same direction it is facing
            - we can do this by keeping track of the current index in the directions array

        - if a robot has visited all the positions for the path, it needs to go backwards to the prvious space
            - turnRight 2x (turn around)
            - move
            - turnRight 2x (face the original direction when going to the space in a previous iteration)

        n is all the open spaces
        m is all the wall spaces
        Time: O(n - m)
        Space: O(n - m)
            ; visited
        """

        def explore(cell, curr_direction):
            visited.add(cell)
            robot.clean()
            for i in range(4):
                next_direct = (i + curr_direction) % 4
                new_cell = (cell[0] + directions[next_direct]
                            [0], cell[1] + directions[next_direct][1])

                if new_cell not in visited and robot.move():
                    explore(new_cell, next_direct)
                    # backtrack to previous position - the robot was moved
                    robot.turnRight()
                    robot.turnRight()
                    robot.move()
                    robot.turnRight()
                    robot.turnRight()

                robot.turnRight()

        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        visited = set()
        explore((0, 0), 0)
