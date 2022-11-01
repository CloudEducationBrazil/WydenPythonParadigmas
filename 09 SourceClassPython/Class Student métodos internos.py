# https://www.javatpoint.com/python-constructors
# métodos da Classe: get(accessor-acesso); set(mutator-modificadores); show
class Student:
    def __init__(self, id, name, age):
        self.id = id;
        self.__name = name;
        self.age = age;
        
    def getName(self):
        return self.__name
        
    def setName(self, name):
        self.__name = name

    def show(self):
        #print("Id: %d \n Name:%s Idade:%d"%(self.id, self.__name, self.age));
        print("Id: ", self.id, " Name:", self.__name, " Idade:", self.age);

student = Student(1, 'Julia', 17)

# métodos da classe
print(student.getName())
student.setName('Julia Cardoso')
student.show()