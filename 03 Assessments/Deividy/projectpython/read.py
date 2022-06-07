import mysql.connector
conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "dbpython"
)

cursor = conn.cursor()

comando = f'SELECT * FROM vendas'
cursor.execute(comando)
resultado = cursor.fetchall()
print("[ID -- Nome -- Valor -- Cliente -- Data]")
print (resultado)


cursor.close()
conn.close()

