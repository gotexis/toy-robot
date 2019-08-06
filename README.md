# Exis' robot

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
