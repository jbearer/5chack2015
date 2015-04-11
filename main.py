import Student
import Dorm
import random

dorms = []
students = []

NUMDORMS = 2
ROOMSPERDORM = 6
NUMSTUDENTS = NUMDORMS * ROOMSPERDORM * 1.5

def initDorms():
    for dorm in range(NUMDORMS):
        dorms.append(Dorm(ROOMSPERDORM / 2,ROOMSPERDORM / 2))
        
def initStudents():
    for student in range(NUMDORMS * ROOMSPERDORM / 2):
        weights = {}
        for dorm in dorms:
            weights[dorm.name()] = random.random()
        students.append(Student(1, None, weights))

if __name__ = '__main__':
    return sum([dorm.totalUtility() for dorm in dorms])