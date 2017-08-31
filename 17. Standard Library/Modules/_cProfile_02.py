"""
cProfile
- Columns:
    - ncalls- number of calls made
    - tottime- total time spent in current function
    - percall- tottime divided by ncalls
    - cumtime- cumulative time spent in current function and subfunctions
    - percall- cumtime divided by primitive calls
    - fileName:lineNumber(function)
"""

import cProfile
import os
from pathlib import Path
import _cProfile_01

cProfile.run("_cProfile_01.main()")
filePath = str(Path(os.path.dirname(__file__)).parent.parent.joinpath("Temp", "cProfile_output.txt"))

cProfile.run("_cProfile_01.main()", filePath)

# On Command Line:
# $ python -m cProfile -o ..\..\Temp\output.txt .\_cProfile_01.py
# output.txt will be binary, pstats needed

print("Done!")
