"""
Packages
"""

from Package1 import ModuleTest
import Package2.ModuleTest

print(ModuleTest.my_multiplier(15, 10))
print(Package2.ModuleTest.my_multiplier(15, 10)) # full Path
