from song import Song


class Album:

    def __init__(self, title, releaseYear):
        self.__title = title
        self.__releaseYear = releaseYear
        self.__songs = []

    def getTitle(self):
        return self.__title

    def getReleaseYear(self):
        return self.__releaseYear

    def getSongs(self):
        return self.__songs

    def addSongs(self, *new_songs):
        new_songs_count = 0
        for new_song in new_songs:
            new_song_is_in_album = False
            for album_song in self.__songs:
                if new_song.equals(album_song):
                    new_song_is_in_album = True
                    break
            if not new_song_is_in_album:
                self.__songs.append(new_song)
                new_songs_count += 1
        return new_songs_count

    def sortBy(self, byKey, reverse):
        sorted_songs = sorted(self.__songs, key=byKey, reverse=not reverse)
        self.__songs = sorted_songs
        return sorted_songs

    def sortByName(self, reverse):
        return self.sortBy(lambda song: song.getTitle(), reverse)

    def sortByPopularity(self, reverse):
        return self.sortBy(lambda song: song.getLikes(), reverse)

    def sortByDuration(self, reverse):
        return self.sortBy(lambda song: song.getDuration(), reverse)

    def sortByReleaseYear(self, reverse):
        return self.sortBy(lambda song: song.getReleaseYear(), reverse)

    def songs_as_str(self):
        songs_as_string = []
        for song in self.__songs:
            songs_as_string.append(str(song))
        return "|".join(songs_as_string)

    def totalLikes(self):
        totalLikes = 0
        for song in self.__songs:
            totalLikes += song.getLikes()
        return totalLikes

    def __str__(self):
        return "Title:" + self.getTitle() + ",Release year:" + str(
            self.getReleaseYear()) + ",songs:{" + self.songs_as_str() + "}"

