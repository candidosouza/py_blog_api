# Descrição em andamento...

# MyBlogAPI: Uma API RESTful de Blog com Django / Django Rest Framework

## Visão Geral
Bem-vindo à documentação da MyBlogAPI! Esta API REST com Django permite aos usuários gerenciar uma plataforma de blog simples. O projeto foi construído com várias tecnologias incríveis, incluindo Docker, Django, Django Rest Framework e outras. Este documento descreve como começar com a configuração, o uso geral e abrange os endpoints disponíveis.

---

## Índice
- [Configuração](#configuração)
- [Utilização](#utilização)
- [Autenticação](#autenticação)
- [Endpoints da API](#endpoints-da-api)
  - [Categoria](#categoria)
  - [Post](#post)
  - [Comentário](#comentário)
- [Interface Admin](#interface-admin)
- [Dependências](#dependências)

## Configuração

...

## Utilização

A API possui vários endpoints que permitem gerenciar categorias, posts e comentários. Todos os endpoints são protegidos por autenticação básica.

## Autenticação
A autenticação é feita através de Basic Authentication. Você precisará de um nome de usuário e uma senha válidos para acessar os endpoints.

## Endpoints da API

...

### Endpoints da API

#### Categoria
- `GET /categories/`: Listar todas as categorias
- `POST /categories/`: Criar uma nova categoria
- `PUT /categories/{id}/`: Atualizar uma categoria existente
- `DELETE /categories/{id}/`: Deletar uma categoria

#### Post
- `GET /posts/`: Listar todos os posts
- `POST /posts/`: Criar um novo post
- `PUT /posts/{id}/`: Atualizar um post existente
- `DELETE /posts/{id}/`: Deletar um post
- `GET /posts/user/{id}/`: Listar todos os posts de um usuário específico
- `GET /categories/{id}/posts/`: Listar todos os posts de uma categoria específica

#### Comentário
- `GET /comments/`: Listar todos os comentários
- `POST /comments/`: Criar um novo comentário
- `PUT /comments/{id}/`: Atualizar um comentário existente
- `DELETE /comments/{id}/`: Deletar um comentário
- `GET /posts/{id}/comments/`: Listar todos os comentários de um post específico

### Endpoints da API (versão 2) QueryParameterVersioning
#### Comentário
- `GET /posts/{id}/comments/?version=2`: Listar todos os comentários de um post específico com a versão 2


## Interface Admin

O Django Admin está disponível para gerenciamento avançado dos modelos. Os modelos disponíveis incluem:

- UserProfile
- Category
- Post
- Comment

## Dependências
- Docker
- Django
- Django Rest Framework
- PyJWT
- Faker
- django-filter
- python-dotenv
- dj-database-url
- django-cors-headers
- django-redis