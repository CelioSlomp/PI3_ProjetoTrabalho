function Verificacoes(form){
    let nome = form.nome.value;
    let email = form.email.value;
    let emailConf = form.emailConf.value;
    let senha = form.password.value;
    let senhaConf = form.passwordConf.value;

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