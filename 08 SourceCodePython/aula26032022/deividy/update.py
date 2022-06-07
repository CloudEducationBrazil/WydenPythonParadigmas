import mysql.connector
conn = mysql.connector.connect(
    host="localhost",
    user="developer",
    password="12",
    database="dbpython"
)

cursor = conn.cursor()

nome_produto = input("Insira o nome do produto que deseja alterar:")
pergunta = input("Deseja alterar o valor do produto:")
if pergunta == 'sim' or 's':
    print("***Lembre-se de não utilizar virgulas para definir o valor, e sim um ponto!***")
    valor = input("Insira o novo valor do produto:")
    comando = f'UPDATE vendas SET valor = {valor} WHERE nome_produto = "{nome_produto}"'
    cursor.execute(comando)
    conn.commit()
    print("As alterações foram feitas com sucesso!")

else:
    print("O Serviço de update foi finalizado sem nenhuma modificação!")

cursor.close()
conn.close()
