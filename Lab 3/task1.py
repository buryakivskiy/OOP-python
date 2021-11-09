import datetime

class RegularTicket:
    numbers = []
    def __init__(self, event, price):
        self.number = self.generateNumber()
        self.price = price
        self.event = event

    @property
    def event(self):
        return self.__event

    @event.setter
    def event(self, event):
        self.__event = event
    
    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, number):
        self.__number = number

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        self.__price = price

    def generateNumber(self):
        number = len(self.numbers)
        self.numbers.append(number)
        return number

    def __str__(self):
        return f'{self.__number} {self.__price}'
    

class AdvanceTicket ( RegularTicket ):
    def __init__(self, event, price):
        super().__init__(event, price*0.6)

class LateTicket ( RegularTicket ):
    def __init__(self, event, price):
        super().__init__(event, price*1.1)

class StudentTicket ( RegularTicket ):
    def __init__(self, event, price):
        super().__init__(event, price*0.5)

def main():
    basePrice = 100
    event = "IT-cluster Kyiv"
    currentDate = "21.09.2020"
    eventDate = "21.09.2020"
    

    
def daysToEvent(ticketDate, eventDate):
    if not isinstance(ticketDate, str) or not isinstance(eventDate, str):
        raise TypeError("Incorrect type") 
    try:
        d1 = datetime.strptime(ticketDate, "%d.%m.%Y")
        d2 = datetime.strptime(eventDate, "%d.%m.%Y")
    except:
        raise ValueError("Invalid  format of date")
    return abs((d2 - d1).days)