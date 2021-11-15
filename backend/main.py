from flask_sqlalchemy import SQLAlchemy
from flask import Flask, jsonify, request
import os

app = Flask(__name__)

# Cria o arquivo do banco de dados
diretorio = os.path.dirname(os.path.abspath(__file__))
arquivobanco = os.path.join(diretorio, "bancodados.db")

# Configura o banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + arquivobanco
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# Classe usuário
class Usuario(db.Model):
    '''Classe genérica usuário
    
    Essa classe é uma classe genérica, que contém todos os atributos comuns
    entre os funcionários e as empresas
    '''
    id = db.Column(db.Integer, primary_key=True)
    nome = db.column(db.String(256))
    email = db.Column(db.String(256))
    senha = db.Column(db.String(256))
    rua = db.Column(db.String(256))
    bairro = db.Column(db.String(256))
    cidade = db.Column(db.String(256))
    complemento = db.Column(db.String(40))


# Classe Empresa
class Empresa(Usuario):
    '''Classe Empresa
    
    Essa classe herda tudo de usuário e ainda complementa com o cnpj
    
    return: todos os atributos no formato json.
    '''
    cnpj = db.Column(db.String(18))

    # Retorna os atributos no formato json.
    def json(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'email': self.email,
            'senha': self.senha,
            'rua': self.rua,
            'bairro': self.bairro,
            'cidade': self.cidade,
            'cnpj': self.cnpj
        }


class Funcionario(Usuario):
    '''Classe Empresa
    
    Essa classe herda tudo de usuário e ainda complementa com o cpf
    
    return: todos os atributos no formato json.
    '''
    cpf = db.Column(db.String(14))

    # Retorna os atributos no formato json.
    def json(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'email': self.email,
            'senha': self.senha,
            'rua': self.rua,
            'bairro': self.bairro,
            'cidade': self.cidade,
            'cpf': self.cpf
        }


# Apenas roda o programa quando esse código é o principal
if __name__ == '__main__':
    # Cria o banco de dados
    db.create_all()


    # Retorna se o backend está funcionando ou não
    @app.route("/backend_operante")
    def rodando():
        return "Backend operante 8)."


    @app.route("/")
    def login():
        return "aqui vai o login"


    @app.route("/feed")
    def feed():
        return "aqui vai o feed"


    @app.route("/adicionar_funcionario", methods=['GET'])
    def incluir_funcionario():
        print("Passou aqui")
        resposta = jsonify({"resultado": "ok", "detalhes": "ok"})
        # receber as informações da nova pessoa
        dados = request.get_json()  # (force=True) dispensa Content-Type na requisição
        try:  # tentar executar a operação
            nova = Funcionario(**dados)  # criar a nova pessoa
            db.session.add(nova)  # adicionar no BD
            db.session.commit()  # efetivar a operação de gravação
            print("salvo no banco de dados.")
        except Exception as e:
            # informar mensagem de erro
            resposta = jsonify({"resultado": "erro", "detalhes": str(e)})
        # adicionar cabeçalho de liberação de origem
        resposta.headers.add("Access-Control-Allow-Origin", "")
        return resposta


    @app.route("/adicionar_empresa", methods=['POST'])
    def adicionar_empresa():
        resposta = jsonify({"resultado": "ok", "detalhes": "ok"})
        # receber as informações da nova empresa
        dados = request.get_json()  # (force=True) dispensa Content-Type na requisição
        try:  # tentar executar a operação
            nova = Empresa(**dados)  # criar a nova pessoa
            db.session.add(nova)  # adicionar no BD
            db.session.commit()  # efetivar a operação de gravação
        except Exception as e:  # em caso de erro...
            # informar mensagem de erro
            resposta = jsonify({"resultado": "erro", "detalhes": str(e)})
        # adicionar cabeçalho de liberação de origem
        resposta.headers.add("Access-Control-Allow-Origin", "")
        return resposta


    # Lista todas as empresas cadastradas
    @app.route("/listar_empresas")
    def listar_empresas():
        empresas = db.session.query(Empresa).all()

        retorno = []
        for i in empresas:
            retorno.append(i.json())

        return jsonify(retorno)


    # Lista todos os funcionários cadastrados
    @app.route("/listar_funcionarios")
    def listar_funcionarios():
        funcionarios = db.session.query(Funcionario).all()

        retorno = []
        for i in funcionarios:
            retorno.append(i.json())

        return jsonify(retorno)


    # Inicia o servidor
    app.run(debug=True)
