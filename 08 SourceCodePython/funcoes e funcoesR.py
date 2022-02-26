def soma(a, b):
    return a + b

def sub(a, b):
    return a - b

def mult(a, b):
    return a * b

def fatorial(n):
    if ( n < 0 ): print('não existe fatorial'); return 
    if ( n == 0 or n == 1): return 1

    n = n * fatorial (n-1)
    
    return n

print (soma(2,7))
print (sub(2,7))
print (mult(2,7))
print (fatorial(3))
