# pip install mysql-connector
import mysql.connector
from mysql.connector import Error

import os


def ConexaoBDAcademico():  # conexão com o BD
    con = None
    try:
        con = mysql.connector.connect(host='localhost', user='developer', password='12',
                                      database='coursejdbc'
                                      )
    except Error as ex:
        print(ex)
    return con


def dql(query):  # select
    vcon = ConexaoBDAcademico()
    cursor = vcon.cursor()
    cursor.execute(query)
    res = cursor.fetchall
    vcon.close()
    return res


def dml(query):  # transações
    try:
        vcon = ConexaoBDAcademico()
        cursor = vcon.cursor()
        cursor.execute(query)
        vcon.commit()
        vcon.close()
    except Error as ex:
        print(ex)


ConexaoBDAcademico()
dql('select * from department')
