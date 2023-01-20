import unittest
from src.guests import Guests
from src.rooms import Rooms
from src.songs import Songs

class TestRooms(unittest.TestCase):

    def setUp(self):
        self.room = Rooms()
        self.guest = Guests('Steve', 'Rosier', 200)

    def test_object(self):
        room_no = self.room.room_number
        people = self.room.guests = ['Steve', 'Jim']
        songs = self.room.songs = ['Highway To Hell', 'Stairway To Heaven']
        self.assertEqual((1, ['Steve', 'Jim'], ['Highway To Hell', 'Stairway To Heaven']), (room_no, people, songs))
        
    def test_add_guest_to_rooms(self):
        