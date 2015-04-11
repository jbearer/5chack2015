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