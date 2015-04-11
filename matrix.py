class Matrix:
    def __init__(self, students, dorms):
        
        maxVal = max([student.firstChoice()[1] for student in students])
        
        roomType = students[0].getRoomType()
        rooms = []
        for dorm in dorms:
            rooms += dorm.emptyRooms(roomType)
            
        self.students_ = students
        self.rooms_ = rooms
            
        #self.data_ = [[maxVal - student.getWeight(room.getDormName()) for room in rooms] for student in students]
        self.data_ = [[student.getWeight(room.getDormName()) for room in rooms] for student in students]
        
        if len(students) < len(rooms):
            numExtraRows = len(rooms) - len(students)
            
            extraRow = []
            for i in range(len(rooms)):
                extraRow += [0]
            
            for i in range(numExtraRows):
                self.data_+= [extraRow]
                
        assert(self.numRooms() == self.numStudents())
            
        #0 represents neutral, 1 prime, 2 star
        #-1 represents a number that is not a zero
        self.zeros_ = []
        for student in range(self.numStudents()):
            row = []
            for room in range(self.numRooms()):
                row += [0]
                
            self.zeros_ += [row]
            
        for row in range(len(self.zeros_)):
            for col in range(len(self.zeros_[row])):
                if self.data_[row][col] != 0:
                    self.zeros_[row][col] = -1
                    
        #False represents uncovered, True covered
        self.coveredRows_ = []
        for i in range(self.numStudents()):
            self.coveredRows_ += [False]
            
        self.coveredCols_ = []
        for i in range(self.numRooms()):
            self.coveredCols_ += [False]
        
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
        for col in range(self.numRooms()):
            self.data_[row][col] += -1*n
            
        self.updateZeros()
            
    def subtractFromCol(self, col, n):
        for row in range(self.numStudents()):
            self.data_[row][col] += -1*n
            
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
        
    def minXRowXColumns(self):
        mins = []
        for row in range(self.numStudents()):
            for col in range(self.numRooms()):
                if not self.coveredRows_[row] and not self.coveredCols_[col]:
                    mins.append(self.data_[row][col])
                
        return min(mins)
        
    def updateZeros(self):
        for row in range(self.numStudents()):
            for col in range(self.numRooms()):
                if self.data_[row][col] == 0:
                    self.zeros_[row][col] = 0
                elif self.data_[row][col] != 0:
                    self.zeros_[row][col] = -1
                

    def findPrimedZerosInRow(self, row):
        col_index = []
        for i in range(len(self.data_[row])):
            if self.zeros_[row][i] == 1:
                col_index += [i]
        return col_index
        
    def findUnprimedZerosInRow(self, row):
        col_index = []
        for i in range(len(self.data_[row])):
            if self.zeros_[row][i] == 0:
                col_index += [i]
        return col_index
        
    def findStarredZerosInCol(self, column):
        row_index = []
        for row in range(len(self.data_)):
            if self.zeros_[row][column] == 2:
                row_index += [row]
        return row_index
        
    def findStarredZerosInRow(self, row):
        col_index = []
        for col in range(self.numRooms()):
            if self.zeros_[row][col] == 2:
                col_index += [col]
        return col_index

    def findPrimedZerosInCol(self, rowNum):
        colInd = []
        for i in range(len(self.data[rowNum])):
            if self.data[rowNum][i] == 2:
                colInd.append(i)
        return colInd
        
    def optimize(self):
        for row in range(len(self.data_)):
            minVal = self.minInRow(row)
            self.subtractFromRow(row, minVal)
            
        return self.step2()
            
    def step2(self):
        for col in range(self.numRooms()):
            minVal = self.minInCol(col)
            self.subtractFromCol(col, minVal)
        return self.starAllZeros()
      
    '''def step3(self):
        carryon = True
        while(carryon == True):
            for row in range(self.numStudents()):
                unprimed = self.findUnprimedZerosInRow(row)
                if unprimed != []:
                    col = unprimed[0]
                    self.primeAllZerosInColumn(col)
                    self.primeAllZerosInRow(row)
                    self.starZero(row, col)
            if self.isDone():
                ret = []
                for student in range(len(self.students_)):
                    for room in range(self.numRooms()):
                        if self.isStarred(student, room):
                            ret.append((self.students_[student], self.rooms_[room]))
                return ret
            else:
                self.step4()
                self.step5()
            #carryon = False
                
    def step4(self):
        for row in range(self.numStudents()):
            starred = self.findStarredZerosInRow(row)
            if not starred:
                self.step5()
                self.coverRow(row)
                cols = self.findPrimedZerosInRow(row)
                for col in cols:
                    self.coverCol(col)
                    """rowsToMark = self.findStarredZerosInCol(col)
                    for rowToMark in rowsToMark:
                        self.coverRow(rowToMark)"""
      
    def step5(self):
        mini = self.minXRowUnXColumns()
        
        for i in range(len(self.data_)):
            if self.getCoveredRows()[i]:
                for j in range(len(self.data_[i])):
                    self.data_[i][j] += -1*mini
        
        for i in range(len(self.data_[0])):
            if self.getCoveredCols()[i]:
                for j in range(len(self.data_)):
                    self.data_[j][i] += mini
        
        self.updateZeros()'''
    def starAllZeros(self):
        for row in range(self.numStudents()):
            for col in range(self.numRooms()):
                if self.data_[row][col] == 0:
                    rowStars = self.findStarredZerosInRow(row)
                    colStars = self.findStarredZerosInCol(col)
                    if not rowStars and not colStars:
                        self.starZero(row, col)
                        
        return self.coverColumns()
                        
    def coverColumns(self):
        for col in range(self.numRooms()):
            if self.findStarredZerosInCol(col):
                self.coverCol(col)
        if self.isDone():
            ret = []
            for student in range(len(self.students_)):
                for room in range(self.numRooms()):
                    if self.isStarred(student, room):
                        ret.append((self.students_[student], self.rooms_[room]))
            return ret
        else:
            return self.primeAndCover()
            
    def primeAndCover(self):
        row = 0
        while row in range(self.numStudents()):
            col = 0
            while col in range(self.numRooms()):
                if self.data_[row][col] == 0:
                    if not self.isCovered(row,col):
                        self.primeZero(row, col)
                        starCol = self.findStarredZerosInRow(row)
                        if starCol:
                            self.coverRow(row)
                            self.uncoverCol(starCol[0])
                            row = 0
                            col = 0
                        else:
                            return self.sequence(row, col)
                col += 1
            row += 1
        #all covered
        return self.subtractMin()
        
    def sequence(self, row, col):
        primes = [(row, col)]
        stars = []
        colStars = self.findStarredZerosInCol(col)
        while colStars:
              stars.append((colStars[0], col))
              nextPrime = self.findPrimedZerosInRow(colStars[0])[0]
              primes.append((colStars[0], nextPrime))  
              colStars = self.findStarredZerosInCol(nextPrime)
        for zero in stars:
            self.makeNeutralZero(zero[0], zero[1])
        for zero in primes:
            self.starZero(zero[0], zero[1])
        for row in range(self.numStudents()):
            for col in range(self.numRooms()):
                if self.zeros_[row][col] == 1:
                    self.zeros_[row][col] = 0
        for row in range(self.numStudents()):
            self.uncoverRow(row)
        for col in range(self.numRooms()):
            self.uncoverCol(col)
        return self.coverColumns()
        
    def subtractMin(self):
        mini = self.minXRowXColumns()
        
        for i in range(len(self.data_)):
            if self.getCoveredRows()[i]:
                for j in range(len(self.data_[i])):
                    self.data_[i][j] += mini
        
        for i in range(len(self.data_[0])):
            if not self.getCoveredCols()[i]:
                for j in range(len(self.data_)):
                    self.data_[j][i] += -1 * mini
        
        self.updateZeros()
        return self.primeAndCover()
                        
        
    def primeAllZerosInColumn(self, col):
        for row in range(self.numStudents()):
            if self.isNeutral(row, col):
                self.primeZero(row, col)
                
    def primeAllZerosInRow(self, row):
        for col in range(self.numRooms()):
            if self.isNeutral(row, col):
                self.primeZero(row, col)
                
    def isDone (self) :
        for col in range(self.numRooms()):
            if self.findStarredZerosInCol(col) == []:
                return False
        return True

    def __str__(self):
        return self.data_.__str__()
