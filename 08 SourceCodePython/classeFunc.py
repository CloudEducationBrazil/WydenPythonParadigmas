class Funcionario:
    def __init__(self, nome, cargo, valor_hora_trabalhada):
        self.nome = nome  # public
        self.cargo = cargo  # public
        self.valor_hora_trabalhada = valor_hora_trabalhada  # public
        self.__horas_trabalhadas = 0  # private
        self.__salario = 0  # private

    @property
    def salario(self):  # pertence a class Funcionario
        return self.__salario

    @salario.setter
    def salario(self, novo_salario):  # pertence a class Funcionario
        raise ValueError(
            "Impossivel alterar salario diretamente. Use a funcao calcula_salario().")

    def registra_hora_trabalhada(self):
        self.__horas_trabalhadas += 1

    def calcula_salario(self):
        self.__salario = self.__horas_trabalhadas * self.valor_hora_trabalhada


juju = Funcionario('Julia', 'Digital Influencer', 180)
juju.registra_hora_trabalhada()
juju.registra_hora_trabalhada()
juju.registra_hora_trabalhada()
juju.registra_hora_trabalhada()
juju.registra_hora_trabalhada()
juju.calcula_salario()
print(juju.valor_hora_trabalhada)
juju.__salario = 700
print(juju.__salario)
print(juju.salario)
print(juju._Funcionario__salario)


class Numero:
    x = 5


print(Numero.x)

num = Numero()
print(num.x)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is " + self.name)


p2 = Person("John", 36)
del p2.age
p2.myfunc()
