#creates an object Song containing a title (str), artist (str), and duration in seconds (int)
class Song:
    def __init__(self, title, artist, duration):
        self.title = title
        self.artist = artist
        self.duration = duration

#creates an object Playlist containing a name (str) and an array of songs
class Playlist:
    def __init__(self, name, songs):
        self.name = name
        self.songs = {}
    def load_songs(self,file):
        with open(file, "r") as f:
            lines = f.readlines()
        for line in lines:
            
