from flask_sqlalchemy import SQLAlchemy
from flask import Flask, jsonify
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
            'id' : self.id,
            'email' : self.email,
            'senha' : self.senha,
            'rua' : self.rua,
            'bairro' : self.bairro,
            'cidade' : self.cidade,
            'complemento' : self.complemento,
            'cnpj' : self.cnpj
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
            'id' : self.id,
            'email' : self.email,
            'senha' : self.senha,
            'rua' : self.rua,
            'bairro' : self.bairro,
            'cidade' : self.cidade,
            'complemento' : self.complemento,
            'cpf' : self.cpf
        }


# A classe Equipe foi escolhida por mim, Celio.
class Equipe(db.Model):
    # Ela possui alguns parâmetros, tais como lider, descricao,
    # area e lista.
    id = db.Column(db.Integer, primary_key=True)
    lider_id = db.Column(db.Integer, db.ForeignKey(Funcionario.id), nullable=False)
    lider = db.relationship("Funcionario")
    descricao = db.Column(db.String(256))
    area = db.Column(db.String(256))
    # O atributo lista recebe uma lista de funcionarios em json
    lista = []
    funcionarios = []
    
    # O método json retorna todas as 'variáveis' do programa
    # em formato json.
    def json(self):
        # Esse for pega os objetos funcionarios e transforma-os
        # em formato json.
        for i in self.lista:
            self.funcionarios.append(i.json())
        
        # Aqui é o retorno da função
        return {
            'id' : self.id,
            'lider' : self.lider.json(),
            'descricao' : self.descricao,
            'funcionarios' : self.funcionarios,
            'area' : self.area
        }


#A class "AreaEmpresa" foi escolhida por mim, Alexandre Zabel"
class AreaEmpresa(db.Model):
    #Ela possui os seguintes parametros, empresa, rh, financeiro e compras
    id = db.Column(db.Integer, primary_key=True)
    empresa_id = db.Column(db.Integer, db.ForeignKey(Empresa.id), nullable=False)
    empresa = db.relationship("Empresa")

    rh = db.Column(db.String(1000))
    financeiro = db.Column(db.String(1000))
    compras = db.Column(db.String(1000))
    #Aqui o metodo json retornará todas as variaves da class em formato json
    def json(self):
        return{
            'id' : self.id,
            'rh' : self.rh,
            'financeiro' : self.financeiro,
            'compras' : self.compras
        }
     
        
# Classe Desempregado, criada por Lucas
class Desempregado(db.Model):
    # A classe possui 4 parâmetros, funcionario, habilidade, urgencia e experiencia.
    id = db.Column(db.Integer, primary_key=True)
    # Quem é a pessoa desempregada
    funcionario_id = db.Column(db.Integer, db.ForeignKey(Funcionario.id), nullable=False)
    funcionario = db.relationship("Funcionario")
    habilidade = db.Column(db.String(256))
    urgencia = db.Column(db.Integer)
    experiencia = db.Column(db.String(256))

    # Retorna os "atributos" do programa em formato json
    def json(self):
        # Retorno da função
        return{
            'id' : self.id,
            'funcionario' : self.funcionario.json(),
            'habilidade' : self.habilidade,
            'urgencia' : self.urgencia,
            'experiencia' : self.experiencia
        }

# Apenas roda o programa quando esse código é o principal
if __name__ == '__main__':
    # Creia o banco de dados
    db.create_all()

    # Aqui cria uns exemplos
    empresa = Empresa(email="joao@gmail.com", senha="Abacaxi1994", bairro="Bom retiro", cidade="Blumenau", complemento="numero 75", cnpj="986.472.320-03", rua="Rua XV de novembro")
    funcionario1 = Funcionario(email="joao@gmail.com", senha="Abacaxi1994", bairro="Bom retiro", cidade="Blumenau", complemento="numero 75", cpf="986.472.320-03", rua="Rua XV de novembro")
    funcionario2 = Funcionario(email="cleber@gmail.com", senha="CleberSoares23", bairro="Centro", cidade="Blumenau", complemento="numero 80", cpf="640.801.060-17", rua="rua rubens do pinho")
    funcionario3 = Funcionario(email="josedasilva@gmail.com", senha="pizzadecalabresa777", bairro="Vila nova", cidade="Pomerode", complemento="numero 770", cpf="211.320.710-97", rua="rua joinville")
    
    # Adiciona e commita os dados
    db.session.add(empresa)
    db.session.add(funcionario1)
    db.session.add(funcionario2)
    db.session.add(funcionario3)
    db.session.commit()
    
    
    # Aqui é aonde eu, Celio, criei o teste
    equipe = Equipe(lider=funcionario1, descricao="aaaa", lista=[funcionario1, funcionario2], area="banco de dados")
    # Aqui adicionei a equipe ao banco de dados e commitei
    db.session.add(equipe)
    db.session.commit()
    # Aqui printa a equipe
    print(equipe)
    print("--------------------------------------------")
    print(equipe.json())
    
    area = AreaEmpresa(empresa=empresa, rh=str(funcionario1.json()), financeiro=str(funcionario2.json()), compras=str(funcionario3.json()))

    db.session.add(area)
    db.session.commit()
    print(area)
    print("--------------------------------------------")
    print(area.json())
    
    desempregado = Desempregado(funcionario=funcionario1, habilidade="Nenhuma", urgencia=5, experiencia="nenhuma")
    db.session.add(desempregado)
    db.session.commit()
    print(desempregado)
    print("--------------------------------------------")
    print(desempregado.json())
    
    # Retorna se o backend está funcionando ou não
    @app.route("/")
    def rodando():
        return "Backend tá indo :D"
    
    # Lista todas as empresas cadastradas
    @app.route("/listar_empresas")
    def listar_empresas():
        empresas = db.session.query(Empresa).all()
        
        retorno = []
        for i in empresas:
            retorno.append(i.json())
        
        return jsonify(retorno)
    
    # Lista todas as equipes préviamente formadas
    @app.route("/listar_equipes")
    def listar_equipes():
        equipes = db.session.query(Equipe).all()
        
        retorno = []
        for i in equipes:
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
    
    # Lista todas as areas das empresas registradas
    @app.route("/listar_areas")
    def listar_areas():
        area = db.session.query(AreaEmpresa).all()
        
        retorno = []
        for i in area:
            retorno.append(i.json())
            
        return jsonify(retorno)
    
    # Lista todas as areas das empresas registradas
    @app.route("/listar_desempregado")
    def listar_desempregado():
        desempregado = db.session.query(Desempregado).all()
        
        retorno = []
        for i in desempregado:
            retorno.append(i.json())
            
        return jsonify(retorno)
    # Inicia o servidor
    app.run(debug=True)