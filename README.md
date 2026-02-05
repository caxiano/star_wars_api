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
  "Luke Skywalker": "http://localhost:8000/people/1"
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

> *"Do. Or do not. There is no try." — Yoda*
