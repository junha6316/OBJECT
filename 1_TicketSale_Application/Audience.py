class Audience:

    __bag = None

    def __init__(self, bag):
        self.__bag = bag

    def getBag(self):
        return self.__bag

    def buy(self, ticket):
        return self.__bag.hold(ticket)