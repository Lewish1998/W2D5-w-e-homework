import unittest
from src.guests import Guests
from src.rooms import Rooms
from src.songs import Songs

class TestGuest(unittest.TestCase):

    def setUp(self):
            self.guest = Guests('Steve', 'Rosier', '180')

    def test_guest_name(self):
        self.assertEqual('Steve', self.guest.name)

    def test_guest_song(self):
        self.assertEqual('Rosier', self.guest.fav_song)

    def test_guest_cash(self):
        self.assertEqual('180', self.guest.cash)