$(function () {
    
function Verificacoes(s) {
    // let {nome, cpf, email, emailConf, senha, senhaConf} = submissao;

    console.log(s);

    const condicaoNome = s.nome.length >= 4 && s.nome.length <= 65;
    const condicaoEmail = s.email === s.emailConf;
    const condicaoSenha = (s.senha === s.senhaConf) && (s.senha.length > 8);
    const condicaoCpf = VerCPF(s.cpf);

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
        alert("CPF Inválido.")
        return false;
    } 
    
} // Funcao 

function VerCPF(cpf) {
    var soma;
    var resto;
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
    alert("Bom Dia")
} 


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

        if(Verificacoes(submissao)) {

        const dados = JSON.stringify({
            nome: nome,
            cpf: cpf,
            email: email,
            senha: senha,
            endereco: endereco,
            bairro: bairro,
            cidade: cidade
        });


        // Aqui vai ter que ter um if para ver se é uma empresa
        // Ou um funcionário que será adicionado ao sistema.
        $.ajax({
            url: "http://localhost:5000/adicionar_funcionario",
            type: 'POST',
            dataType: 'json', // Tipo de formato recebido
            contentType: 'application/json', // Tipo de formato enviado
            data: dados, // Os dados que são enviados
            success: pessoaIncluida, // Chama a funcao para processar o resultado
            error: erroAoIncluir
        });
    }


        function pessoaIncluida(retorno) {
            if (retorno.resultado == "ok") {
                alert("Pessoa incluída com sucesso!");

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


        /*function pessoaIncluida (retorno) {
            if (retorno.resultado == "ok") {
                alert("Pessoa incluída com sucesso!");
    
                $("#nome").val("");
                $("#cpf").val("");
                $("#email").val("");
                $("#password").val("");
                $("#endereco").val("");
                $("#bairro").val("");
                $("#cidade").val("");
    
            } else {
                alert(retorno.resultado + ":" + retorno.detalhes);
            }
        }*/

        /*
            * Fazer mais um desses com jquery com incluirempresa.
            * Utilizando ajax etc.
        */

        function erroAoIncluir(retorno) {
            alert("ERRO: " + retorno.resultado + ":" + retorno.detalhes);
        }
    });
    
});
