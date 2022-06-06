import mysql.connector

conexao = mysql.connector.connect(
    host="localhost", user="developer", password="12", database="coursejdbc")

cursor = conexao.cursor()

if conexao.is_connected():
    print("conectado")
else:
    print('erro')

comando = f'INSERT INTO veiculo (placa, marca,modelo,ano,valorDiaria) VALUES ("HWO1253","TOYOTA","ETIOS","2020",150.55),("HVV7947","HYUNDAI","HB20","2021",350.12),("ADP7232","FORD","KA","2022",370.54),("JUZ8128","JEEP","COMPASS","2022",352.11),("HTH8600","VOLKSWAGEN","FOX","2019",100.00),("ABC1112","CHEVROLET","SPIN","2019",231.99),("LZG9013","CHEVROLET","ONIX","2020",532.99),("JVM9079","PORSCHE","911","2022",600.32),("JZJ6629","TESLA","Y","2020",567.23),("MYV5692","RENAULT","KWID","2016",55.50),("JYV0730","FIAT","ARGO","2022",311.00)'

cursor.execute(comando)
conexao.commit()
print('dados inseridos com sucesso!!!')

cursor.close()
conexao.close()
