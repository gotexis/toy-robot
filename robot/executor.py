from robot.core import Robot

commands = (
    "PLACE X,Y,F"
    "MOVE"
    "LEFT"
    "RIGHT"
    "REPORT"
)


def execute_file(file):
    """
    Note an absolute path shall be passed (Using os.path.join)
    """
    robot = Robot()

    with open(file, 'r') as f:
        queue = f.readlines()

        for line in queue:
            robot.execute_line(line)
