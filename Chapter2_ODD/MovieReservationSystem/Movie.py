class Movie():

    def __init__(self, title, runningTime, fee, discountPolicy):
        self.__title = title
        self.__runningTime = runningTime
        self.__fee = fee
        self.__discountPolicy = discountPolicy

    def getFee(self):
        return self.__fee

    def calculateMovieFee(screening):
        return fee.minus(self.__discountPolicy.calculateDiscountAmount(screening))
        
