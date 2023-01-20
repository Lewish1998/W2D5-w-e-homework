import unittest
from src.guests import Guests
from src.rooms import Rooms
from src.songs import Songs
from src.bar import Bar

class TestBar(unittest.TestCase):

    def setUp(self):
        self.guest_1 = Guests('Lewis', 100, 'House Of Wolves')
        self.room_1 = Rooms(1)
        self.bar = Bar(500)
        
    def test_get_drink_price(self):
        drink = 'Tennents'
        self.assertEqual(4.50, self.bar.drinks[drink])
        drink = 'Magners'
        self.assertEqual(3.75, self.bar.drinks[drink])
        
    def test_add_price_to_till(self):
        self.bar.sell_drink('Magners', self.guest_1)
        self.assertEqual(503.75, self.bar.till)

    def test_remove_money_from_customer(self):
        self.bar.sell_drink('Magners', self.guest_1)
        self.assertEqual(96.25, self.guest_1.cash)
