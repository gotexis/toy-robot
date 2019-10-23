from robot.core import Robot, Board
from robot.executor import execute_line

board = Board()

robot_1 = Robot()
robot_2 = Robot()

# place 2 robots in the same board

robot_1.place(1, 2, 'north', board)
robot_2.place(3, 4, 'south', board)

board.report()

board.get_robot(x=1, y=2)
