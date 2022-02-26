#vet = [1]*5
#print(vet)

#n= 90
#val = 16.8
#print("n=%d, val=%f" % (n,val));

vet = [] 
print (type(vet))
print (dir(vet))

vet.append(2)
vet.append(9)
vet.append(17)
# vet[1] = 12
#a.insert(posicao, elemento)

print()
print(vet)
print(vet[0])
print(vet[1])
print(vet[2])
#print(vet[3])
print(vet[1] * 10)
 
print()
print(len(vet), '\n')

i = 0
for x in vet:
  print('1a impressao => ', vet[i], x)
  i+=1

print()
  
for x in range(len(vet)):
  print('2a impressao => ', vet[x], x)

print('\n')

vetor=list(range(5))
for i in range(0,5):
   vetor[i] = 1  

for x in vetor:
  print(x)