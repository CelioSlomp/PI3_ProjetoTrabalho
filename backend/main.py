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

    

    # Inicia o servidor
    app.run(debug=True)
