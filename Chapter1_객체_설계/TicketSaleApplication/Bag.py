from Invitation import Invitation
from Ticket import Ticket

class Bag():
    self.__amount=0
    self.__invitation = None
    self.__ticket = None

    def __init__(self, **attr):
        self.__invitation = attr.get('invitation')
        self.__amount = attr.get('amount')
        return
    
    
    def hasInvitation(self):
        return self.__invitation != None

    def hasTicket(self):
        self.__ticket != None
    
    def setTicket(self, ticket):
        self.__ticket = ticket
    
    def minusAmount(self, amount):
        self.__amount -= amount
    
    def plusAmount(self, amount):
        self.__ amount += amount