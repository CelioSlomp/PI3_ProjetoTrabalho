from classes import *


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


    @app.route("/adicionar_funcionario", methods=['POST'])
    def incluir_funcionario():
        resposta = jsonify({"resultado": "ok", "detalhes": "ok"})
        # receber as informações da nova pessoa
        dados = request.get_json()  # (force=True) dispensa Content-Type na requisição
        try:  # tentar executar a operação
            nova = Funcionario(**dados)  # criar a nova pessoa
            
            # Verificar se já existe algum email/cpf/cnpj registrado
            novo_user = db.session.query(Funcionario).filter(Funcionario.email == dados["email"]).first()
            if novo_user != None:
                resposta = jsonify({"resultado": "erro", "detalhes": "Email já está cadastrado"})
                return resposta
            
            novo_user = db.session.query(Empresa).filter(Empresa.email == dados["email"]).first()
            if novo_user != None:
                resposta = jsonify({"resultado": "erro", "detalhes": "Email já está cadastrado"})
                return resposta
            
            novo_user = db.session.query(Funcionario).filter(Funcionario.cpf == dados["cpf"]).first()
            if novo_user != None:
                resposta = jsonify({"resultado": "erro", "detalhes": "CPF já está cadastrado"})
                return resposta
            db.session.add(nova)  # adicionar no BD
            db.session.commit()  # efetivar a operação de gravação
            print("salvo no banco de dados.")
        except Exception as e:
            # informar mensagem de erro
            resposta = jsonify({"resultado": "erro", "detalhes": str(e)})
            print("não salvo no banco de dados.")
        # adicionar cabeçalho de liberação de origem
        resposta.headers.add("Access-Control-Allow-Origin", "*")
        return resposta


    @app.route("/adicionar_empresa", methods=['POST'])
    def adicionar_empresa():
        resposta = jsonify({"resultado": "ok", "detalhes": "ok"})
        # receber as informações da nova empresa
        dados = request.get_json()  # (force=True) dispensa Content-Type na requisição
        try:  # tentar executar a operação
            nova = Empresa(**dados)  # criar a nova pessoa
            
            # Verificar se já existe algum email/cpf/cnpj registrado
            novo_user = db.session.query(Empresa).filter(Empresa.email == dados["email"]).first()
            if novo_user != None:
                resposta = jsonify({"resultado": "erro", "detalhes": "Email já está cadastrado"})
                return resposta
            
            novo_user = db.session.query(Funcionario).filter(Funcionario.email == dados["email"]).first()
            if novo_user != None:
                resposta = jsonify({"resultado": "erro", "detalhes": "Email já está cadastrado"})
                return resposta
            
            novo_user = db.session.query(Empresa).filter(Empresa.cnpj == dados["cnpj"]).first()
            if novo_user != None:
                resposta = jsonify({"resultado": "erro", "detalhes": "CNPJ já cadastrado"})
                return resposta
            db.session.add(nova)  # adicionar no BD
            db.session.commit()  # efetivar a operação de gravação
        except Exception as e:  # em caso de erro...
            # informar mensagem de erro
            resposta = jsonify({"resultado": "erro", "detalhes": str(e)})
        # adicionar cabeçalho de liberação de origem
        resposta.headers.add("Access-Control-Allow-Origin", "*")
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


    @app.route("/jalogadon/<int:idusuario>" )
    def jalogadon(idusuario):
        usuarios = db.session.query(Funcionario).filter(Funcionario.id == idusuario).first()
        if usuarios == None:
            usuarios = db.session.query(Empresa).filter(Empresa.id == idusuario).first()
        retorno = []
        retorno.append(usuarios.json())
        resposta = jsonify(retorno)
        resposta.headers.add("Access-Control-Allow-Origin", "*")
        return resposta


    @app.route("/check_login", methods=['POST'])
    def check_login():
        resposta = jsonify({"resultado": "ok", "detalhes": "ok"})
        # receber as informações da nova empresa
        dados = request.get_json()  # (force=True) dispensa Content-Type na requisição
        try:  # tentar executar a operação
            
            # Verificar se já existe algum email/cpf/cnpj registrado
            user = db.session.query(Empresa).filter(Empresa.email == dados["email"]).first()
            
            # Caso não exista uma empresa com esse email, buscará em funcionarios
            if user == None:
                user = db.session.query(Funcionario).filter(Funcionario.email == dados["email"]).first()
            if user.senha != dados["senha"]:
                print("senha incorreta.")
                resposta = jsonify({"resultado": "erro", "detalhes": "Senha incorreta"})
                return resposta
            else:
                resposta = jsonify({"resultado": user.id})
    
                resposta.headers.add("Access-Control-Allow-Origin", "*")
                return resposta


        except Exception as e:  # em caso de erro...
            # informar mensagem de erro
            resposta = jsonify({"resultado": "erro", "detalhes": str(e)})
        # adicionar cabeçalho de liberação de origem
        resposta.headers.add("Access-Control-Allow-Origin", "*")
        return resposta


    @app.route("/deletar_conta/<int:idusuario>", methods=['DELETE'])
    def deletar_conta(idusuario):
        # prepara uma resposta
        resposta = jsonify({"resultado": "ok", "detalhes": "ok"})
        try:
            
            user = db.session.query(Empresa).filter(Empresa.id == idusuario).first()
            
            # Caso não exista uma empresa com esse email, buscará em funcionarios
            if user == None:
                user = db.session.query(Funcionario).filter(Funcionario.id == idusuario).first()
            
            if user.type == "empresa":
                Empresa.query.filter(Empresa.id == idusuario).delete()
            elif user.type == "funcionario":
                Funcionario.query.filter(Funcionario.id == idusuario).delete()
            else:
                pass
            
            db.session.commit()
        except Exception as e:
            # informar mensagem de erro
            resposta = jsonify({"resultado": "erro", "detalhes":str(e)})
        resposta.headers.add("Access-Control-Allow-Origin", "*")  
        return resposta
        

    @app.route("/salvar_requisitos/<int:idusuario>", methods=['POST'])
    def salvar_requisitos(idusuario):
        user = db.session.query(Empresa).filter(Empresa.id == idusuario).first()
        # Caso não exista uma empresa com esse email, buscará em funcionarios
        if user == None:
            user = db.session.query(Funcionario).filter(Funcionario.id == idusuario).first()
        req = request.get_json()
        try:
            user.requisitos = req["requisitos"]
            db.session.commit()
            resposta = jsonify({"resultado": "ok", "detalhes":"ok"})
        except Exception as e:
            resposta = jsonify({"resultado": "erro", "detalhes":str(e)})
        resposta.headers.add("Access-Control-Allow-Origin", "*")
        return resposta


    @app.route("/main/<int:idusuario>", methods=['GET'])
    def main(idusuario):
        user = db.session.query(Empresa).filter(Empresa.id == idusuario).first()
        # Caso não exista uma empresa com esse email, buscará em funcionarios
        if user == None:
            user = db.session.query(Funcionario).filter(Funcionario.id == idusuario).first()       
        listaUsuarios = []
        try:
            reqUser = user.requisitos
            reqUser = reqUser.split(",")
            if(len(reqUser) == 0 or reqUser[0] == None):
                resposta = jsonify({"requisitos nulos"})
                resposta.headers.add("Access-Control-Allow-Origin", "*")
                return resposta

            if user.type == "funcionario":
                empresas = db.session.query(Empresa).all()
                for empresa in empresas:
                    num = 0
                    for i in empresa.requisitos.split(","):
                        for j in reqUser:
                            if i == j:
                                num += num + (1/len(reqUser))
                            else:
                                pass
                    if num >= 0.8:
                        listaUsuarios.append(empresa.json())
                resposta = jsonify(listaUsuarios)
                resposta.headers.add("Access-Control-Allow-Origin", "*")
                return resposta
            else:
                funcionarios = db.session.query(Funcionario).all()
                for funcionario in funcionarios:
                    num = 0
                    for i in funcionario.requisitos.split(","):
                        for j in reqUser:
                            if i == j:
                                num += num + (1/len(reqUser))
                            else:
                                pass
                    if num > 0.8:
                        listaUsuarios.append(funcionario.json())

                resposta = jsonify(listaUsuarios)
                resposta.headers.add("Access-Control-Allow-Origin", "*")
                return resposta
        except Exception as e:
            resposta = jsonify({"resultado": "erro", "detalhes":str(e)})
        resposta.headers.add("Access-Control-Allow-Origin", "*")
        return resposta
    # Inicia o servidor
    app.run(debug=True)
