from numpy import void

class Room:

    roomNumber:int

    floor:int

    people:int = 0

    maxPeople:int

    availability:bool = True

    def __init__(self, roomNumber:int, floor:int, maxPeople:int):
        self.roomNumber = roomNumber
        self.floor = floor
        self.maxPeople = maxPeople

    def setPeople(self, people:int)->void:
        self.people = people

    def makeReservation(self, people:int)->bool:
        if people> self.maxPeople :
            return False
        else:    
            self.people = people
            self.availability = False
            return True

    def isAvailable(self)->bool:
        return self.availability

    def getPeople(self)->int:
        return self.people

    def endReservation(self)->void:
        self.people = 0
        self.availability = True
