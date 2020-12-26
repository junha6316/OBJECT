from TicketOffice import TicketOffice
from TicketSeller import TicketSeller

class Theater:
    
    def __init__(self, ticketSeller):
        self.__ticketSeller = ticketSeller

    def enter(self, audience):
        self.__ticketSeller.sellTo(audience)
        