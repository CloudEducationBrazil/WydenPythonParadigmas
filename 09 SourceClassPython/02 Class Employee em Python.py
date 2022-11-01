class Employee:
    def __init__(self, id, name):
        self.id = id;
        self.name = name;
    def display(self):
        print("Id: %d \n Name: %s" %(self.id, self.name))
emp1 = Employee(1, 'Julia')
emp2 = Employee(2, 'Josy')

emp1.display()
emp2.display