function Verificacoes(form){
    var nome = form.nome.value;
    var email = form.email.value;
    var emailConf = form.emailConf.value;
    var senha = form.password.value;
    var senhaConf = form.passwordConf.value;

    if (nome.length >= 4 && nome.length <= 65){
        form.nome.focus;
        if(email === emailConf){
            form.email.focus;
            if (senha === senhaConf && senha.length > 8){
                form.senha.focus;
                return true;
            } // If Senha
            else{
                alert("Senha diferente ou muito curta, tente novamente.")
                return false;
            }
        } // If Email
        else{
            alert("Emails diferentes, tente novamente.")
            return false;
        } // Else Email
    } //If Nome
    else{
        alert("Nome muito curto, tente outro.")
        return false;
    } // Else Nome
} // Funcao