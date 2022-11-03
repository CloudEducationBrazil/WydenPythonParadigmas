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

lista = []

for x in range(3):
    id = int(input("Matrícula: "))
    nome = input("Nome: ")
    idade = int(input("Idade: "))

    student = Student(id, nome, idade)
    lista.append(student)
    
print()
print(lista)    
for reg in lista:
    #print(reg.getName())
    print()
    reg.show()
