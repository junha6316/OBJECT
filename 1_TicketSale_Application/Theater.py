class Theater:
    __ticketSeller =None

    def __init__(self, ticketSeller):
        self.__ticketSeller = ticketSeller

    def enter(self, audience):
        ticketSeller.sellTo(audience)
        