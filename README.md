# API REST de agendamento de notificação
API Rest desenvolvida em Python e Flask com envio automático de emails de notificações, inspirado no desafio técnico do vídeo da [Javanauta](https://www.youtube.com/watch?v=Hos1iMe2tas&t=3006s)

# Pré-requisitos

Python 3.9+

> ## Bibliotecas

[Flask](https://flask.palletsprojects.com/en/stable/quickstart/)

[Flask-SQLAlchemy](https://flask-sqlalchemy.readthedocs.io/en/stable/)


#### Clone o projeto

    git clone https://github.com/seltonkdd/api-agendamento-notificacao

#### Entre no diretório do projeto

    cd api-agendamento-notificaçao

#### Faça a instalação do ambiente virtual via terminal

    python -m venv env
    .\env\Scripts\activate

#### Instale as bibliotecas

    pip install flask flask_sqlalchemy


# Funcionalidades

- Realiza, consulta e cancela agendamentos
- Envia notificação por email

> ## Descrição dos endpoints

```http
  POST /agendamento
```

| Body   | Tipo       | Descrição                           |
| :---------- | :--------- | :---------------------------------- |
| `email_destinatario` | `string` | **Obrigatório**. Email do destinatário da notificação |
| `telefone_destinatario` | `string` | **Obrigatório**. Telefone do destinatário da notificação |
| `mensagem` | `string` | **Obrigatório**. Mensagem da notificação |

Assim que um novo agendamento for criado, será enviado automaticamente um email notificando o agendamento, forneça o email no `text_email.py`

```http
  GET /agendamento/{id}
```

| Parâmetro   | Tipo       | Descrição                           |
| :---------- | :--------- | :---------------------------------- |
| `id` | `int` | **Obrigatório**. ID do item que você quer buscar |

```http
  DELETE /agendamento/{id}
```

| Parâmetro   | Tipo       | Descrição                                   |
| :---------- | :--------- | :------------------------------------------ |
| `id`      | `int` | **Obrigatório**. O ID do item que você quer cancelar |

Assim que um agendamento for cancelado, será enviado o email notificando o cancelamento

# Uso

>> ## Forneça email e senha para o login da biblioteca smtplib no arquivo `text_email.py`:

```http
    USER_EMAIL = ''
    USER_PASSWORD = ''
```

> ## No terminal, execute o comando `python api_agendamento.py` 

# Testes

>> ## Para rodar os testes, execute o comando `pytest test_api.py`