class Super:
    def soma(self, x, y):
        return x + y


class Sub(Super):
    def soma2(self, x, y, z):
        return x + y + z


print(Sub().soma(2, 3))
print(Sub().soma2(2, 3, 9))


class Super2:
    def hello(self):
        print("Olá, sou a superclasse!")


class Sub2 (Super2):
    def hello(self):
        print("Olá, sou a subclasse!")


class Subsub (Sub2):
    def hello(self):
        print("Olá, sou a subsubclasse!")


teste = Subsub()
teste.hello()
