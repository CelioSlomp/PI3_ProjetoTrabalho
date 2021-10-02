function Verificacoes(form) {
    let nome = form.nome.value;
    let email = form.email.value;
    let emailConf = form.emailConf.value;
    let senha = form.password.value;
    let senhaConf = form.passwordConf.value;
    let cpf = form.cpf.value;
    var empresa = document.querySelector("#empresa");

    alert(empresa)

    if (nome.length >= 4 && nome.length <= 65) {
        form.nome.focus;
        if (email === emailConf) {
            form.email.focus;
            if (senha === senhaConf && senha.length > 8) {
                form.senha.focus;
                if (empresa.checked == true) {
                    if (VerCNPJ(cpf)) {
                        return true;
                    } else {
                        alert("CNPJ inválido")
                        return false;
                    }
                } else {
                    if (VerCPF(cpf)) {
                        return true;
                    }
                    else {
                        alert("CPF Inválido.")
                        return false;
                    }
                }
            } // If Senha
            else {
                alert("Senha diferente ou muito curta, tente novamente.")
                return false;
            }
        } // If Email
        else {
            alert("Emails diferentes, tente novamente.")
            return false;
        } // Else Email
    } //If Nome
    else {
        alert("Nome muito curto, tente outro.")
        return false;
    } // Else Nome
} // Funcao

function VerCPF(cpf) {
    var soma;
    var resto;
    soma = 0;
    if (!cpf || cpf.length != 11 || cpf == "00000000000" ||
        cpf == "11111111111" || cpf == "22222222222" || cpf == "33333333333" ||
        cpf == "44444444444" || cpf == "55555555555" || cpf == "66666666666" ||
        cpf == "77777777777" || cpf == "88888888888" || cpf == "99999999999") {
        return false
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