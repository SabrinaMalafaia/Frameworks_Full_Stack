from flask import Flask, render_template, request
import requests
import sys
sys.path.append('backend')
from backend import user_model
from backend import login_model
from backend import lab_model

app = Flask(__name__, template_folder='frontend/templates')
app.config['JSON_SORT_KEYS'] = False
#############################################################################
# API
#############################################################################

url = 'https://api.postman.com/collections/14803919-028b1b9d-e330-43cf-ad61-ef241582568b?access_key=PMAT-01H82RG3VKGM8N5J027WV36889'

response = requests.get(url)

if response.status_code == 200:
    dados = response.json()  # Se a resposta for JSON
    # Faça algo com os dados
else:
    print('Falha na solicitação:', response.status_code)

#############################################################################
# Index
#############################################################################

# Rota para exibir o Index
@app.route('/')
def index():
    return render_template('Index.html')

#############################################################################
# Login
#############################################################################

# Rota para exibir o Login
@app.route('/logar', methods=['GET'])
def logar():
    login_model.logar()
    return render_template('Login.html')

#############################################################################
# Cadastro User
#############################################################################

# Rota para exibir o formulário de cadastro de usuarios
@app.route('/cadastrar_usuario', methods=['GET'])
def cadastrar_user():
    return render_template('CadastroUser.html')

# Rota para inserir os dados do formulário de cadastro de parceiros no banco de dados - OK
@app.route('/inserir_usuario', methods=['POST'])
def inserir_user():
    if request.method == 'POST':
        print("Rota /inserir_usuario foi chamada.")  # Adicione esta linha
        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]
        cpf_cnpj = request.form["cpf_cnpj"]
        phone = request.form["phone"]
        status = request.form["status"]
        tipo = request.form["tipo"]

        print(f"Valores recebidos: name={name}, email={email}, password={password}, cpf_cnpj={cpf_cnpj}, phone={phone}, status={status}, tipo={tipo}")  # Adicione esta linha

        usuario = user_model.User(name, email, password, cpf_cnpj, phone, status, tipo)

        usuario.criar(name, email, password, cpf_cnpj, phone, status, tipo)

        return "Ok"
    
    return render_template('CadastroUser.html')


#############################################################################
# Cadastro Lab
#############################################################################
# Rota para exibir o formulário de cadastro de laboratorios
@app.route('/cadastrar_lab', methods=['GET'])
def cadastrar_lab():
    return render_template('CadastroLab.html')

# Rota para inserir os dados do formulário de cadastro de laboratorios no banco de dados - OK
@app.route('/inserir_lab', methods=['POST'])
def inserir_lab():
    lab_model.inserir_lab()
    return render_template('CadastrarLab.html')


#############################################################################
# Reserva Lab
#############################################################################
# Rota para exibir o formulário de cadastro de laboratorios
@app.route('/reservar_lab', methods=['GET'])
def reservar_lab():
    return render_template('ReservaLab.html')

# Rota para inserir os dados do formulário de cadastro de laboratorios no banco de dados - OK
@app.route('/reserva_lab', methods=['POST'])
def reserva_lab():
    lab_model.inserir_lab()
    return render_template('ReservaLab.html')


if __name__ == '__main__':
    app.run(debug=True)