import unittest
from io import StringIO
from robot.executor import execute_file
from robot.robot import Robot
import sys
from contextlib import contextmanager
import os


# helper function to test stdout
# https://stackoverflow.com/questions/4219717/how-to-assert-output-with-nosetest-unittest-in-python
@contextmanager
def captured_output():
    new_out, new_err = StringIO(), StringIO()
    old_out, old_err = sys.stdout, sys.stderr
    try:
        sys.stdout, sys.stderr = new_out, new_err
        yield sys.stdout, sys.stderr
    finally:
        sys.stdout, sys.stderr = old_out, old_err


curdir = os.path.dirname(__file__)


class TestFileExecution(unittest.TestCase):

    def test_falling_from_board(self):

        with captured_output() as (out, err):
            robot = Robot(4, 4, "east")
            robot.move()

        output = out.getvalue().strip()
        self.assertEqual(output, "Safety warning - I am about to fall to oblivion!")

    def test_invalid_input(self):

        with captured_output() as (out, err):
            robot = Robot()
            robot.place(100, 100, "nowhere")

        output = out.getvalue().strip()
        self.assertEqual(output, "Invalid input.")

    def test_invalid_command(self):
        # including invalid command

        with captured_output() as (out, err):
            execute_file(os.path.join(curdir, 'test1.txt'))

        output = out.getvalue().strip()
        self.assertEqual(output, "0, 1, NORTH")

    def test_execute_file(self):
        # 2
        with captured_output() as (out, err):
            execute_file(os.path.join(curdir, 'test2.txt'))

        output = out.getvalue().strip()
        self.assertEqual(output, "0, 0, WEST")

    def test_irregular_spaces_in_command(self):
        # 3
        with captured_output() as (out, err):
            execute_file(os.path.join(curdir, 'test3.txt'))

        output = out.getvalue().strip()
        self.assertEqual(output, "3, 3, NORTH")


if __name__ == '__main__':
    unittest.main()
