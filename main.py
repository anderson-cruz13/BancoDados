import mysql.connector

conexao = mysql.connector.connect(
  host="localhost",
  user="root",
  password="admin",
)

cursor = conexao.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS python")
cursor.close()
conexao.close()

conexao = mysql.connector.connect(
  host="localhost",
  user="root",
  password="admin",
  database="python"
)

cursor = conexao.cursor()
cursor.execute("CREATE TABLE pessoas (nome VARCHAR(255), idade INT)")
conexao.commit()

cursor.close()
conexao.close()
