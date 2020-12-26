class Screening():
    
    def __init__(self, movie, sequence, whenScreened):
        self.__movie = movie
        self.__sequence = sequence
        self.__whenScreened = whenScreened

    def reserve(self, customer, audienceCount):
        return Reservation(customer, self, calculateFee(audienceCount), audienceCount)

    def calculateFee(self, audienceCount):
        return movie.calculateMovieFee(self).times(audienceCount)

    def getStartTime(self):
        return self.__whenScreened

    def isSequence(self, sequence):
        return self.__sequence == sequence

    def getMovieFee(self):
        return movie.getFee()


    