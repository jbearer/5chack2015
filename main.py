from Student import Student
from Dorm import Dorm
import random

dorms = []
students = []

NUMDORMS = 2
ROOMSPERDORM = 6
NUMSTUDENTS = NUMDORMS * ROOMSPERDORM * 1.5

def initDorms():
    for dorm in range(NUMDORMS):
        dorms.append(Dorm(ROOMSPERDORM / 2,ROOMSPERDORM / 2, dorm*" "))
        
def initStudents():
    for student in range(NUMDORMS * ROOMSPERDORM / 2):
        weights = {}
        for dorm in dorms:
            weights[dorm.name()] = random.random()
        students.append(Student(1, None, weights))
    dorms[0].getListRooms()[0].addStudent(students[0])
    dorms[0].getListRooms()[1].addStudent(students[1])

if __name__ == '__main__':
    initDorms()
    initStudents()
    print sum([dorm.totalUtil() for dorm in dorms])