class TicketOffice:
    self.__amount= 0
    self.__tickets = []

    def __init__(self, **attr):
        self.__amount = attr.get('amount')
        self.__tickets = attr.get('tickets')

    def sellTicketTo(self, audience):
        self.plusAmount(audience.buy(getTicket()))
        
    def getTicket(self):
        return self.__tickets.pop(0)

    def minusAmount(self, amount):
        self.__amount -= amount

    def plusAmount(self, amount):
        self.__amount += amount


