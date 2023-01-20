import unittest
from src.guests import Guests
from src.rooms import Rooms
from src.songs import Songs
from src.bar import Bar


class TestSongs(unittest.TestCase):
  def setUp(self):
    self.song1 = Songs('Bugging', 'Brakence')

  def test_title(self):
    self.assertEqual('Bugging', self.song1.title)

  def test_artist(self):
    self.assertEqual('Brakence', self.song1.artist)
