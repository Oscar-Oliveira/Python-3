"""
Packages 
- Packages(folders) MUST contain an __init__.py inside 
- __init__.py can be an empty file
"""

from Package1 import ModuleTest
# "as alias" otherwise name clash on ModuleTest
from Package2 import ModuleTest as Second

print(ModuleTest.my_multiplier(15, 10))
print(Second.my_multiplier(15, 10))
