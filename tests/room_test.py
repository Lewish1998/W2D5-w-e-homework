import unittest
from src.guests import Guests
from src.rooms import Rooms
from src.songs import Songs

class TestRooms(unittest.TestCase):
    def setUp(self):
        self.room_1 = Rooms(1)
        self.guest_1 = Guests('Lewis', 100, 'House Of Wolves')
        self.guest_2 = Guests('Emily', 20, 'Chelsea Dagger')
        
    def test_room_number(self):
        self.assertEqual(1, self.room_1.room_number)
                
    def test_space_available(self):
        self.assertEqual(5, self.room_1.space_available)

    def test_check_in_guest_list(self):
        self.room_1.check_in(guest=self.guest_1)
        self.room_1.check_in(guest=self.guest_2)
        self.assertEqual(['Lewis', 'Emily'], self.room_1.guests)

    def test_check_in_space_available(self):
        self.room_1.check_in(guest=self.guest_1)
        self.room_1.check_in(guest=self.guest_2)
        self.assertEqual(3, self.room_1.space_available)

    def test_check_out_guest_list(self):
        self.room_1.check_in(guest=self.guest_1)
        self.assertEqual(['Lewis'], self.room_1.guests)

        self.room_1.check_out(guest=self.guest_1.name)
        self.assertEqual([], self.room_1.guests)

    def test_add_song(self):
        self.room_1.add_song('House Of Wolves')
        song_list = self.room_1.songs
        self.room_1.add_song('Chelsea Smile')
        self.assertEqual(['House Of Wolves', 'Chelsea Smile'], song_list)

    def test_remove_song(self):
        self.room_1.add_song('House Of Wolves')
        song_list = self.room_1.songs
        self.room_1.remove_song('House Of Wolves')
        self.assertEqual([], song_list)

    def test_no_space_remaining(self):
        self.room_1.space_available = 1
        self.room_1.check_in(self.guest_1)
        self.assertEqual(0, self.room_1.space_available)
        self.assertEqual('No space available', self.room_1.check_in(self.guest_2))
        
    def test_pay_entry(self):
        self.room_1.pay_entry(self.guest_1)
        self.assertEqual(93, self.guest_1.cash)

    def test_pay_entry_on_check_in(self):
        self.room_1.check_in(self.guest_1)
        self.assertEqual(93, self.guest_1.cash)
        self.assertEqual(['Lewis'], self.room_1.guests)
