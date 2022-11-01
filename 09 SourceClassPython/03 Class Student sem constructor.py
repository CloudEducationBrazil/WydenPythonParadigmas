# Classe sem constructor
class Student:
    def __init__(self):
        pass
    def show(self, name):
        print("Hello", name);

student = Student()
student.show('Julia')