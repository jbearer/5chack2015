from Student import Student
from Dorm import Dorm
from matrix import Matrix
import random

dorms = []
students = []

NUMDORMS = 6
NUMSINGLES = 1
NUMDOUBLES = 0
ROOMSPERDORM = NUMSINGLES + NUMDOUBLES
NUMSTUDENTS = NUMDORMS * (NUMSINGLES + NUMDOUBLES * 2)

def initDorms():
    global dorms
    West = Dorm(1,0,'West')
    East = Dorm(1,0,'East')
    North = Dorm(1,0,'North')
    South = Dorm(1,0,'South')
    Case = Dorm(1,0,'Case')
    Linde = Dorm(1,0,'Linde')
    dorms += [West, East, North, South, Case, Linde]
        
def initStudents():
    weights1 = {'West': 6, 'East': 10, 'North': 4, 'South': 8, 'Case': 1, 'Linde':7}
    stud1 = Student(1, None, weights1, 'A')
    students.append(stud1)
    
    weights2 = {'West': 1, 'East': 9, 'North': 7, 'South': 20, 'Case': 1, 'Linde':17}
    stud2 = Student(1, None, weights2, 'B')
    students.append(stud2)
    
    weights3 = {'West': 13, 'East': 5, 'North': 20, 'South': 15, 'Case': 7, 'Linde':5}
    stud3 = Student(1, None, weights3, 'C')
    students.append(stud3)
    
    weights4 = {'West': 19, 'East': 19, 'North': 1, 'South': 3, 'Case': 14, 'Linde':20}
    stud4 = Student(1, None, weights4, 'D')
    students.append(stud4)
    
    weights5 = {'West': 13, 'East': 7, 'North': 2, 'South': 20, 'Case': 4, 'Linde':8}
    stud5 = Student(1, None, weights5, 'E')
    students.append(stud5)
    
    weights6 = {'West': 3, 'East': 5, 'North': 18, 'South': 8, 'Case': 12, 'Linde':13}
    stud6 = Student(1, None, weights6, 'F')
    students.append(stud6)
    
if __name__ == '__main__':
    initDorms()
    initStudents()
    for dorm in dorms:
        #print dorm.totalUtil()
        pass
    
    singles = [student for student in students if student.getRoomType() == 1]
    m = Matrix(singles, dorms)
    result = m.optimize()
    for pairing in result:
        print pairing[0], pairing[1]
