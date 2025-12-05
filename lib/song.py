class Song:
    # Class attributes
    count = 0
    artists = []
    genres = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre

        # Update count
        self.add_song_to_count()

        # Add raw data first (duplicates allowed at this stage)
        Song.genres.append(genre)
        Song.artists.append(artist)

        # Update unique sets
        self.add_to_genres(genre)
        self.add_to_artists(artist)

        # Update histograms
        self.add_to_genre_count(genre)
        self.add_to_artist_count(artist)

    # ---------- CLASS METHODS ---------- #

    @classmethod
    def add_song_to_count(cls):
        cls.count += 1

    @classmethod
    def add_to_genres(cls, genre):
        """Add a genre to the unique genres list if not already there."""
        if genre not in cls.genres:
            cls.genres.append(genre)

    @classmethod
    def add_to_artists(cls, artist):
        """Add an artist to the unique artists list if not already there."""
        if artist not in cls.artists:
            cls.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls, genre):
        """Build histogram of genres."""
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1

    @classmethod
    def add_to_artist_count(cls, artist):
        """Build histogram of artists."""
        if artist in cls.artist_count:
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist] = 1
