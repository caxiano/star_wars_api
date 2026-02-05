# 🌌 Star Wars Interactive API

Uma API backend interativa construída com **FastAPI**, que permite aos usuários explorar o universo de **Star Wars** através de perguntas em linguagem natural. O projeto consome dados da [SWAPI](https://swapi.dev/) e retorna respostas estruturadas, legíveis e correlacionadas.

Este projeto foi desenvolvido como **case técnico** para o processo seletivo de **Desenvolvedor Back End Python Júnior**.

---

## Normalização de Dados

Os dados provenientes da SWAPI utilizam URLs para representar relações
entre recursos. Durante o processo de bootstrap da aplicação, todos os
recursos são ingeridos e indexados em memória, permitindo a conversão
dessas relações em estruturas mais legíveis para o consumidor da API,
no formato:

{ "Nome do Recurso": "link interno da API" }

Essa abordagem evita chamadas adicionais à SWAPI e melhora a experiência
de consumo da API.

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
