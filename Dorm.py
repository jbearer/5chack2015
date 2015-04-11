from Room import *

class Dorm:
    def __init__ (self, listRooms):
        self.listRooms_ = listRooms
    
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