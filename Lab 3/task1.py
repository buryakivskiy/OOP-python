from datetime import datetime
import os
import time
import json


class RegularTicket:
    def __init__(self, person, event, price, eventDate):
        self.number = self.generateNumber()
        self.person = person
        self.event = event
        self.price = price
        self.eventDate = eventDate
        self.writeTicket()
    
    def writeTicket(self):
        file = open(self.number + '.json', 'w')
        json.dump(self.__dict__, file, indent=2)
        file.close()
    
    def getTicket(fileName):
        if not os.path.exists(fileName + '.json'):
            raise FileNotFoundError
        file = open(fileName + '.json', "r")
        input = json.load(file)
        person = input['person']
        price = input['price']
        event = input['event']
        eventDate = input['eventDate']
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
        if student == True:
            return StudentTicket(person, event, basePrice, eventDate)
        elif RegularTicket.daysToEvent(eventDate) > 60:
            return AdvanceTicket(person, event, basePrice, eventDate)
        else:
            return LateTicket(person, event, basePrice, eventDate)

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
        super().__init__(person, event, price * 0.6, eventDate)


class LateTicket(RegularTicket):
    def __init__(self, person, event, price, eventDate):
        super().__init__(person, event, price * 1.1, eventDate)


class StudentTicket(RegularTicket):
    def __init__(self, person, event, price, eventDate):
        super().__init__(person, event, price * 0.5, eventDate)

def main():
    RegularTicket.createTicket("ticketDto.json")
    #print(RegularTicket.getTicket('2021-11-11-0-56-53-754854'))

main()