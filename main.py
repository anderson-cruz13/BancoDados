import mysql.connector  # ignore: F401
from bc import Bank


with Bank() as banco:

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
