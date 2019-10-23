from collections import OrderedDict
from copy import deepcopy
from dataclasses import dataclass, field
from typing import List

# board design ------------------------------------------------
#  4
#  3
#  2
#  1
#  0  1  2  3  4

# how to move

direction_clockwise_sequence = OrderedDict(
    [('north', [0, 1]),
     ('east', [1, 0]),
     ('south', [0, -1]),
     ('west', [-1, 0])]
)

directions = list(direction_clockwise_sequence)


@dataclass
class Board:
    size_x          : int  = 4
    size_y          : int  = 4
    placed_robots   : List = field(default_factory=list)

    def report(self):
        for robot in self.placed_robots:
            robot.report()

    def get_robot(self, **criteria):
        # return whether a position is already filled with a robot
        filtered = [
            robot for robot in self.placed_robots
            if all([
                (getattr(robot, k) == v) for k, v in criteria.items()
            ])
        ]
        print(filtered)
        return filtered


@dataclass
class Robot:
    # state
    x:      int   = None
    y:      int   = None
    face:   str   = None

    # board
    board: Board = Board()

    def __repr__(self):
        return f'Robot x:{self.x}, y:{self.y}, face:{self.face}'

    @property
    def is_placed(self):
        """
        :return: Whether the board is placed.
        """
        return all([self.x == 0 or self.x, self.y == 0 or self.y, self.face])

    def place(self, x, y, face, board=None):

        # sync board
        if not board:
            board = self.board
        else:
            self.board = board

        # include self in board placed robot
        if self not in board.placed_robots:
            board.placed_robots.append(self)

        try:
            x = int(x)
            y = int(y)

            if x > self.board.size_x:
                # print(f"x = {x} > {self.board.size_x}")
                print("Invalid input.")
                return
            if y > self.board.size_y:
                # print(f"y = {y} > {self.board.size_y}")
                print("Invalid input.")
                return
            if not face.lower() in directions:
                # print(f"{face.lower()} not in {directions}")
                print("Invalid input.")
                return

        except TypeError:
            # print(x, y, face)
            print("Invalid input.")
            return

        self.x = x
        self.y = y
        self.face = face

    def move(self):

        # get what is required to do
        move_x, move_y = direction_clockwise_sequence[self.face]

        # dry run first for safety
        fake_new_x = deepcopy(self.x)
        fake_new_y = deepcopy(self.y)

        fake_new_x += move_x
        fake_new_y += move_y

        if fake_new_x <= self.board.size_x:
            if fake_new_y <= self.board.size_y:
                self.x += move_x
                self.y += move_y
                return

        print("Safety warning - I am about to fall to oblivion!")

    def right(self):
        directions.index(self.face)

        current_direction_index = directions.index(self.face)

        try:
            new_direction = directions[current_direction_index + 1]
        except IndexError:
            # back to 0
            new_direction = directions[0]

        self.face = new_direction

    def left(self):
        # maybe just rotate 3 times to the left
        for i in range(3):
            self.right()

    def report(self):
        result = f"{self.x}, {self.y}, {self.face.upper()}"  # with space
        print(result)
        return result

    def execute_line(self, line):
        line = line.strip().lower()

        cmd = getattr(self, line, None)
        if cmd:
            if self.is_placed:
                cmd()
            else:
                print("Robot is not placed yet.")

        # place command
        if line.startswith("place "):
            cmd_parse = line.replace("place ", "")
            x, y, f = [s.strip() for s in cmd_parse.split(",")]

            try:
                self.place(x, y, f)
            except Exception as e:
                print(e)
