#creates an object Song containing a title (str), artist (str), and duration in seconds (int)
class Song:
    def __init__(self, title, artist, duration):
        self.title = title
        self.artist = artist
        self.duration = duration
    def __str__(self):
         return(str(self.title) + " (" + str(self.artist) + "): " + str(self.duration))

#creates an object Playlist containing a name (str) and an array of songs
class Playlist:
    def __init__(self, name, songs):
        self.name = name
        self.songs = songs
    def add_song(self, song):
            self.songs.append(song)
    def get_total_duration(self):
        x = 0
        for song in self:
            x += song.duration
        y = x % 60
        z = x - (x % 60)
        return str(y) + ":" + str(z)
    def __str__(self):
            x = ""
            for y in range(len(self.songs)):
                x += str(self.songs[y])
                try:
                    if self.songs[y + 1] in self.songs:
                        x += ", "
                except IndexError:
                    x += ""

            return(x)

def main():
    playlist1 = Playlist("mylist", [])
    song1 = Song("May It Be", "Howard Shore", 206)
    print(song1)
    song2 = Song("Flaming Red Hair", "Howard Shore", 159)
    print(song2)
    playlist1.add_song(song1)
    playlist1.add_song(song2)
    print("Your playlist:", playlist1)
if __name__ == '__main__':
	main()
