"""
try import
"""

try:
    import cProfile as profiler
except:
    import profile as profiler

print(profiler.__all__)
