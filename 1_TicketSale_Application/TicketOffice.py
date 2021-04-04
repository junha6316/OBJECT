class TicketOffice:

    __amount = None
    __tickets = []

    def __init__(self, amount, tickets):
        self.__amount = amount
        self.__tickets = tickets

    def _getTicket(self):
        return tickets.pop(0)

    def sellTicketTo(self, audience):
        self.__plusAmount(audience.buy(self._getTicket()))

    def minusAmount(self, amount):
        self.__amount -= amount
    
    def __plusAmount(self, amount):
        self.__amount += amount