from Room import Room

class Dorm:
    def __init__ (self, numSingles, numDoubles, name):
        self.numSingles_ = numSingles
        self.numDoubles_ = numDoubles
        
        self.listRooms_ = []
        for i in range(numSingles):
            self.listRooms_.append(Room(1, [], name))
        for i in range(numDoubles):
            self.listRooms_.append(Room(2, [], name))
            
        self.numRooms_ = len(self.listRooms_)
        self.name_ = name
    
    def getListRooms(self):
        return self.listRooms_
    
    def existsEmptyRoom (self, num):
        for i in range(len(self.listRooms_)):
            if self.listRooms_[i].roomType() == num:
                if self.listRooms_[i].occupancy() == 0:
                    return True
        return False
                
    def emptyRooms(self, num):
        emptyRoomsL = []
        for i in range(len(self.listRooms_)):
            print self.listRooms_[i].roomType()
            print self.listRooms_[i].occupancy()
            if self.listRooms_[i].roomType() == num:
                if self.listRooms_[i].occupancy() == 0:
                    emptyRoomsL.append(self.listRooms_[i])
        return emptyRoomsL
    
    def fullRooms(self, num):
        fullRoomsL = []
        for i in range(len(self.listRooms_)):
            if self.listRooms_[i].RoomType() == num:
                if self.listRooms_[i].full() == True:
                    fullRoomsL.append(self.listRooms_[i])
        return fullRoomsL
        
    def name(self):
        return self.name_

    def totalUtil(self):
        totalVal = 0
        for i in range(self.numRooms_):
            for j in range(len(self.listRooms_[i].getStudents())):
                totalVal = totalVal + self.listRooms_[i].getStudents()[j].getWeight(self.name_)
        return totalVal