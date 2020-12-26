from decimal import Decimal

class Money():
    CONST_ZERO = Money.wons(0)

    self._CONST_AMOUNT = 0

    def __init__(self, amount):
        self._CONST_AMOUNT = amount

    def wons(self, amount):
        return Money(Decimal(amount))

    def plus(self, amount):
        return Money(self._CONST_AMOUNT + Decimal(amount.amount))

    def minus(self, amount):
        return Money(self._CONST_AMOUNT - Decimal(amount.amount))

    def times(self, percent):
        return Money(self._CONST_AMOUNT * Decimal(percent))

    def isLessThan(self, other):
        return self._CONST_AMOUNT < other._CONST_AMOUNT

    def isGreaterThanOrEqual(self, other):
        return self._CONST_AMOUNT >= other._CONST_AMOUNT
