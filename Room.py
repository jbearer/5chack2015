
class Room:
    def __init__(self):
        self.students_ = []
        self.numStudents_ = None
        
    def __init__(self, numStudents, students):
        self.numStudents_ = numStudents
        
        assert(self.numStudents_ >= len(students))
        
        self.students_ = students
        
    def getStudents(self):
        return self.students_
    
    def roomType(self):
        return self.numStudents_
    
    def occupancy(self):
        return len(self.students_)
    
    def full(self):
        return occupancy(self) == self.numStudents_
    
    def addStudent(self, student):
        assert(len(self.students_) < self.numStudents_)
        self.students_.append(student)
