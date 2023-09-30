from flask import request, jsonify
import conexao

conexao = conexao.ConexaoMySQL()

def logar():
    try:
        conexao.conectar()
        #if request.method == 'GET':
        email = request.form['email']
        senha  = request.form['password']

        sql = "SELECT email, password FROM user WHERE email = %s and password = %s"
        values = (email, senha)

        conexao.executar_query(sql, values)
        
        conexao.desconectar()

        return "Dados inseridos com sucesso!"
    except Exception as e:
        return f"Erro: {str(e)}" 

