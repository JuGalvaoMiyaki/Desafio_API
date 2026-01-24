## `Descrição do desafio`
import email
from typing import Annotated

#criado ambiente virtual
#pacotes instalados
#criado arquivo requirements

from fastapi import FastAPI, Body, HTTPException  # importa a classe FastAPI do pacote fastapi



app = FastAPI() #cria uma variavel app que vai receber a classe FastAPI e permitir a criação de um objeto

usuarios = [] #iniciando lista
contador_id = 0 #iniciando contador

def email_ja_existe(email:str, id_atual:int = None):
    for usuario in usuarios:
        if usuario["email"]== email and usuario["id"] != id_atual:
            return True
    return False



@app.get("/") #cria uma rota no servidor e executa a função abaixo
def mensagem(): #cria uma função chamada mensagem
    return "Tudo okay por aqui" #que irá retornar a mensagem "Tudo ok por aqui"

@app.post("/usuario") #criando metodo post para receber dados
def criar_usuario(nome: Annotated[str, Body()], email: Annotated[str, Body()], idade: Annotated[int, Body()]):
    global contador_id # cria id automatico contador global - possível utilizar a variável fora da função cadastro

    email_existe = email_ja_existe(email)
    if email_existe:
        raise HTTPException(status_code=400, detail="Email ja existente")


    novo_usuario = {
        "id": contador_id,
        "nome": nome,
        "email": email,
        "idade": idade
    }

    usuarios.append(novo_usuario)
    contador_id += 1 # Gera id automatico

    return novo_usuario


@app.get("/usuario") #criando rota para definir usuario
def usuario(): #criando função que será chamada no servidor
    return [usuario.lista_usuario() for usuario in usuarios] #retornar usuario armazenado na lista