# FastAPI Docker App

Este projeto é uma aplicação FastAPI containerizada usando Docker e Docker Compose.

## Estrutura do Projeto

```
fastapi-docker-app
├── app
│   ├── main.py              # Ponto de entrada da aplicação FastAPI
│   ├── api
│   │   └── endpoints.py     # Definição dos endpoints da API
│   └── models
│       └── __init__.py      # Modelos de dados ou schemas (atualmente vazio)
├── tests
│   └── test_endpoints.py    # Testes unitários dos endpoints da API
├── Dockerfile               # Dockerfile para build da imagem da aplicação
├── docker-compose.yml       # Orquestração dos containers
├── requirements.txt         # Dependências Python do projeto
├── Makefile                 # Comandos facilitadores para Docker Compose
└── README.md                # Documentação do projeto
```

## Pré-requisitos

- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/)
- [Make](https://www.gnu.org/software/make/) (opcional, mas recomendado)

## Como rodar o projeto

Você pode utilizar o `Makefile` para facilitar os comandos do Docker Compose.

### Subir a aplicação

```sh
make up
```

A aplicação estará disponível em [http://localhost:8000](http://localhost:8000).

### Parar a aplicação

```sh
make down
```

### Build da imagem

```sh
make build
```

### Ver logs

```sh
make logs
```

### Reiniciar a aplicação

```sh
make restart
```

## Uso manual com Docker Compose

Se preferir, você pode usar os comandos do Docker Compose diretamente:

```sh
docker compose up
docker compose down
docker compose build
```

---

Sinta-se à vontade para contribuir ou abrir issues!