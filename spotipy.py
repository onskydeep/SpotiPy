from album import Album
from song import Song
from artist import Artist


class SpotiPy:
    def __init__(self):
        self.__artists = []

    def getArtists(self):
        return self.__artists

    def is_in_spotipy(self,new_artist):
        for artist in self.__artists:
            if artist.equalss(new_artist):
                return True
        return False

    def addArtists(self, *new_artists):
        for new_artist in new_artists:
            if not self.is_in_spotipy(new_artist):
                self.__artists.append(new_artist)

    def getTopTrendingArtist(self):
        max_likes = 0
        topTrendingArtist = None
        for artist in self.__artists:
            if artist.totalLikes() >= max_likes:
                topTrendingArtist = artist
                max_likes = artist.totalLikes()

        return (topTrendingArtist.getFirstName(), topTrendingArtist.getSecondName())

    def getTopTrendingAlbum(self):
        max_likes = 0
        topTrendingAlbum = None
        for artist in self.__artists:
            for album in artist.getAlbums():
                if album.totalLikes() >= max_likes:
                    max_likes = album.totalLikes()
                    topTrendingAlbum = album

        return topTrendingAlbum.getTitle()

    def getTopTrendingSong(self):
        max_likes = 0
        topTrendingSong = Song(0,0,0,0)
        for artist in self.__artists:
            if artist.mostLikedSong().getLikes() >= max_likes:
                max_likes = artist.mostLikedSong().getLikes()
                topTrendingSong = artist.mostLikedSong()

        return topTrendingSong.getTitle()

    @staticmethod
    def loadFromFile(self, path):
        with open(path, 'r') as file:
            data = []
            for line in file:
                grade_data = line.strip().split(',')
                data.append(grade_data)
                # print(grade_data)

        artists_start_indices = [2]

        for i in range(2, len(data)):
            if data[i][0][0] == '#':  # this means that it's artist line
                artists_start_indices.append(i)

        artists_start_indices.append(len(data))

        spotipy = SpotiPy()

        for j in range(0, len(artists_start_indices) - 1):
            i = artists_start_indices[j]  # this artist's start index
            if data[i][0][0] == '#':
                data[i][0] = data[i][0].split('#')[1]
            firstname = data[i][0]
            lastname = data[i][1]
            birth = data[i][2]  # achieved name,lastname,birth of artist

            albums = []
            albums_starts_at = []
            for k in range(i + 1, artists_start_indices[j + 1]):
                if len(data[k]) == 3:  # this means that it's album line
                    albums_starts_at.append(k)

            for k in albums_starts_at:
                if data[k][0][0] == '%':
                    album_title = data[k][0].split('%')[1]
                else:
                    album_title = data[k][0]
                album_release = int(data[k][1])  # we now have current album name and release date

                line_index = k + 2
                songs = []
                while data[line_index] != ['}']:
                    if data[line_index][0][0] == '|':
                        song_title = data[line_index][0].split('|')[1]
                    else:
                        song_title = data[line_index][0]
                    song_duration = data[line_index][1]
                    song_date = int(data[line_index][2])
                    song_likes = int(data[line_index][3])
                    song_duration = float(song_duration.split(' ')[0]) * 60

                    song = Song(song_title, song_date, 60, 0)
                    song.setDuration(song_duration)

                    for likes in range(0, song_likes):
                        song.like()  # bro xD,
                        # I didn't manage to write better implementation
                        # itiis what itiiis

                    songs.append(song)

                    line_index += 1

                album = Album(album_title, album_release)
                for song in songs:
                    album.addSongs(song)
                albums.append(album)
                # print(str(album))

            singles_line_index = i

            while data[singles_line_index] != ['singles:']:
                singles_line_index += 1

            singles = []
            line_index = singles_line_index + 2

            while data[line_index] != ['}']:
                if data[line_index][0][0] == '|':
                    song_title = data[line_index][0].split('|')[1]
                else:
                    song_title = data[line_index][0]
                song_duration = data[line_index][1]
                song_date = int(data[line_index][2])
                song_likes = int(data[line_index][3])
                song_duration = float(song_duration.split(' ')[0]) * 60

                song = Song(song_title, song_date, 60, 0)
                song.setDuration(song_duration)

                for likes in range(0, song_likes):
                    song.like()

                singles.append(song)
                # print(str(song))
                line_index += 1

            artist = Artist(firstname, lastname, birth, albums, singles)

            spotipy.addArtists(artist)
        return spotipy

