class Song:
    def __init__(self, title, releaseYear, duration=60, likes=0):
        self.__title = title
        self.__releaseYear = releaseYear
        self.__duration = duration
        self.__likes = likes

    def getTitle(self):
        return self.__title

    def getReleaseYear(self):
        return self.__releaseYear

    def getDuration(self):
        return self.__duration

    def getLikes(self):
        return self.__likes

    def setDuration(self, new_duration):
        if new_duration < 0 or new_duration > 720 or self.__duration == new_duration:
            return False
        else:
            self.__duration = new_duration
            return True

    def like(self):
        self.__likes += 1

    def unlike(self):
        self.__likes -= 1 #it wasn't given in the statement what to do when likes amount is less than zero, so i left it way it was

    def __str__(self):
        return "Title:" + self.getTitle() + ",Duration:" + str(
            self.getDuration() / 60) + " minutes," + "Release year:" + str(self.getReleaseYear()) + ",Likes:" + str(
            self.getLikes())

    def equals(self, song):
        return self.__title == song.__title and self.__duration == song.__duration and self.__releaseYear == song.__releaseYear


