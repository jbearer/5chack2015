from Student import Student
from Dorm import Dorm
from matrix import Matrix
import random

dorms = []
students = []

NUMDORMS = 2
NUMSINGLES = 3
NUMDOUBLES = 3
ROOMSPERDORM = NUMSINGLES + NUMDOUBLES
NUMSTUDENTS = NUMDORMS * (NUMSINGLES + NUMDOUBLES * 2)

def initDorms():
    for dorm in range(NUMDORMS):
        dorms.append(Dorm(NUMSINGLES, NUMDOUBLES, dorm*" "))
        
def initStudents():
    for student in range(NUMDORMS * NUMSINGLES - 1):
        weights = {}
        for dorm in dorms:
            weights[dorm.name()] = random.random()
        stud = Student(1, None, weights)
        students.append(stud)
        
        assignedDorm = dorms[random.randrange(0,len(dorms))]
        while (assignedDorm.existsEmptyRoom(1) == False):
            assignedDorm = dorms[random.randrange(0,len(dorms))]
    
        listRooms = assignedDorm.getListRooms()
        room = listRooms[random.randrange(0,NUMSINGLES)]
        while room.full() == True:
            room = listRooms[random.randrange(0,NUMSINGLES)]
        #room.addStudent(stud)
      
    for student in range(NUMDORMS * NUMDOUBLES):
        weights = {}
        for dorm in dorms:
            weights[dorm.name()] = random.random()
        stud = Student(2, None, weights)
        students.append(stud)
        
        assignedDorm = dorms[random.randrange(0,len(dorms))]
        while (assignedDorm.existsEmptyRoom(2) == False):
            assignedDorm = dorms[random.randrange(0,len(dorms))]
    
        listRooms = assignedDorm.getListRooms()
        room = listRooms[random.randrange(NUMSINGLES,len(listRooms))]
        while room.full() == True:
            room = listRooms[random.randrange(NUMSINGLES, len(listRooms))]
        #room.addStudent(stud)
    
if __name__ == '__main__':
    initDorms()
    initStudents()
    for dorm in dorms:
        print dorm.totalUtil()
    
    singles = [student for student in students if student.getRoomType() == 1]
    #m = Matrix(singles, dorms)
