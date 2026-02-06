## `Descrição do desafio`

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
def listar_usuario(): #criando função que será chamada no servidor
    return usuarios

@app.get("/usuario/{id}") #acessando id de usuario /inserir id no lugar de id
def acessar_usuario(id: int): #criando função que será chamada ao acessar a rota - parâmetro: id como inteiro
    for usuario in usuarios: #para cada usuario em usuarios execute o campo abaixo
        if usuario["id"] == id: #se usuario id recebido for igual ao id existente
            return usuario #retorna os dados do usuario
    raise HTTPException(status_code=400, detail="ID não encontrado, digite um ID válido.")


@app.delete("/usuario/{id}") #deletando usuario - definindo rota
def deletar_usuario(id: int): #função que será chamada - recebe numero inteiro como parametro
    for usuario in usuarios:
        if usuario["id"] == id:
            usuarios.remove(usuario) #remove usuario na lista de usuarios.
            return "Usuário removido."
    raise HTTPException(status_code=404, detail="Usuário não encontrado.")

@app.put("/usuario/{id}") #cria rota de atualização com ID do usuario
def atualizar_usuario(nome: Annotated[str, Body()], email: Annotated[str, Body()], idade: Annotated[int, Body()], id: int): #passa esse id e os outros parametros para a função chamada na rota
    for usuario in usuarios: #percorre a lista usuario reprensenta cada elemento da lista usuarios
        email_existe = email_ja_existe(email, id_atual= id) #chamando função e atribuindo valor dos parametros na variavel email_existe
        if usuario["id"] == id:
            if email_existe:
                raise HTTPException(status_code=400, detail="Email ja existente.")

            usuario["nome"] = nome #atualizações
            usuario["email"] = email
            usuario["idade"] = idade
            return usuario
    raise HTTPException(status_code= 404, detail = "Usuario não encontrado.") #se não encontrar usuario retorna mensagem de erro
