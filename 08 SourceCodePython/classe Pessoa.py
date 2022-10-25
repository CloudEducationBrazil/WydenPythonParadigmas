class Aluno:
    def __init__(self, id, nome, idade):
        self.id = id,
        self.__nome = nome, # attr protected
        self.idade = idade

    def __str__(self):
        #return f'Dados:[{self.id}, {self.__nome}, {self.idade}]
        return '%s %s %s' % (self.id, self.idade, self.__nome)
        
    #@property
    def getNome(self):
        return self.__nome
    
    #@__nome.setter
    def setNome(self, nome):
        self.__nome = nome

a1 = Aluno(1, 'Julia', 17)
a2 = Aluno(2, 'Heleno Filho', 53)
a1.setNome('Julia Cardoso')

print (a1.getNome())
print (a1.idade)
print (a2)
