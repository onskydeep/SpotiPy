from song import Song
from album import Album


class Artist:
    def __init__(self, firstName, lastName, birthYear, albums, singles):
        self.__firstName = firstName
        self.__lastName = lastName
        self.__birthyear = birthYear
        self.__albums = albums
        self.__singles = singles

    def getFirstName(self):
        return self.__firstName

    def getSecondName(self):
        return self.__lastName

    def getBirthYear(self):
        return self.__birthyear

    def getAlbums(self):
        return self.__albums

    def getSingle(self):
        return self.__singles

    def mostLikedSong(self):
        mostlikedsong = None
        mostlikes = 0
        for album in self.getAlbums():
            for song in album.getSongs():
                if song.getLikes() >= mostlikes:
                    mostlikedsong = song
                    mostlikes = song.getLikes()

        for song in self.getSingle():
            if song.getLikes() >= mostlikes:
                mostlikedsong = song
                mostlikes = song.getLikes()

        return mostlikedsong

    def leastLikedSong(self):
        leastlikedsong = None
        leastlikes = 9223372036854775807  # max integer in py
        for album in self.getAlbums():
            for song in album.getSongs():
                if song.getLikes() <= leastlikes:
                    leastlikedsong = song
                    leastlikes = song.getLikes()

        for song in self.getSingle():
            if song.getLikes() <= leastlikes:
                leastlikedsong = song
                leastlikes = song.getLikes()

        return leastlikedsong

    def totalLikes(self):
        total_likes = 0
        for album in self.getAlbums():
            for song in album.getSongs():
                total_likes += song.getLikes()

        for song in self.getSingle():
            total_likes += song.getLikes()

        return total_likes

    def equalss(self,new_artist):
        if self.__firstName == new_artist.__firstName and self.getSecondName() == new_artist.getSecondName() and self.getBirthYear() == new_artist.getBirthYear():
            return True
        else:
            return False

    def __str__(self):
        return "Name:" + self.__firstName + " " + self.__lastName + ",Birth Year:" + str(
            self.__birthyear) + ",Total Likes:" + str(self.totalLikes())

