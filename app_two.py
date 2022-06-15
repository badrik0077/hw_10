class Room:

    def __init__(self, number, is_free):
        self.number = number
        self.is_free = is_free


def get_free_rooms(rooms):
    free_rooms = []
    for room in rooms:
        if room.is_free is True:
            free_rooms.append(room)
    return free_rooms


rooms = [Room(14, True), Room(15, False), Room(16, True)]
rooms_free = get_free_rooms(rooms)
