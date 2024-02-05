// recupera o elemento do botão no DOM
let botao_submit = document.getElementById('submit');
let username = document.querySelector('ssb');
let password = document.querySelector('#password');



function mostra_user(){
    alert('user: ' + username);
    alert('password: ' + password);
}

//atrela uma função ao evento de 'click' do botão
botao_submit.addEventListener('click', mostra_user)
