"""
assert
raise an AssertionError if False
"""

MaxInField = 9
Team1 = set(range(1, 12))
Team2 = {1, 2, 4, 7, 5, 7, 11, 10, 23}
Team3 = {1, 2, 4, 7, 5, 8, 11, 10, 23, 13, 14, 15}

print(Team1, len(Team1))
print(Team2, len(Team2))
print(Team3, len(Team3))

try:
    assert len(Team1) <= MaxInField
    assert len(Team2) <= MaxInField
    print('Play the game!!')
except AssertionError:
    print('Teams are not well defined.')
