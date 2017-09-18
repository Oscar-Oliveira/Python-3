class Room():

    def __init__(self, name, description=None):
        self.__name = name
        self.__description = description
        self.__linked_rooms = {}
        self.__character = None

    @property
    def Name(self):
        return self.__name

    @Name.setter
    def Name(self, value):
        self.__name = value
    
    @property
    def Description(self):
        return self.__description

    @Description.setter
    def Description(self, value):
        self.__description = value
    
    @property
    def Character(self):
        return self.__character
    
    @Character.setter
    def Character(self, value):
        self.__character = value

    def link_to_room(self, room, direction):
        self.__linked_rooms[direction] = room

    def move_to_direction(self, direction):
        return self.__linked_rooms[direction] \
               if direction in self.__linked_rooms \
               else self

    def __str__(self):
        return_value = self.Name
        for direction in self.__linked_rooms:
            room = self.__linked_rooms[direction]
            return_value += " [" + room.Name + ": " + direction + "]"
        return_value += " Inside: " + (str(self.__character) if self.__character != None else "Nobody")
        return return_value
