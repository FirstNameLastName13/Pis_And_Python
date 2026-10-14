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
        for song in self.songs:
            x += int(song.duration)
        y = x // 60
        z = x % 60
        z = str(z)
        if len(z) < 2:
            o = "0"
            o += z 
            z = o
        return str(y) + ":" + str(z)
    
    def find_by_artist(self, artist_name):
        x = ""
        for song in self.songs:
            if song.artist == artist_name:
                x += song.title
                x += ", "
        a = x[:-2]
        if a.count(",") == 0:
            print(f"no songs by {artist_name} in your playlist")
        else:
            print(f"songs by {artist_name} in your playlist:", a)
    
    def print_playlist(self):
        print(self.name.upper())
        for song in self.songs:
            print(song.title, ",", song.artist)
    
    def load_songs(self,filename):
        self.songs = []
        with open(filename, "r") as f:
            for line in f.readlines():
                x = line.split(",")
                song = Song(x[0], x[1], x[2])
                self.songs.append(song)

    def __str__(self):
            x = ""
            try:
                for y in range(len(self.songs)):
                    x += str(self.songs[y])
                    try:
                        if self.songs[y + 1] in self.songs:
                            x += ", "
                    except IndexError:
                        x += ""
            except TypeError:
                x = self

            return(x)

def main():
    playlist = Playlist("my playlist", [])
    playlist.load_songs("music.csv")
    playlist.add_song(Song("Animal", "KATSEYE", 158))
    playlist.print_playlist()
    playlist.get_total_duration()
    playlist.find_by_artist("Howard Shore")

if __name__ == '__main__':
	main()
