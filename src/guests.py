class Guests:
    def __init__(self, name, cash, fav_song):
      self.name = name
      self.cash = cash
      self.fav_song = fav_song
    
    def favourite_song(self, room):
      if self.fav_song in room.songs:
          return 'Holy shit I love this song'
      return 'What a shite playlist'
