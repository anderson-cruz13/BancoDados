import mysql.connector
from files import Files
from datetime import datetime


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
                    nome VARCHAR(255),
                    idade INT
                )
                """
            )
            conexao.commit()

        f = Files()
        f.read("users.txt")
        db = f.files

        with Bank() as (cursor, conexao):
            for i in db:
                for user in i.splitlines():
                    user = user.strip()

                    if not user:
                        continue

                    try:
                        nome, birth = user.split(",", 1)
                        nome = nome.strip()
                        birth = birth.strip()

                        # Calcular a idade
                        birth_date = datetime.strptime(birth, "%d/%m/%Y")
                        today = datetime.today()
                        idade = (today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day)))

                        # Inserir no banco de dados
                        cursor.execute(f"""
                                      INSERT INTO pessoas (nome, idade)
                                      VALUES ('{nome}', {idade})""")
                        conexao.commit()
                    except ValueError:
                        print(f"""Erro ao processar a linha: '{user}'.
                              A linha deve conter nome e nascimento separados
                              por vírgula.""")

    def __exit__(self, exc_type, exc_value, traceback):
        pass
