class Bag:

    __amount = 0
    __invitation = None
    __ticket = None

    #이벤트에 당첨된 관람객 가방안에은 초대장이 있을 수도 있고 없을 수도 있음
    def __init__(self, **kwargs):
        self.__amount = kwargs['amount']
        self.__invitation = kwargs['invitation']

    def hold(ticket):
        if self._hasInvitation():
            self._setTicket(ticket)
            return None
        else:
            self._setTicket(ticket)
            self._minusAmount(ticket.getFee())
            return ticket.getFee()

    def _hasInvitation(self):
        return self.__invitation != None

    def _setTicket(self, ticket):
        self.__ticket = ticket


    def _minusAmount(self, amount):
        self.__amount -= amount
        
    def hasTicket(self):
        return self.__ticket != None

    


    def plusAmount(self, amount):
        self.__amount += amount

    
    

