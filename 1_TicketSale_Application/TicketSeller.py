class TicketSeller:
    __ticketOffice = None

    def __init__(self, ticketOffice):
        self.__ticketOffice = ticketOffice

    def getTicketOffice(self):
        return self.__ticketOffice
    
    def sellTo(self, audience):
        self.__ticketOffice.plusAmount(
            audience.buy(
                self.__ticketOffice.getTicket()
                )
                )