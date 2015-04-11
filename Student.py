class Student:
    def __init__(self, roomType, roomMate, weight):
        self.roomType_ = roomType
        self.roomMate_ = roomMate
        self.weight_ = weight
    
    def getRoomType(self):
        return self.roomType_
    
    def getRoomMate(self):
        return self.roomMate_
        
    def getWeight(self, dorm):
        return self.weight_[dorm]
        
    def firstChoice(self):
        choice = ('', -1)
        for dorm in self.weight_.keys():
            if self.weight_[dorm] > choice[1]:
                choice = (dorm, self.weight_[dorm])
                
        return choice