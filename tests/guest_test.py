import unittest
from src.guests import Guests
from src.rooms import Rooms
from src.songs import Songs

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.guest_1 = Guests('Lewis', 100, 'House Of Wolves')
        self.room_1 = Rooms(1)

    def test_guest_name(self):
        self.assertEqual('Lewis', self.guest_1.name)

    def test_guest_cash(self):
        self.assertEqual(100, self.guest_1.cash)

    def test_add_song(self):
        self.room_1.add_song('House Of Wolves')
        song_list = self.room_1.songs
        self.room_1.add_song('Chelsea Smile')
        self.assertEqual(['House Of Wolves', 'Chelsea Smile'], song_list)

    def test_guests_fav_song(self):
        self.room_1.add_song('House Of Wolves')
        self.assertEqual('Holy shit I love this song', self.guest_1.favourite_song(self.room_1)
)
