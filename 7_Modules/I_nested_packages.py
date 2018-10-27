"""
Nested Packages
"""

from Package1 import ModuleTest
from Package1.Package1_1 \
    import ModuleTest as third # nested packages

print(ModuleTest.my_multiplier(15, 10))
print(third.my_multiplier(15, 10))
