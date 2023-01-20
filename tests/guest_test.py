import unittest
from src.guests import Guests
from src.rooms import Rooms
from src.songs import Songs

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.guest_1 = Guests('Lewis', 100)

    def test_guest_name(self):
        self.assertEqual('Lewis', self.guest_1.name)

    def test_guest_cash(self):
        self.assertEqual(100, self.guest_1.cash)