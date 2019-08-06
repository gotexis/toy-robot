# Exis' robot (completed in 2 hours)

python 3.7.3 is preferred. (Use of @dataclass)

update ps:

I got questioned that I completed it quite quick, indeed it was becuase Nick emailed and send the test and also said `time was a factor` at 12pm, by 2pm I was still having lunch, so I thought I had to rush it to show my efficiency, so I did it in 2 hours and completed it by 4pm. The code was `100% original` without any reference.

Also, I know the code is not perfect, but I didn't change it because I want to leave the original timestamp, so below [./robot/robot.py#L94](./robot/robot.py#L94) was actually useless, but I didn't fix it.

Becuase I am a `Fire Emblem` fan, this makes me want to make my own warchess game, hmmm

```python
def right(self):
    directions.index(self.face)  # <-- useless
```


## To use
```python
import os
from robot.executor import execute_file

execute_file(os.path.abspath("path_to_command_file"))

# Or, directly call the robot itself
from robot.robot import Robot

my_robot = Robot()
my_robot.place(1,1,"north")
my_robot.move()

# customizing a board is also supported.

from robot.robot import Board

board = Board(10, 10)
my_robot.board = board
```

## To test

```bash
python -m unittest robot.tests.test.TestFileExecution
```
