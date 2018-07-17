# Primeiro projetinho em flask

Em Python 3.5


## Criar virtualenv:

```python3 -m venv venv```


## Para entrar no virtualenv:

```. venv/bin/activate```


## Execute o requirements

```$ venv/bin/pip3 install -r requirements.txt```


## Atualização em pacotes?

Caso precise instalar um novo pacote no projeto, rode esse script para atualizar o requirementes:

```$ pip3 install -r requirements.txt```


## Comandos para banco

``` python3 run.py db migrate ```
``` python3 run.py db upgrade ```


## Para acessar aplicação via url:

### Rodar pelo terminal:

```python3 run.py runserver```

### Acessar pelo browser:

```http://127.0.0.1:5000/```


## Para desativar virtualenv:

```deactivate```
