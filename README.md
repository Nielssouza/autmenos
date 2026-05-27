# SISPROM

Backend da API do projeto SISPROM, construído com Django e Django REST Framework.

Este repositório está no começo da estruturação. Hoje ele entrega a base do projeto, autenticação com JWT e configurações iniciais para a equipe desenvolver com mais segurança e padrão.

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

Para evitar conflito e bagunça no histórico:

1. Atualize sua branch antes de começar.
2. Crie uma branch para a sua tarefa.
3. Faça commits pequenos e com mensagem clara.
4. Envie sua branch para o GitHub.
5. Abra um Pull Request.

Exemplo:

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
