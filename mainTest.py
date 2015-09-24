from Student import Student
from Dorm import Dorm
from matrix import Matrix
import random

students = []
dorms = []
NUMDORMS = 6
NUMSINGLES = 1
NUMDOUBLES = 1
ROOMSPERDORM = NUMSINGLES + NUMDOUBLES
NUMSTUDENTS = NUMDORMS * (NUMSINGLES + NUMDOUBLES * 2)

def start():
    dormWest = Dorm(1, 1, "West")
    dormNorth = Dorm(1, 1, "North")
    dormEast = Dorm(1, 1, "East")
    dormSouth = Dorm(0, 1, "South")
    dormLinde = Dorm(0, 1, "Linde")
    dormCase = Dorm(0, 1, "Case")
    dorms.append(dormWest)
    dorms.append(dormNorth)
    dorms.append(dormEast)
    dorms.append(dormSouth)
    dorms.append(dormLinde)
    dorms.append(dormCase)

def initStudents():
    listStudents = []
    weight1 = {"West": 10, "East": 1, "South": 1, "North": 6, "Linde": 1, "Case": 6}
    student1 = Student(1, None, weight1, "Noe")
    listStudents.append(student1)
    
    weight2 = {"West": 6, "East": 7, "South": 1, "North": 1, "Linde": 1, "Case": 9}
    student2 = Student(1, None, weight2, "Eduardo")
    listStudents.append(student2)
    
    weight3 = {"West": 5, "East": 6, "South": 3, "North": 1, "Linde": 8, "Case": 2}
    student3 = Student(2, "Hobert", weight3, "Isaiah")
    listStudents.append(student3)
    
    student4 = Student(2, "Isaiah", weight3, "Hobert")
    listStudents.append(student4)
    
    weight5 = {"West": 7, "East": 5, "South": 6, "North": 4, "Linde": 2, "Case": 1}
    student5 = Student (1, None, weight5,"Joseph")
    listStudents.append(student5)
    
    weight6 = {"West": 2, "East": 1, "South": 3, "North": 9, "Linde": 9, "Case": 1}
    student6 = Student(1, None, weight6, "Federico")
    listStudents.append(student6)
    
    weight7 = {"West": 3, "East": 5, "South": 6, "North": 2, "Linde": 2, "Case": 7}
    student7 = Student (1, None, weight7, "Edmundo")
    listStudents.append(student7)
    
    numWantSingleL = []
    for i in range(len(listStudents)):
        if listStudents[i].getRoomType() == 1:
            numWantSingleL.append(listStudents[i])

    listSingles = []
    for i in range(NUMSINGLES):
        listSingles.append(numWantSingleL.pop(random.randrange(0,len(numWantSingleL))))

    listDoubles = []
    
    
    for i in range(0, len(listStudents)):
        if listStudents[i].getRoomType() == 2:
            listDoubles.append(listStudents[i]) 
            
    for i in range(len(numWantSingleL)):
        numWantSingleL[i].setRoomType(2)
        listDoubles.append(numWantSingleL[i])
            
    listDoubles = pairSingles(listDoubles)
    listDoubles = clearUp(listDoubles)
    
    
    assign(listSingles)
    assign(listDoubles)
            
def pairSingles(doubles):
    for i in range(len(doubles)):
        if doubles[i].getRoomMate() == None:
            for j in range(i+1, len(doubles)):
                if doubles[j].getRoomMate() == None:
                    doubles[i].setRoomMate(doubles[j].name_)
                    doubles[j].setRoomMate(doubles[i].name_)
    return doubles

def clearUp(listDoubles):
    i = 0
    while i < len(listDoubles)-1:
        name = listDoubles[i].roomMate_
        j = i + 1
        while j < len(listDoubles):
            if listDoubles[j].name_ == name:
                listDoubles.remove(listDoubles[j])
                j = len(listDoubles)
                i = -1
            j+=1
        i += 1
    return listDoubles
    
def assign(students):
    m = Matrix(students, dorms)
    result = m.optimize()
    for pairing in result:
        print pairing[0]
        #if pairing[0].roomMate_:
        #    print pairing[0].roomMate_
        print pairing[1]
        print ''
    
if __name__ == '__main__':
    
    start()
    initStudents()
    
    