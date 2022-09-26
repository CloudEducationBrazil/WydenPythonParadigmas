dicAlu = [ {'nome': 'Julia', 'idade':17, 'disciplina':['java', 'python'], 'altura':1.5},
           {'nome': 'Rita', 'idade':21, 'disciplina':['c', 'php'], 'altura':1.8}]

print(dicAlu[0])
dicAlu[0]['nome'] = 'rita'
print(dicAlu[0]['nome'])
print(dicAlu[0]['disciplina'][1])
print(dicAlu)

print()
for i in range(len(dicAlu)):
  for key in dicAlu[i].values():
       print(key, end = ' ')
  print()