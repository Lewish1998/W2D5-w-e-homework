import random
class Rooms:

   def __init__(self, room_number):
      self.room_number = room_number
      self.space_available = 5
      self.guests = []
      self.songs = []
   
   def check_in(self, guest):
      if self.space_available > 0:
         self.guests.append(guest)
         self.space_available -= 1
         self.pay_entry(guest)
      else:
         return 'No space available'

   def check_out(self, guest):
      self.guests.remove(guest)
      self.space_available += 1

   def add_song(self, song):
      self.songs.append(song)

   def remove_song(self, song):
      self.songs.remove(song)

   def pay_entry(self, guest):
      guest.cash -= 7