import random
class Rooms:
    def __init__(self):
        # self.room_number = room_number
        self.guests = []
        self.songs = []
        self.empty_rooms = [1,2,3,4,5]
        self.room_num = random.choice(self.empty_rooms)

    def add_guests_to_room(self, guest):
        self.empty_rooms.remove(self.room_num)
        self.guests.append(guest)
        self.songs.append(guest.fav_song)