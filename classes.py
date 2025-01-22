# lst = []
# lst = [x for x in range(12 21):]
# print(lst)
'''
class Product:
    def __init__(self):
        self.name = 'Iphone'
        self.description = 'Its awesome'
        self.price = 700
p1 = Product()
p1.price = 400
print(p1.price)

class Course:
    def __init__(self, name, ratings):
        self.name = name
        self.ratings = ratings
        
        
c1 = Course('C++', 4.8)
print(c1.name)
print(c1.ratings)

'''

class Programmer:
    def setName(self, name):
        self.name = name
    def getName(self):
        return self.name
    def setSalary(self, salary):
        self.salary = salary
    def getSalary(self):
        return self.salary
    
p1 = Programmer()
p1.setName("Ashish")
p1.setSalary(100000)
print(p1.getName())
print(p1.getSalary())

class Student:
    major = 'CSE'
    
    def __init__(self, roll, name):
        self.rollno = roll
        self.name = name

    def __del__(self)
    	print("Destructor Invoked!")

s1 = Student(1, "ashish")
s2 = Student(2, "Vishwaraj")
print(s1.major)
print(s2.major)
print(s1.name)
print(s2.name)
print(Student.major)
