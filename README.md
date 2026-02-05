# 🌌 Star Wars Explorer API 🌌

Uma API backend construída com **FastAPI** que permite explorar o
universo de **Star Wars** de forma simples, rápida e organizada 🚀

Os dados são obtidos da **[SWAPI(https://swapi.dev/)](https://swapi.dev/)**, depois
**normalizados**, **correlacionados** e disponibilizados por meio de
endpoints REST seguros, com autenticação via **JWT**.

Este projeto foi desenvolvido como **case técnico** para a vaga de
**Desenvolvedor Back End Python**.

---

## 🧭 Visão Geral

A **Star Wars Explorer API** permite explorar:

-   👤 Pessoas
-   🎬 Filmes
-   🪐 Planetas
-   🧬 Espécies
-   🚀 Espaçonaves
-   🚗 Veículos

Todos os recursos retornam **relações navegáveis**, utilizando **links
internos da própria API**, tornando a exploração dos dados simples e
intuitiva.

---

## ⚙️ Arquitetura da Solução

A aplicação foi projetada com foco em **simplicidade**, **performance**
e **boas práticas de backend**.

Essa abordagem reduz a latência e evita múltiplas chamadas externas
durante o consumo da API.

### 🔄 Fluxo de Dados

1.  **Startup da aplicação**
    -   Os dados da SWAPI são ingeridos automaticamente
    -   Todas as páginas são consumidas (sem paginação externa)
    -   Os dados são normalizados e correlacionados
2.  **Normalização**
    -   URLs da SWAPI são convertidas em links internos da API

    -   Relações são transformadas no formato:

        ``` json
        {
          "Nome do Recurso": "link_da_api"
        }
        ```
3.  **Persistência**
    -   Os dados finais são armazenados localmente em arquivos JSON
    -   Os arquivos JSON são gerados automaticamente na primeira
        execução e reutilizados nas próximas inicializações
    -   A API passa a operar **sem dependência da SWAPI em tempo de
        execução**
4.  **Execução**
    -   Os endpoints consomem apenas os dados normalizados
    -   Respostas rápidas e consistentes ⚡

---

## 🧩 Decisões de Design

-   O uso de arquivos JSON foi escolhido para simplificar o case e
    garantir rapidez no acesso aos dados
-   A normalização ocorre no startup para evitar custo de processamento
    em tempo de requisição
-   Os routers não acessam fontes externas, apenas dados previamente
    tratados

---

## 🧠 Normalização de Dados

A SWAPI representa relações utilizando URLs.\
Durante o processo de bootstrap da aplicação, essas relações são
resolvidas e convertidas para um formato mais amigável ao consumidor da
API.

### Exemplo

**Antes (SWAPI):**

``` json
"characters": [
  "https://swapi.dev/api/people/1/"
]
```

**Depois (Star Wars Explorer API):**

``` json
"characters": {
  "Luke Skywalker": "http://localhost:8000/api/people/1"
}
```

---

## 🔐 Autenticação

A API utiliza **JWT (JSON Web Token)** para proteger os endpoints.

### Como autenticar no Swagger:

1.  Faça login em `POST /auth/login`

2.  Copie o token retornado

3.  Clique em **Authorize** no Swagger UI

4.  Utilize o formato:

        Bearer SEU_TOKEN_AQUI

---

## 🧪 Testes Automatizados

O projeto utiliza **pytest** para testes automatizados.

### Executando os testes

``` bash
pytest
```

---

## 🛠️ Instalação e Execução

### 📋 Pré-requisitos

-   Python **3.10+**
-   Git
-   Ambiente virtual (recomendado)

### 📦 Clonando o repositório

``` bash
git clone https://github.com/caxiano/star_wars_api.git
cd star_wars_api
```

### 🐍 Criando e ativando o ambiente virtual

``` bash
python -m venv .venv
```

**Windows**

``` bash
.venv\Scripts\activate
```

**Linux / macOS**

``` bash
source .venv/bin/activate
```

### 📥 Instalando as dependências

``` bash
pip install -r requirements.txt
```

### 🔐 Variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto:

``` env
JWT_SECRET_KEY=sua_chave_super_secreta_com_32_caracteres
JWT_ALGORITHM=HS256
JWT_EXPIRE_MINUTES=60
SWAPI_BASE_URL=https://swapi.dev/api
TESTING=0
```

### 🚀 Executando a aplicação

``` bash
uvicorn app.main:app --reload
```

A aplicação estará disponível em:

    http://localhost:8000

### 📖 Documentação interativa

    http://localhost:8000/docs

---

## 🚀 Tecnologias Utilizadas

-   **Python**
-   **FastAPI**
-   **JWT (PyJWT)**
-   **HTTPX**
-   **Pydantic Settings**
-   **Pytest**
-   **Swagger / OpenAPI**

---

## 🔮 Próximas implementações

-   🔐 Sistema de login com **usuário e senha**, com credenciais válidas usado o token **JWT (JSON Web Token)**

-   ❓ Sistema de Perguntas - **Sistema experimental de perguntas**, onde o usuário
pode realizar perguntas simples sobre o universo de Star Wars.

Exemplos de perguntas: - "Quais filmes Luke Skywalker participou?" -
"Quais planetas aparecem no filme A New Hope?" - "Quais naves Han Solo
pilotou?"

A API interpreta a pergunta e direciona automaticamente a consulta para
os **dados correlacionados**, retornando a resposta estruturada.

---

## 🔮 Melhorias Futuras

-   Persistência de dados com **SQLite ou PostgreSQL**
-   Cache distribuído
-   Paginação interna
-   Versionamento da API

---

## 👨‍💻 Autor

**Cassiano Shigueyuki Nishikawa**\
Desenvolvedor Python Back-end / Full Stack

- GitHub: [https://github.com/caxiano](https://github.com/caxiano)
- LinkedIn: [https://www.linkedin.com/in/cassiano-nishikawa/](https://www.linkedin.com/in/cassiano-nishikawa/)

---

> *"Do. Or do not. There is no try." — Yoda* 🌟