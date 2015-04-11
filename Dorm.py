from Room import *

class Dorm:
    def __init__ (self, numSingles, numDoubles, name):
        self.numSingles_ = numSingles
        self.numDoubles_ = numDoubles
        
        self.listRooms_ = []
        for i in range(numSingles):
            listRooms.append(Room(1))
        for i in range(numDoubles):
            listRooms.append(Room(2))
            
        self.numRooms_ = len(listRooms_)
        self.name_ = name
    
    def existsEmptyRoom (self, num):
        for i in range(len(self.listRooms_)):
            if i.roomType() == num:
                if i.occupancy() == 0:
                    return True
        return False
                
    def emptyRooms(self, num):
        emptyRoomsL = []
        for i in range(len(self.listRooms_)):
            if i.RoomType() == num:
                if i.occupancy() == 0:
                    emptyRoomsL.append(i)
        return emptyRoomsL
    
    def fullRooms(self, num):
        fullRoomsL = []
        for i in range(len(self.listRooms_)):
            if i.RoomType() == num:
                if i.full() == True:
                    fullRoomsL.append(i)
        return fullRoomsL
        
    def name(self):
        return self.name_

    def totalUtil(self):
        totalVal = 0
        for i in range(numRooms_):
            for j in range(i.getStudents()):
                totalVal = totalVal + j.getWeight(name_)
        return totalVal