
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
                
        #0 represents neutral, 1 prime, 2 star
        #-1 represents a number that is not a zero
        self.zeros_ = [[0]*self.numDorms()] * self.numStudents()
        for row in self.zeros_:
            for col in row:
                if self.data_[row][col] != 0:
                    self.zeros_[row][col] = -1
                    
        #False represents uncovered, True covered
        self.coveredRows_ = [False]*self.numStudents()
        self.coveredCols_ = [False]*self.numDorms()
        
    def numDorms(self):
        return len(self.data_[0])
    
    def numStudents(self):
        return len(self.data_)
    
    def minInRow(self, row):
        assert(row < self.numStudents())
        
        return min(self.data_[row])
    
    def minInCol(self, col):
        assert(col < self.numDorms())
        
        return min([row[col] for row in self.data_])
    
    def subtractFromRow(self, row, n):
        for val in self.data_[row]:
            val -= n
            
    def subtractFromCol(self, col, n):
        for row in self.data_:
            row[col] -= n
            
    def makeNeutralZero(self, row, col):
        assert(self.zeros_[row][col] != -1)
        
        self.zeros_[row][col] = 0
            
    def primeZero(self, row, col):
        assert(self.zeros_[row][col] != -1)
        
        self.zeros_[row][col] = 1
    
    def starZero(self, row, col):
        assert(self.zeros_[row][col] != -1)
        
        self.zeros_[row][col] = 2
        
    def isNeutral(self, row, col):
        return self.zeros_[row][col] == 0
    
    def isPrime(self, row, col):
        return self.zeros_[row][col] == 1
    
    def isStarred(self, row, col):
        return self.zeros_[row][col] == 2
    
    def coverRow(self, row):
        self.coveredRows_[row] = True
        
    def uncoverRow(self, row):
        self.coveredRows_[row] = False
    
    def coverCol(self, col):
        self.coveredCols_[col] = True
        
    def uncoverCol(self, col):
        self.coveredCols_[col] = False
        
    def isCovered(self, row, col):
        return self.coveredRows_[row] or self.coveredCols_[col]
        
    def getZeros(self):
        return self.zeros_
        
    def getCoveredRows_(self):
        return self.coveredRows_
        
    def getCoveredCols_(self):
        return self.coveredCols_

    def __str__(self):
        return self.data_.__str__()