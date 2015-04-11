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
    weight1 = {"West": 20, "East": 1, "South": 1, "North": 1, "Linde": 1, "Case": 1}
    student1 = Student(1, None, weight1, "Noe")
    listStudents.append(student1)
    
    weight2 = {"West": 6, "East": 15, "South": 1, "North": 1, "Linde": 1, "Case": 1}
    student2 = Student(1, None, weight2, "Eduardo")
    listStudents.append(student2)
    
    weight3 = {"West": 5, "East": 12, "South": 3, "North": 1, "Linde": 2, "Case": 2}
    student3 = Student(2, "Hobert", weight3, "Isaiah")
    listStudents.append(student3)
    student4 = Student(2, "Isaiah", weight3, "Hobert")
    listStudents.append(student4)
    
    weight5 = {"West": 9, "East": 10, "South": 1, "North": 2, "Linde": 2, "Case": 1}
    student5 = Student (1, None, weight5,"Joseph")
    listStudents.append(student5)
    
    weight6 = {"West": 10, "East": 1, "South": 3, "North": 9, "Linde": 1, "Case": 1}
    student6 = Student(1, None, weight6, "Federico")
    listStudents.append(student6)
    
    weight7 = {"West": 13, "East": 5, "South": 1, "North": 2, "Linde": 2, "Case": 2}
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
    
    for i in range(len(numWantSingleL)):
        numWantSingleL[i].setRoomType(2)
        listDoubles.append(numWantSingleL[i])
   
    for i in range(0, len(listStudents)):
        if listStudents[i].getRoomType() == 2:
            listDoubles.append(listStudents[i]) 
            
    listDoubles = pairSingles(listDoubles)
    
    assign(listSingles)
    assign(listDoubles)
            
def pairSingles(doubles):
    for i in range(len(doubles)):
        if doubles[i].getRoomMate() == None:
            for j in range(i, len(doubles)):
                if doubles[j].getRoomMate() == None:
                    doubles[i].setRoomMate(doubles[j])
                    doubles[j].setRoomMate(doubles[i])
    return doubles

def assign(students):
    m = Matrix(students, dorms)
    result = m.optimize()
    for pairing in result:
        print pairing[0], pairing[1]
    
if __name__ == '__main__':
    initStudents()
    start()
    
    