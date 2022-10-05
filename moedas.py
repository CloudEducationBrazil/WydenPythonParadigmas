num = float(input("valor: "))
subtotal= num
lista = []
cedula = [100, 50, 20, 10, 5, 2, 1, 0.50, 0.25, 0.10, 0.05, 0.009]
x = 0

while x < 12:
   troco = subtotal // cedula[x]
   lista.append(int(troco))
   subtotal = round(subtotal - troco * cedula[x], 2)
   x += 1

x = 0
print('NOTAS:')
for di in cedula:
  if x < 6: 
    print (lista[x], 'nota(s) de R$', round(di,2) )
  x += 1

x = 0
print('MOEDAS:')
for di in cedula:
  if x >= 6: 
    print (lista[x], 'moedas(s) de R$', round(di,2) )
  
  x += 1