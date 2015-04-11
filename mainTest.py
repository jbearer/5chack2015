from Student import Student
from Dorm import Dorm
from matrix import Matrix
import random

students = []
dorms = []
NUMDORMS = 6
NUMSINGLES = 3
NUMDOUBLES = 2
ROOMSPERDORM = NUMSINGLES + NUMDOUBLES
NUMSTUDENTS = NUMDORMS * (NUMSINGLES + NUMDOUBLES * 2)

def start():
    dormWest = Dorm(1, 1, "West")
    dormNorth = Dorm(1, 1, "North")
    dormEast = Dorm(1, 1, "East")
    dormSouth = Dorm(1, 1, "South")
    dormLinde = Dorm(1, 1, "Linde")
    dormCase = Dorm(1, 1, "Case")
    dorms.append(dormWest)
    dorms.append(dormNorth)
    dorms.append(dormEast)
    dorms.append(dormSouth)
    dorms.append(dormLinde)
    dorms.append(dormCase)

def initStudents():
    listStudents = []
    weight1 = {"West": 20, "East": 1, "South": 1, "North": 1, "Linde": 1, "Case": 1}
    student1 = Student(1, "Noe", None, weight1)
    listStudents.append(student1)
    
    weight2 = {"West": 6, "East": 15, "South": 1, "North": 1, "Linde": 1, "Case": 1}
    student2 = Student(1, "Eduardo", None, weight2)
    listStudents.append(student2)
    
    weight3 = {"West": 5, "East": 12, "South": 3, "North": 1, "Linde": 2, "Case": 2}
    student3 = Student(2, "Isaiah", "Hobert", weight3)
    listStudents.append(student3)
    student4 = Student(2, "Hobert", "Isaiah", weight3)
    listStudents.append(student4)
    
    weight5 = {"West": 9, "East": 10, "South": 1, "North": 2, "Linde": 2, "Case": 1}
    student5 = Student (1, "Joseph", None, weight5)
    listStudents.append(student5)
    
    weight6 = {"West": 10, "East": 1, "South": 3, "North": 9, "Linde": 1, "Case": 1}
    student6 = Student(1, "Federico", None, weight6)
    listStudents.append(student6)
    
    weight7 = {"West": 13, "East": 5, "South": 1, "North": 2, "Linde": 2, "Case": 2}
    student7 = Student (1, "Edmundo", None, weight7)
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
        listDoubles.append(numWantSingleL[i])
   
    for i in range(0, len(listStudents)):
        if listStudents[i].getRoomType() == 2:
            listDoubles.append(listStudents[i]) 
    
if __name__ == '__main__':
    initStudents()
    start()
    
    """for dorm in dorms:
        print dorm.totalUtil()
    
    singles = [student for student in self.students if student.getRoomType() == 1]
    m = Matrix(singles, self.dorms)
    print m.optimize() """
