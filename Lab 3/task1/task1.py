from datetime import datetime
import os
import time
import json

DAYS_FOR_ADVANCE_TICKET = 60
DAYS_FOR_LATE_TICKET = 10
COEFFICIENT_FOR_ADVANCE = 0.6
COEFFICIENT_FOR_LATE = 1.1
COEFFICIENT_FOR_STUDENT = 0.5


class RegularTicket:
    def __init__(self, person, event, price, eventDate):
        self.number = self.generateNumber()
        self.person = person
        self.event = event
        self.price = price
        self.eventDate = eventDate
        self.writeTicket()

    @property
    def eventDate(self):
        return self.__eventDate

    @eventDate.setter
    def eventDate(self, eventDate):
        self.__eventDate = eventDate

    @property
    def person(self):
        return self.__person

    @person.setter
    def person(self, person):
        self.__person = person

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
    
    def writeTicket(self):
        file = open(self.number + '.json', 'w')
        json.dump(self.__dict__, file, indent=2)
        file.close()
    
    def getTicket(fileName):
        if not os.path.exists(fileName + '.json'):
            raise FileNotFoundError
        file = open(fileName + '.json', "r")
        input = json.load(file)
        person = input['_RegularTicket__person']
        event = input['_RegularTicket__event']
        eventDate = input['_RegularTicket__eventDate']
        if '_StudentTicket__price' in input:
            price = input['_StudentTicket__price']
        elif '_LateTicket__price' in input:
            price = input['_LateTicket__price']
        else:
            price = input['_AdvanceTicket__price']
        file.close()
        return f"{fileName}\n{person}\nevent: {event}\ntotal price: {round(price)}\ndate: {eventDate}"

    def createTicket(fileName):
        if not os.path.exists(fileName):
            raise FileNotFoundError
        file = open(fileName, "r")
        input = json.load(file)
        person = input['person']
        basePrice = input['basePrice']
        event = input['event']
        eventDate = input['eventDate']
        student = False
        if 'student' in input:
            student = input['student']
        file.close()
        return RegularTicket.generateTicket(person, event, eventDate, basePrice, student)

    def generateTicket(person, event, eventDate, basePrice, student=False):
        if (
            not isinstance(eventDate, str)
            and not isinstance(event, str)
            and not isinstance(basePrice, int)
            and not isinstance(person, str)
            and not isinstance(student, bool)
        ):
            raise TypeError("Incorrect type")
        daysToIvent = RegularTicket.daysToEvent(eventDate)
        if student:
            return StudentTicket(person, event, basePrice, eventDate)
        elif daysToIvent > DAYS_FOR_ADVANCE_TICKET:
            return AdvanceTicket(person, event, basePrice, eventDate)
        elif daysToIvent < DAYS_FOR_LATE_TICKET:
            return LateTicket(person, event, basePrice, eventDate)
        else:
            return RegularTicket(person, event, basePrice, eventDate)

    def generateNumber(self):
        currentTime = datetime.now()
        year = currentTime.year
        month = currentTime.month
        day = currentTime.day
        hour = currentTime.hour
        minut = currentTime.minute
        sec = currentTime.second
        mcsec = currentTime.microsecond
        time.sleep(0.001)
        return f"{year}-{month}-{day}-{hour}-{minut}-{sec}-{mcsec}"

    def daysToEvent(eventDate):
        try:
            d1 = datetime.now()
            d2 = datetime.strptime(eventDate, "%d.%m.%Y")
        except:
            raise ValueError("Invalid  format of date")
        days = (d2 - d1).days
        if days < 0:
            raise ValueError("Invalid date")
        else:
            return days

    def __str__(self):
        return f"{self.number}\n{self.person}\nevent: {self.event}\ntotal price: {round(self.price)}"


class AdvanceTicket(RegularTicket):
    def __init__(self, person, event, price, eventDate):
        super().__init__(person, event, price, eventDate)
    
    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        self.__price = price * COEFFICIENT_FOR_ADVANCE

class LateTicket(RegularTicket):
    def __init__(self, person, event, price, eventDate):
        super().__init__(person, event, price, eventDate)
    
    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        self.__price = price * COEFFICIENT_FOR_LATE


class StudentTicket(RegularTicket):
    def __init__(self, person, event, price, eventDate):
        super().__init__(person, event, price, eventDate)
    
    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        self.__price = price * COEFFICIENT_FOR_STUDENT

def main():
    print(RegularTicket.createTicket("ticketDto.json"))
    #print(RegularTicket.getTicket('2021-11-12-18-39-20-130286'))

main()