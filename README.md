# AUTMENOS

Backend da API do projeto SISPROM, construído com Django e Django REST Framework.

Este repositório está no começo da estruturação. Hoje ele entrega a base do projeto, autenticação com JWT e configurações iniciais para a equipe desenvolver com mais segurança e padrão.

## Como este projeto quer funcionar

Queremos trabalhar neste repositório com mentalidade de projeto open source:

- contribuição via `fork` como fluxo principal
- mudanças pequenas e revisáveis
- documentação clara para quem chega sem contexto previo
- discussões e Pull Requests com contexto suficiente para review

Se voce quer contribuir, comece por estes arquivos:

- `README.md`

## Antes de começar

Se você é novo no projeto, siga esta ordem:

1. Clone o repositório.
2. Crie um ambiente virtual.
3. Instale as dependências.
4. Configure o arquivo `.env`.
5. Rode as migrations.
6. Inicie o servidor.

Se alguma etapa falhar, pare nela e corrija antes de ir para a próxima.

## Tecnologias usadas

- Python 3.12+
- Django 6
- Django REST Framework
- Simple JWT
- SQLite no ambiente de desenvolvimento
- `python-decouple` para variáveis de ambiente

## Subindo o projeto localmente

### 1. Clonar o repositório

```bash
git clone https://github.com/Nielssouza/sisprom.git
cd sisprom
```

### 2. Criar e ativar o ambiente virtual

```bash
python -m venv venv
```

No Windows:

```bash
venv\Scripts\activate
```

No Linux ou macOS:

```bash
source venv/bin/activate
```

### 3. Instalar as dependências

```bash
pip install -r requirements.txt
```

### 4. Criar o arquivo `.env`

Use o arquivo de exemplo como base:

```bash
copy .env.example .env
```

Se estiver no Linux ou macOS:

```bash
cp .env.example .env
```

Hoje o projeto usa estas variáveis:

```env
SECRET_KEY=sua-chave-secreta-aqui
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
```

Se quiser gerar uma `SECRET_KEY` nova:

```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

### 5. Aplicar as migrations

```bash
python manage.py migrate
```

### 6. Criar um superusuário

Esse passo é importante para acessar o painel do Django.

```bash
python manage.py createsuperuser
```

### 7. Rodar o servidor

```bash
python manage.py runserver
```

Depois disso, a aplicação deve estar disponível em:

- Home: `http://127.0.0.1:8000/`
- Admin: `http://127.0.0.1:8000/admin/`
- API: `http://127.0.0.1:8000/api/` ou pelos endpoints listados abaixo

## O que já existe no projeto

Hoje este repositório possui:

- estrutura base de um projeto Django
- Django REST Framework configurado
- autenticação com JWT
- CORS liberado para desenvolvimento
- paginação padrão da API
- painel administrativo do Django
- pasta global de templates configurada
- página inicial em Django Template para apoio no onboarding

Importante: ainda não existem apps de negócio cadastrados além da configuração base do projeto.

## Endpoints disponíveis hoje

### Autenticação JWT

Gerar token:

```http
POST /api/token/
```

Exemplo de corpo:

```json
{
  "username": "seu_usuario",
  "password": "sua_senha"
}
```

Renovar token:

```http
POST /api/token/refresh/
```

Validar token:

```http
POST /api/token/verify/
```

### Login do browsable API

```http
/api-auth/
```

## Como autenticar nas requisições

Depois de obter o token, envie o `access` no cabeçalho:

```http
Authorization: Bearer seu_token_aqui
```

Observação: a permissão padrão do projeto está como `IsAuthenticated`, então, em geral, os endpoints da API vão exigir autenticação.

## Estrutura atual do projeto

```text
sisprom/
|-- core/
|   |-- settings.py
|   |-- urls.py
|   |-- asgi.py
|   |-- wsgi.py
|-- templates/
|   |-- home.html
|-- .env.example
|-- manage.py
|-- requirements.txt
|-- README.md
```

## Templates do Django

Hoje o projeto está focado em API, mas agora ele tambem ja vem preparado para renderizar paginas HTML com templates do Django.

No estado atual:

- `APP_DIRS = True` já está habilitado no `core/settings.py`
- isso permite que o Django encontre templates dentro dos apps automaticamente
- `DIRS` aponta para a pasta global `templates/`
- a rota `/` ja renderiza o arquivo `templates/home.html`

### Estrutura que ja existe no projeto

```text
sisprom/
|-- templates/
|   |-- home.html
|-- core/
|-- manage.py
```

Essa home inicial serve como exemplo pratico para a equipe entender como o Django encontra e renderiza um template.

### Estrutura recomendada dentro de um app

Quando um app precisar de páginas HTML, o padrão recomendado é:

```text
meu_app/
|-- templates/
|   |-- meu_app/
|       |-- home.html
```

Esse padrão evita conflito entre arquivos com o mesmo nome em apps diferentes.

### Exemplo de view usando template

```python
from django.shortcuts import render


def home(request):
    return render(request, "meu_app/home.html")
```

Resumo prático: a pasta global ja esta pronta para paginas compartilhadas, e os apps podem continuar usando suas proprias pastas `templates/` quando fizer sentido.

## Comandos úteis no dia a dia

Rodar o servidor:

```bash
python manage.py runserver
```

Criar migrations:

```bash
python manage.py makemigrations
```

Aplicar migrations:

```bash
python manage.py migrate
```

Criar um novo app:

```bash
python manage.py startapp nome_do_app
```

## Fluxo de trabalho com Git

Para evitar conflito e bagunça no historico, trate o fluxo com `fork` como caminho padrao de contribuicao.

### Fluxo principal de contribuição

1. Atualize sua branch antes de começar.
2. Crie uma branch para a sua tarefa.
3. Faça commits pequenos e com mensagem clara.
4. Envie sua branch para o GitHub.
5. Abra um Pull Request.

### Quando usar fork

Se voce nao tiver permissao para enviar branches direto para este repositorio, use o fluxo com `fork`.

Resumo:

1. Crie um `fork` do projeto no GitHub.
2. Clone o seu `fork` para a sua maquina.
3. Adicione o repositorio original como `upstream`.
4. Crie sua branch de trabalho.
5. Envie a branch para o seu `fork`.
6. Abra o Pull Request do seu `fork` para o repositorio principal.

Exemplo:

```bash
git clone https://github.com/SEU_USUARIO/sisprom.git
cd sisprom
git remote add upstream https://github.com/Nielssouza/sisprom.git
git checkout main
git pull upstream main
git checkout -b feature/nome-da-tarefa
```

Depois de terminar sua tarefa:

```bash
git add .
git commit -m "feat: adiciona endpoint de produtos"
git push origin feature/nome-da-tarefa
```

Nesse fluxo:

- `origin` e o seu `fork`
- `upstream` e o repositorio principal do time

Antes de iniciar uma nova tarefa, sincronize seu `main` local com o repositorio principal:

```bash
git checkout main
git pull upstream main
```

### Fluxo alternativo para quem tem permissao de escrita

Se voce tiver permissao para enviar branch direto para o repositorio principal, pode usar este fluxo:

```bash
git checkout main
git pull origin main
git checkout -b feature/nome-da-tarefa
```

Exemplo de commit:

```bash
git add .
git commit -m "feat: adiciona endpoint de produtos"
```

Subindo a branch:

```bash
git push origin feature/nome-da-tarefa
```

## Padrão de commits

- `feat:` nova funcionalidade
- `fix:` correção de bug
- `docs:` documentação
- `refactor:` refatoração sem alterar regra de negócio
- `test:` testes
- `chore:` ajustes de configuração, dependências ou manutenção

## Contribuindo

Para manter o projeto organizado, antes de abrir um PR:

1. Leia este `README.md`.
2. Garanta que a mudanca esta explicada de forma clara.
3. Teste localmente tudo o que voce alterou.
4. Avise no PR se existe alguma limitacao, pendencia ou escolha tecnica em aberto.

Se a mudanca for grande, prefira quebrar em PRs menores.

### Guia de contribuicao

Este projeto quer funcionar com uma rotina parecida com a de projetos open source:

- documentacao clara
- mudancas pequenas
- revisao por Pull Request
- historico facil de entender

Se for sua primeira contribuicao, comece por algo pequeno:

- melhorar documentacao
- corrigir texto ou exemplo
- ajustar uma configuracao simples
- criar uma pequena funcionalidade bem isolada

### Fluxo recomendado

O fluxo principal e via `fork`.

1. Faca um `fork` do repositorio no GitHub.
2. Clone o seu `fork`.
3. Adicione o repositorio principal como `upstream`.
4. Crie uma branch a partir da `main`.
5. Faca sua alteracao.
6. Teste localmente.
7. Envie sua branch para o seu `fork`.
8. Abra um Pull Request para a `main` do repositorio principal.

Exemplo:

```bash
git clone https://github.com/SEU_USUARIO/sisprom.git
cd sisprom
git remote add upstream https://github.com/Nielssouza/sisprom.git
git checkout main
git pull upstream main
git checkout -b feature/minha-alteracao
```

### Como manter seu fork atualizado

Antes de comecar uma nova tarefa:

```bash
git checkout main
git pull upstream main
git push origin main
```

### Padrao para branches

Use nomes curtos e descritivos:

- `feature/nome-da-feature`
- `fix/nome-do-bug`
- `docs/nome-do-ajuste`
- `refactor/nome-do-ajuste`

### O que esperamos em um Pull Request

Todo PR deve explicar:

- o que foi alterado
- por que a mudanca foi feita
- como testar localmente
- se existe algum ponto de atencao para review

Se possivel, inclua:

- prints, quando houver interface
- exemplos de request/response, quando houver API
- observacoes sobre limitacoes conhecidas

### Checklist antes de abrir o PR

- li este README
- minha branch esta atualizada com a `main`
- testei localmente o que alterei
- revisei os arquivos modificados
- escrevi uma descricao clara no PR

### Boas praticas para contribuicao

- Prefira PRs pequenos.
- Nao misture refatoracao com funcionalidade nova sem necessidade.
- Evite mudar varios assuntos diferentes no mesmo PR.
- Atualize a documentacao quando a mudanca afetar onboarding, setup ou uso do projeto.
- Se a mudanca for grande, abra uma discussao antes ou explique bem o contexto no PR.

### Areas boas para primeira contribuicao

Alguns exemplos de tarefas amigaveis para quem esta chegando:

- melhorar o README
- revisar mensagens e textos do projeto
- criar estrutura inicial de apps
- adicionar testes simples
- padronizar exemplos de uso da API

## Convivencia no projeto

Queremos que o SISPROM seja um projeto acolhedor para quem esta aprendendo e tambem para quem ja tem experiencia.

### Nosso compromisso

Ao participar deste projeto, esperamos que todas as pessoas:

- tratem as outras com respeito
- deem feedback com clareza e boa fe
- aceitem correcao tecnica sem ataques pessoais
- ajudem a manter um ambiente seguro para perguntas e aprendizado

### Comportamentos esperados

- usar linguagem respeitosa
- explicar decisoes tecnicas com contexto
- assumir boa intencao nas interacoes
- acolher contribuicoes de iniciantes
- apontar problemas de forma objetiva

### Comportamentos inaceitaveis

- insultos ou ataques pessoais
- humilhacao publica
- discriminacao ou assedio
- provocacao repetitiva sem objetivo construtivo
- exposicao desnecessaria de erros de outra pessoa

### Resolucao de conflitos

Quando houver discordancia:

1. Foque no problema tecnico.
2. Explique a preocupacao com exemplos concretos.
3. Proponha um caminho alternativo.
4. Se necessario, pause a discussao e retome com mais contexto.

## Dicas para quem está chegando agora

- Leia primeiro o arquivo `core/settings.py` para entender a configuração do projeto.
- Leia `core/urls.py` para ver quais rotas já existem.
- Sempre teste localmente antes de subir sua branch.
- Se criar um novo app, lembre de adicioná-lo ao `INSTALLED_APPS`.
- Se algo não subir, confira primeiro o `.env`, o ambiente virtual e as migrations.

## Problemas comuns

### Erro de dependência

Verifique se o ambiente virtual está ativado antes de rodar `pip install -r requirements.txt`.

### Erro por falta de `.env`

Confirme se o arquivo `.env` existe na raiz e se a variável `SECRET_KEY` foi preenchida.

### Erro de banco

Tente rodar novamente:

```bash
python manage.py migrate
```

## Próximos passos esperados para o projeto

Alguns itens que ainda devem entrar conforme o projeto evoluir:

- apps de negócio
- models e serializers
- views e endpoints próprios do sistema
- testes automatizados
- documentação mais detalhada da regra de negócio

## Responsáveis

- Daniel Costa

## Licenca

Este repositorio ainda nao possui uma licenca definida.

Antes de publicar o projeto formalmente como open source, vale escolher uma licenca com o time.
