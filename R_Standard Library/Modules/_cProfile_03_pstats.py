"""
pstats
"""

import pstats
import os
from pathlib import Path

filePath = str(Path(os.path.dirname(__file__)).parent.parent.joinpath("_Temp", "cProfile_output.txt"))

p = pstats.Stats(filePath)
p.strip_dirs().sort_stats(-1).print_stats()
