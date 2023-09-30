from conexao import ConexaoMySQL

conexao = ConexaoMySQL()

class User:
    def __init__(self, name, email, password, cpf_cnpj, phone, status, tipo):
        self.name = name
        self.email = email
        self.password = password
        self.cpf_cnpj = cpf_cnpj
        self.phone = phone
        self.status = status
        self.tipo = tipo
        
        
    def criar(self, name, email, password, cpf_cnpj, phone, status, tipo):
        conexao.conectar()
        query = "INSERT INTO user (name, email, usertype_id, password, is_active, cpf_cnpj, phone) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        values = (name, email, tipo, password, status, cpf_cnpj, phone)
        print(f"Query SQL: {query}")  # Adicione esta linha
        print(f"Valores: {values}")  # Adicione esta linha
        conexao.executar_query(query, values)
        conexao.desconectar()
        return "Usuário criado com sucesso!"

    def consultar(self, user_id):
        conexao.conectar()
        query = "SELECT * FROM user WHERE id = %s"
        result = conexao.executar_query(query, (user_id,))
        conexao.desconectar()
        return result.fetchone()
    

    def editar(self, name, email, password, cpf_cnpj, phone, status, tipo, user_id):
        conexao.conectar()
        query = "UPDATE user SET name = %s , email = %s , usertype_id = %s , password = %s , is_active = %s , cpf_cnpj = %s , phone = %s WHERE id = %s"
        values = (name, email, password, cpf_cnpj, phone, status, tipo, user_id)
        conexao.executar_query(query, values)
        conexao.desconectar()
        return "Usuário atualizado com sucesso!"


    def inativar(self, user_id):
        conexao.conectar()
        query = "UPDATE user SET is_active = %s WHERE id = %s"
        conexao.executar_query(query, (0, user_id))
        conexao.desconectar()
        return "Usuário inativado com sucesso!"

