from Student import Student
from Dorm import Dorm
from matrix import Matrix
import random

dorms = []
students = []

NUMDORMS = 4
NUMSINGLES = 1
NUMDOUBLES = 0
ROOMSPERDORM = NUMSINGLES + NUMDOUBLES
NUMSTUDENTS = NUMDORMS * (NUMSINGLES + NUMDOUBLES * 2)

def initDorms():
    for dorm in range(NUMDORMS):
        dorms.append(Dorm(NUMSINGLES, NUMDOUBLES, dorm*" "))
        
def initStudents():
    weights1 = {'':1, ' ':19, '  ':3, '   ':1}
    stud1 = Student(1, None, weights1, 'a')
    students.append(stud1)
    
    weights2 = {'':11, ' ':18, '  ':6, '   ':20}
    stud2 = Student(1, None, weights2, 'b')
    students.append(stud2)
    
    weights3 = {'':6, ' ':3, '  ':2, '   ':15}
    stud3 = Student(1, None, weights3, 'c')
    students.append(stud3)
    
if __name__ == '__main__':
    initDorms()
    initStudents()
    for dorm in dorms:
        #print dorm.totalUtil()
        pass
    
    singles = [student for student in students if student.getRoomType() == 1]
    m = Matrix(singles, dorms)
    print m.optimize()
