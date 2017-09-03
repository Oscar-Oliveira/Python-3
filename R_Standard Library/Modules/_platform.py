"""
platform
"""

import os
import platform
import pprint as pp

def NewFileAtHome(fileName):
    if platform.platform().startswith('Windows'):
        return os.path.join(os.getenv('HOMEDRIVE'), \
            os.getenv('HOMEPATH'), fileName)
    return os.path.join(os.getenv('HOME'), fileName)

file = NewFileAtHome('test.log')
print("Logfile:", file)

pp.pprint(vars(platform))
