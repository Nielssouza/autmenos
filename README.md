# SISPROM - API Backend

API REST construída com **Django 6** + **Django REST Framework**

## 🛠️ Stack

| Tecnologia | Versão | Função |
|------------|--------|--------|
| Python | 3.12+ | Linguagem |
| Django | 6.0 | Framework web |
| DRF | 3.17 | API REST |
| SimpleJWT | 5.3 | Autenticação JWT |
| SQLite | - | Banco de dados (dev) |

## 🚀 Setup do Projeto

### 1. Clone o repositório

```bash
git clone https://github.com/SEU_USUARIO/sisprom.git
cd sisprom
```

### 2. Crie e ative um ambiente virtual (opcional, mas recomendado)

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Configure as variáveis de ambiente

```bash
# Copie o arquivo de exemplo
copy .env.example .env   # Windows
cp .env.example .env     # Linux/Mac
```

Edite o `.env` e gere uma nova SECRET_KEY:

```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

### 5. Rode as migrations

```bash
python manage.py migrate
```

### 6. Crie um superusuário

```bash
python manage.py createsuperuser
```

### 7. Rode o servidor

```bash
python manage.py runserver
```

A API estará disponível em `http://localhost:8000/`

---

## 🔐 Autenticação JWT

### Obter token (login)

```bash
POST /api/token/
Content-Type: application/json

{
    "username": "seu_usuario",
    "password": "sua_senha"
}
```

**Resposta:**
```json
{
    "access": "eyJ0eXAiOiJKV1Q...",
    "refresh": "eyJ0eXAiOiJKV1Q..."
}
```

### Usar o token nas requisições

```bash
GET /api/seu-endpoint/
Authorization: Bearer eyJ0eXAiOiJKV1Q...
```

### Renovar token

```bash
POST /api/token/refresh/
Content-Type: application/json

{
    "refresh": "eyJ0eXAiOiJKV1Q..."
}
```

---

## 📂 Estrutura do Projeto

```
sisprom/
├── core/                # Configurações do projeto Django
│   ├── settings.py      # Settings (DRF, JWT, CORS configurados)
│   ├── urls.py          # Rotas principais
│   ├── wsgi.py
│   └── asgi.py
├── .env.example         # Template das variáveis de ambiente
├── .gitignore
├── manage.py
├── requirements.txt
└── README.md
```

---

## 🌿 Fluxo de Trabalho com Git (Squad)

### Branches

| Branch | Uso |
|--------|-----|
| `main` | Código estável, pronto para produção |
| `develop` | Branch de integração — merges das features vão pra cá |
| `feature/nome-da-feature` | Cada tarefa/feature nova |
| `bugfix/descricao-do-bug` | Correções de bugs |

### Workflow

1. **Sempre parta da `develop`** para criar sua branch:
   ```bash
   git checkout develop
   git pull origin develop
   git checkout -b feature/minha-feature
   ```

2. **Faça commits pequenos e descritivos:**
   ```bash
   git add .
   git commit -m "feat: adiciona model de Produto"
   ```

3. **Suba sua branch e abra um Pull Request para `develop`:**
   ```bash
   git push origin feature/minha-feature
   ```

4. **Peça code review** de pelo menos 1 colega antes do merge.

5. **Após aprovação**, faça o merge via GitHub (Squash and Merge).

### Convenção de Commits

| Prefixo | Uso |
|---------|-----|
| `feat:` | Nova funcionalidade |
| `fix:` | Correção de bug |
| `docs:` | Documentação |
| `refactor:` | Refatoração sem mudar comportamento |
| `test:` | Testes |
| `chore:` | Tarefas gerais (configs, deps) |

---

## 📝 Criando um Novo App

```bash
python manage.py startapp nome_do_app
```

Depois, adicione ao `INSTALLED_APPS` em `core/settings.py`:

```python
INSTALLED_APPS = [
    ...
    # Apps do projeto
    'nome_do_app',
]
```

---

## 👥 Equipe

| Nome | Papel |
|------|-------|
| Daniel Costa | Tech Lead |
| Estagiário 1 | Dev |
| Estagiário 2 | Dev |
