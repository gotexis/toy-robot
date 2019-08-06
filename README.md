# Exis' robot

python 3.7.3 is preferred. (Use of @dataclass)

update ps:

I got questioned that I completed it quite quick, indeed it was becuase Nick emailed and send the test and also said `time was a factor` at 12pm, by 2pm I was still having lunch, so I thought I had to rush it, so I did it in 2 hours and completed it by 4pm. The code was 100% percent original without any reference.

Also, I know the code is not perfect, but I didn't change it because I want to leave the original timestamp, so `./robot/robot.py:L94` was actually useless, but I didn't fix it.


To use:
```python
import os
from robot.executor import execute_file

execute_file(os.path.abspath("path_to_command_file"))

```

To test:

```bash
python -m unittest robot.tests.test.TestFileExecution
```
