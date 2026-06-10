// ======================================
// AUTMENOS DASHBOARD
// ======================================

document.addEventListener('DOMContentLoaded', () => {

    console.log(
        'Dashboard carregada com sucesso.'
    );

    const hora = new Date().getHours();

    let saudacao = '';

    if (hora < 12) {

        saudacao = 'Bom dia';

    } else if (hora < 18) {

        saudacao = 'Boa tarde';

    } else {

        saudacao = 'Boa noite';

    }

    const titulo =
        document.querySelector('.topbar h1');

    if (titulo) {

        titulo.textContent =
            `${saudacao}, ${titulo.textContent}`;

    }

});