# importando sqlite
import sqlite3 as lite

# https://docs.python.org/3/library/sqlite3.html
# criando conexao
con = lite.connect("teste.db")

print('ok')

# criando tabela
with con:
    cur = con.cursor()
    cur.execute(
        '''CREATE TABLE formulario (id INTEGER PRIMARY KEY AUTOINCREMENT,nome text, email text, telefone text) ''')
