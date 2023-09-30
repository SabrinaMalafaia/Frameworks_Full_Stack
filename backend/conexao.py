import mysql.connector

class ConexaoMySQL:
    def __init__(self, host='localhost', username="root", password="50748523", database="fullstack"):
        self.host = host
        self.username = username
        self.password = password
        self.database = database
        self.connection = None

    def conectar(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.username,
                password=self.password,
                database=self.database
            )
            print("Conexão ao banco estabelecida com sucesso!")
        except mysql.connector.Error as erro:
            print(f"Erro ao conectar ao MySQL: {erro}")

    def desconectar(self):
        if self.connection:
            self.connection.close()
            print("Conexão ao banco encerrada.")

    def executar_query(self, query, values=None):
        if self.connection:
            try:
                cursor = self.connection.cursor()
                if values:
                    cursor.execute(query, values)
                else:
                    cursor.execute(query)
                self.connection.commit()
                print("Query executada com sucesso!")
            except mysql.connector.Error as erro:
                self.connection.rollback()
                print(f"Erro ao executar a query: {erro}")
            finally:
                cursor.close()