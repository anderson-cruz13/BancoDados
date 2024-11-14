import mysql.connector  # ignore: F401


class Bank:
    def __enter__(self):
        self.conexao = mysql.connector.connect(
          host="localhost",
          user="root",
          password="admin",
        )
        self.cursor = self.conexao.cursor()

        self.cursor.execute("CREATE DATABASE IF NOT EXISTS python")
        self.conexao.commit()

    def __exit__(self, exc_type, exc_value, traceback):
        self.cursor.close()
        self.conexao.close()
