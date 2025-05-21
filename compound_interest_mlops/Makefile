# Makefile para automação

.PHONY: up down build test lint

up:
	docker-compose up --build

down:
	docker-compose down

build:
	docker-compose build

test:
	docker-compose run --rm api pytest

lint:
	docker-compose run --rm api flake8 app
