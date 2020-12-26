from abc import *

class DiscountPolicy(metaclass= ABCMeta):
    
    def __init__(self, *conditions):
        self.__conditions = conditions

    def calculateDiscountAmount(self, screening):
        for DiscountCondition in self.__conditions:
            if (DiscountCondition.isSatisfiedBy(screening)):
                return self._getDiscountAmount(screening)

        
        return Money.CONST_ZERO

    @abstractmethod
    def _getDiscountAmount(self, screening):
        pass

class PercentDiscountPolicy(DiscountPolicy):
    def __init__(self, percent, conditions):
        super().__init__(self, conditions)
        self.__precent = percent

    def _getDiscountAmount(self, screening):
        return screening.getMovieFee().times(percent)
        
