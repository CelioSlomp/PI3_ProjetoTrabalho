$(function () {

    function Verificacoes(s) {
        // let {nome, cpf, email, emailConf, senha, senhaConf} = submissao;

        const condicaoNome = s.nome.length >= 4 && s.nome.length <= 65;
        const condicaoEmail = s.email === s.emailConf;
        const condicaoSenha = (s.senha === s.senhaConf) && (s.senha.length > 8);
        const empresa = document.getElementById("empresa");

        if (empresa.checked) {
            var condicaoCpf = VerCNPJ(s.cpf);
        } else {
            var condicaoCpf = VerCPF(s.cpf);
        }

        if (condicaoNome && condicaoEmail && condicaoSenha && condicaoCpf) {
            return true;
        }

        else if (!condicaoNome) {
            alert("Nome muito curto, tente outro.")
            return false;
        } else if (!condicaoEmail) {
            alert("Emails diferentes, tente novamente.")
            return false;
        } else if (!condicaoSenha) {
            alert("Senha diferente ou muito curta, tente novamente.")
            return false;
        } else if (!condicaoCpf) {
            alert("CPF/CNPJ Inválido.")
            return false;
        }

    } // Funcao 

    function VerCPF(cpf) {
        var soma;
        var resto;
        cpf = cpf.replace(/[^\d]+/g, '')
        soma = 0;
        if (!cpf || cpf.length != 11 || cpf == "00000000000" ||
            cpf == "11111111111" || cpf == "22222222222" || cpf == "33333333333" ||
            cpf == "44444444444" || cpf == "55555555555" || cpf == "66666666666" ||
            cpf == "77777777777" || cpf == "88888888888" || cpf == "99999999999") {
            return false;
        }
        for (i = 1; i <= 9; i++) {
            soma = soma + parseInt(cpf.substring(i - 1, i)) * (11 - i);
        }
        resto = (soma * 10) % 11;

        if ((resto == 10) || (resto == 11)) resto = 0;
        if (resto != parseInt(cpf.substring(9, 10))) {
            return false;
        }
        soma = 0;
        for (i = 1; i <= 10; i++) soma = soma + parseInt(cpf.substring(i - 1, i)) * (12 - i);
        resto = (soma * 10) % 11;

        if ((resto == 10) || (resto == 11)) {
            resto = 0;
        }

        if (resto != parseInt(cpf.substring(10, 11))) {
            return false;
        }
        return true;
    } // Funcao

    function VerCNPJ(cnpj) {

        cnpj = cnpj.replace(/[^\d]+/g, '');

        if (cnpj == '') return false;

        if (cnpj.length != 14)
            return false;

        if (cnpj == "00000000000000" || cnpj == "11111111111111" ||
            cnpj == "22222222222222" || cnpj == "33333333333333" ||
            cnpj == "44444444444444" || cnpj == "55555555555555" ||
            cnpj == "66666666666666" || cnpj == "77777777777777" ||
            cnpj == "88888888888888" || cnpj == "99999999999999")
            return false;

        tamanho = cnpj.length - 2
        numeros = cnpj.substring(0, tamanho);
        digitos = cnpj.substring(tamanho);
        soma = 0;
        pos = tamanho - 7;
        for (i = tamanho; i >= 1; i--) {
            soma += numeros.charAt(tamanho - i) * pos--;
            if (pos < 2)
                pos = 9;
        }
        resultado = soma % 11 < 2 ? 0 : 11 - soma % 11;
        if (resultado != digitos.charAt(0))
            return false;

        tamanho = tamanho + 1;
        numeros = cnpj.substring(0, tamanho);
        soma = 0;
        pos = tamanho - 7;
        for (i = tamanho; i >= 1; i--) {
            soma += numeros.charAt(tamanho - i) * pos--;
            if (pos < 2)
                pos = 9;
        }
        resultado = soma % 11 < 2 ? 0 : 11 - soma % 11;
        if (resultado != digitos.charAt(1))
            return false;

        return true;

    } // Funcao


    $(document).on("click", "#botaoCadastro", function () {
        const nome = $("#nome").val();
        const cpf = $("#cpf").val();
        const email = $("#email").val();
        const emailConf = $("#emailConf").val();
        const senha = $("#password").val();
        const senhaConf = $("#passwordConf").val();
        const endereco = $("#endereco").val();
        const bairro = $("#bairro").val();
        const cidade = $("#cidade").val();

        const submissao = {
            nome,
            cpf,
            email,
            emailConf,
            senha,
            senhaConf
        };

        if (Verificacoes(submissao)) {

            const empresa = document.getElementById("empresa");

            if (empresa.checked) {
                var dados = JSON.stringify({
                    nome: nome,
                    cnpj: cpf.replace(/[^\d]+/g, ''),
                    email: email,
                    senha: senha,
                    endereco: endereco,
                    bairro: bairro,
                    cidade: cidade
                });

                $.ajax({
                    url: "http://localhost:5000/adicionar_empresa",
                    type: 'POST',
                    dataType: 'json', // Tipo de formato recebido
                    contentType: 'application/json', // Tipo de formato enviado
                    data: dados, // Os dados que são enviados
                    success: pessoaIncluida, // Chama a funcao para processar o resultado
                    error: erroAoIncluir
                });

                function pessoaIncluida(retorno) {
                    if (retorno.resultado == "ok") {
                        alert("Registrado com sucesso");

                        $("#nome").val("");
                        $("#cpf").val("");
                        $("#email").val("");
                        $("#emailConf").val("");
                        $("#password").val("");
                        $("#passwordConf").val("");
                        $("#endereco").val("");
                        $("#bairro").val("");
                        $("#cidade").val("");

                    } else {
                        alert(retorno.resultado + ":" + retorno.detalhes);
                    }
                }

            } else {
                var dados = JSON.stringify({
                    nome: nome,
                    cpf: cpf.replace(/[^\d]+/g, ''),
                    email: email,
                    senha: senha,
                    endereco: endereco,
                    bairro: bairro,
                    cidade: cidade
                });
                $.ajax({
                    url: "http://localhost:5000/adicionar_funcionario",
                    type: 'POST',
                    dataType: 'json', // Tipo de formato recebido
                    contentType: 'application/json', // Tipo de formato enviado
                    data: dados, // Os dados que são enviados
                    success: pessoaIncluida, // Chama a funcao para processar o resultado
                    error: erroAoIncluir
                });

                function pessoaIncluida(retorno) {
                    if (retorno.resultado == "ok") {
                        alert("Registrado com sucesso");

                        $("#nome").val("");
                        $("#cpf").val("");
                        $("#email").val("");
                        $("#emailConf").val("");
                        $("#password").val("");
                        $("#passwordConf").val("");
                        $("#endereco").val("");
                        $("#bairro").val("");
                        $("#cidade").val("");

                    } else {
                        alert(retorno.resultado + ":" + retorno.detalhes);
                    }
                }
            }

            // Aqui vai ter que ter um if para ver se é uma empresa
            // Ou um funcionário que será adicionado ao sistema.
        }




        /*
            * Fazer mais um desses com jquery com incluirempresa.
            * Utilizando ajax etc.
        */

        function erroAoIncluir(retorno) {
            alert("ERRO: " + retorno.resultado + ":" + retorno.detalhes);
        }
    });

});
