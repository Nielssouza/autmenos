// ======================================
// BUSCA NA TABELA
// ======================================

document.addEventListener('DOMContentLoaded', () => {

    const searchInput = document.getElementById('searchInput');

    if (searchInput) {

        searchInput.addEventListener('keyup', function () {

            const filtro = this.value.toLowerCase();

            const linhas = document.querySelectorAll(
                '#cadastroTable tbody tr'
            );

            linhas.forEach(linha => {

                const texto = linha.innerText.toLowerCase();

                if (texto.includes(filtro)) {
                    linha.style.display = '';
                } else {
                    linha.style.display = 'none';
                }

            });

        });

    }

});


// ======================================
// EXPORTAR CSV
// ======================================

function exportarCSV() {

    const tabela = document.getElementById('cadastroTable');

    if (!tabela) return;

    let csv = [];

    const linhas = tabela.querySelectorAll('tr');

    linhas.forEach(row => {

        const cols = row.querySelectorAll('th, td');

        let linha = [];

        cols.forEach(col => {
            linha.push(
                '"' + col.innerText.replace(/"/g, '""') + '"'
            );
        });

        csv.push(linha.join(';'));

    });

    const csvFile = new Blob(
        [csv.join('\n')],
        { type: 'text/csv;charset=utf-8;' }
    );

    const downloadLink = document.createElement('a');

    downloadLink.href =
        URL.createObjectURL(csvFile);

    downloadLink.download =
        'cadastros_autmenos.csv';

    document.body.appendChild(downloadLink);

    downloadLink.click();

    document.body.removeChild(downloadLink);

}


// ======================================
// BOTÃO EXPORTAR
// ======================================

document.addEventListener('DOMContentLoaded', () => {

    const btnExportar =
        document.getElementById('btnExportar');

    if (btnExportar) {

        btnExportar.addEventListener(
            'click',
            function (e) {

                e.preventDefault();

                exportarCSV();

            }
        );

    }

});


// ======================================
// NOVO CADASTRO
// ======================================

document.addEventListener('DOMContentLoaded', () => {

    const btnNovo =
        document.getElementById('novoCadastro');

    if (btnNovo) {

        btnNovo.addEventListener(
            'click',
            function () {

                alert(
                    'Modal de cadastro será conectado na próxima etapa.'
                );

            }
        );

    }

});


// ======================================
// CONFIRMAÇÃO EXCLUIR
// ======================================

document.addEventListener('click', function (e) {

    if (e.target.classList.contains('btn-delete')) {

        const confirmar = confirm(
            'Deseja realmente excluir este cadastro?'
        );

        if (!confirmar) {

            e.preventDefault();

        }

    }

});


// ======================================
// LOG
// ======================================

console.log(
    'AUTMENOS Admin carregado com sucesso.'
);
function abrirModalCadastro() {

    document
        .getElementById('modalCadastro')
        .style.display = 'flex';

}

function fecharModalCadastro() {

    document
        .getElementById('modalCadastro')
        .style.display = 'none';

}