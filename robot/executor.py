from robot.core import Robot

commands = (
    "PLACE X,Y,F"
    "MOVE"
    "LEFT"
    "RIGHT"
    "REPORT"
)

robot = Robot()


def execute_line(line):

    line = line.strip().lower()

    cmd = getattr(robot, line, None)
    if cmd:
        if robot.is_placed:
            cmd()
        else:
            print("Robot is not placed yet.")

    # place command
    if line.startswith("place "):
        cmd_parse = line.replace("place ", "")
        x, y, f = [s.strip() for s in cmd_parse.split(",")]

        try:
            robot.place(x, y, f)
        except Exception as e:
            print(e)


def execute_file(file):
    """
    Note an absolute path shall be passed (Using os.path.join)
    """
    with open(file, 'r') as f:
        queue = f.readlines()

        for line in queue:
            execute_line(line)
