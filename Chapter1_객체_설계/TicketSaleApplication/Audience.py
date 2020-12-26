from Bag import Bag


class Audience:
    
    def __init__(self, bag):
        self.__bag = bag

    def getBag(self):
        return self.__bag
    
    def buy(self, ticket):
        if self.__bag.hasInvitation():
            self.__bag.setTicket(ticket)
            return 0
        else:
            bag.setTicket(ticket)
            bag.minusAmount(ticket.getFee())
            return ticket.getFee()

        
        