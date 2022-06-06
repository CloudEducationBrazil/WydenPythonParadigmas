import mysql.connector
# Objeto de conexão
conn = mysql.connector.connect(
    host="localhost", user="developer", password="12", database="coursejdbc")
if conn.is_connected():
    print("conectado")
    print(conn.get_server_info())
