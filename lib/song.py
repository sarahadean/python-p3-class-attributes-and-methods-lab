#Whenever a new song is created. Your __init__ method should call a class method add_song_to_count() that increments the value of count by one.

class Song:

    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        Song.add_song_to_count(self)
        Song.add_to_genres(self.genre)
        Song.add_to_artist(self.artist)
        Song.add_to_genre_count(genre)
        Song.add_to_artist_count(artist)

    # class method that updates count every time a new song is added
    @classmethod
    def add_song_to_count(cls, count):
        Song.count += 1

    # adds any new genres to a class attribute genres, a list. This list should contain only unique genres — no duplicates!
    @classmethod
    def add_to_genres(cls, genre):
        if genre not in cls.genres:
            cls.genres.append(genre)

    #adds any new artists to a class attribute artists, a list. This list should only contain unique artists, just like the genres class attribute
    @classmethod
    def add_to_artist(cls, artist):
        if artist not in cls.artists:
            cls.artists.append(artist)

    # adds to a class attribute genre_count, a dictionary in which the keys are the names of each genre. Each genre name key should point to a value that is the number of songs that have that genre.
    @classmethod
    def add_to_genre_count(cls, genre):
        #do .get with genre_count? if included, update += genre
        if cls.genre_count.get(genre):
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1

    @classmethod
    def add_to_artist_count(cls, artist):
        if cls.artist_count.get(artist):
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist] = 1
