import mysql.connector

def Banco():
    return mysql.connector.connect(
        host="localhost",
        user="GC",
        password="1234",
        database="Carro"
    )