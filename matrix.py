
class Matrix:
    def __init__(self, students, dorms):
        maxVal = max([max(student.weights()) for student in students])
        self.data_ = [[maxVal - student.weights()[dorm.name()] for dorm in dorms] for student in students]
        
        if len(students) < len(dorms):
            numExtraRows = len(dorms) - len(students)
            extraRow = [0] * len(dorms)
            self.data_ += extraRows*numExtraRows
            
        elif len(dorms) < len(students):
            numExtraCols = len(students) - len(dorms)
            for row in self.data_:
                row += [0] * numExtraCols
        
    def numDorms(self):
        return len(self.data_[0])
    
    def numStudents(self):
        return len(self.data_)
    
    def minInRow(self, row):
        assert(row < numStudents())
        
        return min(self.data_[row])
    
    def minInCol(self, col):
        assert(col < numDorms())
        
        return min([row[col] for row in self.data_])
    
    def subtractFromRow(self, row, n):
        for val in self.data_[row]:
            val -= n
            
    def subtractFromCol(self, col, n):
        for row in self.data_:
            row[col] -= n
            
    def __str__(self):
        return self.data_.__str__()