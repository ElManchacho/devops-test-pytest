import atexit
from script.cacheFlush import cacheFlush
from script.customclass.cacheFlushClass import cacheFlushClass
from script.customclass.RoomClass import *

if __name__ == "__main__":

    atexit.register(cacheFlush)

    atexit.register(cacheFlushClass)

    newRoom = Room(5,2,4)

    print(newRoom.isAvailable())

    print(newRoom.makeReservation(2))

    print(newRoom.getPeople())

    newRoom.endReservation()