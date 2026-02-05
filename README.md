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

## Melhorias Futuras

- Persistência de dados em SQLite ou PostgreSQL para otimizar consultas relacionais
- Cache distribuído

---

## 👨‍💻 Autor

**Cassiano Shigueyuki Nishikawa**\
Desenvolvedor Python Back-end / Full Stack

- GitHub: [https://github.com/caxiano](https://github.com/caxiano)
- LinkedIn: [https://www.linkedin.com/in/cassiano-nishikawa/](https://www.linkedin.com/in/cassiano-nishikawa/)

---

> *"Do. Or do not. There is no try." — Yoda* 🌟