# chrome-extension://efaidnbmnnnibpcajpcglclefindmkaj/http://univasf.edu.br/~marcelo.linder/arquivos_iapCA/aulas/aula22.pdf
def fibonacci(n):
  if n == 1:
    return 1
  elif n == 2:
    return 1
  else:
    x = fibonacci(n-1) + fibonacci(n-2)
    print(x, end = ' ')
    return x

for num in range(1, 9):
  print(fibonacci(num), end = ' ')