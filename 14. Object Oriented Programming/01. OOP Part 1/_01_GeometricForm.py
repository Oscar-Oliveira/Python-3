"""
Abstract Class - GeometricForm
"""

class GeometricForm():
    """Abstract class"""

    def get_corner(self):
        """Return left-bottom most point of geometric form"""
        raise NotImplementedError("Must implement this")

    def __del__(self):
        print(self.__class__.__name__, self, "destroyed")
