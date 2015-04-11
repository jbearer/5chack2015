
class Room:
    def __init__(self):
        self.students_ = []
        self.capacity_ = None
        
    def __init__(self, capacity, students, dorm):
        self.capacity_ = capacity
        self.dorm_ = dorm
        
        assert(self.capacity_ >= len(students))
        
        self.students_ = students
        
    def getStudents(self):
        return self.students_
        
    def getDormName(self):
        return self.dorm_
    
    def roomType(self):
        return self.capacity_
    
    def occupancy(self):
        return len(self.students_)
    
    def full(self):
        return len(self.students_) == self.capacity_
    
    def addStudent(self, student):
        assert(len(self.students_) < self.capacity_)
        self.students_.append(student)