from src.customclass.RoomClass import *

def test_roomCreation():
    newRoom = Room(5,2,4)

def test_roomReservation():
    newRoom = Room(5,2,4)

    assert newRoom.makeReservation(2) == True

def test_roomAvailabilityCheck():
    newRoom = Room(5,2,4)

    newRoom.makeReservation(2)

    assert newRoom.isAvailable() == False

def test_getPeople():
    
    newRoom = Room(5,2,4)

    newRoom.makeReservation(2)

    assert newRoom.getPeople() == 2

def test_endReservation():
    newRoom = Room(5,2,4)

    newRoom.makeReservation(2)

    newRoom.getPeople() == 2

    newRoom.endReservation()

    assert newRoom.isAvailable() == True