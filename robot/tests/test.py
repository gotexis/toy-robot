import unittest
from io import StringIO
from robot.executor import execute_file
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

    def test_execute_file(self):
        # 1
        with captured_output() as (out, err):
            execute_file(os.path.join(curdir, 'test1.txt'))

        output = out.getvalue().strip()
        self.assertEqual(output, "0, 1, NORTH")

        # 2
        with captured_output() as (out, err):
            execute_file(os.path.join(curdir, 'test2.txt'))

        output = out.getvalue().strip()
        self.assertEqual(output, "0, 0, WEST")

        # 3
        with captured_output() as (out, err):
            execute_file(os.path.join(curdir, 'test3.txt'))

        output = out.getvalue().strip()
        self.assertEqual(output, "3, 3, NORTH")


if __name__ == '__main__':
    unittest.main()
