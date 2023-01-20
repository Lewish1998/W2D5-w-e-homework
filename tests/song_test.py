import unittest
from src.guests import Guests
from src.rooms import Rooms
from src.songs import Songs

class TestSongs(unittest.TestCase):

    def setUp(self):
            self.song1 = Songs('Highway To Hell', 'ACDC')
            
    def test_song_name_and_artist(self):
        song_name = self.song1.name
        artist = self.song1.artist
        self.assertEqual(('Highway To Hell', 'ACDC'), (song_name, artist))
