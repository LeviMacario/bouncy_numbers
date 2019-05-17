<img src="https://images-na.ssl-images-amazon.com/images/I/81CeGTN7AxL._SX425_.jpg" width="127px" align="left"/>

# Bouncy Numbers

[Levi Macario! ;)](https://www.youtube.com/watch?v=2LlDp47_g4Y&t=36s)

<br>

Project is responsible for manipulating bouncy numbers.
<br>


## Índice

- [Introduction](#introduction)
- [Stack](#stack)
- [Requirements](#requirements)
- [Setup](#setup)
- [Architecture](#architecture)

## Introduction

Bouncy Numbers

## Stack

The stack was chosen based on what big companies are using to build their experiences.
Also taken into account was the simplicity, learning curve, easy distribution and quick delivery.

We chose to use [Python 3](https://www.python.org/). <3

## Requirements

This repository is a monorepo that hosts the packages that make up Bouncy Numbers.
To install the dependencies it is necessary to use the [pip](https://pypi.org/project/pip/).

## Setup

Some instructions for developing Bouncy Numbers:

1. **Cloning**

	```sh
	$ git clone git@github.com:LeviMacario/bouncy_numbers.git
	```

2. **Run**

	Enter the main project folder:

	```sh
	$ cd bouncy_numbers
	```

    Create the virtual environment (Using Virtualenv Wrapper):
    ```sh
    $ mkvirtualenv -p python3 bouncy_numbers
    ```

    Access the virtual environment (Using Virtualenv Wrapper):
    ```sh
    $ workon bouncy_numbers
    ```

	Use the pip to install the requirements:

	```sh
	$ pip install -r requirements.txt
	```

	Run the application:

	```sh
	$ python bouncy_numbers.py
	```

## Architecture

- **`bouncy_numbers`**: Structure of project files and folders.
    - **`bouncy_numbers.py`**: Main file of the app.
    - **`.gitignore`**: File responsible for git repository exceptions.
    - **`requirements.txt`**: File that saves all project dependencies.
    - **`README.md`**: File that has instructions for use of the project.
    