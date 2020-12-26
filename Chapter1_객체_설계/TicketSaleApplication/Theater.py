from TicketOffice import TicketOffice
from TicketSeller import TicketSeller

class Theater:
    
    def __init__(self, ticketSeller):
        self.__ticketSeller = ticketSeller

    def enter(self, audience):
        if audience.getBag().hasInvitation():
            ticket = self.__ticketSeller.getTicketOffice().getTicket()
            audience.getBag().setTicket(ticket)
        else:
            ticket = self.__ticketSeller.getTicket()
            audience.getBag().minusAmount(ticket.getFee())
            self.__ticketSeller.getTicketOffice().plusAmount(ticket.getFee())
            audience.getBag().setTicket(ticket)