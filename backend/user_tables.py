from flask import request
#import sys
#sys.path.append('backend')
import conexao
#from backend import conexao

cone = conexao.ConexaoMySQL()

def criarTabelaUserType():

    cone.conectar()

    criar_tabela_usertype = """CREATE TABLE IF NOT EXISTS usertype (
    usertype_id int not null auto_increment,
    type varchar (15),
    primary key (usertype_id)
    )"""
    
    cone.executar_query(criar_tabela_usertype)

    cone.desconectar()


def criarTabelaUser():

    cone.conectar()

    criar_tabela_user = """CREATE TABLE IF NOT EXISTS user (
    user_id int not null auto_increment,
    name varchar(60) not null,
    email varchar(60),
    usertype_id integer,
    password varchar(16),
    is_active tinyint(1) not null,
    cpf_cnpj varchar(14) unique,
    phone char(11),
    primary key (user_id),
    CONSTRAINT fk_tipo FOREIGN KEY (usertype_id) REFERENCES usertype (usertype_id)
    )"""

    cone.executar_query(criar_tabela_user)

    cone.desconectar()


def inserir_tipo():
    try:
        cone.conectar()

        tipo = request.form['tipo']
        
        sql = "INSERT INTO usertype (type) VALUES (%s)"
        values = (tipo)

        cone.executar_query(sql, values)
        
        cone.desconectar()

        return "Dados inseridos com sucesso!"
    except Exception as e:
        return f"Erro: {str(e)}" 

 
def inserir_user():
    try:
        cone.conectar()

        name = request.form['name']
        email  = request.form['email']
        cpf_cnpj = request.form['cpf-cnpj']
        password = request.form['password']
        phone = request.form['phone']
        status = request.form['status']
        tipo = request.form['tipo']
        
        sql = "INSERT INTO user (name, email, usertype_id, password, is_active, cpf_cnpj, phone) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        values = (name, email, tipo, password, status, cpf_cnpj, phone)

        cone.executar_query(sql, values)
        
        cone.desconectar()

        return "Dados inseridos com sucesso!"
    except Exception as e:
        return f"Erro: {str(e)}" 


criarTabelaUserType()
criarTabelaUser()