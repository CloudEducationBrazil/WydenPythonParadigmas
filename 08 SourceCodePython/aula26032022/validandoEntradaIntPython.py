while True:
    try:
        nota = int(input("Informe a nota entre 0 e 10: "))
        if not 0 <= nota <= 10:
            raise ValueError("Nota fora do range permitido")
    except ValueError as e:
        print("Valor inválido:", e)
    else:
        break

print(nota)
