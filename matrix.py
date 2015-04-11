class Matrix:
    def __init__(self, students, dorms):
        maxVal = max([student.firstChoice()[1] for student in students])
        
        roomType = students[0].getRoomType()
        rooms = []
        for dorm in dorms:
            rooms += dorm.emptyRooms(roomType)
            
        self.data_ = [[maxVal - student.getWeight(room.getDormName()) for room in rooms] for student in students]
        
        print self.numRooms()
        print self.numStudents()
        
        if len(students) < len(rooms):
            numExtraRows = len(rooms) - len(students)
            extraRow = [0] * len(rooms)
            self.data_ += [extraRow]*numExtraRows
            
        print self.numRooms()
        print self.numStudents()
            
        if len(rooms) < len(students):
            numExtraCols = len(students) - len(rooms)
            for row in self.data_:
                row += [0] * numExtraCols
                
        assert(self.numRooms() == self.numStudents())
            
        #0 represents neutral, 1 prime, 2 star
        #-1 represents a number that is not a zero
        self.zeros_ = [[0]*self.numRooms()] * self.numStudents()
        for row in range(len(self.zeros_)):
            for col in range(len(self.zeros_[row])):
                if self.data_[row][col] != 0:
                    self.zeros_[row][col] = -1
                    
        #False represents uncovered, True covered
        self.coveredRows_ = [False]*self.numStudents()
        self.coveredCols_ = [False]*self.numRooms()
        
    def numRooms(self):
        return len(self.data_[0])
    
    def numStudents(self):
        return len(self.data_)
    
    def minInRow(self, row):
        assert(row < self.numStudents())
        
        return min(self.data_[row])
    
    def minInCol(self, col):
        assert(col < self.numRooms())
        
        return min([row[col] for row in self.data_])
    
    def subtractFromRow(self, row, n):
        for val in self.data_[row]:
            val -= n
            
        self.updateZeros()
            
    def subtractFromCol(self, col, n):
        for row in self.data_:
            row[col] -= n
            
        self.updateZeros()
            
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
        
    def getCoveredRows(self):
        return self.coveredRows_
        
    def getCoveredCols(self):
        return self.coveredCols_
        
    def minXRowUnXColumns(self):
        mins = []
        for row in range(self.numStudents()):
            for col in range(self.numRooms()):
                if self.coveredRows_[row] and not self.coveredCols_[col]:
                    mins.append(self.data_[row][col])
                
        return min(mins)
        
    def updateZeros(self):
        for row in range(self.numStudents()):
            for col in range(self.numRooms()):
                if self.data_[row][col] == 0:
                    self.zeros_[row][col] == 0
                else :
                    self.zeros_[row][col] == -1
                

    def findPrimedZeros(self, row):
        col_index = []
        for i in range(len(self.data_[row])):
            if self.zeros_[row][i] == 1:
                col_index += [i]
        return col_index
        
    def findStarredZeros(self, column):
        row_index = []
        for row in range(len(self.data_)):
            if self.zeros_[row][column] == 2:
                row_index += [row]
        return row_index

    def indicesOfStarZerosInRow(self, rowNum):
        colInd = []
        for i in range(len(self.data[rowNum])):
            if self.data[rowNum][i] == 2:
                colInd.append(i)
        return colInd 

    def __str__(self):
        return self.data_.__str__()