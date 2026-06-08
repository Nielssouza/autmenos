// ======================================
// AUTMENOS - CADASTROS
// ======================================

document.addEventListener('DOMContentLoaded', () => {

    console.log(
        'Módulo de Cadastros carregado.'
    );

});


// ======================================
// BUSCA + FILTRO
// ======================================

document.addEventListener('DOMContentLoaded', () => {

    const searchInput =
        document.getElementById('searchInput');

    const filtroTipo =
        document.getElementById('filtroTipo');

    if (!searchInput || !filtroTipo) return;

    function aplicarFiltros() {

        const busca =
            searchInput.value.toLowerCase();

        const tipo =
            filtroTipo.value;

        const linhas =
            document.querySelectorAll(
                '#cadastroTable tbody tr'
            );

        linhas.forEach(linha => {

            const texto =
                linha.innerText.toLowerCase();

            const tipoLinha =
                linha.dataset.tipo;

            const passouBusca =
                texto.includes(busca);

            const passouTipo =
                tipo === '' ||
                tipoLinha === tipo;

            linha.style.display =
                passouBusca && passouTipo
                    ? ''
                    : 'none';

        });

    }

    searchInput.addEventListener(
        'keyup',
        aplicarFiltros
    );

    filtroTipo.addEventListener(
        'change',
        aplicarFiltros
    );

});


// ======================================
// EXPORTAR CSV
// ======================================

function exportarCSV() {

    const tabela =
        document.getElementById(
            'cadastroTable'
        );

    if (!tabela) return;

    let csv = [];

    const linhas =
        tabela.querySelectorAll('tr');

    linhas.forEach(row => {

        const cols =
            row.querySelectorAll(
                'th, td'
            );

        let linha = [];

        cols.forEach(col => {

            linha.push(
                '"' +
                col.innerText.replace(
                    /"/g,
                    '""'
                ) +
                '"'
            );

        });

        csv.push(
            linha.join(';')
        );

    });

    const csvFile =
        new Blob(
            [csv.join('\n')],
            {
                type:
                'text/csv;charset=utf-8;'
            }
        );

    const downloadLink =
        document.createElement('a');

    downloadLink.href =
        URL.createObjectURL(csvFile);

    downloadLink.download =
        'cadastros_autmenos.csv';

    document.body.appendChild(
        downloadLink
    );

    downloadLink.click();

    document.body.removeChild(
        downloadLink
    );

}


// ======================================
// BOTÃO CSV
// ======================================

document.addEventListener('DOMContentLoaded', () => {

    const btnCSV =
        document.getElementById(
            'exportCSV'
        );

    if (!btnCSV) return;

    btnCSV.addEventListener(
        'click',
        exportarCSV
    );

});


// ======================================
// BOTÃO EXCEL
// ======================================

document.addEventListener('DOMContentLoaded', () => {

    const btnExcel =
        document.getElementById(
            'exportExcel'
        );

    if (!btnExcel) return;

    btnExcel.addEventListener(
        'click',
        () => {

            alert(
                'Exportação Excel será implementada em breve.'
            );

        }
    );

});


// ======================================
// BOTÃO PDF
// ======================================

document.addEventListener('DOMContentLoaded', () => {

    const btnPDF =
        document.getElementById(
            'exportPDF'
        );

    if (!btnPDF) return;

    btnPDF.addEventListener(
        'click',
        () => {

            alert(
                'Exportação PDF será implementada em breve.'
            );

        }
    );

});


// ======================================
// EXCLUIR
// ======================================

document.addEventListener(
    'click',
    function (e) {

        if (
            e.target.classList.contains(
                'btn-delete'
            )
        ) {

            const confirmar =
                confirm(
                    'Deseja realmente excluir este cadastro?'
                );

            if (!confirmar) {

                e.preventDefault();

            }

        }

    }
);


// ======================================
// EDITAR
// ======================================

document.addEventListener(
    'click',
    function (e) {

        if (
            e.target.classList.contains(
                'btn-edit'
            )
        ) {

            const id =
                e.target.dataset.id;

            console.log(
                'Editar cadastro:',
                id
            );

        }

    }
);