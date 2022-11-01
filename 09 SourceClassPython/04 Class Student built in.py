# https://www.javatpoint.com/python-constructors
# in-built funções da classe: getattr; setattr; delattr, hasattr
class Student:
    def __init__(self, id, name, age):
        self.id = id;
        self.name = name;
        self.age = age;
        
    def show(self):
        #print("Id: %d \n Name:%s Idade:%d"%(self.id, self.name, self.age));
        print("Id: ", self.id, " Name:", self.name, " Idade:", self.age);

student = Student(1, 'Julia', 17)

# functions built in
print(getattr(student, 'name'))
setattr(student, 'name', 'Julia Cardoso')
print(hasattr(student, 'name'))

student.show()
delattr(student, 'age')
#student.show()

# in-built atributos da classe
print(student.__doc__)
print(student.__dict__)
print(student.__module__)
