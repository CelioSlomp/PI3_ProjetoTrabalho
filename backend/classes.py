from config import *

# Classe usuário
class Usuario(db.Model):
    '''Classe genérica usuário

    Essa classe é uma classe genérica, que contém todos os atributos comuns
    entre os funcionários e as empresas
    '''
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(256))
    email = db.Column(db.String(256))
    senha = db.Column(db.String(256))
    endereco = db.Column(db.String(256))
    bairro = db.Column(db.String(256))
    cidade = db.Column(db.String(256))
    
    
    type = db.Column(db.String(50))
    
    __mapper_args__={
        'polymorphic_identity':'usuario',
        'polymorphic_on':type
    }



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
            'endereco': self.endereco,
            'bairro': self.bairro,
            'cidade': self.cidade,
            'cnpj': self.cnpj
        }
    
    __mapper_args__={
        'polymorphic_identity':'empresa',
    }


class Funcionario(Usuario):
    '''Classe Funcionario

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
            'endereco': self.endereco,
            'bairro': self.bairro,
            'cidade': self.cidade,
            'cpf': self.cpf
        }
    
    __mapper_args__={
        'polymorphic_identity':'funcionario',
    }