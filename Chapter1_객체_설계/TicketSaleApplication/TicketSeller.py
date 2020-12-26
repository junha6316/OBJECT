class TicketSeller:
    self.__ticketOffice = None

    def __init__(self, ticketOffice):
        self.__ticketOffice = ticketOffice

    def getTicketOffice(self):
        return self.__ticketOffice

        