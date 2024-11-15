import mysql.connector
from files import Files
from datetime import datetime
import dotenv
import os


dotenv.load_dotenv()


class Bank:
    def __enter__(self):
        self.conexao = mysql.connector.connect(
            host=os.environ['MYSQL_HOST'],
            user=os.environ['MYSQL_USER'],
            password=os.environ['MYSQL_PASSWORD'],
        )
        self.cursor = self.conexao.cursor()

        self.cursor.execute("CREATE DATABASE IF NOT EXISTS python")
        self.conexao.commit()

        self.cursor.execute("USE python")
        self.conexao.commit()

        return self.cursor, self.conexao

    def __exit__(self, exc_type, exc_value, traceback):
        self.cursor.close()
        self.conexao.close()


class BankWrite:
    def __enter__(self):
        with Bank() as (cursor, conexao):
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS pessoas (
                    id INT NOT NULL AUTO_INCREMENT,
                    nome VARCHAR(255),
                    idade DATE,
                    PRIMARY KEY (id)
                )
                """
            )
            conexao.commit()

        f = Files()
        f.read("users.txt")
        db = f.files

        if db:
            with Bank() as (cursor, conexao):
                cursor.executemany(
                    "INSERT INTO pessoas (nome, idade) VALUES (%s, %s)",
                    db,
                )
                conexao.commit()

    def __exit__(self, exc_type, exc_value, traceback):
        pass
