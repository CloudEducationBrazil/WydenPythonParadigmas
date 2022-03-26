while True:
    try:
        nota1 = float(input("Informe uma nota1: "))
        nota2 = float(input("Informe uma nota2: "))
        
        nota3 = nota1 + nota2  

    except ValueError as e:
        print("Valor inválido:", e)
    else:
        break

print(nota1, nota2, nota3)
