from flask import request, jsonify
import mysql.connector
import conexao

def criarTabelaLab():
    try:
        con = conexao.getConexao()

        criar_tabela_lab = """CREATE TABLE IF NOT EXISTS lab (
        lab_id int not null auto_increment,
        andar char(1),
        lab char(6),
        description varchar(60),
        is_active bit not null,
        PRIMARY KEY (lab_id)
        )"""

        cursor = con.cursor()
        cursor.execute(criar_tabela_lab)
        print ("Tabela Grupos criada com sucesso!")

    except mysql.connector.Error as erro:
        return "Erro: {}".format(erro)

    finally:
        if (con.is_connected()):
            cursor.close()
            con.close()
            return "Conexão Finalizada!"


def inserir_lab():
    try:
        con = conexao.getConexao()
        #if request.method == 'POST':
        andar = request.form['andar']
        lab  = request.form['lab']
        descricao = request.form['descri']
        status = request.form['status']

        sql = "INSERT INTO Lab (andar, lab, description, is_active) VALUES (%s, %s, %s, %s)"
        values = (andar, lab, descricao, status)

        cursor = con.cursor()
        cursor.execute(sql, values)
        con.commit()
        
        cursor.close()
        con.close()

        return "Dados inseridos com sucesso!"
    except Exception as e:
        return f"Erro: {str(e)}" 


#execute = criarTabelaLab()