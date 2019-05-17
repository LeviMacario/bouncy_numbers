<img src="https://images-na.ssl-images-amazon.com/images/I/81CeGTN7AxL._SX425_.jpg" width="127px" align="left"/>

# Bouncy Numbers

[Levi Macario! ;)](https://www.youtube.com/watch?v=2LlDp47_g4Y&t=36s)

<br>

Project is responsible for manipulating bouncy numbers.
<br>


## Índice

- [Introduction](#introduction)
- [Stack](#stack)
- [Requisitos](#requisitos)
- [Instalação](#instalação)
- [Estrutura do projeto](#estrutura-do-projeto)

## Introduction

Fortes API é uma interface de extração de dados do sistema Fortes AG do IEPRO.
O produto foi criado a partir da necessidade dos desenvolvedores
de integrar os sistemas do IEPRO com e possam focar nas demais funcionalidades
que sejam solicitadas!

## Stack

A stack foi escolhida com base no que empresas grandes estão usando para construir suas experiências.
Também foi levado em consideração a simplicidade, curva de aprendizado e requisitos
como fácil distribuição e entrega rápida.

Tendo isso em vista, optamos por usar [Python 3](https://www.python.org/).

## Requisitos

Este repositório é um monorepo que aloja os pacotes que compõem a Fortes API.
Para instalar as dependências é necessário usar o [pip](https://pypi.org/project/pip/).

## Instalação

Algumas instruções para desenvolver na Fortes API:

1. **Clonando o repositório**

	```sh
	$ git clone git@github.com:ieprodev/fortesapi.git
	```

2. **Rodando o servidor**

	Entre na pasta principal do projeto:

	```sh
	$ cd fortesapi
	```

    Crie o ambiente virtual
    ```sh
    $ mkvirtualenv -p python3 fortesapi
    ```

    Acesse o ambiente virtual
    ```sh
    $ workon fortesapi
    ```

	Use o pip para instalar as dependências:

	```sh
	$ pip install -r requirements.txt
	```

    Crie uma cópia de .flaskenv.example para .flaskenv (Esse arquivo é necessário para carregar as variáveis de ambiente):

	```sh
	$ cp .flaskenv.example .flaskenv
	```

	Inicie a aplicação (em ambiente de desenvolvimento):

	```sh
	$ make runpublic
	```

## Estrutura do projeto

- **`fortesapi`**: Toda a estrutura de arquivos e pastas do projeto.
    - **`database`**: Contém a estrutura de arquivos e pastas relacionadas ao banco de dados.
        - **`constants.py`**: Variáveis globais que armazenem as strings com os códigos SQL.
        - **`sqlserver.py`**: Classe para se conectar ao banco e realizar as consultas necessárias.
    - **`views`**: Todas as views que são utilizadas para os endpoints da API.
        - **`bank_accounts.py`**: Views responsáveis pelos favorecidos.
        - **`favored.py`**: Views responsáveis pelas contas.
    - **`fortesapi.py`**: Arquivo principal para instanciação da app central.
    - **`.gitignore`**: Arquivo responsável pelas exceções do repositório git.
    - **`requirements.txt`**: Arquivo que guarda todas as dependências do projeto.
    - **`README.md`**: Arquivo que possui as instruções para uso do projeto.
    - **`Makefile`**: Arquivo que possui tasks automatizadas do projeto.
    - **`.flaskenv.example`**: Arquivo que possui as variáveis de ambiente de desenvolvimento do projeto.
    