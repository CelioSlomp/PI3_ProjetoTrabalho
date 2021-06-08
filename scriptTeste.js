function verificarCadastro(form) {

    var nome, usuario, email, senha, csenha;
    nome = form.nomec.value;
    usuario = form.login.value;
    email = form.email.value;
    
    senha = form.senha.value;
    csenha = form.csenha.value;

    if (nome.length >= 5) {
        if (usuario.length >= 4 && usuario.length <= 16) {
            if (senha.length >= 4 && senha.length <= 18) {
                if (senha === csenha) {
                    document.getElementById("cadastro").action = "Sucesso.html";
                    alert('Seus Dados foram enviados com sucesso!');
                    form.senha.focus();
                    return 1;
                }
                else {
                    alert('Senhas diferentes. Por favor insira as mesmas senhas.');
                    form.senha.focus();
                    return 0;
                }
            }
            else {
                if (senha.length < 4) {
                    alert('Senha menor de 4 dígitos. Por favor insira um valor maior.');
                }
                else if (senha.length > 18) {
                    alert('Senha maior de 18 dígitos. Por favor insira um valor menor.');
                }
                form.senha.focus();
                return 0;
            }
        }
        else {
            if (usuario.length < 4) {
                alert('Usuário menor de 4 dígitos. Por favor insira um valor maior.');
            }
            else if (usuario.length > 16) {
                alert('Usuário maior de 16 dígitos. Por favor insira um valor menor.');
            }
            form.usuario.focus();
            return 0;
        }
    }
    else {
        alert('Nome menor de 5 dígitos. Por favor insira um valor maior');
        form.nome.focus();
        return 0;
    }
}